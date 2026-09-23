# -*- coding: utf-8 -*-
"""
universal_converters.py
======================================================================
Módulo de Conversores Universales de Alta Fidelidad Académica
Para el proyecto Conversor-HTML-A-MD (UPC EEBE / GREELEC)

Formatos Soportados:
  1. PDF a Markdown Científico (PyMuPDF / fitz, tablas, figuras, LaTeX)
  2. DOCX a Markdown (Word XML, OMML a LaTeX, tablas GFM, imágenes)
  3. Jupyter Notebook (.ipynb) a Markdown (código, salidas, gráficos)
  4. Markdown a HTML Académico Imprimible / PDF (@media print, KaTeX/MathJax)
  5. Markdown a Anki (.apkg y .tsv) con soporte MathJax y Dark Mode
  6. Excel / CSV a Tablas Markdown GFM
  7. Extractor de Formulario Resumen de Ecuaciones
  8. Extractor de Netlists SPICE / LTspice
  9. Generador de Glosario Técnico Indexado (A-Z)
  10. Motor de Conversión por Lotes Universal (Batch Engine)
======================================================================
"""

import os
import re
import sys
import json
import base64
import zipfile
import math
from pathlib import Path
from typing import Optional, Callable, List, Dict, Tuple, Any
import xml.etree.ElementTree as ET

# Intentar importar librerías opcionales con degradación elegante
try:
    import fitz  # PyMuPDF
    HAS_FITZ = True
except ImportError:
    HAS_FITZ = False

try:
    import genanki
    HAS_GENANKI = True
except ImportError:
    HAS_GENANKI = False

try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False


# ======================================================================
# 1. CONVERSOR PDF A MARKDOWN CIENTÍFICO (PyMuPDF)
# ======================================================================

