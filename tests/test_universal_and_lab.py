"""
Test Suite for Universal Converters, Flashcards, Instrumentation, and Virtual Lab
"""
import os
import sys
import json
from pathlib import Path
import pytest
from bs4 import BeautifulSoup

# Ensure project root is on sys.path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import universal_converters as uc
import conversor_html_notebooklm as app


def test_universal_converters_functions_exist():
    assert callable(uc.convert_pdf_to_markdown)
    assert callable(uc.convert_docx_to_markdown)
    assert callable(uc.convert_ipynb_to_markdown)
    assert callable(uc.convert_markdown_to_printable_html)
    assert callable(uc.convert_markdown_to_anki)
    assert callable(uc.convert_excel_csv_to_markdown)
    assert callable(uc.extract_formula_sheet_from_files)
    assert callable(uc.extract_spice_netlists_from_files)
    assert callable(uc.generate_technical_glossary_from_files)
    assert callable(uc.batch_convert_universal)


def test_ipynb_converter(tmp_path):
    nb_data = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["# Sensor Measurement\n", "Bridge equation: $V_o = V_s \\cdot \\frac{\\Delta R}{4R}$"]
            },
            {
                "cell_type": "code",
                "execution_count": 1,
                "metadata": {},
                "outputs": [
                    {
                        "name": "stdout",
                        "output_type": "stream",
                        "text": ["Sensitivity: 2.5 mV/V\n"]
                    }
                ],
                "source": ["R0 = 120\n", "dR = 1.2\n", "print('Done')"]
            }
        ],
        "metadata": {
            "language_info": {"name": "python"}
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }
    nb_file = tmp_path / "test_nb.ipynb"
    nb_file.write_text(json.dumps(nb_data), encoding="utf-8")
    out_md = tmp_path / "output_nb.md"
    
    md_content, meta = uc.convert_ipynb_to_markdown(nb_file, out_md, extract_images=False)
    assert "# Sensor Measurement" in md_content
    assert "Bridge equation" in md_content
    assert "Sensitivity: 2.5 mV/V" in md_content
    assert out_md.exists()


def test_markdown_to_printable_html(tmp_path):
    md_file = tmp_path / "input.md"
    md_file.write_text("# Laboratori de Sensors\n\nEquació: $$V_{out} = G \\cdot (V_+ - V_-)$$\n\n| Sensor | Tipus |\n|---|---|\n| Pt100 | RTD |", encoding="utf-8")
    out_html = tmp_path / "output.html"
    
    res_path = uc.convert_markdown_to_printable_html(md_file, out_html, course_title="Guia UPC")
    assert res_path.exists()
    html_content = res_path.read_text(encoding="utf-8")
    assert "<!DOCTYPE html>" in html_content
    assert "mathjax" in html_content.lower() or "katex" in html_content.lower()
    assert "Pt100" in html_content


def test_markdown_to_anki(tmp_path):
    md_file = tmp_path / "questions.md"
    md_file.write_text("""# Preguntes d'Examen

### Pregunta 1: Com funciona un pont de Wheatstone?
Mesura variacions de resistència convertint-les en tensió diferencial de sortida.
Respuesta: Convertidor de resistència a tensió mitjançant 4 branques.

* **Pt100 RTD**: Sensor de temperatura resistiu amb coeficient positiu alpha de 0.00385 ohms/ohm/C.
""", encoding="utf-8")
    
    tsv_out = tmp_path / "flashcards.tsv"
    stats = uc.convert_markdown_to_anki([md_file], tsv_out)
    assert tsv_out.exists()
    assert stats["total_cards"] >= 2


def test_extract_formula_sheet(tmp_path):
    md_file = tmp_path / "course.md"
    md_file.write_text("""
El factor de galga ve donat per:
$$GF = \\frac{\\Delta R / R}{\\epsilon} = 1 + 2\\nu + \\frac{\\Delta \\rho / \\rho}{\\epsilon}$$

Per a un filtre Sallen-Key:
$$f_c = \\frac{1}{2\\pi \\sqrt{R_1 R_2 C_1 C_2}}$$
""", encoding="utf-8")
    
    out_sheet = tmp_path / "formulas.md"
    sheet, count = uc.extract_formula_sheet_from_files([md_file], out_sheet)
    assert out_sheet.exists()
    assert count >= 2
    assert "GF =" in sheet or "Delta R" in sheet or "f_c =" in sheet


