"""
Script to download and parse all official UPC GREELEC teaching guides.
"""
import os
import re
import json
import time
import urllib.request
import fitz  # PyMuPDF
from pathlib import Path

DATA_DIR = Path("data/upc_guides")
MD_DIR = Path("data/upc_guides_md")
DATA_DIR.mkdir(parents=True, exist_ok=True)
MD_DIR.mkdir(parents=True, exist_ok=True)

with open('upc_degree_subjects.json', 'r', encoding='utf-8') as f:
    all_subs = json.load(f)

compulsory = [s for s in all_subs if s['code'].startswith('2309') or s['code'] == '230339']
print(f"Total compulsory subjects to process: {len(compulsory)}")


def download_pdf(url: str, dest_path: Path) -> bool:
    if dest_path.exists() and dest_path.stat().st_size > 1000:
        return True
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            if len(data) > 1000:
                dest_path.write_bytes(data)
                return True
    except Exception as e:
        print(f"  Error downloading {url}: {e}")
    return False


def parse_guide_pdf(pdf_path: Path, sub_meta: dict) -> dict:
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text() for page in doc])
    
    # Extract acronym: "230900 - CCE - Componentes..."
    m_title = re.search(r'(\d{6})\s*-\s*([A-Za-z0-9\-]+)\s*-\s*([^\n]+)', text)
    code = sub_meta['code']
    acronym = m_title.group(2).strip() if m_title else sub_meta['slug'].upper()
    title = m_title.group(3).strip() if m_title else sub_meta['name']

    # Extract ECTS
    m_ects = re.search(r'Cr[eé]ditos\s+ECTS:\s*([\d\.]+)', text, re.I)
    ects = float(m_ects.group(1)) if m_ects else 6.0

    # Extract Department
    m_dept = re.search(r'Unidad que imparte:\s*\n?\s*([^\n]+)', text, re.I)
    dept = m_dept.group(1).strip() if m_dept else "ETSETB"

    # Extract Professors
    m_prof = re.search(r'Profesorado responsable:\s*\n?\s*([^\n]+)', text, re.I)
    prof_resp = m_prof.group(1).strip() if m_prof else ""

    # Extract Learning Objectives
    obj_match = re.search(r'OBJETIVOS DE APRENDIZAJE[^\n]*\n(.*?)(?=HORAS TOTALES|CONTENIDOS|COMPETENCIAS|$)', text, re.DOTALL | re.I)
    objectives = obj_match.group(1).strip() if obj_match else ""

    # Extract Hours
    m_hours = re.search(r'Dedicaci[oó]n total:\s*(\d+)\s*h', text, re.I)
    hours = int(m_hours.group(1)) if m_hours else int(ects * 25)

    # Extract Contents / Temas
    contents = []
    # Match blocks: "Tema X. Title" followed by Description
    re_tema = re.findall(r'(Tema\s+\d+[\.:\s][^\n]+)\n\s*Descripci[oó]n:\s*\n?(.*?)(?=(?:Tema\s+\d+|SISTEMA DE CALIFICACI[OÓ]N|BIBLIOGRAF|Dedicaci[oó]n:|$))', text, re.DOTALL | re.I)
    if re_tema:
        for t_title, t_desc in re_tema:
            # clean desc
            clean_d = " ".join([l.strip() for l in t_desc.splitlines() if not l.strip().startswith("Dedicación") and not l.strip().startswith("Grupo") and not l.strip().startswith("Aprendizaje")])
            contents.append({
                "title": t_title.strip(),
                "description": clean_d.strip()
            })
    else:
        # Fallback split
        c_block = re.search(r'CONTENIDOS\s*\n(.*?)(?=SISTEMA DE CALIFICACI[OÓ]N|BIBLIOGRAF|$)', text, re.DOTALL | re.I)
        if c_block:
            lines = [l.strip() for l in c_block.group(1).splitlines() if len(l.strip()) > 3]
            curr_title = "Contenido General"
            curr_desc = []
            for l in lines:
                if re.match(r'^(?:Tema|Unidad|Bloque)\s+\d+', l, re.I):
                    if curr_desc:
                        contents.append({"title": curr_title, "description": " ".join(curr_desc)})
                    curr_title = l
                    curr_desc = []
                else:
                    curr_desc.append(l)
            if curr_desc:
                contents.append({"title": curr_title, "description": " ".join(curr_desc)})

    # Extract Evaluation
    eval_match = re.search(r'SISTEMA DE CALIFICACI[OÓ]N\s*\n(.*?)(?=BIBLIOGRAF[IÍ]A|$)', text, re.DOTALL | re.I)
    eval_desc = eval_match.group(1).strip() if eval_match else ""

    # Extract Bibliography
    bib_match = re.search(r'BIBLIOGRAF[IÍ]A\s*\n(.*?)(?=Fecha:|$)', text, re.DOTALL | re.I)
    bib_raw = bib_match.group(1).strip() if bib_match else ""
    bib_list = [l.strip() for l in bib_raw.splitlines() if len(l.strip()) > 10][:5]

    data = {
        "code": code,
        "acronym": acronym,
        "title": title,
        "ects": ects,
        "hours": hours,
        "department": dept,
        "responsible_professor": prof_resp,
        "objectives": objectives,
        "contents": contents,
        "evaluation": eval_desc,
        "bibliography": bib_list,
        "pdf_url": sub_meta['url']
    }
    return data