def convert_pdf_to_markdown(
    pdf_path: Path,
    output_path: Path,
    extract_images: bool = True,
    progress_callback: Optional[Callable[[int, str], None]] = None
) -> Tuple[str, Dict[str, Any]]:
    """
    Convierte un documento PDF a Markdown con alta fidelidad:
    - Extrae estructura jerárquica (H1, H2, H3) según tamaño de fuente.
    - Reconoce tablas integradas con page.find_tables().
    - Extrae imágenes incrustadas a la carpeta assets/.
    - Convierte caracteres matemáticos y griegos a formato LaTeX.
    """
    if not HAS_FITZ:
        raise RuntimeError("La librería 'PyMuPDF' (fitz) no está disponible. Instálela con 'pip install pymupdf'.")

    pdf_path = Path(pdf_path)
    output_path = Path(output_path)
    doc_stem = pdf_path.stem
    assets_dir = output_path.parent / "assets"
    if extract_images:
        assets_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(str(pdf_path))
    total_pages = len(doc)
    stats = {
        "pages": total_pages,
        "images": 0,
        "tables": 0,
        "math_formulas": 0,
        "word_count": 0
    }

    md_lines = []
    meta = doc.metadata or {}
    title = meta.get("title") or doc_stem.replace("_", " ").title()
    author = meta.get("author") or "Documento Técnico / UPC"
    
    md_lines.append("---")
    md_lines.append(f"title: \"{title}\"")
    md_lines.append(f"author: \"{author}\"")
    md_lines.append(f"source: \"{pdf_path.name}\"")
    md_lines.append(f"pages: {total_pages}")
    md_lines.append(f"converter: \"Universal PDF to MD Pro\"")
    md_lines.append("---\n")
    md_lines.append(f"# {title}\n")

    GREEK_MATH_MAP = {
        'α': r'\alpha ', 'β': r'\beta ', 'γ': r'\gamma ', 'δ': r'\delta ',
        'ε': r'\varepsilon ', 'θ': r'\theta ', 'λ': r'\lambda ', 'μ': r'\mu ',
        'π': r'\pi ', 'ρ': r'\rho ', 'σ': r'\sigma ', 'τ': r'\tau ',
        'φ': r'\phi ', 'ω': r'\omega ', 'Δ': r'\Delta ', 'Ω': r'\Omega ',
        'Σ': r'\Sigma ', 'Φ': r'\Phi ', '≈': r'\approx ', '≠': r'\neq ',
        '≤': r'\le ', '≥': r'\ge ', '±': r'\pm ', '∞': r'\infty ',
        '∫': r'\int ', '∑': r'\sum ', '√': r'\sqrt', '×': r'\times '
    }

    for page_num in range(total_pages):
        if progress_callback:
            progress_callback(int((page_num / max(1, total_pages)) * 100), f"Página {page_num + 1}/{total_pages}")

        page = doc[page_num]
        
        # 1. Extraer Tablas de la página
        table_rects = []
        try:
            tabs = page.find_tables()
            for tab in tabs:
                table_rects.append(tab.bbox)
                df = tab.extract()
                if df and len(df) > 1:
                    stats["tables"] += 1
                    md_lines.append("\n")
                    headers = [str(c or "").strip().replace("\n", " ") for c in df[0]]
                    md_lines.append("| " + " | ".join(headers) + " |")
                    md_lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
                    for row in df[1:]:
                        cells = [str(c or "").strip().replace("\n", " ") for c in row]
                        md_lines.append("| " + " | ".join(cells) + " |")
                    md_lines.append("\n")
        except Exception:
            pass

        # 2. Extraer Imágenes de la página
        if extract_images:
            img_list = page.get_images(full=True)
            for img_idx, img_info in enumerate(img_list):
                xref = img_info[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                if len(image_bytes) > 2048:
                    img_filename = f"{doc_stem}_p{page_num+1}_{img_idx+1}.{image_ext}"
                    img_file_path = assets_dir / img_filename
                    img_file_path.write_bytes(image_bytes)
                    stats["images"] += 1
                    rel_img_path = f"assets/{img_filename}"
                    md_lines.append(f"\n![Figura {stats['images']}: Página {page_num+1}]({rel_img_path})\n")

        # 3. Extraer Bloques de Texto
        blocks = page.get_text("dict", flags=fitz.TEXT_DEHYPHENATE)["blocks"]
        blocks.sort(key=lambda b: (b.get("bbox", [0, 0])[1], b.get("bbox", [0, 0])[0]))

        for b in blocks:
            b_bbox = b.get("bbox")
            if b_bbox and any(fitz.Rect(b_bbox).intersects(fitz.Rect(tr)) for tr in table_rects):
                continue

            if b.get("type") == 0:
                block_text = ""
                max_size = 0
                is_bold = False

                for line in b.get("lines", []):
                    line_spans = []
                    for span in line.get("spans", []):
                        txt = span.get("text", "")
                        if not txt.strip():
                            continue
                        size = span.get("size", 10)
                        flags = span.get("flags", 0)
                        font = span.get("font", "").lower()
                        if size > max_size:
                            max_size = size
                        if flags & 2 or "bold" in font:
                            is_bold = True

                        for sym, tex in GREEK_MATH_MAP.items():
                            if sym in txt:
                                txt = txt.replace(sym, tex)
                                stats["math_formulas"] += 1

                        line_spans.append(txt)

                    if line_spans:
                        block_text += " ".join(line_spans) + "\n"

                block_text = block_text.strip()
                if not block_text:
                    continue

                stats["word_count"] += len(block_text.split())

                if max_size >= 19:
                    md_lines.append(f"\n# {block_text}\n")
                elif max_size >= 15:
                    md_lines.append(f"\n## {block_text}\n")
                elif max_size >= 12.5 and is_bold:
                    md_lines.append(f"\n### {block_text}\n")
                elif is_bold and len(block_text) < 80:
                    md_lines.append(f"\n**{block_text}**\n")
                else:
                    if any(op in block_text for op in [r'\int', r'\sum', r'\frac', '=', r'\approx']) and len(block_text) < 120 and ('\n' not in block_text):
                        md_lines.append(f"\n$$\n{block_text}\n$$\n")
                        stats["math_formulas"] += 1
                    else:
                        md_lines.append(f"{block_text}\n")

    doc.close()
    full_md = "\n".join(md_lines)
    full_md = re.sub(r'\n{3,}', '\n\n', full_md)
    output_path.write_text(full_md, encoding="utf-8")
    return full_md, stats


# ======================================================================
# 2. CONVERSOR DOCX A MARKDOWN (Word XML con OMML a LaTeX Nativo)
# ======================================================================

def convert_docx_to_markdown(
    docx_path: Path,
    output_path: Path,
    extract_images: bool = True
) -> Tuple[str, Dict[str, Any]]:
    """
    Convierte documentos de Word (.docx) a Markdown:
    - Extrae y convierte fórmulas matemáticas de Word (OMML) a LaTeX real.
    - Convierte tablas XML a tablas GFM.
    - Extrae imágenes incrustadas de word/media/ a assets/.
    - Mapea estilos de párrafo a encabezados H1-H4.
    """
    docx_path = Path(docx_path)
    output_path = Path(output_path)
    doc_stem = docx_path.stem
    assets_dir = output_path.parent / "assets"
    if extract_images:
        assets_dir.mkdir(parents=True, exist_ok=True)

    stats = {"images": 0, "tables": 0, "math_formulas": 0, "paragraphs": 0}

    NS = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
        'm': 'http://schemas.openxmlformats.org/officeDocument/2006/math',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'
    }

    def omml_to_latex(node) -> str:
        tag = node.tag.split('}')[-1] if '}' in node.tag else node.tag
        
        if tag == 'f':
            num = "".join(omml_to_latex(c) for c in node.find('m:num', NS) or [])
            den = "".join(omml_to_latex(c) for c in node.find('m:den', NS) or [])
            return f"\\frac{{{num.strip()}}}{{{den.strip()}}}"
        
        elif tag == 'sSup':
            e = "".join(omml_to_latex(c) for c in node.find('m:e', NS) or [])
            sup = "".join(omml_to_latex(c) for c in node.find('m:sup', NS) or [])
            return f"{{{e.strip()}}}^{{{sup.strip()}}}"

        elif tag == 'sSub':
            e = "".join(omml_to_latex(c) for c in node.find('m:e', NS) or [])
            sub = "".join(omml_to_latex(c) for c in node.find('m:sub', NS) or [])
            return f"{{{e.strip()}}}_{{{sub.strip()}}}"

        elif tag == 'sSubSup':
            e = "".join(omml_to_latex(c) for c in node.find('m:e', NS) or [])
            sub = "".join(omml_to_latex(c) for c in node.find('m:sub', NS) or [])
            sup = "".join(omml_to_latex(c) for c in node.find('m:sup', NS) or [])
            return f"{{{e.strip()}}}_{{{sub.strip()}}}^{{{sup.strip()}}}"

        elif tag == 'rad':
            deg_node = node.find('m:deg', NS)
            e_node = node.find('m:e', NS)
            deg = "".join(omml_to_latex(c) for c in deg_node or []) if deg_node is not None else ""
            e = "".join(omml_to_latex(c) for c in e_node or []) if e_node is not None else ""
            if deg.strip():
                return f"\\sqrt[{deg.strip()}]{{{e.strip()}}}"
            return f"\\sqrt{{{e.strip()}}}"

        elif tag == 'd':
            inner = "".join(omml_to_latex(c) for c in node.find('m:e', NS) or [])
            return f"\\left( {inner.strip()} \\right)"

        elif tag == 't':
            return node.text or ""

        res = ""
        for child in node:
            res += omml_to_latex(child)
        return res

    md_lines = []
    md_lines.append(f"# {doc_stem.replace('_', ' ').title()}\n")

    with zipfile.ZipFile(str(docx_path), 'r') as docx_zip:
        if extract_images:
            for zip_info in docx_zip.infolist():
                if zip_info.filename.startswith("word/media/"):
                    img_data = docx_zip.read(zip_info.filename)
                    img_name = Path(zip_info.filename).name
                    target_img = assets_dir / f"{doc_stem}_{img_name}"
                    target_img.write_bytes(img_data)
                    stats["images"] += 1

        xml_content = docx_zip.read('word/document.xml')
        root = ET.fromstring(xml_content)
        body = root.find('w:body', NS)
        if body is None:
            return "", stats

        for elem in body:
            tag_name = elem.tag.split('}')[-1]

            if tag_name == 'p':
                stats["paragraphs"] += 1
                p_text = ""
                p_style = ""
                p_pr = elem.find('w:pPr', NS)
                if p_pr is not None:
                    p_style_elem = p_pr.find('w:pStyle', NS)
                    if p_style_elem is not None:
                        p_style = p_style_elem.attrib.get(f"{{{NS['w']}}}val", "").lower()

                for child in elem:
                    c_tag = child.tag.split('}')[-1]
                    if c_tag == 'r':
                        t_elem = child.find('w:t', NS)
                        if t_elem is not None and t_elem.text:
                            r_pr = child.find('w:rPr', NS)
                            is_b = r_pr is not None and (r_pr.find('w:b', NS) is not None)
                            is_i = r_pr is not None and (r_pr.find('w:i', NS) is not None)
                            txt = t_elem.text
                            if is_b and is_i: txt = f"***{txt}***"
                            elif is_b: txt = f"**{txt}**"
                            elif is_i: txt = f"*{txt}*"
                            p_text += txt
                    
                    elif c_tag in ('oMath', 'oMathPara'):
                        tex = omml_to_latex(child).strip()
                        if tex:
                            stats["math_formulas"] += 1
                            if c_tag == 'oMathPara':
                                p_text += f"\n$$\n{tex}\n$$\n"
                            else:
                                p_text += f" ${tex}$ "

                p_text = p_text.strip()
                if not p_text:
                    continue

                if "heading1" in p_style or "título1" in p_style or "titulo1" in p_style:
                    md_lines.append(f"\n## {p_text}\n")
                elif "heading2" in p_style or "título2" in p_style or "titulo2" in p_style:
                    md_lines.append(f"\n### {p_text}\n")
                elif "heading3" in p_style or "título3" in p_style or "titulo3" in p_style:
                    md_lines.append(f"\n#### {p_text}\n")
                else:
                    md_lines.append(f"{p_text}\n")

            elif tag_name == 'tbl':
                stats["tables"] += 1
                rows = []
                for tr in elem.findall('w:tr', NS):
                    row_cells = []
                    for tc in tr.findall('w:tc', NS):
                        cell_texts = []
                        for p in tc.findall('w:p', NS):
                            c_p_text = "".join(t.text for t in p.findall('.//w:t', NS) if t.text)
                            if c_p_text.strip():
                                cell_texts.append(c_p_text.strip())
                        row_cells.append(" ".join(cell_texts) or " ")
                    if row_cells:
                        rows.append(row_cells)

                if rows:
                    md_lines.append("\n")
                    headers = rows[0]
                    md_lines.append("| " + " | ".join(headers) + " |")
                    md_lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
                    for r in rows[1:]:
                        while len(r) < len(headers):
                            r.append(" ")
                        md_lines.append("| " + " | ".join(r[:len(headers)]) + " |")
                    md_lines.append("\n")

    full_md = "\n".join(md_lines)
    full_md = re.sub(r'\n{3,}', '\n\n', full_md)
    output_path.write_text(full_md, encoding="utf-8")
    return full_md, stats


