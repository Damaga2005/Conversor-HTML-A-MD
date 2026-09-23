# -*- coding: utf-8 -*-
"""
Tests for High-Precision Multi-Format Formula and Problem Extraction
====================================================================
Verifies:
1. OMML-to-LaTeX converter (Word DOCX formulas: fractions, matrices, integrals, sums, limits, radicals, delimiters).
2. HTML & MathML / KaTeX / data-latex formula shielding and conversion to pure LaTeX.
3. Universal Multi-Format Formula Sheet Extractor (extract_formula_sheet_from_files).
4. Universal Problem & Exercise Extractor (extract_problems_from_files and extract_problems_from_text).
5. LaTeX formula syntax cleaning and auto-balancing (clean_latex_formula).
"""
import pytest
import xml.etree.ElementTree as ET
from pathlib import Path

import universal_converters as uc
import conversor_html_notebooklm as chn

def test_omml_fractions_and_radicals():
    ns = uc.OMML_NS
    
    # 1. Fraction: num / den
    f_xml = """<m:f xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
        <m:num><m:t>V_s</m:t></m:num>
        <m:den><m:t>R_1 + R_2</m:t></m:den>
    </m:f>"""
    f_elem = ET.fromstring(f_xml)
    tex = uc.omml_to_latex(f_elem, ns)
    assert tex == r"\frac{V_s}{R_1 + R_2}"

    # 2. Square Root
    rad_xml = """<m:rad xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
        <m:deg/>
        <m:e><m:t>2 \cdot \pi \cdot f</m:t></m:e>
    </m:rad>"""
    rad_elem = ET.fromstring(rad_xml)
    tex_rad = uc.omml_to_latex(rad_elem, ns)
    assert tex_rad == r"\sqrt{2 \cdot \pi \cdot f}"

    # 3. N-th Root: \sqrt[3]{x}
    nrad_xml = """<m:rad xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
        <m:deg><m:t>3</m:t></m:deg>
        <m:e><m:t>x^2 + 1</m:t></m:e>
    </m:rad>"""
    nrad_elem = ET.fromstring(nrad_xml)
    tex_nrad = uc.omml_to_latex(nrad_elem, ns)
    assert tex_nrad == r"\sqrt[3]{x^2 + 1}"

def test_omml_matrix():
    ns = uc.OMML_NS
    m_xml = """<m:m xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
        <m:mr>
            <m:e><m:t>z11</m:t></m:e>
            <m:e><m:t>z12</m:t></m:e>
        </m:mr>
        <m:mr>
            <m:e><m:t>z21</m:t></m:e>
            <m:e><m:t>z22</m:t></m:e>
        </m:mr>
    </m:m>"""
    m_elem = ET.fromstring(m_xml)
    tex = uc.omml_to_latex(m_elem, ns)
    assert r"\begin{matrix}" in tex
    assert "z11 & z12" in tex
    assert r"\\" in tex
    assert r"\end{matrix}" in tex

def test_omml_nary_and_limits():
    ns = uc.OMML_NS
    
    # Sum with limits: \sum_{i=1}^{N} x_i
    sum_xml = """<m:nary xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
        <m:naryPr><m:chr m:val="∑"/></m:naryPr>
        <m:sub><m:t>i=1</m:t></m:sub>
        <m:sup><m:t>N</m:t></m:sup>
        <m:e><m:t>x_i</m:t></m:e>
    </m:nary>"""
    sum_elem = ET.fromstring(sum_xml)
    tex_sum = uc.omml_to_latex(sum_elem, ns)
    assert r"\sum" in tex_sum
    assert "_{i=1}" in tex_sum
    assert "^{N}" in tex_sum
    assert "x_i" in tex_sum

    # Integral: \int_{0}^{\infty} e^{-st} dt
    int_xml = """<m:nary xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
        <m:naryPr><m:chr m:val="∫"/></m:naryPr>
        <m:sub><m:t>0</m:t></m:sub>
        <m:sup><m:t>\infty</m:t></m:sup>
        <m:e><m:t>e^{-st} dt</m:t></m:e>
    </m:nary>"""
    int_elem = ET.fromstring(int_xml)
    tex_int = uc.omml_to_latex(int_elem, ns)
    assert r"\int" in tex_int
    assert "_{0}" in tex_int
    assert "^{\infty}" in tex_int

def test_omml_accents_and_boxes():
    ns = uc.OMML_NS
    
    # Vector: \vec{v}
    vec_xml = """<m:acc xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
        <m:accPr><m:chr m:val="→"/></m:accPr>
        <m:e><m:t>v</m:t></m:e>
    </m:acc>"""
    vec_elem = ET.fromstring(vec_xml)
    assert uc.omml_to_latex(vec_elem, ns) == r"\vec{v}"

    # Box: \boxed{E = mc^2}
    box_xml = """<m:box xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
        <m:e><m:t>E = mc^2</m:t></m:e>
    </m:box>"""
    box_elem = ET.fromstring(box_xml)
    assert uc.omml_to_latex(box_elem, ns) == r"\boxed{E = mc^2}"