def generate_markdown(data: dict) -> str:
    md = f"""# 📘 Guía Docente Oficial: {data['code']} · {data['acronym']} - {data['title']}

> 🏛️ **Universidad:** Universitat Politècnica de Catalunya (UPC) · ETSETB  
> 🎓 **Titulación:** Grado en Ingeniería Electrónica de Telecomunicación (Plan 2018)  
> ⏱️ **Créditos ECTS:** {data['ects']} ({data['hours']} horas totales)  
> 🏢 **Unidad que imparte:** {data['department']}  
> 👤 **Profesorado responsable:** {data['responsible_professor'] or 'Equipo docente'}  
> 🔗 **PDF Oficial UPC:** [{data['code']}.pdf]({data['pdf_url']})  

---

## 🎯 Objetivos de Aprendizaje
{data['objectives'] or 'Formación teórica y experimental de nivel universitario conforme a la memoria verificada del grado.'}

---

## 📚 Temario y Contenidos
"""
    for i, t in enumerate(data['contents']):
        md += f"\n### {t['title']}\n{t['description']}\n"

    if data['evaluation']:
        md += f"\n---\n\n## 📝 Sistema de Calificación\n{data['evaluation']}\n"

    if data['bibliography']:
        md += "\n---\n\n## 📖 Bibliografía de Referencia\n"
        for b in data['bibliography']:
            md += f"- {b}\n"

    return md


# Execution loop
parsed_records = []
pdf_dir = Path("data/upc_pdf_raw")
pdf_dir.mkdir(parents=True, exist_ok=True)

for i, sub in enumerate(compulsory):
    code = sub['code']
    slug = sub['slug']
    print(f"[{i+1}/{len(compulsory)}] Descargando y procesando {code} ({slug})...")
    pdf_path = pdf_dir / f"{code}_{slug}.pdf"
    
    ok = download_pdf(sub['url'], pdf_path)
    if ok:
        try:
            guide_data = parse_guide_pdf(pdf_path, sub)
            parsed_records.append(guide_data)
            
            # Save JSON
            json_file = DATA_DIR / f"{code}.json"
            json_file.write_text(json.dumps(guide_data, indent=2, ensure_ascii=False), encoding="utf-8")
            
            # Save Markdown
            md_file = MD_DIR / f"{code}_{guide_data['acronym']}.md"
            md_file.write_text(generate_markdown(guide_data), encoding="utf-8")
            print(f"  -> OK: {guide_data['acronym']} ({len(guide_data['contents'])} temas)")
        except Exception as e:
            print(f"  -> Error parsing {code}: {e}")
    else:
        print(f"  -> Fallo descarga {code}")
    time.sleep(0.1)

print(f"\nProceso finalizado. Total guías procesadas: {len(parsed_records)}")
with open("data/all_upc_compulsory_guides.json", "w", encoding="utf-8") as out:
    json.dump(parsed_records, out, indent=2, ensure_ascii=False)