# ======================================================================
# 3. CONVERSOR JUPYTER NOTEBOOK (.ipynb) A MARKDOWN
# ======================================================================

def convert_ipynb_to_markdown(
    ipynb_path: Path,
    output_path: Path,
    extract_images: bool = True
) -> Tuple[str, Dict[str, Any]]:
    """
    Convierte un Notebook de Jupyter (.ipynb) a Markdown:
    - Extrae celdas Markdown y código Python con resaltado de sintaxis.
    - Decodifica y guarda gráficos embebidos (PNG/SVG Base64) a assets/.
    - Formatea salidas de consola y preserva fórmulas matemáticas.
    """
    ipynb_path = Path(ipynb_path)
    output_path = Path(output_path)
    doc_stem = ipynb_path.stem
    assets_dir = output_path.parent / "assets"
    if extract_images:
        assets_dir.mkdir(parents=True, exist_ok=True)

    stats = {"code_cells": 0, "markdown_cells": 0, "images": 0}

    data = json.loads(ipynb_path.read_text(encoding="utf-8"))
    cells = data.get("cells", [])

    md_lines = []
    md_lines.append(f"# {doc_stem.replace('_', ' ').title()}\n")
    md_lines.append(f"> *Convertido automáticamente desde Jupyter Notebook `{ipynb_path.name}`*\n\n---\n")

    for idx, cell in enumerate(cells):
        cell_type = cell.get("cell_type")
        source = "".join(cell.get("source", []))

        if cell_type == "markdown":
            stats["markdown_cells"] += 1
            md_lines.append(f"\n{source.strip()}\n")

        elif cell_type == "code":
            stats["code_cells"] += 1
            md_lines.append(f"\n```python\n{source.strip()}\n```\n")

            outputs = cell.get("outputs", [])
            for out_idx, out in enumerate(outputs):
                out_type = out.get("output_type")

                if out_type == "stream":
                    txt_out = "".join(out.get("text", [])).strip()
                    if txt_out:
                        md_lines.append(f"```text\n[Salida]:\n{txt_out}\n```\n")

                elif out_type in ("display_data", "execute_result"):
                    data_dict = out.get("data", {})
                    if "image/png" in data_dict and extract_images:
                        b64_data = data_dict["image/png"]
                        img_bytes = base64.b64decode(b64_data)
                        img_name = f"{doc_stem}_cell_{idx+1}_{out_idx+1}.png"
                        (assets_dir / img_name).write_bytes(img_bytes)
                        stats["images"] += 1
                        md_lines.append(f"\n![Gráfico {stats['images']}](assets/{img_name})\n")
                    
                    elif "text/latex" in data_dict:
                        latex_str = "".join(data_dict["text/latex"]).strip()
                        md_lines.append(f"\n$$\n{latex_str}\n$$\n")

                    elif "text/plain" in data_dict:
                        txt_plain = "".join(data_dict["text/plain"]).strip()
                        if txt_plain and not txt_plain.startswith("<"):
                            md_lines.append(f"```text\n{txt_plain}\n```\n")

    full_md = "\n".join(md_lines)
    full_md = re.sub(r'\n{3,}', '\n\n', full_md)
    output_path.write_text(full_md, encoding="utf-8")
    return full_md, stats