def test_extract_spice_netlist(tmp_path):
    md_file = tmp_path / "circuits.md"
    md_file.write_text("""
```spice
* Filtre Passabaix Actiu Sallen-Key
V1 in 0 SIN(0 1 1k)
R1 in n1 10k
R2 n1 out 10k
C1 n1 out 10nF
C2 out 0 10nF
.tran 0.1m 10m
.end
```
""", encoding="utf-8")
    
    netlists = uc.extract_spice_netlists_from_files([md_file], tmp_path)
    assert len(netlists) >= 1
    assert netlists[0].exists()
    content = netlists[0].read_text(encoding="utf-8")
    assert "Sallen-Key" in content
    assert ".end" in content


def test_technical_glossary(tmp_path):
    md_file = tmp_path / "notes.md"
    md_file.write_text("""
* **CMRR**: Common-Mode Rejection Ratio quina mesura la capacitat d'un amplificador diferencial d'atenuar pertorbacions comunes.
* **Offset Voltage**: Tensio d'entrada diferencial necessaria per anul·lar la sortida d'un AO real.
""", encoding="utf-8")
    out_glossary = tmp_path / "glossary.md"
    glossary, count = uc.generate_technical_glossary_from_files([md_file], out_glossary)
    assert out_glossary.exists()
    assert count >= 1
    assert "CMRR" in glossary


def test_flashcards_generator(tmp_path):
    # Create a mock entrenament html file with BANC format
    mock_html = tmp_path / "Tema 1_entrenament.html"
    banc_json = [
        {
            "n": 1,
            "q": "El sensor Pt100 es un sensor de temperatura resistiu lineal de platí.",
            "a": "V",
            "j": "Presenta una relació altament precisa de resistència en funció de la temperatura.",
            "df": "IEC 60751"
        }
    ]
    mock_html.write_text(f"""
    <html><body>
    <script>
    const BANC = {json.dumps(banc_json)};
    function check() {{}}
    </script>
    </body></html>
    """, encoding="utf-8")
    
    tsv_path = app.generate_course_flashcards_tsv(tmp_path, tmp_path)
    assert tsv_path is not None
    assert tsv_path.exists()
    content = tsv_path.read_text(encoding="utf-8")
    assert "Tema 1" in content or "Tema_1" in content
    assert "Pt100" in content


def test_virtual_lab_html_integrity():
    lab_path = os.path.join(root_dir, "Laboratorio_Virtual_Sensores.html")
    assert os.path.exists(lab_path)
    
    with open(lab_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Check title
    assert "Laboratorio Virtual de Sensores" in soup.title.string
    
    # 2. Check subject filter buttons
    subject_bar = soup.find('div', class_='subject-bar-container')
    assert subject_bar is not None
    assert "SM: Mesura" in subject_bar.text
    assert "CCE: Circuits" in subject_bar.text
    assert "PEE: Potència" in subject_bar.text
    assert "CAF: Camps & RF" in subject_bar.text
    assert "SC: Control" in subject_bar.text
    
    # 3. Check all 20 modules in MODULE_DATA by title number
    for m_id in range(1, 21):
        assert f'{m_id}. ' in html, f"Module {m_id} not found in lab HTML"
        
    # Check new modules 17..20
    assert "ISO124" in html
    assert "Lock-In" in html or "Demodulador" in html
    assert "4-20" in html or "4-20mA" in html
    assert "Roseta de Galgues" in html or "Cercle de Mohr" in html
    
    # 4. Check new instruments modals
    assert soup.find('div', id='modal-logic') is not None
    assert soup.find('div', id='modal-noise') is not None
    assert soup.find('div', id='modal-firmware') is not None
    
    # 5. Check black screen fix in JS
    assert "build3DGeometry()" in html
    assert "window.onload" in html


if __name__ == '__main__':
    pytest.main(["-v", __file__])