def test_clean_latex_formula():
    # 1. Unclosed braces auto-balance
    t1 = uc.clean_latex_formula(r"\frac{V_o}{V_s")
    assert t1.count("{") == t1.count("}")

    # 2. Wikipedia displaystyle cleanup
    t2 = uc.clean_latex_formula(r"{\displaystyle \int_0^T f(t) dt}")
    assert "displaystyle" not in t2
    assert r"\int" in t2

    # 3. Unicode square root
    t3 = uc.clean_latex_formula("√(R^2 + X^2)")
    assert t3 == r"\sqrt{R^2 + X^2}"

    # 4. Standard trig/log function backslashes
    t4 = uc.clean_latex_formula("sin(omega * t) + cos(phi)")
    assert r"\sin" in t4
    assert r"\cos" in t4

def test_html_math_shielding():
    from bs4 import BeautifulSoup
    html = """
    <div>
        <p>Ecuación en span: <span data-latex="V_o = V_s \\cdot \\frac{R_2}{R_1 + R_2}">formula</span></p>
        <math display="block">
            <mfrac>
                <mrow><mi>Δ</mi><mi>R</mi></mrow>
                <mrow><msub><mi>R</mi><mn>0</mn></msub></mrow>
            </mfrac>
        </math>
        <div class="problem">
            <h3>Problema 1: Sensor de Presión</h3>
            <p>Se dispone de un puente con sensibilidad S = 2.5 mV/V y alimentación Vs = 10 V.</p>
        </div>
    </div>
    """
    soup = BeautifulSoup(html, "html.parser")
    soup, registry, count = chn.extract_and_shield_math(soup)
    assert count >= 2
    assert any("V_o" in v for v in registry.values())
    assert any(r"\frac" in v for v in registry.values())

def test_extract_problems_from_text():
    sample_text = """
# Guía de Problemas Oficiales

## Problema 1: Cadena Piezorresistiva con Galgas
### Enunciado
Se instrumenta una viga en voladizo para medir deformaciones mecánicas.
Constante nominal R0 = 120.0 Ohm y factor de galga K = 2.05. Tensión Vs = 10.0 V.

Se pide:
1. Calcular la variación máxima de resistencia.
2. Deducir la tensión de salida.

### Solución
La variación de resistencia viene dada por:
$$ \Delta R = R_0 \cdot K \cdot \varepsilon $$
Sustituyendo los datos:
$$ \Delta R = 0.369\,\Omega $$
**Resultado:** $\boxed{0.369\,\Omega}$
"""
    probs = uc.extract_problems_from_text(sample_text, source_name="test_doc.md")
    assert len(probs) == 1
    p = probs[0]
    assert "Problema 1" in p["id"]
    assert "Galgas" in p["title"]
    assert len(p["parameters"]) >= 3
    assert len(p["questions"]) >= 2
    assert r"\Delta R" in p["solution"]
    assert len(p["boxed_answers"]) >= 1

def test_multi_format_formula_sheet_extractor(tmp_path):
    # Create sample MD
    md_file = tmp_path / "tema1.md"
    md_file.write_text("# Tema 1\nFormula: $$V = I \\cdot R$$\nY también: $P = V \\cdot I$\n", encoding="utf-8")

    # Create sample HTML
    html_file = tmp_path / "tema2.html"
    html_file.write_text("<html><body><p>Ley de Coulomb: <span data-latex=\"F = k \\frac{q_1 q_2}{r^2}\">F</span></p></body></html>", encoding="utf-8")

    out_file = tmp_path / "_Formulario_Maestro.md"
    md_result, count = uc.extract_formula_sheet_from_files([md_file, html_file], out_file)

    assert count >= 3
    assert out_file.exists()
    content = out_file.read_text(encoding="utf-8")
    assert "Tema 1" in content
    assert "Tema 2" in content
    assert "V = I" in content
    assert "q_1" in content

def test_multi_format_problem_extractor(tmp_path):
    md_file = tmp_path / "ejercicios.md"
    md_file.write_text("""
## Ejercicio 1: Divisor de Tensión
### Enunciado
Calcular la tensión en R2 para Vin = 24.0 V, R1 = 1000 Ohm y R2 = 2000 Ohm.
### Solución
$$ V_{out} = V_{in} \\frac{R_2}{R_1 + R_2} = 16.0\\,\\text{V} $$
**Resultado:** $\\boxed{16.0\\,\\text{V}}$
""", encoding="utf-8")

    out_file = tmp_path / "_Banco_Problemas.md"
    md_result, probs = uc.extract_problems_from_files([md_file], out_file)

    assert len(probs) == 1
    assert out_file.exists()
    content = out_file.read_text(encoding="utf-8")
    assert "Ejercicio 1" in content
    assert "Divisor de Tensión" in content
    assert "16.0" in content