# ======================================================================
# 4. CONVERSOR MARKDOWN A HTML ACADÉMICO IMPRIMIBLE / PDF
# ======================================================================

def convert_markdown_to_printable_html(
    md_path: Path,
    output_html_path: Path,
    course_title: str = "Sistemes de Mesura · UPC GREELEC"
) -> Path:
    """
    Convierte un archivo Markdown en un documento HTML autocontenido
    con diseño tipográfico premium estilo Apple/macOS, soporte KaTeX/MathJax,
    estilos de impresión (@media print A4) y tabla de contenidos interactiva.
    """
    md_path = Path(md_path)
    output_html_path = Path(output_html_path)
    raw_md = md_path.read_text(encoding="utf-8", errors="replace")

    html_body = []
    lines = raw_md.splitlines()
    in_code = False
    code_lang = ""
    code_buf = []

    for line in lines:
        if line.startswith("```"):
            if not in_code:
                in_code = True
                code_lang = line[3:].strip()
                code_buf = []
            else:
                in_code = False
                joined = "\n".join(code_buf).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                html_body.append(f"<pre><code class=\"language-{code_lang}\">{joined}</code></pre>")
            continue

        if in_code:
            code_buf.append(line)
            continue

        if line.startswith("# "):
            html_body.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith("## "):
            html_body.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("### "):
            html_body.append(f"<h3>{line[4:]}</h3>")
        elif line.startswith("#### "):
            html_body.append(f"<h4>{line[5:]}</h4>")
        elif line.startswith("> [!"):
            m = re.match(r'> \[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION|EXAMPLE)\]', line)
            if m:
                c_type = m.group(1).lower()
                html_body.append(f"<div class=\"callout callout-{c_type}\"><b>{m.group(1)}:</b> ")
            else:
                html_body.append(f"<blockquote>{line[2:]}</blockquote>")
        elif line.startswith("> "):
            html_body.append(f"<blockquote>{line[2:]}</blockquote>")
        elif line.startswith("- "):
            html_body.append(f"<li>{line[2:]}</li>")
        elif line.strip() == "---":
            html_body.append("<hr/>")
        elif line.strip():
            p = line
            p = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', p)
            p = re.sub(r'\*(.+?)\*', r'<em>\1</em>', p)
            p = re.sub(r'`(.+?)`', r'<code>\1</code>', p)
            html_body.append(f"<p>{p}</p>")

    body_content = "\n".join(html_body)

    html_template = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>{md_path.stem} · {course_title}</title>
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  <style>
    :root {{
      --primary: #0a84ff;
      --bg: #ffffff;
      --text: #1d1d1f;
      --border: #d2d2d7;
      --code-bg: #f5f5f7;
    }}
    @media (prefers-color-scheme: dark) {{
      :root {{
        --primary: #2997ff;
        --bg: #161618;
        --text: #f5f5f7;
        --border: #333336;
        --code-bg: #212124;
      }}
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      line-height: 1.65;
      color: var(--text);
      background: var(--bg);
      max-width: 880px;
      margin: 0 auto;
      padding: 40px 24px;
    }}
    h1 {{ font-size: 2.2em; border-bottom: 2px solid var(--primary); padding-bottom: 10px; margin-top: 20px; }}
    h2 {{ font-size: 1.6em; border-bottom: 1px solid var(--border); padding-bottom: 6px; margin-top: 30px; }}
    h3 {{ font-size: 1.3em; margin-top: 24px; }}
    p, li {{ font-size: 15px; }}
    code {{ background: var(--code-bg); padding: 2px 6px; border-radius: 4px; font-family: "SF Mono", monospace; font-size: 13px; }}
    pre {{ background: var(--code-bg); padding: 16px; border-radius: 8px; overflow-x: auto; border: 1px solid var(--border); }}
    table {{ width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 14px; }}
    th, td {{ border: 1px solid var(--border); padding: 8px 12px; text-align: left; }}
    th {{ background: var(--code-bg); font-weight: 600; }}
    blockquote {{ border-left: 4px solid var(--primary); margin: 16px 0; padding-left: 14px; color: #86868b; }}
    .callout {{ border-left: 4px solid var(--primary); background: rgba(10,132,255,0.06); padding: 12px 16px; border-radius: 6px; margin: 16px 0; }}
    .callout-warning {{ border-color: #ff9f0a; background: rgba(255,159,10,0.08); }}
    .callout-caution {{ border-color: #ff453a; background: rgba(255,69,58,0.08); }}
    .callout-tip {{ border-color: #30d158; background: rgba(48,209,88,0.08); }}
    .header-bar {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border); padding-bottom: 12px; margin-bottom: 30px; }}
    .btn-print {{ background: var(--primary); color: white; border: none; padding: 8px 16px; border-radius: 6px; font-weight: bold; cursor: pointer; }}
    @media print {{
      .header-bar, .btn-print {{ display: none; }}
      body {{ max-width: 100%; padding: 0; background: #fff !important; color: #000 !important; }}
      h1, h2, h3 {{ page-break-after: avoid; }}
      pre, table {{ page-break-inside: avoid; }}
      @page {{ size: A4; margin: 2cm; }}
    }}
  </style>
</head>
<body>
  <div class="header-bar">
    <div>
      <span style="font-size: 13px; color: var(--primary); font-weight: bold;">{course_title}</span>
      <div style="font-size: 11px; color: #86868b;">Documento Técnico Oficial Generado</div>
    </div>
    <button class="btn-print" onclick="window.print()">🖨️ Guardar PDF / Imprimir</button>
  </div>
  {body_content}
</body>
</html>"""

    output_html_path.write_text(html_template, encoding="utf-8")
    return output_html_path


# ======================================================================
# 5. CONVERSOR MARKDOWN A ANKI (.apkg y .tsv)
# ======================================================================

def convert_markdown_to_anki(
    md_paths: List[Path],
    output_tsv: Path,
    output_apkg: Optional[Path] = None,
    deck_name: str = "Sistemes de Mesura · Examen UPC"
) -> Dict[str, Any]:
    """
    Extrae automáticamente preguntas de test, definiciones de glosario y tarjetas
    conceptuales desde archivos Markdown, generando:
    - Archivo TSV universal compatible con Anki Web y Desktop.
    - Paquete binario .apkg auto-importable con soporte MathJax y Dark Mode.
    """
    output_tsv = Path(output_tsv)
    tsv_lines = []
    cards_data = []

    re_q_block = re.compile(r'(?:###|\*\*|\[P\d+\])\s*([^\n\?]+[\?:]?)(.*?)(?:Respuesta|Solución|Correcta|Oficial):\s*([^\n]+)', re.IGNORECASE | re.DOTALL)
    re_def = re.compile(r'^\s*[-*]?\s*\*\*([^*]+)\*\*:\s*(.+)$', re.MULTILINE)

    for p in md_paths:
        p = Path(p)
        if not p.exists() or p.suffix.lower() != '.md':
            continue
        text = p.read_text(encoding="utf-8", errors="replace")

        # 1. Preguntas de test
        for m in re_q_block.finditer(text):
            q_text = m.group(1).strip()
            details = m.group(2).strip().replace("\t", " ")
            ans = m.group(3).strip()
            
            front = f"<div style='font-size:16px; font-weight:bold;'>{q_text}</div>"
            if details:
                front += f"<div style='font-size:13px; margin-top:8px; color:#94a3b8;'>{details}</div>"
            
            back = f"<div style='font-size:18px; font-weight:bold; color:#30d158;'>Respuesta: {ans}</div>"
            back += f"<div style='font-size:11px; margin-top:10px; color:#86868b;'>Tema: {p.stem}</div>"

            cards_data.append((front, back, p.stem))
            tsv_lines.append(f"{front}\t{back}\t{p.stem}")

        # 2. Definiciones técnicas
        for m in re_def.finditer(text):
            term = m.group(1).strip()
            definition = m.group(2).strip().replace("\t", " ")
            if len(term) < 60 and len(definition) > 15:
                front = f"<div style='font-size:18px; font-weight:bold; color:#38bdf8;'>{term}</div>"
                back = f"<div style='font-size:14px; line-height:1.5;'>{definition}</div>"
                back += f"<div style='font-size:11px; margin-top:10px; color:#86868b;'>Fuente: {p.stem}</div>"
                cards_data.append((front, back, p.stem))
                tsv_lines.append(f"{front}\t{back}\t{p.stem}")

    output_tsv.parent.mkdir(parents=True, exist_ok=True)
    output_tsv.write_text("\n".join(tsv_lines), encoding="utf-8")

    apkg_generated = False
    if HAS_GENANKI and output_apkg and cards_data:
        try:
            model_id = 1607392319
            deck_id = 2059382910
            
            custom_model = genanki.Model(
                model_id,
                'Modelo Cientifico UPC Dark',
                fields=[{'name': 'Question'}, {'name': 'Answer'}, {'name': 'Topic'}],
                templates=[{
                    'name': 'Card 1',
                    'qfmt': '{{Question}}',
                    'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
                }],
                css="""
                .card {
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                    text-align: center;
                    font-size: 15px;
                    color: #f5f5f7;
                    background-color: #161820;
                    padding: 24px;
                }
                b { color: #0a84ff; }
                hr { border: none; border-top: 1px solid #333a4d; margin: 18px 0; }
                """
            )

            deck = genanki.Deck(deck_id, deck_name)
            for f, b, tag in cards_data:
                note = genanki.Note(model=custom_model, fields=[f, b, tag], tags=[tag.replace(" ", "_")])
                deck.add_note(note)

            genanki.Package(deck).write_to_file(str(output_apkg))
            apkg_generated = True
        except Exception:
            pass

    return {
        "total_cards": len(cards_data),
        "tsv_path": str(output_tsv),
        "apkg_path": str(output_apkg) if apkg_generated else None
    }


# ======================================================================
# 6. CONVERSOR EXCEL / CSV A TABLAS MARKDOWN GFM
# ======================================================================

def convert_excel_csv_to_markdown(
    file_path: Path,
    output_path: Path
) -> Tuple[str, int]:
    """
    Convierte una hoja de cálculo Excel (.xlsx, .xls) o archivo CSV
    en tablas Markdown estándar GFM con alineación de columnas.
    """
    file_path = Path(file_path)
    output_path = Path(output_path)
    ext = file_path.suffix.lower()

    tables_count = 0
    md_lines = [f"# Datos de Laboratorio: {file_path.stem.replace('_', ' ').title()}\n"]

    if ext == ".csv":
        import csv
        with open(file_path, mode='r', encoding='utf-8', errors='replace') as f:
            reader = csv.reader(f)
            rows = [r for r in reader if any(c.strip() for c in r)]
            if rows:
                tables_count += 1
                headers = rows[0]
                md_lines.append("| " + " | ".join(headers) + " |")
                md_lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
                for r in rows[1:]:
                    while len(r) < len(headers): r.append("")
                    md_lines.append("| " + " | ".join(r[:len(headers)]) + " |")
                md_lines.append("\n")

    elif ext in (".xlsx", ".xls"):
        if not HAS_PANDAS:
            raise RuntimeError("La librería 'pandas' es requerida para procesar archivos Excel.")
        excel_file = pd.ExcelFile(str(file_path))
        for sheet_name in excel_file.sheet_names:
            df = excel_file.parse(sheet_name)
            if not df.empty:
                tables_count += 1
                md_lines.append(f"### Hoja: {sheet_name}\n")
                md_table = df.to_markdown(index=False)
                md_lines.append(md_table + "\n\n")

    full_md = "\n".join(md_lines)
    output_path.write_text(full_md, encoding="utf-8")
    return full_md, tables_count


# ======================================================================
# 7. EXTRACTOR DE FORMULARIO RESUMEN DE ECUACIONES
# ======================================================================

def extract_formula_sheet_from_files(
    md_paths: List[Path],
    output_path: Path,
    course_name: str = "Sistemes de Mesura (UPC EEBE)"
) -> Tuple[str, int]:
    """
    Examina una lista de documentos Markdown, extrae todas las fórmulas LaTeX
    únicas (inline y display) y compila un Formulario Maestro clasificado por temas.
    """
    output_path = Path(output_path)
    total_formulas = 0
    doc_sections = []

    re_display = re.compile(r'\$\$(.+?)\$\$', re.DOTALL)
    re_inline = re.compile(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)')

    for p in sorted(md_paths):
        p = Path(p)
        if not p.exists() or p.suffix.lower() != '.md':
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        
        formulas_in_doc = set()
        for m in re_display.finditer(text):
            f = m.group(1).strip()
            if len(f) > 3 and not f.startswith("!"):
                formulas_in_doc.add(f)

        for m in re_inline.finditer(text):
            f = m.group(1).strip()
            if any(op in f for op in ['=', r'\frac', r'\sqrt', r'\int', r'\sum', r'\alpha', r'\beta', r'\Delta']) and len(f) > 3:
                formulas_in_doc.add(f)

        if formulas_in_doc:
            doc_sections.append((p.stem.replace("_", " ").title(), list(formulas_in_doc)))
            total_formulas += len(formulas_in_doc)

    md_out = [
        f"# 📐 Formulario Oficial de Ecuaciones y Modelos Matemáticos\n",
        f"> **Asignatura:** {course_name}  \n",
        f"> **Total Fórmulas Compiladas:** {total_formulas} ecuaciones únicas  \n\n---\n"
    ]

    for topic_title, f_list in doc_sections:
        md_out.append(f"## 📚 {topic_title}\n")
        md_out.append("| Nº | Expresión Matemática (LaTeX) | Formato Display |\n| :--- | :--- | :--- |")
        for i, form in enumerate(sorted(f_list), 1):
            clean_f = form.replace("|", r"\|").replace("\n", " ")
            md_out.append(f"| {i} | `${clean_f}$` | $${clean_f}$$ |")
        md_out.append("\n")

    result = "\n".join(md_out)
    output_path.write_text(result, encoding="utf-8")
    return result, total_formulas


# ======================================================================
# 8. EXTRACTOR DE NETLISTS SPICE / LTSPICE
# ======================================================================

def extract_spice_netlists_from_files(
    md_paths: List[Path],
    output_dir: Path
) -> List[Path]:
    """
    Busca bloques de código ```spice o ```cir en los documentos y los guarda
    como archivos ejecutables de simulación (.cir) para LTspice o Ngspice.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    created_files = []

    re_spice = re.compile(r'```(?:spice|cir)\s*\n(.*?)\n```', re.DOTALL | re.IGNORECASE)

    for p in md_paths:
        p = Path(p)
        if not p.exists() or p.suffix.lower() != '.md':
            continue
        text = p.read_text(encoding="utf-8", errors="replace")

        matches = re_spice.findall(text)
        for idx, spice_code in enumerate(matches):
            circuit_name = f"{p.stem}_circuito_{idx+1}.cir"
            out_file = output_dir / circuit_name
            out_file.write_text(spice_code.strip() + "\n", encoding="utf-8")
            created_files.append(out_file)

    return created_files


# ======================================================================
# 9. GENERADOR DE GLOSARIO TÉCNICO INDEXADO (A-Z)
# ======================================================================

def generate_technical_glossary_from_files(
    md_paths: List[Path],
    output_path: Path
) -> Tuple[str, int]:
    """
    Extrae todos los términos clave definidos en negrita en los documentos,
    los clasifica alfabéticamente (A-Z) y genera un diccionario técnico.
    """
    output_path = Path(output_path)
    terms_dict = {}

    re_term = re.compile(r'^\s*[-*]?\s*\*\*([A-Za-zÁÉÍÓÚáéíóú0-9\s\-_/]{3,50})\*\*:\s*([^\n]{20,})', re.MULTILINE)

    for p in md_paths:
        p = Path(p)
        if not p.exists() or p.suffix.lower() != '.md':
            continue
        text = p.read_text(encoding="utf-8", errors="replace")

        for m in re_term.finditer(text):
            t = m.group(1).strip()
            d = m.group(2).strip()
            if t not in terms_dict:
                terms_dict[t] = []
            terms_dict[t].append((d, p.stem))

    sorted_terms = sorted(terms_dict.keys(), key=lambda s: s.upper())
    md_out = [
        "# 📖 Glosario Técnico de Metrología e Instrumentación (A-Z)\n",
        f"> **Términos Totales Catalogados:** {len(sorted_terms)} conceptos clave  \n\n---\n"
    ]

    current_letter = ""
    for term in sorted_terms:
        first_char = term[0].upper()
        if first_char != current_letter:
            current_letter = first_char
            md_out.append(f"\n## 🔤 {current_letter}\n")

        defs = terms_dict[term]
        main_def, source = defs[0]
        md_out.append(f"- **{term}**: {main_def} *(Fuente: {source})*")

    result = "\n".join(md_out)
    output_path.write_text(result, encoding="utf-8")
    return result, len(sorted_terms)


# ======================================================================
# 10. MOTOR DE CONVERSIÓN POR LOTES UNIVERSAL (BATCH ENGINE)
# ======================================================================

def batch_convert_universal(
    input_dir: Path,
    output_dir: Path,
    progress_callback: Optional[Callable[[int, str], None]] = None
) -> Dict[str, Any]:
    """
    Escanea recursivamente un directorio procesando automáticamente:
    .html / .htm -> Markdown de alta fidelidad
    .pdf         -> Markdown científico
    .docx        -> Markdown con OMML a LaTeX
    .ipynb       -> Markdown con salidas y gráficos
    .xlsx / .csv -> Tablas Markdown GFM
    Genera además el Gran Índice, el Formulario Resumen y el Glosario.
    """
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    supported_extensions = {".html", ".htm", ".pdf", ".docx", ".ipynb", ".xlsx", ".csv"}
    all_files = [f for f in input_dir.rglob("*") if f.is_file() and f.suffix.lower() in supported_extensions]

    stats = {
        "total_files": len(all_files),
        "html_count": 0,
        "pdf_count": 0,
        "docx_count": 0,
        "ipynb_count": 0,
        "excel_count": 0,
        "converted_files": []
    }

    converted_md_paths = []

    for idx, f in enumerate(all_files):
        ext = f.suffix.lower()
        if progress_callback:
            progress_callback(int((idx / max(1, len(all_files))) * 100), f"Procesando: {f.name}")

        rel_path = f.relative_to(input_dir)
        target_md = output_dir / rel_path.with_suffix(".md")
        target_md.parent.mkdir(parents=True, exist_ok=True)

        try:
            if ext in (".html", ".htm"):
                from conversor_html_notebooklm import convert_single_html_file
                convert_single_html_file(f, target_md)
                stats["html_count"] += 1
                converted_md_paths.append(target_md)
            elif ext == ".pdf":
                convert_pdf_to_markdown(f, target_md)
                stats["pdf_count"] += 1
                converted_md_paths.append(target_md)
            elif ext == ".docx":
                convert_docx_to_markdown(f, target_md)
                stats["docx_count"] += 1
                converted_md_paths.append(target_md)
            elif ext == ".ipynb":
                convert_ipynb_to_markdown(f, target_md)
                stats["ipynb_count"] += 1
                converted_md_paths.append(target_md)
            elif ext in (".xlsx", ".csv"):
                convert_excel_csv_to_markdown(f, target_md)
                stats["excel_count"] += 1
                converted_md_paths.append(target_md)
            
            stats["converted_files"].append(str(target_md))
        except Exception:
            pass

    if converted_md_paths:
        try:
            form_file = output_dir / "_Formulario_Oficial_Examen.md"
            extract_formula_sheet_from_files(converted_md_paths, form_file)
            gloss_file = output_dir / "_Glosario_Conceptos_Clave.md"
            generate_technical_glossary_from_files(converted_md_paths, gloss_file)
        except Exception:
            pass

    return stats
