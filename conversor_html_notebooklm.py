import os
import re
import sys
import time
import json
import base64
import threading
import subprocess
import sqlite3
import zipfile
import hashlib
import random
import tempfile
from pathlib import Path
import webbrowser
from collections import defaultdict
from typing import Optional

# Configurar stdout/stderr a UTF-8 de forma segura para consola Windows
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.scrolledtext import ScrolledText
from bs4 import BeautifulSoup, Tag, NavigableString, Comment
import markdownify

# ----------------------------------------------------------------------
# 1. TABLA DE OPERADORES Y SÍMBOLOS MATEMÁTICOS PARA MATHML
# ----------------------------------------------------------------------
OPERATOR_MAP = {
    "±": r"\pm", "&plusmn;": r"\pm",
    "×": r"\times", "&times;": r"\times",
    "÷": r"\div", "&divide;": r"\div",
    "·": r"\cdot", "•": r"\bullet",
    "≤": r"\le", "&le;": r"\le",
    "≥": r"\ge", "&ge;": r"\ge",
    "≠": r"\ne", "&ne;": r"\ne",
    "≈": r"\approx", "&asymp;": r"\approx",
    "≡": r"\equiv", "&equiv;": r"\equiv",
    "∈": r"\in", "&isin;": r"\in",
    "∉": r"\notin", "&notin;": r"\notin",
    "⊂": r"\subset", "&sub;": r"\subset",
    "⊆": r"\subseteq", "&sube;": r"\subseteq",
    "⊄": r"\not\subset", "⊈": r"\not\subseteq",
    "⊃": r"\supset", "&sup;": r"\supset",
    "⊇": r"\supseteq", "&supe;": r"\supseteq",
    "∪": r"\cup", "&cup;": r"\cup",
    "∩": r"\cap", "&cap;": r"\cap",
    "∖": r"\setminus", "∅": r"\emptyset",
    "∑": r"\sum", "&sum;": r"\sum",
    "∏": r"\prod", "&prod;": r"\prod",
    "∐": r"\coprod",
    "∫": r"\int", "&int;": r"\int",
    "∬": r"\iint", "∭": r"\iiint", "∮": r"\oint",
    "∂": r"\partial", "&part;": r"\partial",
    "∇": r"\nabla", "&nabla;": r"\nabla",
    "∞": r"\infty", "&infin;": r"\infty",
    "→": r"\to", "⟶": r"\longrightarrow", "←": r"\leftarrow", "⟵": r"\longleftarrow",
    "⇒": r"\Rightarrow", "⟹": r"\Longrightarrow", "⇐": r"\Leftarrow", "⟸": r"\Longleftarrow",
    "⇔": r"\Leftrightarrow", "⟺": r"\Longleftrightarrow",
    "↔": r"\leftrightarrow", "↕": r"\updownarrow",
    "↑": r"\uparrow", "↓": r"\downarrow", "⇑": r"\Uparrow", "⇓": r"\Downarrow",
    "↦": r"\mapsto", "⟼": r"\longmapsto",
    "∀": r"\forall", "∃": r"\exists", "∄": r"\nexists",
    "¬": r"\neg", "∧": r"\land", "∨": r"\lor", "⊕": r"\oplus", "⊗": r"\otimes",
    "…": r"\dots", "...": r"\dots", "⋯": r"\cdots", "⋮": r"\vdots", "⋱": r"\ddots",
    "°": r"^\circ", "′": "'", "″": "''",
    "∝": r"\propto", "∝": r"\propto", "∼": r"\sim", "≃": r"\simeq",
    "⊥": r"\perp", "∥": r"\parallel", "∠": r"\angle",
    "α": r"\alpha", "β": r"\beta", "γ": r"\gamma", "δ": r"\delta",
    "ε": r"\varepsilon", "ϵ": r"\epsilon", "ζ": r"\zeta", "η": r"\eta",
    "θ": r"\theta", "ϑ": r"\vartheta", "ι": r"\iota", "κ": r"\kappa",
    "λ": r"\lambda", "μ": r"\mu", "ν": r"\nu", "ξ": r"\xi",
    "π": r"\pi", "ϖ": r"\varpi", "ρ": r"\rho", "ϱ": r"\varrho",
    "σ": r"\sigma", "ς": r"\varsigma", "τ": r"\tau", "υ": r"\upsilon",
    "φ": r"\varphi", "ϕ": r"\phi", "χ": r"\chi", "ψ": r"\psi", "ω": r"\omega",
    "Γ": r"\Gamma", "Δ": r"\Delta", "Θ": r"\Theta", "Λ": r"\Lambda",
    "Ξ": r"\Xi", "Π": r"\Pi", "Σ": r"\Sigma", "Υ": r"\Upsilon",
    "Φ": r"\Phi", "Ψ": r"\Psi", "Ω": r"\Omega"
}

NAMED_MATH_FUNCS = {
    "sin", "cos", "tan", "cot", "sec", "csc",
    "sinh", "cosh", "tanh", "coth",
    "arcsin", "arccos", "arctan",
    "ln", "log", "exp", "lim", "max", "min", "sup", "inf", "det", "dim", "gcd"
}

def clean_math_text(txt: str) -> str:
    txt = txt.strip()
    return OPERATOR_MAP.get(txt, txt)

def parse_mathml_to_latex(node) -> str:
    """Traduce un nodo MathML de forma recursiva a sintaxis LaTeX matemáticamente precisa."""
    if node is None:
        return ""
    if isinstance(node, NavigableString):
        return clean_math_text(str(node))

    tag = node.name.lower() if node.name else ""

    # Prioridad 1: Anotación TeX/LaTeX original embebida
    if tag in ("math", "semantics"):
        ann = node.find("annotation", attrs={"encoding": re.compile(r"tex|latex", re.I)})
        if ann and ann.string and ann.string.strip():
            return ann.string.strip()

    children = [c for c in node.children if isinstance(c, Tag) or (isinstance(c, NavigableString) and c.strip())]

    if tag in ("math", "semantics", "mrow", "mstyle", "mpadded", "mphantom"):
        return "".join(parse_mathml_to_latex(c) for c in children)

    elif tag == "mi":
        t = clean_math_text(node.get_text())
        if t.lower() in NAMED_MATH_FUNCS:
            return f"\\{t.lower()} "
        if t.startswith("\\"):
            return f"{t} "
        if len(t) > 1:
            return f"\\mathrm{{{t}}}"
        return t

    elif tag == "mn":
        return node.get_text().strip()

    elif tag == "mo":
        t = clean_math_text(node.get_text())
        if t in ("+", "-", "*", "=", "<", ">", ":", "!", "?", "/", "(", ")", "[", "]", "|"):
            return f" {t} " if t in ("+", "-", "=", "<", ">") else t
        return f" {t} " if t.startswith("\\") else t

    elif tag == "mtext":
        t = node.get_text().strip()
        return f"\\text{{{t}}}" if t else ""

    elif tag == "mfrac":
        num = parse_mathml_to_latex(children[0]) if len(children) > 0 else ""
        den = parse_mathml_to_latex(children[1]) if len(children) > 1 else ""
        return f"\\frac{{{num.strip()}}}{{{den.strip()}}}"

    elif tag == "msqrt":
        inner = "".join(parse_mathml_to_latex(c) for c in children).strip()
        return f"\\sqrt{{{inner}}}"

    elif tag == "mroot":
        base = parse_mathml_to_latex(children[0]) if len(children) > 0 else ""
        idx = parse_mathml_to_latex(children[1]) if len(children) > 1 else ""
        return f"\\sqrt[{idx.strip()}]{{{base.strip()}}}"

    elif tag == "msup":
        base = parse_mathml_to_latex(children[0]) if len(children) > 0 else ""
        exp = parse_mathml_to_latex(children[1]) if len(children) > 1 else ""
        base_s = f"{{{base.strip()}}}" if len(base.strip()) > 1 and not (base.strip().startswith("{") and base.strip().endswith("}")) else base.strip()
        return f"{base_s}^{{{exp.strip()}}}"

    elif tag == "msub":
        base = parse_mathml_to_latex(children[0]) if len(children) > 0 else ""
        sub = parse_mathml_to_latex(children[1]) if len(children) > 1 else ""
        base_s = f"{{{base.strip()}}}" if len(base.strip()) > 1 and not (base.strip().startswith("{") and base.strip().endswith("}")) else base.strip()
        return f"{base_s}_{{{sub.strip()}}}"

    elif tag == "msubsup":
        base = parse_mathml_to_latex(children[0]) if len(children) > 0 else ""
        sub = parse_mathml_to_latex(children[1]) if len(children) > 1 else ""
        exp = parse_mathml_to_latex(children[2]) if len(children) > 2 else ""
        base_s = f"{{{base.strip()}}}" if len(base.strip()) > 1 and not (base.strip().startswith("{") and base.strip().endswith("}")) else base.strip()
        return f"{base_s}_{{{sub.strip()}}}^{{{exp.strip()}}}"

    elif tag == "munder":
        base = parse_mathml_to_latex(children[0]) if len(children) > 0 else ""
        und = parse_mathml_to_latex(children[1]) if len(children) > 1 else ""
        return f"\\underset{{{und.strip()}}}{{{base.strip()}}}"

    elif tag == "mover":
        base = parse_mathml_to_latex(children[0]) if len(children) > 0 else ""
        ovr = parse_mathml_to_latex(children[1]) if len(children) > 1 else ""
        if ovr.strip() in ("^", r"\hat", "ˆ"): return f"\\hat{{{base.strip()}}}"
        if ovr.strip() in ("-", r"\bar", "¯"): return f"\\bar{{{base.strip()}}}"
        if ovr.strip() in ("→", r"\to", r"\vec"): return f"\\vec{{{base.strip()}}}"
        return f"\\overset{{{ovr.strip()}}}{{{base.strip()}}}"

    elif tag == "munderover":
        base = parse_mathml_to_latex(children[0]) if len(children) > 0 else ""
        und = parse_mathml_to_latex(children[1]) if len(children) > 1 else ""
        ovr = parse_mathml_to_latex(children[2]) if len(children) > 2 else ""
        return f"{base.strip()}_{{{und.strip()}}}^{{{ovr.strip()}}}"

    elif tag == "mfenced":
        op = node.get("open", "(")
        cl = node.get("close", ")")
        inner = "".join(parse_mathml_to_latex(c) for c in children).strip()
        return f"\\left{op} {inner} \\right{cl}"

    elif tag == "menclose":
        notation = node.get("notation", "box").lower()
        inner = "".join(parse_mathml_to_latex(c) for c in children).strip()
        if "box" in notation or "roundedbox" in notation:
            return f"\\boxed{{{inner}}}"
        elif "circle" in notation:
            return f"\\textcircled{{{inner}}}"
        elif "updiagonalstrike" in notation or "downdiagonalstrike" in notation or "horizontalstrike" in notation:
            return f"\\cancel{{{inner}}}"
        return f"\\overline{{{inner}}}"

    elif tag == "mtable":
        rows = []
        for r in node.find_all("mtr", recursive=False):
            cells = [parse_mathml_to_latex(d).strip() for d in r.find_all("mtd", recursive=False)]
            rows.append(" & ".join(cells))
        return "\\begin{matrix} " + " \\\\ ".join(rows) + " \\end{matrix}"

    elif tag == "mspace":
        width = node.get("width", "")
        if "negative" in width:
            return r"\!"
        return r"\quad "

    return "".join(parse_mathml_to_latex(c) for c in children)

UNICODE_SUP_MAP = {
    "⁰": "^0", "¹": "^1", "²": "^2", "³": "^3", "⁴": "^4",
    "⁵": "^5", "⁶": "^6", "⁷": "^7", "⁸": "^8", "⁹": "^9",
    "⁺": "^+", "⁻": "^-", "ⁿ": "^n"
}

UNICODE_SUB_MAP = {
    "₀": "_0", "₁": "_1", "₂": "_2", "₃": "_3", "₄": "_4",
    "₅": "_5", "₆": "_6", "₇": "_7", "₈": "_8", "₉": "_9",
    "₊": "_+", "₋": "_-", "ᵢ": "_i", "ⱼ": "_j", "ₙ": "_n"
}

GREEK_MAP = {
    "α": r"\alpha", "β": r"\beta", "γ": r"\gamma", "δ": r"\delta",
    "ε": r"\varepsilon", "ϵ": r"\epsilon", "ζ": r"\zeta", "η": r"\eta",
    "θ": r"\theta", "ϑ": r"\vartheta", "ι": r"\iota", "κ": r"\kappa",
    "λ": r"\lambda", "μ": r"\mu", "ν": r"\nu", "ξ": r"\xi",
    "π": r"\pi", "ϖ": r"\varpi", "ρ": r"\rho", "ϱ": r"\varrho",
    "σ": r"\sigma", "ς": r"\varsigma", "τ": r"\tau", "υ": r"\upsilon",
    "φ": r"\varphi", "ϕ": r"\phi", "χ": r"\chi", "ψ": r"\psi", "ω": r"\omega",
    "Γ": r"\Gamma", "Δ": r"\Delta", "Θ": r"\Theta", "Λ": r"\Lambda",
    "Ξ": r"\Xi", "Π": r"\Pi", "Σ": r"\Sigma", "Υ": r"\Upsilon",
    "Φ": r"\Phi", "Ψ": r"\Psi", "Ω": r"\Omega"
}

def clean_wikipedia_latex(tex: str) -> str:
    """Limpia wrappers visuales como {\\displaystyle ...} frecuentes en Wikipedia."""
    if not tex: return ""
    tex = tex.strip()
    m = re.match(r"^\{\\displaystyle\s*(.*)\}$", tex, flags=re.DOTALL)
    if m:
        tex = m.group(1).strip()
    return tex

def clean_latex_formula(tex: str) -> str:
    """Pule y normaliza la expresión LaTeX para máxima legibilidad y rigor matemático."""
    if not tex: return ""
    tex = tex.strip()
    tex = clean_wikipedia_latex(tex)

    # Raíz cuadrada: √[ ... ] o √( ... ) -> \sqrt{ ... }
    tex = re.sub(r"√\s*\[\s*(.*?)\s*\]", r"\\sqrt{\1}", tex)
    tex = re.sub(r"√\s*\(\s*(.*?)\s*\)", r"\\sqrt{\1}", tex)
    tex = re.sub(r"√\s*([a-zA-Z0-9_\{\}\\]+)", r"\\sqrt{\1}", tex)

    # Fracciones dentro de raíz: \sqrt{ A / B } -> \sqrt{\frac{A}{B}}
    tex = re.sub(r"\\sqrt\{\s*([^/{]+?)\s*/\s*([a-zA-Z0-9_\{\}\(\)\+\-\s]+?)\s*\}", r"\\sqrt{\\frac{\1}{\2}}", tex)

    # Derivadas: dy/dx o dy / dx -> \frac{\mathrm{d}y}{\mathrm{d}x}
    tex = re.sub(r"\bd([a-zA-Z])\s*/\s*d([a-zA-Z])\b", r"\\frac{\\mathrm{d}\1}{\\mathrm{d}\2}", tex)

    # Fracciones comunes: 1 / ( ... ) -> \frac{1}{...}
    tex = re.sub(r"\b1\s*/\s*\(\s*([^()]+)\s*\)", r"\\frac{1}{\1}", tex)
    tex = re.sub(r"\b1\s*/\s*([A-Za-z](?:_[a-zA-Z0-9]+)?)\b", r"\\frac{1}{\1}", tex)
    tex = re.sub(r"\(1/([a-zA-Z])\)", r"\\frac{1}{\1}", tex)

    # Entidades HTML en fórmulas
    tex = tex.replace("&lt;", "<").replace("&gt;", ">").replace("&le;", r"\le ").replace("&ge;", r"\ge ")
    tex = tex.replace("&ne;", r"\ne ").replace("&plusmn;", r"\pm ").replace("&times;", r"\times ").replace("&amp;", r"\&")

    # Carácter % en LaTeX requiere \% para no comentar el resto de la fórmula
    tex = re.sub(r"(?<!\\)%", r"\\%", tex)

    # Convertir números decimales con coma a formato LaTeX: 2,2 -> 2{,}2
    tex = re.sub(r"(\d+),(\d+)", r"\1{,}\2", tex)

    # Funciones estándar a comandos LaTeX (negative lookbehind evita doblar \sin -> \\sin)
    tex = re.sub(r"(?<!\\)\b(ln|log|exp|sin|cos|tan|cot|sec|csc|sinh|cosh|tanh|coth|arcsin|arccos|arctan|det|dim|gcd)\b", r"\\\1", tex)
    tex = re.sub(r"(?<!\\)\b(max|màx)\b", r"\\max", tex)
    tex = re.sub(r"(?<!\\)\b(min|mín)\b", r"\\min", tex)
    tex = re.sub(r"(?<!\\)\b(lim|lím)\b", r"\\lim", tex)

    # Subíndices textuales con más de una letra: _{ref} -> _{\text{ref}} (evita renderizado en cursiva matemática de producto)
    tex = re.sub(r"_\{([a-zA-ZáéíóúàèòïüçÁÉÍÓÚÀÈÒÏÜÇ]{2,})\}", lambda m: f"_{{\\text{{{m.group(1)}}}}}" if not m.group(1).startswith("text") and m.group(1) not in ["max", "min", "lim", "sup", "inf"] else m.group(0), tex)

    # Auto-balanceo preventivo de llaves abiertas sin cerrar
    open_braces = tex.count("{")
    close_braces = tex.count("}")
    if open_braces > close_braces:
        tex += "}" * (open_braces - close_braces)

    # Quitar dobles espacios
    tex = re.sub(r"\s+", " ", tex).strip()
    return tex

def html_formula_node_to_latex(node) -> str:
    """Convierte un nodo de fórmula HTML enriquecida (<span class="f">, <var>, <sub>, etc.) a LaTeX."""
    if node is None: return ""
    if isinstance(node, NavigableString):
        s = str(node)
        s = s.replace("−", "-").replace("·", r" \cdot ").replace("×", r" \times ")
        s = s.replace("≈", r" \approx ").replace("≠", r" \ne ").replace("≤", r" \le ").replace("≥", r" \ge ")
        s = s.replace("→", r" \implies ").replace("⟶", r" \implies ")
        s = s.replace("Σ", r"\sum ").replace("∑", r"\sum ")
        for u_char, sup_tex in UNICODE_SUP_MAP.items(): s = s.replace(u_char, sup_tex)
        for u_char, sub_tex in UNICODE_SUB_MAP.items(): s = s.replace(u_char, sub_tex)
        for g_char, g_tex in GREEK_MAP.items(): s = s.replace(g_char, f" {g_tex} ")
        return s

    tag = node.name.lower() if node.name else ""

    if tag == "var":
        inner = "".join(html_formula_node_to_latex(c) for c in node.children).strip()
        for g_char, g_tex in GREEK_MAP.items():
            if inner == g_char or inner == g_tex.strip():
                return f" {g_tex} "
        return inner

    elif tag in ("sub", "msub"):
        inner = "".join(html_formula_node_to_latex(c) for c in node.children).strip()
        if re.search(r"[a-zA-ZáéíóúàèòïüçÁÉÍÓÚÀÈÒÏÜÇ]{2,}", inner) and "\\" not in inner:
            return f"_{{\\text{{{inner}}}}}"
        return f"_{{{inner}}}"

    elif tag in ("sup", "msup"):
        inner = "".join(html_formula_node_to_latex(c) for c in node.children).strip()
        return f"^{{{inner}}}"

    elif tag == "span":
        classes = node.get("class", [])
        if isinstance(classes, str): classes = [classes]
        if any(c in ["ov", "ovl", "overline", "bar"] for c in classes):
            inner = "".join(html_formula_node_to_latex(c) for c in node.children).strip()
            return f"\\bar{{{inner}}}"
        return "".join(html_formula_node_to_latex(c) for c in node.children)

    return "".join(html_formula_node_to_latex(c) for c in node.children)

def extract_figs_from_scripts(soup: BeautifulSoup) -> None:
    """Extrae diccionarios de imágenes (FIGS, window.__IMG__, etc.) de scripts para asignar sus URLs a img[data-fig]."""
    figs_dict = {}
    for script in soup.find_all("script"):
        st = script.get_text()
        if "data:image/" in st:
            for m in re.finditer(r'["\']([a-zA-Z0-9_\.-]+)["\']\s*:\s*["\'](data:image/[^"\']+)["\']', st):
                figs_dict[m.group(1)] = m.group(2)
    if figs_dict:
        for img in soup.find_all("img"):
            dfig = img.get("data-fig") or img.get("id")
            if dfig and dfig in figs_dict and (not img.get("src") or img.get("src").startswith("#")):
                img["src"] = figs_dict[dfig]

def extract_and_shield_math(soup: BeautifulSoup) -> tuple[BeautifulSoup, dict[str, str], int]:
    r"""
    Detecta todas las expresiones matemáticas (MathJax, KaTeX, MathML, SVGs con TeX, fórmulas HTML e imágenes de fórmulas)
    y las reemplaza por tokens seguros únicos, devolviendo un diccionario de restauración.
    Esto previene al 100% que los caracteres LaTeX (_ * { } ^ \ ~) sean alterados o escapados.
    """
    math_registry = {}
    counter = 0

    # 1. MathJax en scripts (<script type="math/tex">)
    for script in soup.find_all("script", attrs={"type": re.compile(r"math/tex", re.I)}):
        is_block = "mode=display" in script.get("type", "")
        latex_code = script.string.strip() if script.string else ""
        latex_code = clean_latex_formula(latex_code)
        token = f"TOKENMATHFML{counter}X"
        counter += 1
        if is_block:
            math_registry[token] = f"\n\n$$\n{latex_code}\n$$\n\n"
        else:
            math_registry[token] = f"${latex_code}$"
        script.replace_with(NavigableString(f" {token} "))

    # 2. KaTeX: descartar capa visual html duplicada para conservar únicamente la capa semántica
    for katex_html in soup.find_all(class_="katex-html"):
        katex_html.decompose()

    # 3. MathML (<math>)
    for math_tag in soup.find_all("math"):
        display_mode = (
            math_tag.get("display") == "block" or
            math_tag.get("mode") == "display" or
            (math_tag.parent and math_tag.parent.name in ("div", "p") and len(math_tag.parent.get_text().strip()) == len(math_tag.get_text().strip()))
        )
        latex_code = ""
        tex_ann = math_tag.find("annotation", attrs={"encoding": re.compile(r"tex|latex", re.I)})
        if tex_ann and tex_ann.string:
            latex_code = tex_ann.string.strip()
        
        if not latex_code:
            try:
                latex_code = parse_mathml_to_latex(math_tag).strip()
            except Exception:
                pass
        
        if not latex_code:
            try:
                import mathml2latex.mathml as m2l
                latex_code = m2l.process_mathml(math_tag).strip()
            except Exception:
                latex_code = math_tag.get_text(separator=" ", strip=True)

        latex_code = clean_latex_formula(latex_code)
        token = f"TOKENMATHFML{counter}X"
        counter += 1
        if display_mode:
            math_registry[token] = f"\n\n$$\n{latex_code}\n$$\n\n"
        else:
            math_registry[token] = f"${latex_code}$"
        math_tag.replace_with(NavigableString(f" {token} "))

    # 4. Contenedores de ecuaciones numeradas (.eq, .eqwrap, .eqblock, .eqbody)
    for eq_container in soup.find_all(lambda el: el.has_attr("class") and any(c in ["eq", "eqwrap", "eqblock", "eqbody"] for c in (el["class"] if isinstance(el["class"], list) else [el["class"]]))):
        tag_el = eq_container.find(class_=re.compile(r"^(n|eqn|eqnum)$"))
        tag_text = tag_el.get_text().strip() if tag_el else ""

        # Caso A: Contiene span.f (fórmula HTML enriquecida con var, sub, sup, ov, etc.)
        f_span = eq_container.find(class_="f")
        if f_span:
            raw_tex = html_formula_node_to_latex(f_span)
            clean_tex = clean_latex_formula(raw_tex)
            token = f"TOKENMATHFML{counter}X"
            counter += 1
            if tag_text:
                math_registry[token] = f"\n\n$$\n{clean_tex} \\qquad {tag_text}\n$$\n\n"
            else:
                math_registry[token] = f"\n\n$$\n{clean_tex}\n$$\n\n"
            eq_container.replace_with(NavigableString(f" {token} "))
            continue

        # Caso B: Contiene SVG con comentario TeX (Matplotlib / LaTeX)
        svg_el = eq_container.find("svg")
        if svg_el:
            comments = [c.strip() for c in svg_el.find_all(string=lambda t: isinstance(t, Comment))]
            tex = ""
            for c in comments:
                m = re.search(r"\$(.*?)\$", c)
                if m:
                    tex = m.group(1).strip()
                    break
            if tex:
                clean_tex = clean_latex_formula(tex)
                token = f"TOKENMATHFML{counter}X"
                counter += 1
                if tag_text:
                    math_registry[token] = f"\n\n$$\n{clean_tex} \\qquad {tag_text}\n$$\n\n"
                else:
                    math_registry[token] = f"\n\n$$\n{clean_tex}\n$$\n\n"
                eq_container.replace_with(NavigableString(f" {token} "))
                continue

    # 5. Fórmulas en SVG restantes (comentarios Matplotlib, aria-label, data-latex, o class="math")
    for svg in soup.find_all("svg"):
        comments = [c.strip() for c in svg.find_all(string=lambda t: isinstance(t, Comment))]
        tex = ""
        for c in comments:
            m = re.search(r"\$(.*?)\$", c)
            if m:
                tex = m.group(1).strip()
                break
        if not tex:
            data_tex = svg.get("data-latex", "") or svg.get("data-tex", "") or svg.get("aria-label", "")
            desc = svg.find("desc")
            desc_text = desc.get_text().strip() if desc else ""
            candidate_tex = data_tex or (desc_text if (desc_text.startswith("\\") or "$" in desc_text) else "")
            if candidate_tex:
                tex = candidate_tex.strip("$").strip()

        if tex:
            cleaned_tex = clean_latex_formula(tex)
            classes = svg.get("class", [])
            if isinstance(classes, str): classes = [classes]
            parent = svg.parent
            parent_classes = parent.get("class", []) if parent else []
            if isinstance(parent_classes, str): parent_classes = [parent_classes]

            is_display_container = (
                "md-svg" in parent_classes or
                "eq" in parent_classes or
                "formula" in parent_classes or
                any(c in ["display", "disp", "block", "md-svg"] for c in classes) or
                any(c in ["display", "disp", "block"] for c in parent_classes)
            )
            is_inline = not is_display_container and (
                "eqi" in classes or
                "mi-svg" in parent_classes or
                (parent and parent.name in ["p", "li", "td", "span"] and len(parent.get_text().strip()) > len(tex))
            )
            token = f"TOKENMATHFML{counter}X"
            counter += 1
            if is_inline:
                math_registry[token] = f"${cleaned_tex}$"
            else:
                math_registry[token] = f"\n\n$$\n{cleaned_tex}\n$$\n\n"
            
            # Reemplazar el contenedor padre si es un wrapper exclusivo (span.mi-svg, span.md-svg, etc.)
            target_node = svg
            if parent and parent.name in ["span", "div"] and any(c in ["mi-svg", "md-svg", "formula-svg", "eq-svg"] for c in parent_classes):
                if len(parent.find_all(True)) == 1:
                    target_node = parent
            target_node.replace_with(NavigableString(f" {token} "))

    # 6. Imágenes de fórmulas con alt LaTeX (Wikipedia, WordPress, CodeCogs, etc.)
    for img in soup.find_all("img"):
        classes = img.get("class", [])
        if isinstance(classes, str): classes = [classes]
        alt_text = img.get("alt", "").strip()
        src = img.get("src", "").lower()
        is_math_img = (
            any("math" in c.lower() for c in classes) or
            "latex" in src or
            "codecogs.com" in src or
            (alt_text.startswith(("\\", "$")) and len(alt_text) > 2)
        )
        if is_math_img and alt_text:
            cleaned_tex = clean_latex_formula(alt_text.strip("$").strip())
            is_block = (
                "display" in " ".join(classes).lower() or
                "display" in src or
                any(kw in cleaned_tex for kw in ["\\begin{align", "\\begin{equation", "\\\\"]) or
                (img.parent and img.parent.name in ("div", "p") and len(img.parent.get_text(strip=True)) == 0)
            )
            token = f"TOKENMATHFML{counter}X"
            counter += 1
            if is_block:
                math_registry[token] = f"\n\n$$\n{cleaned_tex}\n$$\n\n"
            else:
                math_registry[token] = f"${cleaned_tex}$"
            img.replace_with(NavigableString(f" {token} "))

    # 7. Elementos matemáticos inline en el texto: <span class="ov"> / <span class="ovl"> (media/overline)
    for span in list(soup.find_all(class_=re.compile(r"^(ov|ovl)$"))):
        inner = span.get_text().strip()
        token = f"TOKENMATHFML{counter}X"
        counter += 1
        math_registry[token] = f"$\\bar{{{inner}}}$"
        span.replace_with(NavigableString(f" {token} "))

    # 8. Fracciones en spans HTML (<span class="frac"> con .num y .den)
    for frac in list(soup.find_all(lambda el: el.has_attr("class") and any(c in ["frac", "fraction"] for c in (el["class"] if isinstance(el["class"], list) else [el["class"]])))):
        num = frac.find(class_=re.compile(r"^(num|numerador|numerator)$"))
        den = frac.find(class_=re.compile(r"^(den|denominador|denominator)$"))
        if num and den:
            num_tex = html_formula_node_to_latex(num).strip()
            den_tex = html_formula_node_to_latex(den).strip()
            token = f"TOKENMATHFML{counter}X"
            counter += 1
            math_registry[token] = f"$\\frac{{{num_tex}}}{{{den_tex}}}$"
            frac.replace_with(NavigableString(f" {token} "))

    # 9. Variables científicas y subíndices/superíndices vinculados (<var> + <sub>/<sup>)
    for var in list(soup.find_all("var")):
        if var.find_parent(["pre", "code"]):
            continue
        v_txt = var.get_text().strip()
        v_tex = GREEK_MAP.get(v_txt, v_txt)

        next_sib = var.next_sibling
        sub_tex = ""
        sup_tex = ""
        to_decompose = []

        if next_sib and getattr(next_sib, "name", None) == "sub":
            s_txt = next_sib.get_text().strip()
            if len(s_txt) > 1 and s_txt.isalpha() and s_txt not in ["max", "min"]:
                sub_tex = f"_{{\\text{{{s_txt}}}}}"
            elif s_txt in ["max", "màx"]:
                sub_tex = r"_{\max}"
            elif s_txt in ["min", "mín"]:
                sub_tex = r"_{\min}"
            else:
                sub_tex = f"_{{{s_txt}}}"
            to_decompose.append(next_sib)

            next2 = next_sib.next_sibling
            if next2 and getattr(next2, "name", None) == "sup":
                sup_tex = f"^{{{next2.get_text().strip()}}}"
                to_decompose.append(next2)
        elif next_sib and getattr(next_sib, "name", None) == "sup":
            sup_tex = f"^{{{next_sib.get_text().strip()}}}"
            to_decompose.append(next_sib)

        # Si posee subíndice/superíndice, es letra griega o símbolo algebraico unívoco
        if sub_tex or sup_tex or v_txt in GREEK_MAP or (len(v_txt) == 1 and v_txt.isalpha()):
            for el in to_decompose:
                el.decompose()
            token = f"TOKENMATHFML{counter}X"
            counter += 1
            math_registry[token] = f"${v_tex}{sub_tex}{sup_tex}$"
            var.replace_with(NavigableString(f" {token} "))

    return soup, math_registry, counter


# ----------------------------------------------------------------------
# 2. LIMPIEZA DE RUIDO, COMPONENTES ESTRUCTURALES Y REESCRITURA
# ----------------------------------------------------------------------

def clean_soup_noise(soup: BeautifulSoup) -> BeautifulSoup:
    """Elimina scripts no matemáticos, estilos, cookies y elementos publicitarios sin perder contenido de valor."""
    for comment in soup.find_all(string=lambda s: isinstance(s, Comment)):
        comment.extract()

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    for el in soup.find_all(attrs={"aria-hidden": "true"}):
        if not any("katex" in c.lower() for c in el.get("class", [])):
            el.decompose()

    for el in soup.find_all(lambda t: t.has_attr("style") and ("display:none" in t["style"].replace(" ", "").lower() or "visibility:hidden" in t["style"].replace(" ", "").lower())):
        el.decompose()

    for el in soup.find_all(lambda t: t.has_attr("class") and any("cookie" in c.lower() or "gdpr" in c.lower() or "popup-modal" in c.lower() for c in (t["class"] if isinstance(t["class"], list) else [t["class"]]))):
        el.decompose()

    return soup

def extract_base64_images(soup: BeautifulSoup, assets_dir: Path, doc_stem: str) -> int:
    """Extrae imágenes base64 embebidas en archivos locales limpios para aligerar y ordenar el Markdown."""
    extracted = 0
    for i, img in enumerate(soup.find_all("img")):
        src = img.get("src", "").strip()
        if src.startswith("data:image/"):
            m = re.match(r"data:image/([a-zA-Z0-9+_-]+);base64,(.+)", src, flags=re.DOTALL)
            if m:
                raw_ext = m.group(1).lower().replace("svg+xml", "svg").replace("jpeg", "jpg")
                ext = "png" if "png" in raw_ext else ("jpg" if "jpg" in raw_ext else ("svg" if "svg" in raw_ext else "png"))
                b64_str = re.sub(r"\s+", "", m.group(2))
                try:
                    data = base64.b64decode(b64_str)
                    assets_dir.mkdir(parents=True, exist_ok=True)
                    fname = f"{doc_stem}_img_{i+1}.{ext}"
                    fpath = assets_dir / fname
                    fpath.write_bytes(data)
                    # Enlace relativo al markdown
                    img["src"] = f"assets/{fname}"
                    extracted += 1
                except Exception:
                    pass
    return extracted

def extract_and_shield_diagrams(soup: BeautifulSoup) -> tuple[BeautifulSoup, dict[str, str], int]:
    """Tokeniza y protege diagramas (Mermaid / PlantUML) para evitar escape accidental de _, * y >."""
    diagram_registry = {}
    count = 0
    for el in soup.find_all(lambda t: t.name in ("div", "pre") and any("mermaid" in c.lower() for c in (t.get("class") if isinstance(t.get("class"), list) else [t.get("class") or ""]))):
        diagram = el.get_text().strip()
        if diagram:
            token = f"TOKENDIAGRAMX{count}X"
            diagram_registry[token] = f"\n\n```mermaid\n{diagram}\n```\n\n"
            el.replace_with(NavigableString(f"\n\n{token}\n\n"))
            count += 1

    for el in soup.find_all(lambda t: t.name in ("div", "pre") and any("plantuml" in c.lower() for c in (t.get("class") if isinstance(t.get("class"), list) else [t.get("class") or ""]))):
        diagram = el.get_text().strip()
        if diagram:
            token = f"TOKENDIAGRAMX{count}X"
            diagram_registry[token] = f"\n\n```plantuml\n{diagram}\n```\n\n"
            el.replace_with(NavigableString(f"\n\n{token}\n\n"))
            count += 1

    return soup, diagram_registry, count

def preprocess_callouts_and_admonitions(soup: BeautifulSoup) -> BeautifulSoup:
    """Convierte divs/asides de alerta en bloques blockquote de formato GitHub (> [!NOTE], etc.)."""
    CALLOUT_TYPES = {
        "warning": "WARNING",
        "warn": "WARNING",
        "alert": "WARNING",
        "danger": "CAUTION",
        "error": "CAUTION",
        "caution": "CAUTION",
        "attention": "IMPORTANT",
        "atencion": "IMPORTANT",
        "atencio": "IMPORTANT",
        "alerta": "IMPORTANT",
        "importante": "IMPORTANT",
        "important": "IMPORTANT",
        "tip": "TIP",
        "consejo": "TIP",
        "clau": "TIP",
        "claus": "TIP",
        "concepte-clau": "TIP",
        "note": "NOTE",
        "nota": "NOTE",
        "info": "NOTE",
        "observacio": "NOTE",
        "propietat": "NOTE"
    }

    for tag in soup.find_all(["div", "aside", "blockquote"]):
        if tag.name == "blockquote":
            continue
        if tag.find(lambda t: t.name == "p" and t.string and t.string.startswith("[!")):
            continue

        classes = tag.get("class", [])
        if isinstance(classes, str): classes = [classes]
        classes_str = " ".join(classes).lower()
        
        callout_found = None
        for key, alert_type in CALLOUT_TYPES.items():
            if key in classes_str:
                callout_found = alert_type
                break
        
        if callout_found:
            tag.name = "blockquote"
            marker = soup.new_tag("p")
            marker.string = f"[!{callout_found}]"
            tag.insert(0, marker)
            tag["class"] = []

    return soup

def preprocess_navigation_bars(soup: BeautifulSoup) -> BeautifulSoup:
    """Separa spans internos de enlaces de navegación (← Tornar Índex) y formatea barras de pie de página."""
    for a in soup.find_all("a"):
        spans = a.find_all("span")
        if len(spans) >= 2:
            texts = [s.get_text().strip() for s in spans if s.get_text().strip()]
            if texts:
                new_text = " ".join(texts)
                for s in spans:
                    s.decompose()
                a.string = new_text

    for nav in soup.find_all(["nav", "div"], class_=re.compile(r"^(navfoot|navigation|nav-bar)$")):
        links = nav.find_all("a")
        if links:
            p = soup.new_tag("p")
            p.append(NavigableString("\n\n---\n\n"))
            for i, a in enumerate(links):
                if i > 0:
                    p.append(NavigableString(" • "))
                p.append(a)
            p.append(NavigableString("\n\n"))
            nav.replace_with(p)

    return soup

def preprocess_course_components(soup: BeautifulSoup) -> BeautifulSoup:
    """Procesa y estiliza componentes didácticos propios de los cursos (tarjetas índice, pasos, defs, boxes, ejercicios)."""
    # 0. Tarjetas de índice estructuradas (.card con ctitle / card-title)
    for card in soup.find_all(class_="card"):
        ctitle = card.find(class_=re.compile(r"^(ctitle|card-title)$"))
        if not ctitle:
            continue
        href = card.get("href", "")
        cnum = card.find(class_=re.compile(r"^(cnum|card-num)$"))
        cdesc = card.find(class_=re.compile(r"^(cdesc|card-desc)$"))
        cmeta = card.find(class_=re.compile(r"^(cmeta|card-meta)$"))
        
        num_str = cnum.get_text().strip() if cnum else ""
        prefix = f"{num_str}. " if num_str else ""
        title_text = ctitle.get_text().strip()
        desc_text = cdesc.get_text().strip() if cdesc else ""
        meta_text = cmeta.get_text().strip() if cmeta else ""
        
        new_div = soup.new_tag("div")
        h3 = soup.new_tag("h3")
        if href:
            a_link = soup.new_tag("a", href=href)
            a_link.string = f"{prefix}{title_text}"
            h3.append(a_link)
        else:
            h3.string = f"{prefix}{title_text}"
        new_div.append(h3)
        if desc_text:
            p_desc = soup.new_tag("p")
            p_desc.string = desc_text
            new_div.append(p_desc)
        if meta_text:
            p_meta = soup.new_tag("p")
            em = soup.new_tag("em")
            em.string = f"⏱️ {meta_text}"
            p_meta.append(em)
            new_div.append(p_meta)
        card.replace_with(new_div)

    # 1. Separar números en encabezados: <span class="num">1</span>Texto -> 1 Texto
    for num_span in soup.find_all(class_=re.compile(r"^(num|card-num|cardnum|cnum|dnum)$")):
        num_text = num_span.get_text().strip()
        num_span.replace_with(NavigableString(f"{num_text} "))

    # 2. Convertir <div class="defs"> en lista de definiciones no intrusiva para el TOC
    for defs in soup.find_all(class_="defs"):
        ul = soup.new_tag("ul")
        for def_item in defs.find_all(class_="def"):
            h = def_item.find(["h4", "h5", "strong", "b"])
            p = def_item.find("p")
            li = soup.new_tag("li")
            term_html = "".join(str(c) for c in h.children) if h else ""
            desc_html = p.get_text().strip() if p else ""
            li.append(BeautifulSoup(f"<strong>{term_html}</strong>: {desc_html}", "html.parser"))
            ul.append(li)
        defs.replace_with(ul)

    # 3. Formatear <div class="step"> interactivos con details/summary
    for step in soup.find_all(class_="step"):
        btn = step.find(class_="step-btn")
        body = step.find(class_="step-body")
        if not btn and not body:
            continue
        btn_text = btn.get_text().strip() if btn else "Resolució"
        if btn: btn.decompose()
        body_node = body if body else step
        body_content = "".join(str(c) for c in body_node.children)
        details_html = f"\n\n<details>\n<summary><b>🔍 Desplegar {btn_text}</b></summary>\n\n{body_content}\n\n</details>\n\n"
        step.replace_with(BeautifulSoup(details_html, "html.parser"))

    # 4. Formatear <div class="example"> y <div class="exemple"> como bloques callout GFM
    for ex in soup.find_all(class_=re.compile(r"^(example|exemple)$")):
        tag = ex.find(class_=re.compile(r"^(tag|cap)$"))
        tag_text = tag.get_text().strip() if tag else "Exercici Resolt"
        if tag: tag.decompose()
        
        h_title = ex.find(["h3", "h4", "h5", "strong"])
        title_text = f" — {h_title.get_text().strip()}" if h_title and h_title.name in ["h3", "h4"] else ""
        if h_title and h_title.name in ["h3", "h4"]:
            h_title.decompose()
            
        ex.name = "blockquote"
        prefix = soup.new_tag("p")
        prefix.append(NavigableString("[!EXAMPLE] "))
        strong = soup.new_tag("strong")
        strong.string = f"{tag_text}{title_text}"
        prefix.append(strong)
        ex.insert(0, prefix)

    # 5. Formatear <div class="box ...">
    for box in soup.find_all(class_="box"):
        if box.name == "blockquote" or box.find(lambda t: t.name == "p" and t.string and t.string.startswith("[!")):
            continue

        classes = box.get("class", [])
        if isinstance(classes, str): classes = [classes]

        # Extraer título pedagógico si existe (.cap, .box-title, .title, .tag, h3, h4)
        box_title = box.find(class_=re.compile(r"^(cap|box-title|boxtitle|title|tag)$")) or box.find(["h3", "h4"])
        title_text = box_title.get_text().strip() if box_title else ""
        if box_title:
            box_title.decompose()
        
        callout_type = "NOTE"
        if "objectius" in classes: callout_type = "NOTE"
        elif "resum" in classes: callout_type = "TIP"
        elif "nota" in classes or "warn" in classes: callout_type = "WARNING"
        elif "atencio" in classes or "alerta" in classes or "important" in classes: callout_type = "IMPORTANT"
        elif "clau" in classes or "concepte-clau" in classes or "llegir" in classes: callout_type = "TIP"
        elif "dada" in classes: callout_type = "NOTE"

        box.name = "blockquote"
        prefix = soup.new_tag("p")
        prefix.append(NavigableString(f"[!{callout_type}]"))
        if title_text:
            prefix.append(NavigableString(" "))
            strong = soup.new_tag("strong")
            strong.string = title_text
            prefix.append(strong)
        box.insert(0, prefix)
        box["class"] = []

    return soup

def preprocess_footnotes(soup: BeautifulSoup) -> BeautifulSoup:
    """Estandariza referencias y notas al pie en sintaxis GFM [^1] y [^1]: Nota."""
    for sup in soup.find_all("sup", class_=re.compile(r"footnote|reference|cite", re.I)):
        a = sup.find("a")
        if a:
            num = re.sub(r"\D", "", a.get_text())
            if num:
                sup.replace_with(NavigableString(f"[^{num}]"))

    footnotes_section = soup.find(class_=re.compile(r"footnotes|doc-endnotes", re.I)) or soup.find("section", role="doc-endnotes")
    if footnotes_section:
        notes = []
        for li in footnotes_section.find_all("li"):
            num = re.sub(r"\D", "", li.get("id", ""))
            for back in li.find_all("a", class_=re.compile(r"backref|reverse", re.I)):
                back.decompose()
            txt = li.get_text().replace("↩", "").strip()
            if num and txt:
                notes.append(f"[^{num}]: {txt}")
        if notes:
            footnotes_section.replace_with(NavigableString("\n\n" + "\n\n".join(notes) + "\n\n"))

    return soup

def preprocess_media_elements(soup: BeautifulSoup) -> BeautifulSoup:
    """Preserva referencias enriquecidas a videos (YouTube/Vimeo/locales) y audios mediante nodos semánticos."""
    # 1. iframes de video
    for iframe in soup.find_all("iframe"):
        src = iframe.get("src", "")
        if "youtube.com" in src or "youtu.be" in src:
            video_id = ""
            m = re.search(r"(?:embed/|v=|youtu\.be/)([a-zA-Z0-9_-]+)", src)
            if m: video_id = m.group(1)
            yt_url = f"https://www.youtube.com/watch?v={video_id}" if video_id else src
            p = soup.new_tag("p")
            p.append(NavigableString("🎥 "))
            strong = soup.new_tag("strong")
            strong.string = "Video:"
            p.append(strong)
            p.append(NavigableString(" "))
            a = soup.new_tag("a", href=yt_url)
            a.string = "Ver en YouTube"
            p.append(a)
            iframe.replace_with(p)
        elif "vimeo.com" in src:
            p = soup.new_tag("p")
            p.append(NavigableString("🎥 "))
            strong = soup.new_tag("strong")
            strong.string = "Video:"
            p.append(strong)
            p.append(NavigableString(" "))
            a = soup.new_tag("a", href=src)
            a.string = "Ver en Vimeo"
            p.append(a)
            iframe.replace_with(p)
        elif src:
            title = iframe.get("title", "").strip() or "Recurso Multimedia"
            p = soup.new_tag("p")
            p.append(NavigableString("🔗 "))
            strong = soup.new_tag("strong")
            strong.string = "Contenido:"
            p.append(strong)
            p.append(NavigableString(" "))
            a = soup.new_tag("a", href=src)
            a.string = title
            p.append(a)
            iframe.replace_with(p)
        else:
            iframe.decompose()

    # 2. <video>
    for vid in soup.find_all("video"):
        src = vid.get("src", "")
        if not src:
            src_tag = vid.find("source")
            if src_tag: src = src_tag.get("src", "")
        if src:
            name = Path(src).name or "Ver Video"
            p = soup.new_tag("p")
            p.append(NavigableString("🎥 "))
            strong = soup.new_tag("strong")
            strong.string = "Video:"
            p.append(strong)
            p.append(NavigableString(" "))
            a = soup.new_tag("a", href=src)
            a.string = name
            p.append(a)
            vid.replace_with(p)
        else:
            vid.decompose()

    # 3. <audio>
    for aud in soup.find_all("audio"):
        src = aud.get("src", "")
        if not src:
            src_tag = aud.find("source")
            if src_tag: src = src_tag.get("src", "")
        if src:
            name = Path(src).name or "Reproducir Audio"
            p = soup.new_tag("p")
            p.append(NavigableString("🎵 "))
            strong = soup.new_tag("strong")
            strong.string = "Audio:"
            p.append(strong)
            p.append(NavigableString(" "))
            a = soup.new_tag("a", href=src)
            a.string = name
            p.append(a)
            aud.replace_with(p)
        else:
            aud.decompose()

    return soup

def rewrite_internal_links(soup: BeautifulSoup, source_path: Optional[Path] = None) -> BeautifulSoup:
    """Convierte enlaces internos .html/.htm en .md y resuelve con heurística semántica enlaces locales disonantes."""
    parent_files = []
    exact_map = {}
    if source_path and source_path.parent.exists():
        parent_dir = source_path.parent
        parent_files = [
            f for f in parent_dir.glob("*.*")
            if f.suffix.lower() in [".html", ".htm", ".md"] and not f.name.startswith("_")
        ]
        exact_map = {f.name.lower(): f.stem for f in parent_files}
        exact_map.update({f.stem.lower(): f.stem for f in parent_files})

    def get_tokens(s):
        return set(re.findall(r'[a-zA-Z0-9]+', s.lower()))

    def get_content_words(s):
        return {w for w in re.findall(r'[a-zA-Z]+', s.lower()) if w not in {'unitat', 'doc', 'tema', 'html', 'md', 'de', 'i', 'el', 'la', 'les', 'd'}}

    def resolve_local_stem(path_str: str) -> Optional[str]:
        if not parent_files:
            return None
        clean = Path(path_str).name.lower()
        if clean in exact_map:
            return exact_map[clean]
        stem = Path(path_str).stem.lower()
        if stem in exact_map:
            return exact_map[stem]

        # 1. Búsqueda de índice especial
        if stem in ["index", "00_index"] or "index" in stem:
            idx_candidates = [f.stem for f in parent_files if "index" in f.name.lower()]
            if idx_candidates:
                return sorted(idx_candidates)[0]

        # 2. Token exact match
        tokens = get_tokens(stem)
        for f in parent_files:
            if tokens == get_tokens(f.stem):
                return f.stem

        # 3. Match por palabras clave de contenido y número de unidad/documento
        nums = set(re.findall(r'\b\d+\b', stem))
        content_words = get_content_words(stem)
        best_candidate = None
        best_score = 0
        for f in parent_files:
            f_nums = set(re.findall(r'\b\d+\b', f.stem.lower()))
            f_words = get_content_words(f.stem)
            num_overlap = bool(nums & f_nums)
            word_overlap = len(content_words & f_words)
            score = word_overlap * 2 + (5 if num_overlap else 0)
            if word_overlap >= 2 and score > best_score:
                best_score = score
                best_candidate = f.stem

        return best_candidate

    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if not re.match(r"^(https?://|mailto:|ftp:|#|javascript:)", href, re.I):
            parts = href.split("#", 1)
            path_part = parts[0]
            anchor_part = f"#{parts[1]}" if len(parts) > 1 else ""

            resolved_stem = resolve_local_stem(path_part)
            if resolved_stem:
                a["href"] = f"{resolved_stem}.md{anchor_part}"
            elif path_part.lower().endswith((".html", ".htm")):
                stem = Path(path_part).stem
                a["href"] = f"{stem}.md{anchor_part}"
    return soup

def preprocess_figures_and_captions(soup: BeautifulSoup) -> BeautifulSoup:
    """Preserva figuras y leyendas de manera limpia sin corromper URLs de imágenes."""
    for fig in soup.find_all("figure"):
        caption = fig.find("figcaption")
        caption_text = caption.get_text().strip() if caption else ""
        if caption:
            caption.decompose()
        img = fig.find("img")
        if img:
            new_div = soup.new_tag("div")
            new_div.append(img)
            if caption_text:
                p = soup.new_tag("p")
                em = soup.new_tag("em")
                em.string = f"Figura: {caption_text}"
                p.append(em)
                new_div.append(p)
            fig.replace_with(new_div)
    return soup

def preprocess_definition_lists(soup: BeautifulSoup) -> BeautifulSoup:
    """Convierte listas de definición <dl><dt><dd> en Markdown estructurado y legible."""
    for dl in soup.find_all("dl"):
        wrapper = soup.new_tag("div")
        for child in dl.children:
            if not isinstance(child, Tag):
                continue
            if child.name == "dt":
                p = soup.new_tag("p")
                strong = soup.new_tag("strong")
                strong.string = child.get_text().strip()
                p.append(strong)
                wrapper.append(p)
            elif child.name == "dd":
                p = soup.new_tag("p")
                p.append(NavigableString(f": {child.get_text().strip()}"))
                wrapper.append(p)
        dl.replace_with(wrapper)
    return soup

def preprocess_task_lists(soup: BeautifulSoup) -> BeautifulSoup:
    """Convierte checkboxes HTML en checkboxes de Markdown interactivos (- [x] y - [ ])."""
    for inp in soup.find_all("input", attrs={"type": "checkbox"}):
        checked = inp.has_attr("checked")
        marker = "[x] " if checked else "[ ] "
        inp.replace_with(NavigableString(marker))
    return soup

def preprocess_details_summary(soup: BeautifulSoup) -> BeautifulSoup:
    """Preserva desplegables interactivos <details> y <summary> para una lectura enriquecida."""
    for details in soup.find_all("details"):
        summary = details.find("summary")
        summary_text = summary.get_text().strip() if summary else "Detalles"
        if summary:
            summary.decompose()
        inner_content = details.decode_contents()
        new_tag = soup.new_tag("div")
        new_tag.append(NavigableString(f"\n\n<details>\n<summary><b>{summary_text}</b></summary>\n\n"))
        inner_soup = BeautifulSoup(inner_content, "html.parser")
        new_tag.append(inner_soup)
        new_tag.append(NavigableString(f"\n\n</details>\n\n"))
        details.replace_with(new_tag)
    return soup

def extract_metadata(soup: BeautifulSoup) -> dict:
    """Extrae metadatos clave para enriquecer la lectura tanto de humanos como de LLMs."""
    meta = {}
    title_tag = soup.find("title")
    og_title = soup.find("meta", property="og:title")
    meta_title = soup.find("meta", attrs={"name": "title"})
    if og_title and og_title.get("content"):
        meta["title"] = og_title["content"].strip()
    elif meta_title and meta_title.get("content"):
        meta["title"] = meta_title["content"].strip()
    elif title_tag and title_tag.string:
        meta["title"] = title_tag.string.strip()

    author = soup.find("meta", attrs={"name": re.compile(r"author", re.I)}) or soup.find(class_=re.compile(r"author", re.I))
    if author:
        meta["author"] = author.get("content", "") or author.get_text().strip()

    date = soup.find("meta", attrs={"name": re.compile(r"date|publish", re.I)}) or soup.find("time")
    if date:
        meta["date"] = date.get("content", "") or date.get("datetime", "") or date.get_text().strip()

    desc = soup.find("meta", attrs={"name": "description"}) or soup.find("meta", property="og:description")
    if desc and desc.get("content"):
        meta["description"] = desc["content"].strip()

    canonical = soup.find("link", rel="canonical")
    if canonical and canonical.get("href"):
        meta["source"] = canonical["href"].strip()

    return meta


# ----------------------------------------------------------------------
# 3. MOTOR DE TABLAS 2D GFM (ROWSPAN, COLSPAN Y DETECCIÓN DE CÓDIGO)
# ----------------------------------------------------------------------

def is_code_table(table_tag: Tag) -> bool:
    """Detecta si una tabla es en realidad un bloque de código con números de línea (Prism, Rouge, etc.)."""
    classes = " ".join(table_tag.get("class", []) if isinstance(table_tag.get("class", []), list) else [table_tag.get("class", "")]).lower()
    if any(k in classes for k in ["highlight", "syntaxhighlighter", "code-table", "blob-wrapper"]):
        return True
    cells = table_tag.find_all(["td", "th"])
    cell_classes = " ".join([" ".join(c.get("class", [])) for c in cells if c.get("class")]).lower()
    if ("gutter" in cell_classes or "line-numbers" in cell_classes or "hljs-ln-numbers" in cell_classes) and ("code" in cell_classes or "blob-code" in cell_classes or "hljs-ln-code" in cell_classes):
        return True
    return False

def extract_code_from_table(table_tag: Tag) -> str:
    """Extrae limpiamente el código fuente de una tabla con gutter de números de línea."""
    code_cells = table_tag.find_all(lambda el: el.name == "td" and any(k in " ".join(el.get("class", [])).lower() for k in ["code", "blob-code", "hljs-ln-code", "lines"]))
    if not code_cells:
        code_cells = [td for td in table_tag.find_all("td") if not any(g in " ".join(td.get("class", [])).lower() for g in ["gutter", "line-number", "lineno"])]
    
    code_lines = []
    lang = ""
    for c in code_cells:
        pre = c.find("pre") or c
        classes = " ".join(pre.get("class", []))
        m = re.search(r"(?:lang(?:uage)?-|brush:\s*)([a-zA-Z0-9_+#-]+)", classes, re.I)
        if m: lang = m.group(1).lower()
        code_lines.append(c.get_text().strip("\r\n"))
    
    full_code = "\n".join(code_lines)
    return f"\n\n```{lang}\n{full_code}\n```\n\n"

def convert_html_table_to_gfm_2d(table_tag: Tag, inline_converter) -> str:
    """Convierte una tabla HTML compleja en GFM mediante matriz 2D con soporte exacto para rowspan y colspan."""
    if is_code_table(table_tag):
        return extract_code_from_table(table_tag)

    rows = table_tag.find_all("tr")
    if not rows:
        return ""

    grid = {}       # (r, c) -> contenido formateado
    align_grid = {} # c -> alineación

    for r_idx, row in enumerate(rows):
        c_idx = 0
        for cell in row.find_all(["th", "td"]):
            while (r_idx, c_idx) in grid:
                c_idx += 1

            rowspan = int(cell.get("rowspan", 1))
            colspan = int(cell.get("colspan", 1))

            align = cell.get("align", "").lower()
            if not align and cell.has_attr("style"):
                s = cell["style"].lower()
                if "text-align:center" in s.replace(" ", ""): align = "center"
                elif "text-align:right" in s.replace(" ", ""): align = "right"
                elif "text-align:left" in s.replace(" ", ""): align = "left"

            # Formatear el contenido interno de la celda
            has_subtags = any(isinstance(c, Tag) for c in cell.children)
            if not has_subtags:
                cell_text = cell.get_text().strip()
            else:
                for br in cell.find_all("br"):
                    br.replace_with(NavigableString(" HTMLBRTAG "))
                for p in cell.find_all("p"):
                    p.append(NavigableString(" HTMLBRTAG "))
                    p.unwrap()

                child_parts = []
                for c in cell.children:
                    if isinstance(c, NavigableString):
                        child_parts.append(str(c))
                    elif isinstance(c, Tag):
                        child_parts.append(inline_converter.convert_soup(c))

                cell_text = "".join(child_parts).strip()
                cell_text = re.sub(r"\s*HTMLBRTAG\s*", "<br>", cell_text)

            cell_text = re.sub(r"[\r\n]+", " ", cell_text)
            cell_text = cell_text.replace("|", "\\|")
            cell_text = re.sub(r"(<br\s*/?>\s*)+", "<br>", cell_text)
            cell_text = re.sub(r"^(?:\s*<br\s*/?>\s*)+|(?:\s*<br\s*/?>\s*)+$", "", cell_text).strip()

            for dr in range(rowspan):
                for dc in range(colspan):
                    tr = r_idx + dr
                    tc = c_idx + dc
                    if dr == 0 and dc == 0:
                        grid[(tr, tc)] = cell_text
                    else:
                        grid[(tr, tc)] = f"{cell_text} (cont.)" if (dr > 0 and len(cell_text) < 30 and not cell_text.startswith("$")) else ""
                    
                    if align:
                        align_grid[tc] = align

            c_idx += colspan

    if not grid:
        return ""

    max_r = max(r for r, c in grid.keys()) + 1
    max_c = max(c for r, c in grid.keys()) + 1

    alignments = [align_grid.get(c, "left") for c in range(max_c)]

    def make_align_spec(a):
        if a == "center": return ":---:"
        if a == "right": return "---:"
        return ":---"

    sep_row = [make_align_spec(a) for a in alignments]

    output_lines = []
    output_lines.append("| " + " | ".join(grid.get((0, c), "") for c in range(max_c)) + " |")
    output_lines.append("| " + " | ".join(sep_row) + " |")
    for r in range(1, max_r):
        output_lines.append("| " + " | ".join(grid.get((r, c), "") for c in range(max_c)) + " |")

    return "\n\n" + "\n".join(output_lines) + "\n\n"

def extract_and_shield_tables(soup: BeautifulSoup, inline_converter) -> tuple[BeautifulSoup, dict[str, str], int]:
    """Tokeniza las tablas para proteger su estructura antes del pase de Markdownify."""
    table_registry = {}
    count = 0
    for i, tbl in enumerate(soup.find_all("table")):
        token = f"TOKENTABLEGFM{i}X"
        table_registry[token] = convert_html_table_to_gfm_2d(tbl, inline_converter)
        tbl.replace_with(NavigableString(f"\n\n{token}\n\n"))
        count += 1
    return soup, table_registry, count


# ----------------------------------------------------------------------
# 4. CONVERSOR PERSONALIZADO MARKDOWNIFY DE ULTRA FIDELIDAD
# ----------------------------------------------------------------------

class UltraFaithfulMarkdownConverter(markdownify.MarkdownConverter):
    """Conversor personalizado con tipografía semántica y prevención de escapes accidentales."""

    def escape(self, text: str, *args, **kwargs) -> str:
        if "TOKENMATHFML" in text or "TOKENTABLEGFM" in text or "TOKENDIAGRAM" in text:
            return text
        if "$" in text:
            parts = re.split(r"(\$\$.*?\$\$|\$.*?\$)", text, flags=re.DOTALL)
            for i, part in enumerate(parts):
                if not (part.startswith("$") and part.endswith("$")):
                    parts[i] = super().escape(part, *args, **kwargs)
            return "".join(parts)
        return super().escape(text, *args, **kwargs)

    def convert_pre(self, el, text, *args, **kwargs):
        """Detecta automáticamente el lenguaje del bloque de código desde clases CSS."""
        if not text:
            return ""
        code_tag = el.find("code")
        candidates = []
        if el.get("class"):
            candidates.extend(el.get("class") if isinstance(el.get("class"), list) else [el.get("class")])
        if code_tag and code_tag.get("class"):
            candidates.extend(code_tag.get("class") if isinstance(code_tag.get("class"), list) else [code_tag.get("class")])

        lang = ""
        for c in candidates:
            m = re.search(r"(?:lang(?:uage)?-|brush:\s*|highlight-source-)([a-zA-Z0-9_+#-]+)", str(c), re.I)
            if m:
                lang = m.group(1).lower()
                break
        
        code_text = code_tag.get_text() if code_tag else el.get_text()
        code_text = code_text.strip("\r\n")
        return f"\n\n```{lang}\n{code_text}\n```\n\n"

    def convert_blockquote(self, el, text, *args, **kwargs):
        """Formatea alertas y citas estilo GitHub Markdown (> [!NOTE], etc.) con prefijo uniforme."""
        lines = [line.strip() for line in text.strip().split("\n")]
        quoted_lines = []
        for line in lines:
            if line:
                quoted_lines.append(f"> {line}")
            elif quoted_lines and quoted_lines[-1] != ">":
                quoted_lines.append(">")
        return "\n\n" + "\n".join(quoted_lines) + "\n\n"

    def convert_mark(self, el, text, *args, **kwargs):
        return f"=={text}=="

    def convert_kbd(self, el, text, *args, **kwargs):
        return f"<kbd>{text}</kbd>"

    def convert_sub(self, el, text, *args, **kwargs):
        return f"<sub>{text}</sub>"

    def convert_sup(self, el, text, *args, **kwargs):
        return f"<sup>{text}</sup>"

    def convert_del(self, el, text, *args, **kwargs):
        return f"~~{text}~~"

    def convert_s(self, el, text, *args, **kwargs):
        return f"~~{text}~~"

    def convert_strike(self, el, text, *args, **kwargs):
        return f"~~{text}~~"

    def convert_ins(self, el, text, *args, **kwargs):
        return f"<ins>{text}</ins>"

    def convert_u(self, el, text, *args, **kwargs):
        return f"<u>{text}</u>"

    def convert_hr(self, el, text, *args, **kwargs):
        return "\n\n---\n\n"


# ----------------------------------------------------------------------
# 5. ÍNDICE DE CONTENIDOS (TOC) Y DETECCIÓN SEGURA DE CODIFICACIÓN
# ----------------------------------------------------------------------

def slugify(text: str) -> str:
    """Genera anclajes limpios compatibles con GitHub / Obsidian."""
    s = text.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_-]+", "-", s)
    return s.strip("-")

def generate_toc_from_markdown(md_text: str) -> str:
    """Genera un Índice de Contenidos interactivo para documentos extensos."""
    lines = md_text.splitlines()
    toc_entries = []
    
    for line in lines:
        m = re.match(r"^(#{2,4})\s+(.+)$", line)
        if m:
            level = len(m.group(1)) - 2
            heading = m.group(2).strip()
            if any(k in heading.lower() for k in ["índice", "tabla de contenidos", "toc", "resumen"]):
                continue
            slug = slugify(heading)
            indent = "  " * level
            toc_entries.append(f"{indent}- [{heading}](#{slug})")
            
    if len(toc_entries) < 3:
        return ""
        
    return "## 📑 Índice de Contenidos\n\n" + "\n".join(toc_entries) + "\n\n---\n\n"

def generate_formula_sheet_from_markdown(md_text: str) -> str:
    """Genera una tabla resumen Markdown (GFM) con todas las fórmulas matemáticas del documento."""
    blocks = re.findall(r"\$\$\n*(.*?)\n*\$\$", md_text, flags=re.DOTALL)
    if not blocks:
        return ""

    entries = []
    seen = set()
    has_explicit_tags = False

    # 1. Comprobar si existen ecuaciones con numeración oficial (\qquad (x.y), \tag{...}, (x.y))
    for b in blocks:
        if re.search(r"(?:\\qquad|\\quad|\\tag)\s*\(?[0-9]", b) or re.search(r"\([0-9]+(?:\.[0-9]+)+\)", b):
            has_explicit_tags = True
            break

    for idx, block in enumerate(blocks, 1):
        b = block.strip()
        m_tag = re.search(r"(?:\\qquad|\\quad)\s*(\([^\)]+\))", b)
        if not m_tag:
            m_tag = re.search(r"\\tag\{([^\}]+)\}", b)
        if not m_tag:
            m_tag = re.search(r"(\([0-9]+(?:\.[0-9]+)+\))\s*$", b)

        if m_tag:
            tag = m_tag.group(1).strip()
            if not tag.startswith("(") and not tag.endswith(")"):
                tag = f"({tag})"
            formula = b[:m_tag.start()] + b[m_tag.end():]
        else:
            if has_explicit_tags:
                # Si hay ecuaciones numeradas oficiales, omitir expresiones intermedias sin número
                continue
            tag = f"({idx})"
            formula = b

        formula = " ".join(formula.split()).strip()
        # Escapar barras verticales para que no rompan las columnas de la tabla GFM
        formula = formula.replace("|", r"\|")
        if not formula:
            continue

        key = (tag, formula)
        if key in seen:
            continue
        seen.add(key)
        entries.append((tag, formula))

    if not entries:
        return ""

    lines = [
        "## 📐 Formulario Resumen de Ecuaciones",
        "",
        "| Nº / Ref | Expresión Matemática |",
        "| :---: | :--- |"
    ]
    for tag, formula in entries:
        lines.append(f"| **{tag}** | ${formula}$ |")

    return "\n".join(lines) + "\n\n"

def generate_master_topic_document(
    output_dir: Path,
    topic_title: str = None,
    include_formula_sheet: bool = True
) -> tuple[Path, dict]:
    """Genera un archivo Markdown unificado (_Cuaderno_Maestro_*.md) combinando todos los capítulos del tema."""
    output_dir = Path(output_dir)
    md_files = sorted([
        f for f in output_dir.glob("*.md")
        if not f.name.startswith("_")
    ])

    if not md_files:
        return None, {}

    if not topic_title:
        topic_title = output_dir.name.replace("_", " ").replace("-", " ").title()

    stats = {"chapters": len(md_files), "words": 0, "chars": 0, "math": 0, "tables": 0}
    timestamp = time.strftime("%Y-%m-%d %H:%M")

    # Cabecera maestra
    master_lines = [
        f"# 📚 Cuaderno Maestro: {topic_title}",
        "",
        "> ℹ️ **Documento Unificado y Consolidado para NotebookLM, Claude, Gemini & Obsidian**  ",
        f"> 📂 **Carpeta de origen:** `{output_dir.name}` | 📄 **Capítulos incluidos:** {len(md_files)}  ",
        f"> 📅 **Generado:** {timestamp}",
        "",
        "---",
        ""
    ]

    # Índice General Maestro
    toc_lines = [
        "## 📑 Índice General del Cuaderno Maestro",
        ""
    ]

    chapters_payload = []
    stem_to_slug = {}

    for idx, f in enumerate(md_files, 1):
        content = f.read_text(encoding="utf-8")

        # Extraer primer H1 o usar nombre de archivo
        h1_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        if h1_match:
            ch_title = h1_match.group(1).strip()
        else:
            ch_title = f.stem.replace("_", " ").replace("-", " ").title()

        ch_slug = slugify(ch_title)
        stem_to_slug[f.stem] = ch_slug
        toc_lines.append(f"{idx}. [{ch_title}](#{ch_slug})")

        # Subsecciones H2 para el índice maestro
        for h2 in re.findall(r"^##\s+(.+)$", content, re.MULTILINE):
            h2_clean = h2.strip()
            if any(w in h2_clean.lower() for w in ["índice", "toc", "formulario", "resumen"]):
                continue
            toc_lines.append(f"   - [{h2_clean}](#{slugify(h2_clean)})")

        # Limpiar contenido del capítulo para la fusión:
        # Remover YAML Frontmatter local
        clean_content = re.sub(r"^---\n.*?\n---\n*", "", content, flags=re.DOTALL)
        # Remover TOC local para evitar duplicación interna
        clean_content = re.sub(r"## 📑 Índice de Contenidos\n\n.*?\n---\n*", "", clean_content, flags=re.DOTALL)
        # Remover formulario local individual si existe (se consolidará al final del cuaderno)
        clean_content = re.sub(r"## 📐 Formulario Resumen de Ecuaciones\n\n.*?$", "", clean_content, flags=re.DOTALL)
        clean_content = clean_content.strip()

        # Conteo de estadísticas acumuladas
        stats["math"] += len(re.findall(r"\$\$|\$", clean_content)) // 2
        stats["tables"] += len(re.findall(r"\| :---", clean_content))
        stats["words"] += len(clean_content.split())
        stats["chars"] += len(clean_content)

        chapters_payload.append((ch_title, f.stem, clean_content))

    toc_lines.append("\n---\n")
    master_lines.extend(toc_lines)

    # Ensamblar capítulos
    for ch_title, stem, ch_body in chapters_payload:
        master_lines.append(f"<!-- INICIO CAPÍTULO: {stem} -->\n")
        master_lines.append(ch_body)
        master_lines.append(f"\n\n<!-- FIN CAPÍTULO: {stem} -->\n\n---\n")

    master_md = "\n".join(master_lines)

    # Reescritura de enlaces cruzados internos hacia anclajes del documento unificado
    for stem, ch_slug in stem_to_slug.items():
        master_md = re.sub(r'\]\(' + re.escape(stem) + r'\.md(?:#[^\)]*)?\)', f'](#{ch_slug})', master_md)

    # Guía pedagógica para Audio Overview (NotebookLM Deep Dive)
    audio_guide = [
        "## 🎙️ Guía de Estudio y Audio Overview (Podcast) para NotebookLM",
        "",
        "Para aprovechar al máximo este Cuaderno Maestro en **Google NotebookLM**, recomendamos personalizar el **Audio Overview** (Podcast educativo) con las siguientes directrices:",
        "",
        "- **Rol y Tono:** Conversación dinámica y didáctica entre dos profesores de la UPC especializados en instrumentación electrónica y sistemas de medida.",
        "- **Enfoque conceptual:** Explicar el trasfondo físico y matemático de las derivas, el ruido, las incertidumbres y los transductores, utilizando metáforas del mundo real en vez de limitarse a leer ecuaciones.",
        "- **Punto de tensión pedagógica:** Analizar una de las preguntas complejas del banco de autoevaluación (marcada como Falsa por una sutil trampa técnica) y discutir por qué suele inducir a error en el examen.",
        "- **Síntesis final:** Resumen de las 3 reglas de oro de diseño electrónico expuestas a lo largo de este tema.",
        ""
    ]
    master_md = master_md + "\n\n---\n\n" + "\n".join(audio_guide)

    # Gran Formulario Maestro consolidado al final
    if include_formula_sheet:
        master_formula_sheet = generate_formula_sheet_from_markdown(master_md)
        if master_formula_sheet:
            master_md = master_md + "\n\n---\n\n" + master_formula_sheet

    master_md = re.sub(r"\n{3,}", "\n\n", master_md)
    master_md = re.sub(r"(?:---\s*\n+){2,}", "---\n\n", master_md).strip()

    safe_title = re.sub(r"[^\w\-_]", "_", topic_title).strip("_")
    master_file = output_dir / f"_Cuaderno_Maestro_{safe_title}.md"
    master_file.write_text(master_md, encoding="utf-8")

    return master_file, stats

def generate_course_dashboard(
    output_dir: Path,
    topic_title: str,
    total_stats: dict,
    files_detail: list
) -> Path:
    """Genera un reporte analítico del curso (_Reporte_Analitico_*.md) con métricas y densidad matemática."""
    output_dir = Path(output_dir)
    if not topic_title:
        topic_title = output_dir.name.replace("_", " ").replace("-", " ").title()

    timestamp = time.strftime("%Y-%m-%d %H:%M")
    total_docs = len(files_detail)
    total_words = sum(f.get("words", 0) for f in files_detail)
    total_chars = sum(f.get("chars", 0) for f in files_detail)
    total_math = sum(f.get("math", 0) for f in files_detail)
    total_tables = sum(f.get("tables", 0) for f in files_detail)
    total_diagrams = sum(f.get("diagrams", 0) for f in files_detail)

    avg_words = int(total_words / total_docs) if total_docs else 0
    avg_math = round(total_math / total_docs, 1) if total_docs else 0.0
    avg_tables = round(total_tables / total_docs, 1) if total_docs else 0.0

    lines = [
        f"# 📊 Reporte Analítico del Curso: {topic_title}",
        "",
        "> ℹ️ **Auditoría de Contenidos, Fidelidad y Densidad Matemática**  ",
        f"> 📅 **Generado:** {timestamp} | 📁 **Directorio:** `{output_dir.name}`  ",
        "",
        "---",
        "",
        "## 📈 Resumen Ejecutivo",
        "",
        "| Métrica Global | Total Acumulado | Promedio por Capítulo |",
        "| :--- | :---: | :---: |",
        f"| 📄 **Capítulos / Documentos** | **{total_docs}** | - |",
        f"| 📝 **Palabras Totales** | **{total_words:,}** | ~{avg_words:,} |",
        f"| 📐 **Fórmulas Matemáticas (LaTeX)** | **{total_math}** | ~{avg_math} |",
        f"| 📋 **Tablas GFM (Estructuradas)** | **{total_tables}** | ~{avg_tables} |",
        f"| 🖼️ **Diagramas y Esquemas** | **{total_diagrams}** | - |",
        "",
        "---",
        "",
        "## 🔬 Desglose y Densidad por Capítulo",
        "",
        "| Capítulo / Documento | Palabras | Fórmulas | Tablas | Densidad Matemática* | Clasificación |",
        "| :--- | :---: | :---: | :---: | :---: | :---: |"
    ]

    for item in files_detail:
        name = item.get("name", "")
        words = item.get("words", 0)
        math_count = item.get("math", 0)
        tables_count = item.get("tables", 0)
        density = round((math_count / words) * 1000, 2) if words > 0 else 0.0

        if density >= 5.0:
            classification = "Muy Analítico 🔴"
        elif density >= 1.0:
            classification = "Analítico 🟡"
        else:
            classification = "Conceptual 🟢"

        lines.append(f"| `{name}` | {words:,} | {math_count} | {tables_count} | {density:.2f} eq/1k | {classification} |")

    lines.extend([
        "",
        r"*\* Densidad Matemática = Cantidad de expresiones matemáticas por cada 1.000 palabras.*",
        "",
        "---",
        "",
        "## 💡 Guía de Estudio Recomendada para NotebookLM",
        "",
        "- 🔴 **Capítulos de Alta Densidad Analítica (> 5 eq/1k palabras):** Contienen el núcleo matemático y los modelos dinámicos/estáticos. Ideales para formular preguntas de resolución numérica y derivaciones a la IA.",
        "- 🟡 **Capítulos de Densidad Media (1 a 5 eq/1k palabras):** Equilibrio óptimo entre teoría física y relaciones cuantitativas. Claves para sintetizar principios de funcionamiento.",
        "- 🟢 **Capítulos Conceptuales (< 1 eq/1k palabras):** Marco normativo, definiciones y clasificaciones. Perfectos para generar cuestionarios conceptuales y tarjetas mnemotécnicas.",
        ""
    ])

    safe_title = re.sub(r"[^\w\-_]", "_", topic_title).strip("_")
    report_file = output_dir / f"_Reporte_Analitico_{safe_title}.md"
    report_file.write_text("\n".join(lines), encoding="utf-8")
    return report_file

def read_html_file_safely(file_path: Path) -> tuple[str, str]:
    """Detecta la codificación exacta del archivo HTML inspeccionando BOM y metadatos."""
    raw = file_path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        return raw.decode("utf-8-sig"), "utf-8-sig"
    
    head_sample = raw[:2048].decode("ascii", errors="ignore")
    m = re.search(r'<meta[^>]+charset=["\']?([a-zA-Z0-9_-]+)', head_sample, re.I)
    if not m:
        m = re.search(r'content=["\'][^"\']*charset=([a-zA-Z0-9_-]+)', head_sample, re.I)
    
    if m:
        encoding = m.group(1).lower()
        if encoding in ("utf8", "utf-8"): encoding = "utf-8"
        try:
            return raw.decode(encoding), encoding
        except Exception:
            pass
            
    try:
        return raw.decode("utf-8"), "utf-8"
    except UnicodeDecodeError:
        pass
        
    try:
        return raw.decode("cp1252"), "cp1252 (Windows-1252)"
    except Exception:
        return raw.decode("utf-8", errors="replace"), "utf-8 (fallback)"


# ----------------------------------------------------------------------
# 6. PIPELINE PRINCIPAL DE CONVERSIÓN Y EXTRACCIÓN DE AUTOEVALUACIÓN
# ----------------------------------------------------------------------

def extract_quiz_questions(html_content: str) -> list[dict]:
    """
    Extrae bancos de 50 preguntas/afirmaciones de scripts interactivos (BANC, DATA.items, ITEMS).
    Devuelve lista de diccionarios: [{"n": int, "q": str, "a": str, "j": str, "ref": str}]
    """
    questions = []

    def _clean_text(s: str) -> str:
        if not s: return ""
        return s.strip().replace("&nbsp;", " ").replace("&mdash;", "—").replace("&ndash;", "–").replace("&hellip;", "…")

    # 1. Formato BANC = [...] (Temas 1 y 2)
    m1 = re.search(r'(?:var|const|let)\s+BANC\s*=\s*(\[.*?\]);\s*(?:let|const|var|\n|function)', html_content, re.DOTALL)
    if m1:
        try:
            raw_items = json.loads(m1.group(1))
            for item in raw_items:
                ref_doc = item.get("df", "") or item.get("dt", "") or (f"Document {item.get('d', '')}" if item.get('d') else "")
                if ref_doc.lower().endswith(".html"):
                    ref_doc = ref_doc[:-5] + ".md"
                questions.append({
                    "n": item.get("n", 0),
                    "q": _clean_text(item.get("q", "")),
                    "a": item.get("a", "").strip().upper(),
                    "j": _clean_text(item.get("j", "")),
                    "ref": ref_doc
                })
        except Exception:
            pass

    # 2. Formato DATA = { blocs: [...], items: [...] } (Temas 3, 4, 5)
    if not questions:
        m2 = re.search(r'const\s+DATA\s*=\s*(\{.*?\});\s*(?:let|const|var|\n)', html_content, re.DOTALL)
        if m2:
            try:
                data_obj = json.loads(m2.group(1))
                blocs = data_obj.get("blocs", [])
                for item in data_obj.get("items", []):
                    b_idx = item.get("bloc", 0)
                    b_name = blocs[b_idx] if 0 <= b_idx < len(blocs) else f"Bloc {b_idx}"
                    questions.append({
                        "n": item.get("n", 0),
                        "q": _clean_text(item.get("text", "")),
                        "a": item.get("resp", "").strip().upper(),
                        "j": _clean_text(item.get("just", "")),
                        "ref": b_name
                    })
            except Exception:
                pass

    # 3. Formato ITEMS = [...] (Temas 6, 7, 8, 9, 10)
    if not questions:
        m3 = re.search(r'(?:var|const|let)\s+ITEMS\s*=\s*(\[.*?\]);\s*(?:let|const|var|\n|function)', html_content, re.DOTALL)
        if m3:
            try:
                raw_items = json.loads(m3.group(1))
                for item in raw_items:
                    questions.append({
                        "n": item.get("n", 0),
                        "q": _clean_text(item.get("q", "")),
                        "a": item.get("a", "").strip().upper(),
                        "j": _clean_text(item.get("j", "")),
                        "ref": f"Document {item.get('d', '')}" if item.get('d') else ""
                    })
            except Exception:
                pass

    return questions

def extract_and_format_interactive_quiz(html_content: str, doc_title: str = "") -> str:
    """
    Formatea el banco de preguntas/afirmaciones en Markdown pedagógico con tarjetas
    interactivas desplegables y solucionario rápido.
    """
    questions = extract_quiz_questions(html_content)
    if not questions:
        return ""

    md_lines = [
        "## 🧠 Banc d'Afirmacions d'Autoavaluació (Entrenament d'Examen)",
        "",
        "> [!TIP] **Com utilitzar aquest material d'entrenament**",
        "> Aquest banc conté **50 afirmacions clau** dissenyades per consolidar els conceptes de la unitat i preparar els qüestionaris d'avaluació continuada.",
        "> Intenta respondre mentalment **Vertader (V)** o **Fals (F)** abans de desplegar la solució i la justificació tècnica.",
        ""
    ]

    for item in questions:
        n = item["n"]
        q = item["q"]
        ans = item["a"]
        just = item["j"]
        ref = item["ref"]

        ans_label = "✅ **Vertader (V)**" if ans == "V" else "❌ **Fals (F)**"
        ref_line = f"\n> **📚 Document de referència:** `{ref}`" if ref else ""

        md_lines.append(f"### Qüestió {n:02d}")
        md_lines.append(f"> 📌 **Afirmació:** *{q}*")
        md_lines.append("> ")
        md_lines.append("> - [ ] **V** (Vertader)")
        md_lines.append("> - [ ] **F** (Fals)")
        md_lines.append("> ")
        md_lines.append("> <details>")
        md_lines.append("> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>")
        md_lines.append("> ")
        md_lines.append(f"> **Resposta Correcta:** {ans_label}")
        md_lines.append("> ")
        md_lines.append(f"> **Justificació Tècnica:** *{just}*")
        if ref_line:
            md_lines.append(ref_line)
        md_lines.append("> </details>")
        md_lines.append("")

    # Tabla Resumen (Solucionari Ràpid)
    md_lines.append("---")
    md_lines.append("")
    md_lines.append("## 📋 Solucionari Ràpid (Taula de Respostes i Justificacions)")
    md_lines.append("")
    md_lines.append("| Nº | Resposta | Justificació Tècnica Resumida | Referència |")
    md_lines.append("| :---: | :---: | :--- | :--- |")

    for item in questions:
        n = item["n"]
        ans = f"**{item['a']}**"
        just_clean = item["j"].replace("|", "\\|").replace("\n", " ")
        if len(just_clean) > 120:
            just_clean = just_clean[:117] + "..."
        ref_clean = item["ref"].replace("|", "\\|")
        md_lines.append(f"| **{n:02d}** | {ans} | {just_clean} | {ref_clean} |")

    md_lines.append("")
    return "\n".join(md_lines)


def convert_html_to_markdown(
    html_content: str,
    title: str = "",
    rewrite_links: bool = True,
    include_meta: bool = True,
    include_yaml: bool = False,
    generate_toc: bool = True,
    include_formula_sheet: bool = False,
    assets_dir: Path = None,
    doc_stem: str = "doc",
    source_path: Optional[Path] = None
) -> tuple[str, dict]:
    """
    Convierte cualquier HTML a Markdown ultra fiel.
    Devuelve la cadena Markdown resultante y un diccionario con métricas del proceso.
    """
    stats = {"math": 0, "tables": 0, "diagrams": 0, "b64_images": 0, "quiz_questions": 0}

    html_content = html_content.replace("\u00a0", " ")
    for ch in ["\u200b", "\u200c", "\u200d", "\ufeff"]:
        html_content = html_content.replace(ch, "")

    # 0. Extraer banco de preguntas/afirmaciones interactivas antes de cualquier limpieza
    quiz_markdown = extract_and_format_interactive_quiz(html_content, title)

    soup = BeautifulSoup(html_content, "html.parser")

    # 1. Extraer metadatos
    metadata = extract_metadata(soup)
    doc_title = metadata.get("title") or title or ""

    # 2. Extraer figuras referenciadas en scripts (data-fig) e imágenes base64 a archivos físicos
    extract_figs_from_scripts(soup)
    if assets_dir:
        stats["b64_images"] = extract_base64_images(soup, assets_dir, doc_stem)

    # 3. Tokenizar y proteger fórmulas matemáticas
    soup, math_registry, stats["math"] = extract_and_shield_math(soup)

    # 4. Limpiar ruido publicitario y scripts no matemáticos
    soup = clean_soup_noise(soup)

    # 5. Tokenizar y proteger diagramas (Mermaid / PlantUML) y multimedia
    soup, diagram_registry, stats["diagrams"] = extract_and_shield_diagrams(soup)
    soup = preprocess_media_elements(soup)

    # 6. Reescritura de enlaces locales (.html -> .md) con resolución inteligente de índices
    if rewrite_links:
        soup = rewrite_internal_links(soup, source_path=source_path)

    # 7. Componentes didácticos y de diseño moderno
    soup = preprocess_navigation_bars(soup)
    soup = preprocess_course_components(soup)
    soup = preprocess_callouts_and_admonitions(soup)
    soup = preprocess_figures_and_captions(soup)
    soup = preprocess_definition_lists(soup)
    soup = preprocess_task_lists(soup)
    soup = preprocess_details_summary(soup)
    soup = preprocess_footnotes(soup)

    # Instancia de conversión
    converter = UltraFaithfulMarkdownConverter(
        heading_style="ATX",
        bullets="-",
        code_language="",
        autolinks=True
    )

    # 8. Tokenizar y proteger tablas GFM (con matriz 2D para rowspan/colspan)
    soup, table_registry, stats["tables"] = extract_and_shield_tables(soup, converter)

    # 9. Seleccionar cuerpo principal
    main_target = soup.find("article") or soup.find("main") or soup.find("body") or soup

    # 10. Convertir DOM a Markdown
    markdown = converter.convert_soup(main_target)

    # 11. Restaurar tablas protegidas
    for token, table_md in table_registry.items():
        markdown = markdown.replace(token, table_md)

    # 12. Restaurar fórmulas matemáticas protegidas
    for token, math_md in math_registry.items():
        markdown = markdown.replace(token, math_md)

    # 13. Restaurar diagramas protegidos
    for token, diag_md in diagram_registry.items():
        markdown = markdown.replace(token, diag_md)

    # 14. Post-procesamiento estético y normalización de espacios
    # Limpieza de entidades HTML residuales
    markdown = markdown.replace("&nbsp;", " ").replace("&mdash;", "—").replace("&ndash;", "–").replace("&hellip;", "…")
    markdown = markdown.replace("&thinsp;", " ").replace("&ensp;", " ").replace("&emsp;", " ")
    # Limpieza de spans y divs vacíos residuales
    markdown = re.sub(r"<(?:span|div|section)[^>]*>\s*</(?:span|div|section)>", "", markdown)
    # Limpieza de enlaces vacíos []()
    markdown = re.sub(r"\[\s*\]\([^\)]*\)", "", markdown)
    # Normalización de puntuación y espacios
    markdown = re.sub(r" +([,\.!\?;:])", r"\1", markdown)
    # Conversión de superíndices y subíndices HTML residuales vinculados a bases o autónomos
    def _repl_sup(m):
        base = m.group(1).strip("$").strip()
        exp = m.group(2).strip().strip("$").strip().replace("−", "-")
        return f"${base}^{{{exp}}}$"
    markdown = re.sub(r"([a-zA-Z0-9_\$\)\}\]]+)\s*<sup>\s*(.*?)\s*</sup>", _repl_sup, markdown)
    markdown = re.sub(r"<sup>\s*(.*?)\s*</sup>", lambda m: f"$^{{{m.group(1).strip().strip('$').strip().replace('−', '-')}}}$", markdown)

    def _repl_sub(m):
        base = m.group(1).strip("$").strip()
        sub = m.group(2).strip().strip("$").strip().replace("−", "-")
        return f"${base}_{{{sub}}}$"
    markdown = re.sub(r"([a-zA-Z0-9_\$\)\}\]]+)\s*<sub>\s*(.*?)\s*</sub>", _repl_sub, markdown)
    markdown = re.sub(r"<sub>\s*(.*?)\s*</sub>", lambda m: f"$_{{{m.group(1).strip().strip('$').strip().replace('−', '-')}}}$", markdown)

    # Formateo canónico de bloques matemáticos display
    markdown = re.sub(r"\n*\$\$\n*(.*?)\n*\$\$\n*", r"\n\n$$\n\1\n$$\n\n", markdown, flags=re.DOTALL)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    markdown = "\n".join(line.rstrip() for line in markdown.splitlines()).strip()

    # 15. Estructurar título principal y metadatos antes del TOC
    body_header_parts = []
    has_h1 = markdown.startswith("# ")
    if doc_title and not has_h1:
        body_header_parts.append(f"# {doc_title}")

    if include_meta:
        meta_badges = []
        if metadata.get("date"):
            meta_badges.append(f"📅 **Fecha:** {metadata['date']}")
        if metadata.get("author"):
            meta_badges.append(f"👤 **Autor:** {metadata['author']}")
        if metadata.get("source"):
            meta_badges.append(f"🔗 **Fuente:** [{metadata['source']}]({metadata['source']})")

        if meta_badges or metadata.get("description"):
            meta_block = "> " + " | ".join(meta_badges) if meta_badges else ""
            if metadata.get("description"):
                desc_line = f"> 📝 *{metadata['description']}*"
                meta_block = f"{meta_block}\n{desc_line}" if meta_block else desc_line
            body_header_parts.append(f"{meta_block}\n\n---")

    # 16. Generación de TOC (posicionada inmediatamente tras título/metadatos)
    toc_str = ""
    if generate_toc:
        toc_str = generate_toc_from_markdown(markdown)

    # Ensamblar contenido principal
    if body_header_parts:
        markdown = "\n\n".join(body_header_parts) + "\n\n" + (toc_str + "\n\n" if toc_str else "") + markdown
    elif toc_str:
        markdown = toc_str + "\n\n" + markdown

    # 17. Incorporar Banco de Autoevaluación interactivo si existe
    if quiz_markdown:
        markdown = markdown + "\n\n---\n\n" + quiz_markdown
        stats["quiz_questions"] = 50

    # 18. Formulario Resumen de Ecuaciones
    if include_formula_sheet:
        formula_sheet = generate_formula_sheet_from_markdown(markdown)
        if formula_sheet:
            markdown = markdown + "\n\n---\n\n" + formula_sheet

    # 19. YAML Frontmatter al inicio absoluto del documento
    if include_yaml and (doc_title or metadata):
        yaml_lines = ["---"]
        if doc_title: yaml_lines.append(f'title: "{doc_title}"')
        if metadata.get("author"): yaml_lines.append(f'author: "{metadata["author"]}"')
        if metadata.get("date"): yaml_lines.append(f'date: "{metadata["date"]}"')
        if metadata.get("source"): yaml_lines.append(f'source: "{metadata["source"]}"')
        if metadata.get("description"): yaml_lines.append(f'description: "{metadata["description"]}"')
        yaml_lines.append("---\n")
        markdown = "\n".join(yaml_lines) + "\n\n" + markdown

    markdown = re.sub(r">\s*\[!([A-Z]+)\](?:\s*\n>\s*)+\[!([A-Z]+)\]", r"> [!\2]", markdown)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    markdown = re.sub(r"(?:---\s*\n+){2,}", "---\n\n", markdown)
    return markdown.strip(), stats


# ----------------------------------------------------------------------
# 7. PROCESAMIENTO POR LOTES Y ARCHIVO INDIVIDUAL
# ----------------------------------------------------------------------

def convert_single_file(
    input_file: str,
    output_file: str,
    rewrite_links: bool = True,
    include_meta: bool = True,
    include_yaml: bool = False,
    generate_toc: bool = True,
    include_formula_sheet: bool = False,
    extract_b64: bool = True
) -> dict:
    in_path = Path(input_file)
    out_path = Path(output_file)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    
    html, enc = read_html_file_safely(in_path)
    title_hint = in_path.stem.replace("-", " ").replace("_", " ").title()
    assets_dir = out_path.parent / "assets" if extract_b64 else None
    
    md_text, stats = convert_html_to_markdown(
        html,
        title=title_hint,
        rewrite_links=rewrite_links,
        include_meta=include_meta,
        include_yaml=include_yaml,
        generate_toc=generate_toc,
        include_formula_sheet=include_formula_sheet,
        assets_dir=assets_dir,
        doc_stem=in_path.stem,
        source_path=in_path
    )
    with open(out_path, "w", encoding="utf-8") as fp:
        fp.write(md_text)
    
    stats["encoding"] = enc
    return stats

def process_batch(
    input_folder: str,
    output_folder: str,
    progress_callback=None,
    rewrite_links: bool = True,
    include_meta: bool = True,
    include_yaml: bool = False,
    generate_toc: bool = True,
    include_formula_sheet: bool = False,
    create_master_doc: bool = False,
    create_dashboard: bool = True,
    extract_b64: bool = True,
    cancel_event: threading.Event = None
) -> tuple[int, dict, list]:
    in_path = Path(input_folder)
    out_path = Path(output_folder)
    out_path.mkdir(parents=True, exist_ok=True)

    files = sorted(list(in_path.glob("**/*.html")) + list(in_path.glob("**/*.htm")))
    total_stats = {"math": 0, "tables": 0, "diagrams": 0, "b64_images": 0, "quiz_questions": 0}
    if not files:
        return 0, total_stats, []
    total_files = len(files)
    converted = 0
    generated_files = []
    files_detail = []

    for idx, f in enumerate(files):
        if cancel_event and cancel_event.is_set():
            break

        rel = f.relative_to(in_path)
        dest = out_path / rel.with_suffix(".md")
        dest.parent.mkdir(parents=True, exist_ok=True)
        assets_dir = dest.parent / "assets" if extract_b64 else None

        html, enc = read_html_file_safely(f)
        title_hint = f.stem.replace("-", " ").replace("_", " ").title()
        
        md_text, stats = convert_html_to_markdown(
            html,
            title=title_hint,
            rewrite_links=rewrite_links,
            include_meta=include_meta,
            include_yaml=include_yaml,
            generate_toc=generate_toc,
            include_formula_sheet=include_formula_sheet,
            assets_dir=assets_dir,
            doc_stem=f.stem,
            source_path=f
        )
        with open(dest, "w", encoding="utf-8") as fp:
            fp.write(md_text)

        generated_files.append(dest)

        words_count = len(md_text.split())
        chars_count = len(md_text)
        files_detail.append({
            "name": dest.name,
            "words": words_count,
            "chars": chars_count,
            "math": stats.get("math", 0),
            "tables": stats.get("tables", 0),
            "diagrams": stats.get("diagrams", 0),
            "b64_images": stats.get("b64_images", 0)
        })

        for k in total_stats:
            total_stats[k] += stats.get(k, 0)
        converted += 1

        if progress_callback:
            progress_callback(idx + 1, total_files, f.name, stats)

    # Generación de Cuaderno Maestro Unificado si se solicitó
    if create_master_doc and converted > 1 and not (cancel_event and cancel_event.is_set()):
        master_file, master_stats = generate_master_topic_document(
            out_path,
            topic_title=in_path.name,
            include_formula_sheet=include_formula_sheet
        )
        if master_file:
            generated_files.insert(0, master_file)
            total_stats["master_document"] = str(master_file.name)

    # Generación de Reporte Analítico del Lote si se solicitó
    if create_dashboard and converted > 1 and not (cancel_event and cancel_event.is_set()):
        dash_file = generate_course_dashboard(
            out_path,
            topic_title=in_path.name,
            total_stats=total_stats,
            files_detail=files_detail
        )
        if dash_file:
            generated_files.append(dash_file)
            total_stats["dashboard"] = str(dash_file.name)

    return converted, total_stats, generated_files

def generate_course_glossary(output_dir: Path) -> Path:
    """
    Genera un diccionario/glosario de conceptos clave centralizado (_Glosario_Conceptos_Clave.md)
    escaneando todos los archivos Markdown generados en output_dir.
    """
    target = output_dir / "_Glosario_Conceptos_Clave.md"
    md_files = sorted([f for f in output_dir.glob("**/*.md") if not f.name.startswith("_")])
    terms = {}

    for f in md_files:
        try:
            content = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        first_h1 = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        doc_title = first_h1.group(1).strip() if first_h1 else f.stem.replace("_", " ")
        rel_path = f.relative_to(output_dir).as_posix()

        lines = content.splitlines()
        for line in lines:
            line_s = line.strip()
            # Patrón 1: lista con negrita '- **Término**: Definición'
            m1 = re.match(r"^[-*]\s+\*\*([A-Za-záéíóúàèòïüçÁÉÍÓÚÀÈÒÏÜÇ0-9\s/_\-–\(\)\.\,]+)\*\*\s*[:–—]\s*(.+)$", line_s)
            if m1:
                term = m1.group(1).strip()
                defn = m1.group(2).strip()
                if 2 <= len(term) <= 50 and len(defn) >= 20:
                    tl = term.lower()
                    if not tl.startswith(("figura", "taula", "tabla", "nº", "exemple", "exercici", "pas", "observaci", "resum", "nota", "com ", "on ", "aproximaci", "mètode", "opció", "fase")):
                        if term not in terms:
                            terms[term] = (defn, doc_title, rel_path)

            # Patrón 2: párrafo con negrita '**Término**: Definición'
            m2 = re.match(r"^\*\*([A-Za-záéíóúàèòïüçÁÉÍÓÚÀÈÒÏÜÇ0-9\s/_\-–\(\)\.\,]+)\*\*\s*[:–—]\s*(.+)$", line_s)
            if m2:
                term = m2.group(1).strip()
                defn = m2.group(2).strip()
                if 2 <= len(term) <= 50 and len(defn) >= 25:
                    tl = term.lower()
                    if not tl.startswith(("figura", "taula", "tabla", "nº", "exemple", "exercici", "pas", "observaci", "resum", "nota", "com ", "on ", "aproximaci", "mètode", "opció", "fase")):
                        if term not in terms:
                            terms[term] = (defn, doc_title, rel_path)

    if not terms:
        return None

    # Agrupar alfabéticamente
    grouped = defaultdict(list)
    for term in sorted(terms.keys(), key=lambda s: s.lower()):
        first_letter = term[0].upper()
        for char, repl in [("À", "A"), ("Á", "A"), ("È", "E"), ("É", "E"), ("Í", "I"), ("Ò", "O"), ("Ó", "O"), ("Ú", "U")]:
            if first_letter == char:
                first_letter = repl
        if not first_letter.isalpha():
            first_letter = "#"
        defn, title, rel = terms[term]
        grouped[first_letter].append((term, defn, title, rel))

    letters = sorted(grouped.keys())
    nav_links = " · ".join([f"[{L}](#{L.lower() if L != '#' else 'simbols'})" for L in letters])

    out = [
        "# 📚 Glossari General de Conceptes Clau · Sistemes de Mesura",
        "",
        "> [!NOTE] **Diccionari de Termes Tècnics i Fonaments Didàctics**",
        f"> Aquest document recopila de manera centralitzada **{len(terms)} definicions essencials** extretes de tots els temes del curs.",
        "> Inclou referències creuades a cada capítol per facilitar la consulta ràpida en NotebookLM, Obsidian i lectors Markdown.",
        "",
        f"**Navegació Ràpida:** {nav_links}",
        "",
        "---",
        ""
    ]

    for letter in letters:
        sec_id = letter.lower() if letter != '#' else 'simbols'
        out.append(f"## {letter}")
        out.append("")
        for term, defn, title, rel in grouped[letter]:
            out.append(f"### {term}")
            out.append(f"> {defn}")
            out.append(f">")
            out.append(f"> 📖 *Font: [{title}]({rel})*")
            out.append("")
        out.append("---")
        out.append("")

    out.append("## 🤖 Com treure el màxim partit a aquest Glossari amb la IA (NotebookLM)")
    out.append("")
    out.append("Copia i enganxa aquests prompts directament al xat de NotebookLM o Claude:")
    out.append("")
    out.append("1. **Qüestionari creuat:** *«Fes-me un qüestionari de 10 preguntes conceptuals basat en les definicions d'aquest glossari, alternant preguntes de resposta curta i elecció múltiple.»*")
    out.append("2. **Diferenciació conceptual:** *«Explica clarament quina és la diferència funcional i matemàtica entre [Terme A] i [Terme B] segons el curs.»*")
    out.append("3. **Síntesi per a examen:** *«Genera un esquema de repàs d'una sola pàgina que relacioni tots els termes clau del Tema 2 amb els mètodes de mesura del Tema 6.»*")
    out.append("")

    target.write_text("\n".join(out), encoding="utf-8")
    return target

def create_anki_apkg(output_path: Path, deck_name: str, cards_data: list, deck_id=2059400110, model_id=1607392319) -> bool:
    """
    Genera un paquete .apkg de Anki 100% compatible con Anki 2.1+, Anki 23/24 (Rust backend) y AnkiMobile.
    Utiliza genanki si está disponible, o un generador SQLite3 de alta compatibilidad con el esquema completo de Anki.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Intento 1: genanki (el estándar de facto para Anki)
    try:
        import genanki

        css_style = """
        .card {
            font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            font-size: 18px;
            text-align: left;
            color: #f5f5f7;
            background-color: #161617;
            padding: 26px;
            border-radius: 14px;
            line-height: 1.6;
        }
        .tema-tag {
            display: inline-block;
            background: #0071e3;
            color: #ffffff;
            padding: 5px 14px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
            margin-bottom: 16px;
            letter-spacing: 0.5px;
        }
        .question {
            font-size: 20px;
            font-weight: 600;
            color: #ffffff;
            margin-bottom: 16px;
        }
        .divider {
            border-top: 1px solid #2c2c2e;
            margin: 22px 0;
        }
        .answer-v {
            color: #30d158;
            font-size: 22px;
            font-weight: 700;
            margin-bottom: 14px;
        }
        .answer-f {
            color: #ff453a;
            font-size: 22px;
            font-weight: 700;
            margin-bottom: 14px;
        }
        .justification {
            background-color: #1c1c1e;
            border-left: 3px solid #0071e3;
            padding: 16px 20px;
            border-radius: 8px;
            color: #d1d1d6;
            font-size: 16px;
        }
        """

        model = genanki.Model(
            model_id,
            "Sistemes de Mesura Apple Pro",
            fields=[
                {"name": "Question"},
                {"name": "Answer"},
                {"name": "AnswerClass"},
                {"name": "Justification"},
                {"name": "Tags"},
            ],
            templates=[
                {
                    "name": "Card 1",
                    "qfmt": "<div class='tema-tag'>{{Tags}}</div><div class='question'>{{Question}}</div>",
                    "afmt": "{{FrontSide}}<div class='divider'></div><div class='{{AnswerClass}}'>{{Answer}}</div><div class='justification'>{{Justification}}</div>",
                },
            ],
            css=css_style
        )

        deck = genanki.Deck(deck_id, deck_name)

        def sanitize_html(s: str) -> str:
            return re.sub(r'<(?!\/?(?:b|i|br|span|small|div|hr|code|p)\b)', '&lt;', s)

        for c in cards_data:
            q_raw = c.get("question", "")
            a_raw = c.get("answer", "")
            j_raw = c.get("justification", "")
            tags_list = c.get("tags", ["Sistemes_de_Mesura"])
            tag_str = " ".join(tags_list)

            is_v = "VERTADER" in a_raw.upper()
            ans = "✅ VERTADER (V)" if is_v else "❌ FALS (F)"
            ans_class = "answer-v" if is_v else "answer-f"

            q_clean = sanitize_html(q_raw)
            j_clean = sanitize_html(j_raw)

            note = genanki.Note(
                model=model,
                fields=[q_clean, ans, ans_class, j_clean, tag_str],
                tags=tags_list
            )
            deck.add_note(note)

        pkg = genanki.Package(deck)
        pkg.write_to_file(str(output_path))
        return True
    except Exception:
        pass

    # Intento 2: Generador SQLite nativo con esquema Rust-compatible
    now = int(time.time())
    now_ms = int(time.time() * 1000)

    temp_dir = tempfile.mkdtemp()
    db_path = os.path.join(temp_dir, "collection.anki2")

    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        cur.executescript("""
        CREATE TABLE col (
            id integer primary key, crt integer not null, mod integer not null, scm integer not null,
            ver integer not null, dty integer not null, usn integer not null, ls integer not null,
            conf text not null, models text not null, decks text not null, dconf text not null, tags text not null
        );
        CREATE TABLE notes (
            id integer primary key, guid text not null, mid integer not null, mod integer not null,
            usn integer not null, tags text not null, flds text not null, sfld text not null,
            csum integer not null, flags integer not null, data text not null
        );
        CREATE TABLE cards (
            id integer primary key, nid integer not null, did integer not null, ord integer not null,
            mod integer not null, usn integer not null, type integer not null, queue integer not null,
            due integer not null, ivl integer not null, factor integer not null, reps integer not null,
            lapses integer not null, left integer not null, odue integer not null, odid integer not null,
            flags integer not null, data text not null
        );
        CREATE TABLE revlog (
            id integer primary key, cid integer not null, usn integer not null, ease integer not null,
            ivl integer not null, lastIvl integer not null, factor integer not null, time integer not null, type integer not null
        );
        CREATE TABLE graves (usn integer not null, oid integer not null, type integer not null);
        CREATE INDEX ix_notes_usn on notes (usn);
        CREATE INDEX ix_cards_usn on cards (usn);
        CREATE INDEX ix_cards_nid on cards (nid);
        CREATE INDEX ix_cards_sched on cards (did, queue, due);
        """)

        css_style = """
        .card {
            font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", sans-serif;
            font-size: 18px;
            text-align: left;
            color: #f5f5f7;
            background-color: #161617;
            padding: 24px;
            border-radius: 12px;
            line-height: 1.5;
        }
        .tema-tag {
            display: inline-block;
            background: #0071e3;
            color: #ffffff;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
            margin-bottom: 14px;
        }
        .question { font-size: 20px; font-weight: 600; color: #ffffff; margin-bottom: 16px; }
        .divider { border-top: 1px solid #2c2c2e; margin: 20px 0; }
        .answer-v { color: #30d158; font-size: 20px; font-weight: 700; margin-bottom: 12px; }
        .answer-f { color: #ff453a; font-size: 20px; font-weight: 700; margin-bottom: 12px; }
        .justification { background-color: #1c1c1e; border-left: 3px solid #0071e3; padding: 12px 16px; border-radius: 6px; color: #d1d1d6; font-size: 16px; }
        """

        model = {
            str(model_id): {
                "id": model_id,
                "name": "Sistemes de Mesura Apple Pro",
                "type": 0,
                "mod": now,
                "usn": -1,
                "sortf": 0,
                "did": deck_id,
                "tmpls": [
                    {
                        "name": "Card 1",
                        "ord": 0,
                        "qfmt": "<div class='tema-tag'>{{Tags}}</div><div class='question'>{{Question}}</div>",
                        "afmt": "{{FrontSide}}\n<div class='divider'></div>\n<div class='{{AnswerClass}}'>{{Answer}}</div>\n<div class='justification'>{{Justification}}</div>",
                        "bqfmt": "",
                        "bafmt": "",
                        "did": None
                    }
                ],
                "flds": [
                    {"name": "Question", "ord": 0, "sticky": False, "rtl": False, "font": "Arial", "size": 20, "media": []},
                    {"name": "Answer", "ord": 1, "sticky": False, "rtl": False, "font": "Arial", "size": 20, "media": []},
                    {"name": "AnswerClass", "ord": 2, "sticky": False, "rtl": False, "font": "Arial", "size": 16, "media": []},
                    {"name": "Justification", "ord": 3, "sticky": False, "rtl": False, "font": "Arial", "size": 16, "media": []},
                    {"name": "Tags", "ord": 4, "sticky": False, "rtl": False, "font": "Arial", "size": 14, "media": []}
                ],
                "css": css_style,
                "latexPre": "\\documentclass[12pt]{article}\n\\special{papersize=3in,5in}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amssymb,amsmath}\n\\pagestyle{empty}\n\\setlength{\\parindent}{0in}\n\\begin{document}\n",
                "latexPost": "\\end{document}",
                "req": [[0, "all", [0]]]
            }
        }

        decks = {
            "1": {
                "id": 1,
                "mod": now,
                "name": "Default",
                "usn": 0,
                "maxTaken": 60,
                "collapsed": False,
                "browserCollapsed": False,
                "desc": "",
                "dyn": 0,
                "conf": 1,
                "extendNew": 10,
                "extendRev": 50,
                "lrnToday": [0, 0],
                "newToday": [0, 0],
                "revToday": [0, 0],
                "timeToday": [0, 0]
            },
            str(deck_id): {
                "id": deck_id,
                "mod": now,
                "name": deck_name,
                "usn": -1,
                "maxTaken": 60,
                "collapsed": False,
                "browserCollapsed": False,
                "desc": "Banco Oficial de Preguntas - Sistemes de Mesura (EEBE · UPC)",
                "dyn": 0,
                "conf": 1,
                "extendNew": 10,
                "extendRev": 50,
                "lrnToday": [0, 0],
                "newToday": [0, 0],
                "revToday": [0, 0],
                "timeToday": [0, 0]
            }
        }

        dconf = {
            "1": {
                "id": 1,
                "mod": now,
                "name": "Default",
                "usn": 0,
                "maxTaken": 60,
                "autoplay": True,
                "timer": 0,
                "replayq": True,
                "new": {"bury": False, "delays": [1.0, 10.0], "initialFactor": 2500, "ints": [1, 4, 0], "order": 1, "perDay": 50},
                "rev": {"bury": False, "ease4": 1.3, "fuzz": 0.05, "ivlFct": 1.0, "maxIvl": 36500, "minSpace": 1, "perDay": 200},
                "lapse": {"delays": [10.0], "leechAction": 0, "leechFails": 8, "minInt": 1, "mult": 0.0}
            }
        }

        conf = {
            "nextPos": 1,
            "estTimes": True,
            "activeDecks": [1, deck_id],
            "sortType": "noteFld",
            "timeLim": 0,
            "sortBackwards": False,
            "addToCur": True,
            "curDeck": deck_id,
            "curModel": model_id,
            "collapseTime": 1200
        }

        cur.execute("""
            INSERT INTO col VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (1, now, now_ms, now_ms, 11, 0, 0, 0, json.dumps(conf), json.dumps(model), json.dumps(decks), json.dumps(dconf), "{}"))

        current_time_id = int(time.time() * 1000)
        for idx, c in enumerate(cards_data):
            note_id = current_time_id + idx * 2
            card_id = current_time_id + idx * 2 + 1

            question = c.get("question", "")
            answer = c.get("answer", "")
            justification = c.get("justification", "")
            tags_list = c.get("tags", ["Sistemes_de_Mesura"])
            tag_str = " ".join(tags_list)

            is_v = "VERTADER" in answer.upper()
            ans_str = "✅ VERTADER (V)" if is_v else "❌ FALS (F)"
            ans_class = "answer-v" if is_v else "answer-f"

            def to_mathjax(text):
                text = re.sub(r'\$\$(.+?)\$\$', r'\[\1\]', text, flags=re.DOTALL)
                text = re.sub(r'\$([^\$\n]+?)\$', r'\(\1\)', text)
                return text.replace("\n", "<br>")

            q_fmt = to_mathjax(question)
            j_fmt = to_mathjax(justification)

            flds = f"{q_fmt}\x1f{ans_str}\x1f{ans_class}\x1f{j_fmt}\x1f{tag_str}"
            sfld = question[:50]
            csum = int(hashlib.sha1(sfld.encode('utf-8')).hexdigest()[:8], 16)
            guid = hashlib.md5(f"{deck_id}_{idx}_{sfld}".encode('utf-8')).hexdigest()[:10]

            cur.execute("""
                INSERT INTO notes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (note_id, guid, model_id, now, -1, f" {tag_str} ", flds, sfld, csum, 0, ""))

            cur.execute("""
                INSERT INTO cards VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (card_id, note_id, deck_id, 0, now, -1, 0, 0, idx + 1, 0, 2500, 0, 0, 0, 0, 0, 0, ""))

        conn.commit()
        conn.close()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(str(output_path), "w", zipfile.ZIP_DEFLATED) as zf:
            zf.write(db_path, "collection.anki2")
            zf.writestr("media", "{}")

        try:
            os.remove(db_path)
            os.rmdir(temp_dir)
        except Exception:
            pass
        return True
    except Exception as e:
        return False

def generate_formula_cheatsheet(output_dir: Path) -> Path:
    """
    Genera el documento _Formulario_Oficial_Examen.md sintetizando todas las ecuaciones,
    constantes físicas y criterios de diseño de los 10 temas del curso para examen y NotebookLM.
    """
    target = output_dir / "_Formulario_Oficial_Examen.md"
    content = r"""# 📐 Formulario Oficial de Examen · Sistemes de Mesura
> 🏛️ **Universitat Politècnica de Catalunya (UPC · EEBE)**  
> 📚 **Guía Rápida de Ecuaciones, Leyes Físicas y Criterios de Diseño (Temas 1 al 10)**  
> ⚡ **Formato optimizado para NotebookLM, consulta en pantalla y preparación de examen**

---

## 📑 Índice de Bloques Temáticos
1. [Tema 1: Características Estáticas y Dinámicas de Sensores](#tema-1-características-estáticas-y-dinámicas-de-sensores)
2. [Tema 2: Puentes de Medida (Wheatstone y Variantes)](#tema-2-puentes-de-medida-wheatstone-y-variantes)
3. [Tema 3: Amplificación y Acondicionamiento de Señal (INA)](#tema-3-amplificación-y-acondicionamiento-de-señal-ina)
4. [Tema 4: Ruido e Interferencias en Instrumentación](#tema-4-ruido-e-interferencias-en-instrumentación)
5. [Tema 5 y 6: Filtros Analógicos Activos y Respuesta Temporal](#tema-5-y-6-filtros-analógicos-activos-y-respuesta-temporal)
6. [Tema 7: Convertidores Digital-Analógico (DAC)](#tema-7-convertidores-digital-analógico-dac)
7. [Tema 8: Convertidores Analógico-Digital (ADC)](#tema-8-convertidores-analógico-digital-adc)
8. [Tema 9: Muestreo y Retención (Sample & Hold)](#tema-9-muestreo-y-retención-sample--hold)
9. [Tema 10: Calibración, Linealización e Incertidumbre (GUM)](#tema-10-calibración-linealización-e-incertidumbre-gum)

---

## Tema 1: Características Estáticas y Dinámicas de Sensores

### 1.1 Sensibilidad Estática
$$\begin{equation}
S = \frac{dy}{dx} \quad \text{o} \quad S_0 = \left. \frac{dy}{dx} \right|_{x_0}
\end{equation}$$
- Para respuesta lineal: $y = S \cdot x + y_0$.
- Unidades: $[\text{Unidades de Salida}] / [\text{Unidades de Entrada}]$.

### 1.2 Errores Estáticos
- **Error Absoluto:**
  $$\begin{equation}
  e_a = y_{\text{mesurat}} - y_{\text{patró}}
  \end{equation}$$
- **Error Relativo:**
  $$\begin{equation}
  e_r = \frac{y_{\text{mesurat}} - y_{\text{patró}}}{y_{\text{patró}}} \times 100\%
  \end{equation}$$
- **No-Linealidad respecto al Fondo de Escala (FSR):**
  $$\begin{equation}
  \varepsilon_{NL} = \frac{\max |y_i - y_{\text{lin},i}|}{\text{FSR}} \times 100\%
  \end{equation}$$
- **Histéresis Máxima:**
  $$\begin{equation}
  H_{\max} = \frac{\max |y_{\text{pujada}} - y_{\text{baixada}}|}{\text{FSR}} \times 100\%
  \end{equation}$$

### 1.3 Sensores Resistivos de Temperatura
- **RTD (Pt100, aproximación lineal en rango industrial):**
  $$\begin{equation}
  R(T) = R_0 \left( 1 + \alpha \Delta T \right) \quad \text{con } \alpha \approx 3.85 \times 10^{-3} \text{ }^\circ\text{C}^{-1}
  \end{equation}$$
- **Termistor NTC (Ecuación Exponencial simplificada):**
  $$\begin{equation}
  R(T) = R_0 \exp\left[ \beta \left( \frac{1}{T} - \frac{1}{T_0} \right) \right], \quad \alpha = \frac{1}{R} \frac{dR}{dT} = -\frac{\beta}{T^2}
  \end{equation}$$
  *(Temperaturas siempre en Kelvin en la formulación de $\beta$)*.

### 1.4 Galgas Extensométricas (Strain Gauges)
- **Factor de Galga ($K$ o $GF$):**
  $$\begin{equation}
  K = \frac{\Delta R / R}{\varepsilon} = 1 + 2\nu + \frac{\Delta \rho / \rho}{\varepsilon}
  \end{equation}$$
  - Metálicas: $K \approx 2.0$ a $2.1$ (predomina cambio geométrico con coeficiente de Poisson $\nu$).
  - Semiconductoras (Piezorresistivas): $K \approx 100$ a $150$ (predomina efecto piezorresistivo $\Delta \rho / \rho$).

---

## Tema 2: Puentes de Medida (Wheatstone y Variantes)

### 2.1 Ecuación General del Puente de Wheatstone
$$\begin{equation}
V_o = V_s \left( \frac{R_1}{R_1 + R_2} - \frac{R_4}{R_3 + R_4} \right)
\end{equation}$$
- **Condición de Equilibrio ($V_o = 0$):**
  $$\begin{equation}
  R_1 R_3 = R_2 R_4
  \end{equation}$$

### 2.2 Configuraciones con Sensores Piezorresistivos / Galgas
| Configuración | Galgas Activas | Tensión de Salida $V_o$ | Linealidad | Compensación Térmica |
| :--- | :---: | :---: | :---: | :---: |
| **Cuarto de Puente (1/4)** | 1 ($R_1 = R + \Delta R$) | $$V_o \approx \frac{V_s}{4} \frac{\Delta R}{R}$$ | No lineal (error $\approx \frac{1}{2} \frac{\Delta R}{R}$) | Requiere galga ficticia dummy |
| **Medio Puente Push-Pull (1/2)** | 2 ($R_1=R+\Delta R, R_2=R-\Delta R$) | $$V_o = \frac{V_s}{2} \frac{\Delta R}{R}$$ | **Exactamente lineal** | Excelente ($\Delta T$ idéntica) |
| **Puente Completo (4/4)** | 4 (flexión o tracción/comp.) | $$V_o = V_s \frac{\Delta R}{R}$$ | **Exactamente lineal** ($4\times$ sensibilidad) | Total intrínseca |

---

## Tema 3: Amplificación y Acondicionamiento de Señal (INA)

### 3.1 Amplificador de Instrumentación Clásico (3 Operacionales)
$$\begin{equation}
V_o = \left( 1 + \frac{2 R_1}{R_g} \right) \frac{R_3}{R_2} (V_2 - V_1)
\end{equation}$$
- **Ganancia Diferencial ($G_d$)** fijada por una única resistencia $R_g$:
  $$\begin{equation}
  G_d = 1 + \frac{2 R_1}{R_g} \quad (\text{cuando } R_3 = R_2)
  \end{equation}$$
- Impedancia de entrada diferencial y en modo común: extremadamente elevada ($> 10^9 \,\Omega$).

### 3.2 Relación de Rechazo en Modo Común (CMRR)
$$\begin{equation}
\text{CMRR} = \left| \frac{A_d}{A_{cm}} \right|, \quad \text{CMRR}_{\text{dB}} = 20 \log_{10} \left| \frac{A_d}{A_{cm}} \right|
\end{equation}$$
- **Efecto de la Tolerancia de las Resistencias ($\delta = \Delta R / R$):**
  $$\begin{equation}
  \text{CMRR}_{\text{peor caso}} \approx \frac{1 + G_1}{4 \delta}
  \end{equation}$$
  *(Con resistencias al 1% ($\delta=0.01$), el CMRR de la etapa diferencial cae a $\approx 54\text{ dB}$ si $G_1=1$)*.

---

## Tema 4: Ruido e Interferencias en Instrumentación

### 4.1 Fuentes de Ruido Físico Intrínseco
- **Ruido Térmico Johnson-Nyquist (en cualquier resistencia $R$):**
  $$\begin{equation}
  v_n = \sqrt{4 k_B T R \Delta f} \quad (\text{V}_{\text{rms}}), \quad e_n = \sqrt{4 k_B T R} \quad (\text{V}/\sqrt{\text{Hz}})
  \end{equation}$$
  - Constante de Boltzmann: $k_B \approx 1.38 \times 10^{-23} \text{ J/K}$.
  - A $T = 300\text{ K}$ ($27^\circ\text{C}$): $e_n \approx 4 \sqrt{R\,(\text{k}\Omega)} \text{ nV}/\sqrt{\text{Hz}}$.
- **Ruido de Disparo (Shot Noise en uniones PN con corriente continua $I_{DC}$):**
  $$\begin{equation}
  i_{sh} = \sqrt{2 q I_{DC} \Delta f} \quad (\text{A}_{\text{rms}}), \quad q \approx 1.602 \times 10^{-19} \text{ C}
  \end{equation}$$
- **Suma Cuadrática de Fuentes de Ruido Incorreladas:**
  $$\begin{equation}
  v_{n,\text{total}} = \sqrt{v_{n1}^2 + v_{n2}^2 + \dots + v_{nk}^2}
  \end{equation}$$

### 4.2 Factor y Figura de Ruido
$$\begin{equation}
F = \frac{\text{SNR}_{\text{in}}}{\text{SNR}_{\text{out}}}, \quad \text{NF} = 10 \log_{10} F \quad (\text{dB})
\end{equation}$$

---

## Tema 5 y 6: Filtros Analógicos Activos y Respuesta Temporal

### 5.1 Función de Transferencia y Atenuación
- **Filtro Butterworth (Respuesta Máximamente Plana en banda de paso):**
  $$\begin{equation}
  |H(j\omega)| = \frac{1}{\sqrt{1 + \left( \frac{\omega}{\omega_c} \right)^{2n}}}
  \end{equation}$$
  - Pendiente en banda atenuada (Roll-off): $-20n \text{ dB/década}$ o $-6n \text{ dB/octava}$.
- **Filtro Chebyshev:** Mayor pendiente de transición a costa de rizado (ripple) $\varepsilon$ en banda pasante.
- **Filtro Bessel:** Retardo de grupo $\tau_g(\omega) = -\frac{d\phi}{d\omega} \approx \text{cte}$, respuesta transitoria sin sobreoscilación.

### 5.2 Celda Sallen-Key Pasa-Bajos de 2º Orden
$$\begin{equation}
f_0 = \frac{1}{2\pi \sqrt{R_1 R_2 C_1 C_2}}, \quad Q = \frac{\sqrt{R_1 R_2 C_1 C_2}}{C_2(R_1 + R_2)}
\end{equation}$$

---

## Tema 7: Convertidores Digital-Analógico (DAC)

### 7.1 Relación de Entrada/Salida
$$\begin{equation}
V_o = V_{\text{ref}} \sum_{i=1}^{N} b_i 2^{-i} = \frac{V_{\text{ref}}}{2^N} \times D
\end{equation}$$
- **Peso del Bit Menos Significativo (LSB):**
  $$\begin{equation}
  1 \text{ LSB} = \frac{V_{\text{ref}}}{2^N}
  \end{equation}$$
- **Tensión de Fondo de Escala Real (Full Scale Range):**
  $$\begin{equation}
  V_{FS} = V_{\text{ref}} \left( 1 - 2^{-N} \right) = V_{\text{ref}} - 1 \text{ LSB}
  \end{equation}$$

### 7.2 Métricas de Linealidad
- **DNL (No Linealidad Diferencial):** Condición de monotonicidad estricta: $|\text{DNL}| < 1 \text{ LSB}$.
- **INL (No Linealidad Integral):** Desviación máxima respecto a la recta ideal o recta de ajuste.

---

## Tema 8: Convertidores Analógico-Digital (ADC)

### 8.1 Criterio de Nyquist-Shannon y Aliasing
$$\begin{equation}
f_s \ge 2 f_{\max}
\end{equation}$$
- El filtro antialiasing analógico previo debe garantizar una atenuación de al menos $6.02N\text{ dB}$ en $f = f_s - f_{\max}$.

### 8.2 Ruido de Cuantificación y Relación Señal/Ruido Teórica (SNR)
- **Paso de Cuantificación (Quantum $q$):**
  $$\begin{equation}
  q = \frac{V_{\text{FSR}}}{2^N}
  \end{equation}$$
- **Varianza del Error de Cuantificación (suponiendo distribución uniforme en $[-q/2, +q/2]$):**
  $$\begin{equation}
  \sigma_q^2 = \frac{q^2}{12} \quad \implies \quad v_{q,\text{rms}} = \frac{q}{\sqrt{12}}
  \end{equation}$$
- **Relación Señal/Ruido Máxima (Señal senoidal a fondo de escala):**
  $$\begin{equation}
  \text{SNR}_{\max} = 6.02 N + 1.76 \quad (\text{dB})
  \end{equation}$$
- **Número Efectivo de Bits (ENOB):**
  $$\begin{equation}
  \text{ENOB} = \frac{\text{SINAD}_{\text{dB}} - 1.76}{6.02}
  \end{equation}$$

---

## Tema 9: Muestreo y Retención (Sample & Hold)

### 9.1 Aperture Jitter (Incertidumbre de Tiempo de Muestreo)
$$\begin{equation}
\Delta V = \left. \frac{dv(t)}{dt} \right|_{\max} \Delta t_a = 2\pi f_{\max} V_{\text{peak}} \Delta t_a
\end{equation}$$
- **Condición para que el error de apertura no supere $1/2\text{ LSB}$:**
  $$\begin{equation}
  \Delta t_a < \frac{1}{2\pi f_{\max} 2^N}
  \end{equation}$$

### 9.2 Caída de Retención (Droop Rate)
$$\begin{equation}
\frac{dV_H}{dt} = \frac{I_{\text{fuga}}}{C_H}
\end{equation}$$

---

## Tema 10: Calibración, Linealización e Incertidumbre (GUM)

### 10.1 Ley de Propagación de Incertidumbres Combinadas (Variables Incorreladas)
$$\begin{equation}
u_c^2(y) = \sum_{i=1}^{n} c_i^2 u^2(x_i) = \sum_{i=1}^{n} \left( \frac{\partial f}{\partial x_i} \right)^2 u^2(x_i)
\end{equation}$$
- Coeficientes de sensibilidad: $c_i = \frac{\partial f}{\partial x_i}$.

### 10.2 Evaluación de Incertidumbres Estándar
- **Tipo A (Estadística de $n$ mediciones repetidas):**
  $$\begin{equation}
  u(x) = \frac{s(x)}{\sqrt{n}} = \sqrt{\frac{\sum_{j=1}^n (x_j - \bar{x})^2}{n(n - 1)}}
  \end{equation}$$
- **Tipo B (Distribución Rectangular / Uniforme de semi-anchura $a$):**
  $$\begin{equation}
  u(x) = \frac{a}{\sqrt{3}}
  \end{equation}$$
- **Tipo B (Distribución Triangular):**
  $$\begin{equation}
  u(x) = \frac{a}{\sqrt{6}}
  \end{equation}$$
- **Incertidumbre Expandida ($U$):**
  $$\begin{equation}
  U = k \cdot u_c(y) \quad (k=2 \text{ para } 95.45\% \text{ de nivel de confianza})
  \end{equation}$$

---
> 💡 **Consejo para NotebookLM:** Sube este documento como fuente prioritaria bajo el nombre `_Formulario_Oficial_Examen.md`. Cuando le pidas al modelo resolver problemas numéricos del examen, dile: *"Usa las fórmulas y constantes del Formulario Oficial para deducir y comprobar los resultados numéricos"*.
"""
    target.write_text(content.strip() + "\n", encoding="utf-8")
    return target

def generate_course_flashcards_tsv(output_dir: Path, input_dir: Path) -> Path:
    """
    Genera un archivo TSV (_Flashcards_Examen.tsv) y un paquete Anki nativo (_Flashcards_Examen.apkg)
    con las 500 afirmaciones de autoevaluación de todos los temas del curso.
    """
    target_tsv = output_dir / "_Flashcards_Examen.tsv"
    target_apkg = output_dir / "_Flashcards_Examen.apkg"
    rows = []
    cards_for_apkg = []

    html_files = sorted(list(input_dir.glob("**/*.html")) + list(input_dir.glob("**/*.htm")))
    
    for f in html_files:
        if "entrenament" in f.name.lower():
            m_tema = re.search(r"Tema\s*(\d+)", str(f), re.I) or re.search(r"Unitat\s*(\d+)", str(f), re.I) or re.search(r"U(\d+)", str(f), re.I)
            t_num = m_tema.group(1) if m_tema else "X"
            tema_label = f"Tema {t_num}"

            try:
                html, _ = read_html_file_safely(f)
                questions = extract_quiz_questions(html)
                for q in questions:
                    n = q["n"]
                    statement = q["q"].replace("\t", " ").replace("\n", "<br>")
                    ans = q["a"]
                    just = q["j"].replace("\t", " ").replace("\n", "<br>")
                    ref = q["ref"].replace("\t", " ")

                    ans_str = "VERTADER (V) ✅" if ans in ["V", "VERTADER", "VERDADERO", "TRUE"] else "FALS (F) ❌"
                    ans_color = "#16a34a" if "VERTADER" in ans_str else "#dc2626"

                    front = f"<b>[{tema_label} · Qüestió #{n:02d}]</b><br><br>{statement}"
                    back = f"<b>Resposta:</b> <span style='color:{ans_color};font-weight:bold;'>{ans_str}</span><br><br><b>Justificació Tècnica:</b><br>{just}"
                    if ref:
                        back += f"<br><br><small style='color:#64748b;'><i>Referència: {ref}</i></small>"
                    
                    tags = f"Sistemes_de_Mesura Tema_{t_num} Autoavaluacio Examen"
                    rows.append(f"{front}\t{back}\t{tags}")

                    cards_for_apkg.append({
                        "question": f"[{tema_label} · Qüestió #{n:02d}]<br><br>{statement}",
                        "answer": ans_str,
                        "justification": f"{just}" + (f"<br><br><small style='color:#86868b;'><i>Referència: {ref}</i></small>" if ref else ""),
                        "tags": [f"Tema_{t_num}", "Autoavaluacio", "Sistemes_de_Mesura"]
                    })
            except Exception:
                pass

    if not rows:
        return None

    tsv_content = "#separator:tab\n#html:true\n#tags column:3\n" + "\n".join(rows) + "\n"
    target_tsv.write_text(tsv_content, encoding="utf-8")

    # Generar paquete Anki .apkg nativo
    try:
        create_anki_apkg(target_apkg, "Sistemes de Mesura (EEBE · UPC)", cards_for_apkg)
    except Exception:
        pass

    return target_tsv

def generate_grand_course_index(output_dir: Path, course_stats: dict) -> Path:
    """Genera el documento índice global del curso con métricas de los 10 temas, enlaces al glosario/flashcards y guía para NotebookLM."""
    target = output_dir / "_Gran_Indice_Sistemes_de_Mesura.md"

    topics_detail = course_stats.get("topics_detail", [])
    total_files = course_stats.get("total_files", 0)
    total_math = course_stats.get("math", 0)
    total_words = course_stats.get("total_words", 0)
    total_quizzes = course_stats.get("quiz_questions", 0)
    global_density = (total_math / total_words * 1000) if total_words > 0 else 0

    lines = [
        "# 🎓 Guía Maestra y Gran Índice · Sistemes de Mesura (UPC)",
        "",
        "> 🏛️ **Grado:** Telecomunicaciones (ETSETB — Universitat Politècnica de Catalunya)",
        f"> 📚 **Estructura del Curso:** {len(topics_detail)} Unidades Temáticas",
        f"> 📄 **Documentos Procesados:** {total_files} capítulos pedagógicos",
        f"> 📐 **Rigor Matemático:** {total_math:,} expresiones LaTeX puras",
        f"> 🧠 **Banco de Evaluación:** {total_quizzes} afirmaciones/problemas con soluciones",
        f"> 📊 **Volumen Total:** {total_words:,} palabras ({global_density:.1f} fórmulas/1.000 palabras)",
        "> 📖 **Glosario Central:** [_Glosario_Conceptos_Clave.md](_Glosario_Conceptos_Clave.md) (Diccionario técnico A-Z)",
        "> 📐 **Formulario Oficial:** [_Formulario_Oficial_Examen.md](_Formulario_Oficial_Examen.md) (Ecuaciones y leyes para examen)",
        "> 🗂️ **Deck de Flashcards:** [_Flashcards_Examen.apkg](_Flashcards_Examen.apkg) / [TSV](_Flashcards_Examen.tsv) (500 tarjetas Anki con MathJax)",
        "",
        "---",
        "",
        "## 📑 Plan de Estudios y Cuadernos Maestros para NotebookLM",
        "",
        "Cada tema dispone de un **Cuaderno Maestro Unificado** (`_Cuaderno_Maestro_*.md`), especialmente diseñado para subirse a **Google NotebookLM** sin agotar el límite de fuentes y proporcionando al modelo el contexto holístico del tema, junto con su **Reporte Analítico** (`_Reporte_Analitico_*.md`).",
        "",
        "| Unidad | Capítulos | Fórmulas LaTeX | Densidad | Preguntas Examen | Cuaderno Maestro (NotebookLM) | Reporte Analítico |",
        "| :---: | :---: | :---: | :---: | :---: | :---: | :---: |"
    ]

    for item in topics_detail:
        t_name = item["name"]
        n_files = item["files"]
        m_count = item["math"]
        dens = item["density"]
        cat = item["category"]
        m_doc = item.get("master_doc", "")
        dash = item.get("dashboard", "")

        link_master = f"[{m_doc}]({t_name}/{m_doc})" if m_doc else "*(No generado)*"
        link_dash = f"[📊 Reporte]({t_name}/{dash})" if dash else "*(No generado)*"

        lines.append(f"| **{t_name}** | {n_files} | {m_count} | {dens:.1f} ({cat}) | 50 Qüestions | {link_master} | {link_dash} |")

    lines.extend([
        "",
        "---",
        "",
        "## 🗂️ Recursos Centrales de Estudio",
        "",
        "### 📚 1. Glosario Técnico de Conceptos Clave",
        "- Acceso directo: [`_Glosario_Conceptos_Clave.md`](_Glosario_Conceptos_Clave.md)",
        "- Contiene todas las definiciones formales del curso ordenadas alfabéticamente de la A a la Z con enlaces a los documentos fuente.",
        "",
        "### 🗂️ 2. Flashcards de Examen para Anki / Quizlet",
        "- Archivo exportado: [`_Flashcards_Examen.tsv`](_Flashcards_Examen.tsv)",
        "- **Cómo importar en Anki:** Abre Anki -> Menú *Archivo* -> *Importar...* -> Selecciona `_Flashcards_Examen.tsv`. Se crearán automáticamente 500 tarjetas con formato pedagógico, respuesta oculta y justificación técnica completa.",
        "",
        "---",
        "",
        "## 🤖 Guía de Estudio con Inteligencia Artificial (NotebookLM & LLMs)",
        "",
        "### 1. Estrategia de Carga en NotebookLM",
        "- **Recomendación Óptima:** Crea un cuaderno en NotebookLM por cada tema o bloque de examen y sube directamente el archivo `_Cuaderno_Maestro_Tema_X.md` correspondiente.",
        "- **Ventaja:** Al subir el Cuaderno Maestro, NotebookLM absorbe el índice, todos los capítulos teóricos, los ejercicios resueltos paso a paso y el formulario resumen de ecuaciones en una única fuente de alta densidad.",
        "",
        "### 2. Prompts de Estudio Recomendados",
        "",
        "#### 🎯 Simulación de Examen y Autoevaluación",
        "> *«Actúa como el profesor de Sistemes de Mesura de la UPC. Utilizando el banco de afirmaciones del Cuaderno Maestro, hazme 5 preguntas aleatorias de tipo Verdadero/Falso. Espera mi respuesta antes de darme la solución y la justificación técnica.»*",
        "",
        "#### 📐 Deducción Matemática y Resolución de Dudas",
        "> *«Explícame paso a paso cómo se deduce la fórmula de combinación de incertidumbres en este tema y qué condiciones deben cumplirse para aplicar la aproximación lineal.»*",
        "",
        "#### 🔍 Tarjetas de Repaso Rápido (Flashcards)",
        "> *«Genera una tabla comparativa con las 5 definiciones y conceptos más críticos de esta unidad, destacando las trampas conceptuales habituales de examen.»*",
        ""
    ])

    content = "\n".join(lines)
    target.write_text(content, encoding="utf-8")
    return target

def process_all_course_temas(
    root_folder: str,
    output_folder: str,
    progress_callback=None,
    rewrite_links: bool = True,
    include_meta: bool = True,
    include_yaml: bool = False,
    generate_toc: bool = True,
    include_formula_sheet: bool = True,
    create_master_doc: bool = True,
    create_dashboard: bool = True,
    extract_b64: bool = True,
    cancel_event: threading.Event = None
) -> tuple[int, dict, list]:
    """
    Convierte secuencialmente todos los temas del curso (Tema 1 .. Tema 10)
    generando los Cuadernos Maestros, Reportes Analíticos y el Gran Índice General.
    """
    in_root = Path(root_folder)
    out_root = Path(output_folder)
    out_root.mkdir(parents=True, exist_ok=True)

    tema_dirs = []
    for entry in sorted(in_root.iterdir()):
        if entry.is_dir() and any(k in entry.name.lower() for k in ["tema", "unitat", "unidad", "cap"]):
            if list(entry.glob("*.html")) or list(entry.glob("*.htm")):
                tema_dirs.append(entry)

    def _tema_num(p: Path):
        digits = "".join(ch for ch in p.name if ch.isdigit())
        return int(digits) if digits else 999
    tema_dirs.sort(key=_tema_num)

    if not tema_dirs:
        return process_batch(
            root_folder, output_folder,
            progress_callback=progress_callback,
            rewrite_links=rewrite_links,
            include_meta=include_meta,
            include_yaml=include_yaml,
            generate_toc=generate_toc,
            include_formula_sheet=include_formula_sheet,
            create_master_doc=create_master_doc,
            create_dashboard=create_dashboard,
            extract_b64=extract_b64,
            cancel_event=cancel_event
        )

    course_stats = {
        "topics_count": len(tema_dirs),
        "total_files": 0,
        "math": 0,
        "tables": 0,
        "diagrams": 0,
        "b64_images": 0,
        "quiz_questions": 0,
        "total_words": 0,
        "topics_detail": []
    }
    all_generated_files = []

    total_temas = len(tema_dirs)
    for t_idx, t_dir in enumerate(tema_dirs):
        if cancel_event and cancel_event.is_set():
            break

        t_out = out_root / t_dir.name
        t_out.mkdir(parents=True, exist_ok=True)

        def make_topic_callback(curr_t_idx, curr_t_name):
            def cb(curr, total, fname, fstats):
                if progress_callback:
                    progress_callback(
                        f"Tema {curr_t_idx+1}/{total_temas}: [{curr}/{total}]",
                        fname,
                        curr_t_idx,
                        total_temas
                    )
            return cb

        conv_count, t_stats, gen_files = process_batch(
            str(t_dir), str(t_out),
            progress_callback=make_topic_callback(t_idx, t_dir.name) if progress_callback else None,
            rewrite_links=rewrite_links,
            include_meta=include_meta,
            include_yaml=include_yaml,
            generate_toc=generate_toc,
            include_formula_sheet=include_formula_sheet,
            create_master_doc=create_master_doc,
            create_dashboard=create_dashboard,
            extract_b64=extract_b64,
            cancel_event=cancel_event
        )

        all_generated_files.extend(gen_files)
        course_stats["total_files"] += conv_count
        course_stats["math"] += t_stats.get("math", 0)
        course_stats["tables"] += t_stats.get("tables", 0)
        course_stats["diagrams"] += t_stats.get("diagrams", 0)
        course_stats["b64_images"] += t_stats.get("b64_images", 0)
        course_stats["quiz_questions"] += t_stats.get("quiz_questions", 0)

        t_words = 0
        for gf in gen_files:
            if gf.suffix.lower() == ".md" and not gf.name.startswith("_"):
                try:
                    t_words += len(gf.read_text(encoding="utf-8").split())
                except Exception:
                    pass

        course_stats["total_words"] += t_words
        density = (t_stats.get("math", 0) / t_words * 1000) if t_words > 0 else 0
        cat_badge = "Muy Analítico 🔴" if density > 15 else ("Analítico 🟡" if density > 5 else "Conceptual 🟢")

        course_stats["topics_detail"].append({
            "name": t_dir.name,
            "files": conv_count,
            "math": t_stats.get("math", 0),
            "tables": t_stats.get("tables", 0),
            "words": t_words,
            "density": density,
            "category": cat_badge,
            "master_doc": t_stats.get("master_document", ""),
            "dashboard": t_stats.get("dashboard", "")
        })

    grand_index = generate_grand_course_index(out_root, course_stats)
    if grand_index:
        all_generated_files.insert(0, grand_index)
        course_stats["grand_index"] = str(grand_index.name)

    glossary_file = generate_course_glossary(out_root)
    if glossary_file:
        all_generated_files.append(glossary_file)
        course_stats["glossary"] = str(glossary_file.name)

    cheatsheet_file = generate_formula_cheatsheet(out_root)
    if cheatsheet_file:
        all_generated_files.append(cheatsheet_file)
        course_stats["formula_cheatsheet"] = str(cheatsheet_file.name)

    flashcards_file = generate_course_flashcards_tsv(out_root, in_root)
    if flashcards_file:
        all_generated_files.append(flashcards_file)
        course_stats["flashcards"] = str(flashcards_file.name)

    return course_stats["total_files"], course_stats, all_generated_files


# ----------------------------------------------------------------------
# 8. MÓDULOS DE AMPLIACIÓN: BUSCADOR SPOTLIGHT, SIMULADOR EXAMEN Y DRAG & DROP
# ----------------------------------------------------------------------

def load_all_course_quizzes(in_root: Path) -> list[dict]:
    """Carga todas las preguntas oficiales de los archivos entrenament.html del curso."""
    questions = []
    html_files = sorted(list(in_root.glob("**/*.html")) + list(in_root.glob("**/*.htm")))
    for f in html_files:
        if "entrenament" in f.name.lower():
            m_tema = re.search(r"Tema\s*(\d+)", str(f), re.I) or re.search(r"Unitat\s*(\d+)", str(f), re.I) or re.search(r"U(\d+)", str(f), re.I)
            t_num = int(m_tema.group(1)) if m_tema else 0
            try:
                html, _ = read_html_file_safely(f)
                qs = extract_quiz_questions(html)
                for q in qs:
                    q["tema_num"] = t_num
                    q["tema_label"] = f"Tema {t_num}" if t_num > 0 else "General"
                    q["source_file"] = f.name
                    questions.append(q)
            except Exception:
                pass
    return questions

def load_quizzes_from_tsv(tsv_path: Path) -> list[dict]:
    """Carga preguntas oficiales desde el archivo TSV de flashcards si los HTML no estan accesibles."""
    questions = []
    if not tsv_path.exists():
        return questions
    try:
        lines = tsv_path.read_text(encoding="utf-8", errors="ignore").splitlines()
        for line in lines:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 2:
                continue
            front, back = parts[0], parts[1]
            m_t = re.search(r"\[Tema\s*(\d+)", front, re.I)
            t_num = int(m_t.group(1)) if m_t else 1
            q_clean = re.sub(r"<b>\[.*?\]</b><br><br>", "", front).strip()
            q_clean = q_clean.replace("<br>", " ")
            resp = "V" if "VERTADER" in back.upper() else "F"
            m_just = re.search(r"<b>Justificaci.*?T.*?cnica:</b><br>(.*?)(?:<br><br><small|$)", back, re.DOTALL | re.I)
            just = m_just.group(1).strip() if m_just else ""
            just = re.sub(r"<.*?>", "", just)
            m_ref = re.search(r"Refer.*?ncia:\s*(.*?)</", back, re.I)
            ref = m_ref.group(1).strip() if m_ref else f"Tema {t_num}"
            questions.append({
                "n": len(questions) + 1,
                "q": q_clean,
                "a": resp,
                "j": just,
                "ref": ref,
                "tema_num": t_num,
                "tema_label": f"Tema {t_num}",
                "source_file": "_Flashcards_Examen.tsv"
            })
    except Exception:
        pass
    return questions

def search_course_content(base_dir: Path, query: str, max_results: int = 35) -> list[dict]:
    """Buscador ultrarrápido tipo Spotlight en todos los archivos Markdown generados."""
    if not query or len(query.strip()) < 2:
        return []

    q = query.strip().lower()
    q_words = q.split()
    results = []

    md_files = sorted(list(base_dir.glob("**/*.md")))
    for f in md_files:
        topic_match = re.search(r"Tema[_\s]*(\d+)", str(f), re.I)
        topic_label = f"Tema {topic_match.group(1)}" if topic_match else "General"
        
        try:
            content = f.read_text(encoding="utf-8", errors="ignore")
            lines = content.splitlines()
            
            file_title = f.stem.replace("_", " ")
            for line in lines[:10]:
                if line.startswith("# "):
                    file_title = line[2:].strip()
                    break

            for i, line in enumerate(lines):
                line_lower = line.lower()
                if all(w in line_lower for w in q_words):
                    snippet = line.strip()
                    snippet = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", snippet)
                    snippet = re.sub(r"[*_`#]", "", snippet)
                    if len(snippet) > 120:
                        idx = line_lower.find(q_words[0])
                        start = max(0, idx - 40)
                        end = min(len(snippet), idx + 80)
                        snippet = ("..." if start > 0 else "") + snippet[start:end] + ("..." if end < len(snippet) else "")
                    
                    results.append({
                        "file": f.name,
                        "path": f,
                        "topic": topic_label,
                        "title": file_title,
                        "line": i + 1,
                        "snippet": snippet
                    })
                    if len(results) >= max_results:
                        return results
        except Exception:
            continue

    return results

def setup_windows_drag_and_drop(widget, on_drop_callback):
    """Configura Drag & Drop nativo de Windows (WM_DROPFILES) en el widget Tkinter vía ctypes."""
    if sys.platform != "win32":
        return None
    try:
        import ctypes
        from ctypes import wintypes
        shell32 = ctypes.windll.shell32
        user32 = ctypes.windll.user32
        GWL_WNDPROC = -4
        WM_DROPFILES = 0x0233

        hwnd = widget.winfo_id()
        if not hwnd:
            return None

        if ctypes.sizeof(ctypes.c_void_p) == 8:
            SetWindowLongPtr = user32.SetWindowLongPtrW
            GetWindowLongPtr = user32.GetWindowLongPtrW
            SetWindowLongPtr.restype = ctypes.c_void_p
            SetWindowLongPtr.argtypes = [wintypes.HWND, ctypes.c_int, ctypes.c_void_p]
            GetWindowLongPtr.restype = ctypes.c_void_p
            GetWindowLongPtr.argtypes = [wintypes.HWND, ctypes.c_int]
            user32.CallWindowProcW.argtypes = [ctypes.c_void_p, wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM]
            user32.CallWindowProcW.restype = ctypes.c_longlong
            wndproc_t = ctypes.WINFUNCTYPE(ctypes.c_longlong, wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM)
        else:
            SetWindowLongPtr = user32.SetWindowLongW
            GetWindowLongPtr = user32.GetWindowLongW
            wndproc_t = ctypes.WINFUNCTYPE(ctypes.c_long, wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM)

        shell32.DragAcceptFiles(hwnd, True)
        old_proc = GetWindowLongPtr(hwnd, GWL_WNDPROC)

        def py_wnd_proc(h, msg, wp, lp):
            if msg == WM_DROPFILES:
                hdrop = wp
                num_files = shell32.DragQueryFileW(hdrop, 0xFFFFFFFF, None, 0)
                files = []
                for i in range(num_files):
                    length = shell32.DragQueryFileW(hdrop, i, None, 0)
                    buf = ctypes.create_unicode_buffer(length + 1)
                    shell32.DragQueryFileW(hdrop, i, buf, length + 1)
                    files.append(buf.value)
                shell32.DragFinish(hdrop)
                if on_drop_callback:
                    widget.after(0, lambda: on_drop_callback(files))
                return 0
            return user32.CallWindowProcW(old_proc, h, msg, wp, lp)

        c_proc = wndproc_t(py_wnd_proc)
        widget._dnd_c_proc = c_proc
        SetWindowLongPtr(hwnd, GWL_WNDPROC, c_proc)
        return c_proc
    except Exception:
        return None

def score_exam(answers: list[dict]) -> tuple:
    """Calcula la calificación del examen bajo baremo UPC (+1 acierto, -0.33 fallo, 0 blanco)."""
    total = len(answers)
    if total == 0:
        return 0, 0, 0, 0, 0.0

    correct_count = 0
    wrong_count = 0
    blank_count = 0

    for a in answers:
        u = a.get('user_choice', '').upper()
        c = a.get('correct', '').upper()
        if u == 'BLANK' or not u:
            blank_count += 1
        elif u == c or (u in ["V", "VERTADER", "VERDADERO"] and c in ["V", "VERTADER", "VERDADERO"]) or (u in ["F", "FALS", "FALSO"] and c in ["F", "FALS", "FALSO"]):
            correct_count += 1
        else:
            wrong_count += 1

    net_points = max(0.0, (correct_count * 1.0) - (wrong_count * 0.33))
    grade = (net_points / total) * 10.0
    return total, correct_count, wrong_count, blank_count, round(grade, 2)


# ----------------------------------------------------------------------
# 9. INTERFAZ GRÁFICA MULTIHILO CON VISOR MARKDOWN Y PORTAPAPELES
# ----------------------------------------------------------------------

def run_gui():
    # 1. Habilitar High-DPI en Windows para renderizado nítido
    try:
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass

    root = tk.Tk()
    root.title("Sistemes de Mesura · Conversor Pro (Apple Studio Edition)")
    root.geometry("1020x840")
    root.minsize(920, 720)

    # ------------------------------------------------------------------
    # PALETA APPLE.COM SPACE BLACK / TITANIUM PRO
    # ------------------------------------------------------------------
    COLOR_CANVAS = "#000000"          # Apple True Black
    COLOR_HEADER = "#161617"          # Apple Navigation Bar
    COLOR_CARD = "#1c1c1e"            # Apple System Card Gray 6
    COLOR_CARD_BORDER = "#2c2c2e"     # Hairline border divider
    COLOR_INSET = "#121214"           # Dark Inset container
    COLOR_INPUT_BG = "#0a0a0c"        # Inset Code / Entry field
    COLOR_TEXT_PRIMARY = "#f5f5f7"    # Apple White / Silver
    COLOR_TEXT_MUTED = "#86868b"      # Apple signature neutral gray
    COLOR_ACCENT_BLUE = "#0071e3"     # Apple Signature Blue
    COLOR_ACCENT_HOVER = "#0077ed"    # Apple Blue hover
    COLOR_ACCENT_GREEN = "#30d158"    # Apple Green
    COLOR_ACCENT_GREEN_HOVER = "#34c759"
    COLOR_ACCENT_RED = "#ff453a"      # Apple Red
    COLOR_ACCENT_RED_HOVER = "#ff6961"
    COLOR_ACCENT_AMBER = "#ff9f0a"    # Apple Amber / Gold
    COLOR_ACCENT_PURPLE = "#bf5af2"   # Apple Purple
    COLOR_ACCENT_CYAN = "#64d2ff"     # Apple Cyan

    root.configure(bg=COLOR_CANVAS)

    # Detección de fuentes tipográficas Apple / San Francisco
    FONT_FAMILY = "Segoe UI"
    try:
        from tkinter import font as tkfont
        for f in ["SF Pro Display", "SF Pro Text", "Segoe UI Variable Display", "Segoe UI", "Helvetica Neue", "Arial"]:
            if f in tkfont.families():
                FONT_FAMILY = f
                break
    except Exception:
        pass

    FONT_TITLE = (FONT_FAMILY, 15, "bold")
    FONT_SUBTITLE = (FONT_FAMILY, 9)
    FONT_HEAD = (FONT_FAMILY, 9, "bold")
    FONT_BODY = (FONT_FAMILY, 9)
    FONT_CODE = ("Consolas", 9)
    FONT_SMALL = (FONT_FAMILY, 8)

    style = ttk.Style()
    style.theme_use("clam")

    # Configuración de estilos Apple TTK
    style.configure("Hidden.TNotebook", background=COLOR_CANVAS, borderwidth=0, tabmargins=[0, 0, 0, 0])
    style.layout("Hidden.TNotebook.Tab", [])
    style.configure("Modern.Horizontal.TProgressbar", background=COLOR_ACCENT_BLUE, troughcolor=COLOR_INPUT_BG, borderwidth=0, thickness=6)
    style.configure("Modern.TCombobox", fieldbackground=COLOR_INPUT_BG, background=COLOR_CARD, foreground=COLOR_TEXT_PRIMARY, arrowcolor=COLOR_TEXT_MUTED, borderwidth=1)
    style.map("Modern.TCombobox", fieldbackground=[("readonly", COLOR_INPUT_BG)])

    def create_btn(parent, text, command, bg="#2c2c2e", fg=COLOR_TEXT_PRIMARY, hover_bg="#3a3a3c", font=FONT_HEAD, padx=16, pady=7, **kwargs):
        b = tk.Button(parent, text=text, command=command, bg=bg, fg=fg, activebackground=hover_bg, activeforeground=fg, font=font, cursor="hand2", relief="flat", bd=0, padx=padx, pady=pady, **kwargs)
        b.bind("<Enter>", lambda e: b.config(bg=hover_bg) if b["state"] != "disabled" else None)
        b.bind("<Leave>", lambda e: b.config(bg=bg) if b["state"] != "disabled" else None)
        return b

    def make_card(parent, title=""):
        c = tk.Frame(parent, bg=COLOR_CARD, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER)
        if title:
            h = tk.Frame(c, bg=COLOR_CARD)
            h.pack(fill="x", padx=16, pady=(12, 4))
            tk.Label(h, text=title, font=FONT_HEAD, fg=COLOR_TEXT_PRIMARY, bg=COLOR_CARD).pack(side="left")
        return c

    # Variables de control
    mode_var = tk.StringVar(value="batch")
    in_var = tk.StringVar()
    out_var = tk.StringVar()
    preset_var = tk.StringVar(value="NotebookLM (Recomendado)")

    rewrite_links_var = tk.BooleanVar(value=True)
    include_meta_var = tk.BooleanVar(value=True)
    include_yaml_var = tk.BooleanVar(value=False)
    generate_toc_var = tk.BooleanVar(value=True)
    extract_b64_var = tk.BooleanVar(value=True)
    formula_sheet_var = tk.BooleanVar(value=True)
    master_doc_var = tk.BooleanVar(value=True)
    dashboard_var = tk.BooleanVar(value=True)

    cancel_event = threading.Event()
    is_running = False

    # Cabecera superior Apple.com Studio Pro
    header_frame = tk.Frame(root, bg=COLOR_HEADER, padx=24, pady=12)
    header_frame.pack(fill="x")
    hairline_top = tk.Frame(root, bg=COLOR_CARD_BORDER, height=1)
    hairline_top.pack(fill="x")

    h_left = tk.Frame(header_frame, bg=COLOR_HEADER)
    h_left.pack(side="left")

    title_row = tk.Frame(h_left, bg=COLOR_HEADER)
    title_row.pack(anchor="w")

    tk.Label(title_row, text="", font=(FONT_FAMILY, 15), fg=COLOR_TEXT_PRIMARY, bg=COLOR_HEADER).pack(side="left", padx=(0, 7))
    tk.Label(title_row, text="Sistemes de Mesura", font=FONT_TITLE, fg=COLOR_TEXT_PRIMARY, bg=COLOR_HEADER).pack(side="left")
    tk.Label(title_row, text="Studio Ultra", font=FONT_SMALL, fg=COLOR_TEXT_MUTED, bg="#242426", padx=8, pady=2).pack(side="left", padx=(8, 0))

    tk.Label(
        h_left,
        text="Conversor HTML a Markdown Ultra-Fiel · Máxima fidelidad LaTeX y estructuración para NotebookLM y Obsidian",
        fg=COLOR_TEXT_MUTED, bg=COLOR_HEADER, font=FONT_SUBTITLE
    ).pack(anchor="w", pady=(3, 0))

    h_right = tk.Frame(header_frame, bg=COLOR_HEADER)
    h_right.pack(side="right")
    create_btn(h_right, "🔍 Spotlight (Ctrl+K)", lambda: open_spotlight_modal(), bg="#242426", hover_bg="#3a3a3c", font=FONT_SMALL, padx=12, pady=4).pack(side="left", padx=4)
    create_btn(h_right, "🎯 Examen UPC", lambda: open_exam_simulator_modal(), bg="#112530", hover_bg="#1b3b4d", font=FONT_SMALL, padx=12, pady=4).pack(side="left", padx=4)
    tk.Label(h_right, text="UPC · EEBE", fg=COLOR_TEXT_MUTED, bg="#242426", font=FONT_SMALL, padx=10, pady=4).pack(side="left", padx=4)
    tk.Label(h_right, text="v3.0 Ultra", fg=COLOR_ACCENT_GREEN, bg="#132a19", font=FONT_SMALL, padx=10, pady=4).pack(side="left", padx=4)

    # Apple Segmented Tab Navigation Bar
    seg_nav_outer = tk.Frame(root, bg=COLOR_CANVAS, pady=8)
    seg_nav_outer.pack(fill="x")

    seg_pill_box = tk.Frame(seg_nav_outer, bg=COLOR_CARD, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER, padx=4, pady=4)
    seg_pill_box.pack()

    tab_btns = []
    def select_apple_tab(idx):
        notebook.select(idx)
        for i, b in enumerate(tab_btns):
            if i == idx:
                b.config(bg=COLOR_ACCENT_BLUE, fg="#ffffff", activebackground=COLOR_ACCENT_HOVER)
            else:
                b.config(bg=COLOR_CARD, fg=COLOR_TEXT_MUTED, activebackground="#242426")

    for i, (tab_label, icon) in enumerate([
        ("Conversión", "⚡"),
        ("Visor Markdown & Prompts", "👁️"),
        ("Biblioteca del Curso", "🗂️")
    ]):
        btn_t = tk.Button(
            seg_pill_box, text=f"{icon}  {tab_label}",
            font=(FONT_FAMILY, 9, "bold"),
            bg=COLOR_ACCENT_BLUE if i == 0 else COLOR_CARD,
            fg="#ffffff" if i == 0 else COLOR_TEXT_MUTED,
            activebackground=COLOR_ACCENT_HOVER, activeforeground="#ffffff",
            cursor="hand2", relief="flat", bd=0, padx=22, pady=6,
            command=lambda idx=i: select_apple_tab(idx)
        )
        btn_t.pack(side="left", padx=2)
        tab_btns.append(btn_t)

    # Notebook con pestañas ocultas gobernadas por el Segmented Control
    notebook = ttk.Notebook(root, style="Hidden.TNotebook")
    notebook.pack(fill="both", expand=True, padx=20, pady=(0, 10))

    tab_convert = tk.Frame(notebook, bg=COLOR_CANVAS)
    tab_viewer = tk.Frame(notebook, bg=COLOR_CANVAS)
    tab_resources = tk.Frame(notebook, bg=COLOR_CANVAS)

    notebook.add(tab_convert, text="Conversión")
    notebook.add(tab_viewer, text="Visor")
    notebook.add(tab_resources, text="Recursos")

    def on_notebook_tab_changed(event):
        try:
            sel_id = notebook.index(notebook.select())
            for i, b in enumerate(tab_btns):
                if i == sel_id:
                    b.config(bg=COLOR_ACCENT_BLUE, fg="#ffffff")
                else:
                    b.config(bg=COLOR_CARD, fg=COLOR_TEXT_MUTED)
        except Exception:
            pass
    notebook.bind("<<NotebookTabChanged>>", on_notebook_tab_changed)

    # ==================================================================
    # PESTAÑA 1: CONVERSIÓN Y OPCIONES
    # ==================================================================
    p1 = tk.Frame(tab_convert, bg=COLOR_CANVAS, padx=4, pady=4)
    p1.pack(fill="both", expand=True)

    # ------------------------------------------------------------------
    # CARD 1: MODO Y PERFIL RÁPIDO (APPLE SEGMENTED CONTROLS)
    # ------------------------------------------------------------------
    card_mode = make_card(p1, "⚙️ Modo de Operación y Perfil")
    card_mode.pack(fill="x", pady=(0, 8))

    top_bar = tk.Frame(card_mode, bg=COLOR_CARD, padx=16, pady=10)
    top_bar.pack(fill="x")

    mode_sub = tk.Frame(top_bar, bg=COLOR_CARD)
    mode_sub.pack(side="left")

    tk.Label(mode_sub, text="Modo:", font=FONT_HEAD, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD).pack(side="left", padx=(0, 8))

    mode_pill_box = tk.Frame(mode_sub, bg=COLOR_INSET, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER, padx=3, pady=3)
    mode_pill_box.pack(side="left")

    mode_btns = {}

    def update_mode():
        m = mode_var.get()
        if m == "batch":
            lbl_in.config(text="Carpeta de origen (HTML):")
            lbl_out.config(text="Carpeta de destino (Markdown):")
            chk_master.config(state="normal")
            chk_dash.config(state="normal")
            try:
                btn_exec.config(text="⚡ Convertir Lote", bg=COLOR_ACCENT_BLUE)
            except Exception:
                pass
        elif m == "all_course":
            lbl_in.config(text="Carpeta raíz del curso (contiene Tema 1..10):")
            lbl_out.config(text="Carpeta de destino para el curso completo:")
            chk_master.config(state="normal")
            chk_dash.config(state="normal")
            try:
                btn_exec.config(text="🎓 Iniciar Conversión de los 10 Temas", bg=COLOR_ACCENT_GREEN)
            except Exception:
                pass
        else:
            lbl_in.config(text="Archivo HTML individual:")
            lbl_out.config(text="Archivo Markdown resultante (.md):")
            chk_master.config(state="disabled")
            chk_dash.config(state="disabled")
            try:
                btn_exec.config(text="⚡ Convertir Archivo Único", bg=COLOR_ACCENT_BLUE)
            except Exception:
                pass

    def select_apple_mode(val):
        mode_var.set(val)
        update_mode()
        for k, btn in mode_btns.items():
            if k == val:
                btn.config(bg=COLOR_ACCENT_BLUE, fg="#ffffff")
            else:
                btn.config(bg=COLOR_INSET, fg=COLOR_TEXT_MUTED)

    for text_mode, val_mode in [
        ("📁 Lote", "batch"),
        ("📄 Archivo Único", "single"),
        ("🎓 Curso Completo (10 Temas)", "all_course")
    ]:
        b = tk.Button(
            mode_pill_box, text=text_mode, font=(FONT_FAMILY, 9, "bold"),
            bg=COLOR_ACCENT_BLUE if val_mode == mode_var.get() else COLOR_INSET,
            fg="#ffffff" if val_mode == mode_var.get() else COLOR_TEXT_MUTED,
            activebackground=COLOR_ACCENT_HOVER, activeforeground="#ffffff",
            cursor="hand2", relief="flat", bd=0, padx=14, pady=5,
            command=lambda v=val_mode: select_apple_mode(v)
        )
        b.pack(side="left", padx=2)
        mode_btns[val_mode] = b

    preset_sub = tk.Frame(top_bar, bg=COLOR_CARD)
    preset_sub.pack(side="right")

    tk.Label(preset_sub, text="Perfil:", font=FONT_HEAD, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD).pack(side="left", padx=(0, 6))

    def on_preset_selected(event=None):
        val = preset_var.get()
        if "NotebookLM" in val:
            rewrite_links_var.set(True)
            generate_toc_var.set(True)
            include_meta_var.set(True)
            include_yaml_var.set(False)
            extract_b64_var.set(True)
            formula_sheet_var.set(True)
            master_doc_var.set(True)
            dashboard_var.set(True)
        elif "Obsidian" in val:
            rewrite_links_var.set(True)
            generate_toc_var.set(True)
            include_meta_var.set(True)
            include_yaml_var.set(True)
            extract_b64_var.set(True)
            formula_sheet_var.set(True)
            master_doc_var.set(False)
            dashboard_var.set(True)
        elif "GitHub" in val:
            rewrite_links_var.set(True)
            generate_toc_var.set(True)
            include_meta_var.set(True)
            include_yaml_var.set(False)
            extract_b64_var.set(True)
            formula_sheet_var.set(False)
            master_doc_var.set(False)
            dashboard_var.set(False)

    preset_combo = ttk.Combobox(
        preset_sub, textvariable=preset_var, state="readonly", width=22, style="Modern.TCombobox",
        values=["NotebookLM (Recomendado)", "Obsidian Vault", "GitHub / Estándar", "Personalizado"]
    )
    preset_combo.pack(side="left")
    preset_combo.bind("<<ComboboxSelected>>", on_preset_selected)

    def on_custom_toggle():
        preset_combo.set("Personalizado")

    # ------------------------------------------------------------------
    # CARD 2: RUTAS DE ORIGEN Y DESTINO
    # ------------------------------------------------------------------
    card_paths = make_card(p1, "📁 Rutas de Entrada y Salida")
    card_paths.pack(fill="x", pady=(0, 8))

    paths_inner = tk.Frame(card_paths, bg=COLOR_CARD, padx=16, pady=6)
    paths_inner.pack(fill="x")

    lbl_in = tk.Label(paths_inner, text="Carpeta de origen (HTML):", font=FONT_HEAD, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD)
    lbl_in.pack(anchor="w")

    f1 = tk.Frame(paths_inner, bg=COLOR_CARD)
    f1.pack(fill="x", pady=(2, 6))
    entry_in = tk.Entry(f1, textvariable=in_var, font=FONT_CODE, bg=COLOR_INPUT_BG, fg=COLOR_TEXT_PRIMARY, insertbackground=COLOR_ACCENT_BLUE, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER)
    entry_in.pack(side="left", fill="x", expand=True, ipady=4, padx=(0, 8))

    def select_in():
        m = mode_var.get()
        if m in ["batch", "all_course"]:
            d = filedialog.askdirectory(title="Selecciona la carpeta de archivos HTML")
            if d:
                in_var.set(d)
                if not out_var.get():
                    out_var.set(str(Path(d) / "Markdown_Output"))
        else:
            f = filedialog.askopenfilename(title="Selecciona un archivo HTML", filetypes=[("Archivos HTML", "*.html;*.htm"), ("Todos", "*.*")])
            if f:
                in_var.set(f)
                if not out_var.get():
                    out_var.set(str(Path(f).with_suffix(".md")))

    def paste_in():
        try:
            val = root.clipboard_get().strip().strip('"').strip("'")
            if val:
                in_var.set(val)
                p = Path(val)
                if not out_var.get():
                    out_var.set(str(p / "Markdown_Output") if mode_var.get() != "single" else str(p.with_suffix(".md")))
        except Exception:
            pass

    create_btn(f1, "Examinar...", select_in, bg="#2c2c2e", hover_bg="#3a3a3c").pack(side="right", padx=(4, 0))
    create_btn(f1, "📋 Pegar", paste_in, bg="#2c2c2e", hover_bg="#3a3a3c").pack(side="right", padx=(4, 0))

    lbl_out = tk.Label(paths_inner, text="Carpeta de destino (Markdown):", font=FONT_HEAD, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD)
    lbl_out.pack(anchor="w")

    f2 = tk.Frame(paths_inner, bg=COLOR_CARD)
    f2.pack(fill="x", pady=(2, 4))
    entry_out = tk.Entry(f2, textvariable=out_var, font=FONT_CODE, bg=COLOR_INPUT_BG, fg=COLOR_TEXT_PRIMARY, insertbackground=COLOR_ACCENT_BLUE, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER)
    entry_out.pack(side="left", fill="x", expand=True, ipady=4, padx=(0, 8))

    def select_out():
        if mode_var.get() != "single":
            d = filedialog.askdirectory(title="Selecciona la carpeta de destino Markdown")
            if d: out_var.set(d)
        else:
            f = filedialog.asksaveasfilename(title="Guardar como Markdown", defaultextension=".md", filetypes=[("Markdown", "*.md")])
            if f: out_var.set(f)

    def paste_out():
        try:
            val = root.clipboard_get().strip().strip('"').strip("'")
            if val: out_var.set(val)
        except Exception:
            pass

    create_btn(f2, "Examinar...", select_out, bg="#2c2c2e", hover_bg="#3a3a3c").pack(side="right", padx=(4, 0))
    create_btn(f2, "📋 Pegar", paste_out, bg="#2c2c2e", hover_bg="#3a3a3c").pack(side="right", padx=(4, 0))

    # ------------------------------------------------------------------
    # CARD 3: OPCIONES DE FORMATO Y RIGOR
    # ------------------------------------------------------------------
    card_opts = make_card(p1, "🛠️ Opciones de Formato y Rigor")
    card_opts.pack(fill="x", pady=(0, 8))

    opts_inner = tk.Frame(card_opts, bg=COLOR_CARD, padx=16, pady=4)
    opts_inner.pack(fill="x")

    def make_chk(parent, text, var, fg=COLOR_TEXT_PRIMARY, font=FONT_BODY):
        return tk.Checkbutton(
            parent, text=text, variable=var, command=on_custom_toggle,
            font=font, fg=fg, bg=COLOR_CARD, selectcolor=COLOR_INPUT_BG,
            activebackground=COLOR_CARD, activeforeground=COLOR_ACCENT_CYAN,
            bd=0, highlightthickness=0
        )

    row_opt1 = tk.Frame(opts_inner, bg=COLOR_CARD)
    row_opt1.pack(fill="x", pady=1)
    make_chk(row_opt1, "🔗 Adaptar enlaces locales (.html → .md)", rewrite_links_var).pack(side="left", padx=(0, 18))
    make_chk(row_opt1, "📑 Índice de contenidos (TOC)", generate_toc_var).pack(side="left", padx=(0, 18))
    make_chk(row_opt1, "🖼️ Extraer imágenes Base64 a assets/", extract_b64_var).pack(side="left")

    row_opt2 = tk.Frame(opts_inner, bg=COLOR_CARD)
    row_opt2.pack(fill="x", pady=1)
    make_chk(row_opt2, "🏷️ Metadatos (Autor, Fecha)", include_meta_var).pack(side="left", padx=(0, 18))
    make_chk(row_opt2, "📐 Formulario Resumen de Ecuaciones", formula_sheet_var).pack(side="left", padx=(0, 18))
    make_chk(row_opt2, "📝 Cabecera YAML Frontmatter", include_yaml_var).pack(side="left")

    row_opt3 = tk.Frame(opts_inner, bg=COLOR_CARD)
    row_opt3.pack(fill="x", pady=1)
    chk_master = make_chk(row_opt3, "📚 Cuaderno Maestro Unificado (_Cuaderno_Maestro.md)", master_doc_var, fg=COLOR_ACCENT_CYAN, font=FONT_HEAD)
    chk_master.pack(side="left", padx=(0, 18))
    chk_dash = make_chk(row_opt3, "📊 Reporte Analítico del Lote (_Reporte_Analitico.md)", dashboard_var, fg=COLOR_ACCENT_GREEN, font=FONT_HEAD)
    chk_dash.pack(side="left")

    # ------------------------------------------------------------------
    # CARD 4: CONSOLA DE ACTIVIDAD Y MONITOR
    # ------------------------------------------------------------------
    card_console = make_card(p1, "💻 Consola de Actividad")
    card_console.pack(fill="both", expand=True, pady=(0, 8))

    cons_inner = tk.Frame(card_console, bg=COLOR_CARD, padx=16, pady=4)
    cons_inner.pack(fill="both", expand=True)

    log_header = tk.Frame(cons_inner, bg=COLOR_CARD)
    log_header.pack(fill="x")
    tk.Label(log_header, text="Registro en Tiempo Real:", font=FONT_SMALL, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD).pack(side="left")
    lbl_progress_text = tk.Label(log_header, text="", font=FONT_SMALL, fg=COLOR_ACCENT_CYAN, bg=COLOR_CARD)
    lbl_progress_text.pack(side="right")

    log_area = ScrolledText(cons_inner, height=5, font=FONT_CODE, bg=COLOR_INPUT_BG, fg=COLOR_TEXT_PRIMARY, insertbackground=COLOR_ACCENT_BLUE, bd=0, highlightthickness=1, highlightbackground=COLOR_CARD_BORDER)
    log_area.pack(fill="both", expand=True, pady=(4, 6))

    log_area.tag_config("success", foreground=COLOR_ACCENT_GREEN)
    log_area.tag_config("error", foreground=COLOR_ACCENT_RED)
    log_area.tag_config("info", foreground=COLOR_ACCENT_CYAN)
    log_area.tag_config("warn", foreground=COLOR_ACCENT_AMBER)

    def log(msg, tag=None):
        log_area.insert("end", f"[{time.strftime('%H:%M:%S')}] {msg}\n", tag)
        log_area.see("end")

    log("Sistema listo. Configura las rutas para iniciar la conversión.", "info")

    progress_bar = ttk.Progressbar(cons_inner, orient="horizontal", mode="determinate", style="Modern.Horizontal.TProgressbar")
    progress_bar.pack(fill="x", pady=(0, 6))

    # Botonera de acciones principales
    btn_frame = tk.Frame(p1, bg=COLOR_CANVAS)
    btn_frame.pack(fill="x", pady=(4, 0))

    def open_destination():
        dst = out_var.get().strip()
        target = Path(dst) if mode_var.get() != "single" else Path(dst).parent
        if target.exists():
            if sys.platform == "win32":
                os.startfile(str(target))
            else:
                subprocess.run(["xdg-open", str(target)])

    btn_open = create_btn(btn_frame, "📂 Abrir Carpeta", open_destination, bg="#2c2c2e", hover_bg="#3a3a3c")
    btn_cancel = create_btn(btn_frame, "⏹ Detener", lambda: None, bg=COLOR_ACCENT_RED, hover_bg=COLOR_ACCENT_RED_HOVER, fg="#ffffff")
    btn_cancel.config(state="disabled")

    def switch_to_viewer():
        notebook.select(tab_viewer)

    btn_go_viewer = create_btn(btn_frame, "👁️ Ver en Visor", switch_to_viewer, bg="#2c2c2e", hover_bg="#3a3a3c", fg=COLOR_ACCENT_CYAN)

    def on_cancel():
        cancel_event.set()
        log("Detención solicitada por el usuario...", "warn")

    btn_cancel.config(command=on_cancel)

    # ==================================================================
    # PESTAÑA 2: VISOR MARKDOWN EN VIVO, BÚSQUEDA Y PORTAPAPELES
    # ==================================================================
    p2 = tk.Frame(tab_viewer, bg=COLOR_CANVAS, padx=4, pady=4)
    p2.pack(fill="both", expand=True)

    viewer_card_top = make_card(p2)
    viewer_card_top.pack(fill="x", pady=(0, 8))

    viewer_top = tk.Frame(viewer_card_top, bg=COLOR_CARD, padx=16, pady=8)
    viewer_top.pack(fill="x")

    tk.Label(viewer_top, text="📄 Documento:", font=FONT_HEAD, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD).pack(side="left", padx=(0, 8))

    combo_viewer = ttk.Combobox(viewer_top, state="readonly", width=34, style="Modern.TCombobox")
    combo_viewer.pack(side="left", fill="x", expand=True, padx=(0, 8))

    def on_viewer_file_selected(event=None):
        sel = combo_viewer.get().strip()
        if not sel:
            return
        dst_folder = Path(out_var.get().strip())
        target_path = dst_folder / sel if mode_var.get() != "single" else Path(out_var.get().strip())
        if target_path.exists():
            load_content_into_viewer(target_path)

    combo_viewer.bind("<<ComboboxSelected>>", on_viewer_file_selected)

    def refresh_viewer_list():
        dst_str = out_var.get().strip()
        if not dst_str:
            return
        dst_folder = Path(dst_str) if mode_var.get() != "single" else Path(dst_str).parent
        if dst_folder.exists():
            mds = sorted([f.name for f in dst_folder.glob("*.md")])
            masters = [m for m in mds if m.startswith("_Cuaderno_Maestro")]
            reports = [m for m in mds if m.startswith("_Reporte_Analitico")]
            others = [m for m in mds if not m.startswith("_Cuaderno_Maestro") and not m.startswith("_Reporte_Analitico")]
            ordered = masters + reports + others
            combo_viewer["values"] = ordered
            if ordered:
                combo_viewer.set(ordered[0])
                on_viewer_file_selected()

    create_btn(viewer_top, "🔄", refresh_viewer_list, bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_HEAD).pack(side="left", padx=(0, 6))

    def copy_viewer_to_clipboard():
        txt = viewer_text.get("1.0", "end-1c")
        if not txt.strip():
            return
        root.clipboard_clear()
        root.clipboard_append(txt)
        lbl_copy_msg.config(text="✅ ¡Copiado!", fg=COLOR_ACCENT_GREEN)
        root.after(3000, lambda: lbl_copy_msg.config(text=""))

    btn_copy_viewer = create_btn(
        viewer_top, "📋 Copiar para NotebookLM", copy_viewer_to_clipboard,
        bg=COLOR_ACCENT_BLUE, hover_bg=COLOR_ACCENT_HOVER, fg="white", font=FONT_HEAD
    )
    btn_copy_viewer.pack(side="left", padx=(0, 6))

    def open_in_editor():
        sel = combo_viewer.get().strip()
        if not sel:
            return
        dst_folder = Path(out_var.get().strip())
        target_path = dst_folder / sel if mode_var.get() != "single" else Path(out_var.get().strip())
        if target_path.exists():
            if sys.platform == "win32":
                os.startfile(str(target_path))
            else:
                subprocess.run(["xdg-open", str(target_path)])

    create_btn(viewer_top, "📝 Abrir en Editor", open_in_editor, bg="#2c2c2e", hover_bg="#3a3a3c").pack(side="left", padx=(0, 6))

    viewer_theme_mode = tk.StringVar(value="dark")

    def toggle_viewer_theme():
        mode = viewer_theme_mode.get()
        if mode == "dark":
            viewer_theme_mode.set("light")
            btn_theme.config(text="🌙 Modo Oscuro")
            viewer_text.config(bg="#ffffff", fg="#1d1d1f", insertbackground="#0071e3")
            viewer_text.tag_config("h1", foreground="#0071e3")
            viewer_text.tag_config("h2", foreground="#0077ed")
            viewer_text.tag_config("h3", foreground="#2997ff")
            viewer_text.tag_config("math", foreground="#b45309")
            viewer_text.tag_config("quote", foreground="#86868b")
            viewer_text.tag_config("table", foreground="#30d158")
            viewer_text.tag_config("hr", foreground="#d2d2d7")
            viewer_text.tag_config("search_highlight", background="#fef08a", foreground="#78350f")
            viewer_text.tag_config("search_current", background="#30d158", foreground="#ffffff")
        else:
            viewer_theme_mode.set("dark")
            btn_theme.config(text="☀️ Modo Claro")
            viewer_text.config(bg=COLOR_INPUT_BG, fg=COLOR_TEXT_PRIMARY, insertbackground=COLOR_ACCENT_BLUE)
            viewer_text.tag_config("h1", foreground=COLOR_ACCENT_CYAN)
            viewer_text.tag_config("h2", foreground=COLOR_ACCENT_BLUE)
            viewer_text.tag_config("h3", foreground="#60a5fa")
            viewer_text.tag_config("math", foreground="#ffd60a")
            viewer_text.tag_config("quote", foreground=COLOR_TEXT_MUTED)
            viewer_text.tag_config("table", foreground=COLOR_ACCENT_GREEN)
            viewer_text.tag_config("hr", foreground="#3a3a3c")
            viewer_text.tag_config("search_highlight", background="#78350f", foreground="#fef08a")
            viewer_text.tag_config("search_current", background=COLOR_ACCENT_GREEN, foreground="#ffffff")

    btn_theme = create_btn(viewer_top, "☀️ Modo Claro", toggle_viewer_theme, bg="#2c2c2e", hover_bg="#3a3a3c")
    btn_theme.pack(side="left")

    lbl_copy_msg = tk.Label(viewer_top, text="", font=FONT_HEAD, bg=COLOR_CARD)
    lbl_copy_msg.pack(side="right", padx=6)

    # ------------------------------------------------------------------
    # CARD NOTEBOOKLM PROMPT ASSISTANT
    # ------------------------------------------------------------------
    card_prompts = make_card(p2)
    card_prompts.pack(fill="x", pady=(0, 8))

    prompts_inner = tk.Frame(card_prompts, bg=COLOR_CARD, padx=16, pady=8)
    prompts_inner.pack(fill="x")

    tk.Label(prompts_inner, text="🤖 Prompts para NotebookLM:", font=FONT_HEAD, fg=COLOR_TEXT_PRIMARY, bg=COLOR_CARD).pack(side="left", padx=(0, 10))

    def copy_prompt(prompt_text, name):
        root.clipboard_clear()
        root.clipboard_append(prompt_text)
        lbl_copy_msg.config(text=f"✅ Prompt '{name}' copiado!", fg=COLOR_ACCENT_CYAN)
        root.after(3000, lambda: lbl_copy_msg.config(text=""))

    p_exam = "Actúa como el profesor de Sistemes de Mesura de la UPC. Utilizando el banco de afirmaciones del Cuaderno Maestro, hazme 5 preguntas aleatorias de tipo Verdadero/Falso. Espera mi respuesta antes de darme la solución y la justificación técnica."
    p_math = "Explícame paso a paso cómo se deduce el modelo y las ecuaciones principales de este tema, indicando claramente las hipótesis de partida y el significado físico de cada variable."
    p_flash = "Genera una tabla comparativa con las 5 definiciones y conceptos más críticos de esta unidad, destacando las trampas conceptuales habituales de examen."

    create_btn(prompts_inner, "🎯 Simulación Examen", lambda: copy_prompt(p_exam, "Examen"), bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_SMALL, padx=12, pady=4).pack(side="left", padx=(0, 6))
    create_btn(prompts_inner, "📐 Deducción Fórmulas", lambda: copy_prompt(p_math, "Fórmulas"), bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_SMALL, padx=12, pady=4).pack(side="left", padx=(0, 6))
    create_btn(prompts_inner, "🔍 Repaso Conceptos", lambda: copy_prompt(p_flash, "Conceptos"), bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_SMALL, padx=12, pady=4).pack(side="left")

    # Barra de estadísticas del archivo activo en el visor
    stats_bar = tk.Frame(p2, bg=COLOR_INSET, padx=16, pady=6, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER)
    stats_bar.pack(fill="x", pady=(0, 8))

    lbl_viewer_stats = tk.Label(
        stats_bar,
        text="📊 Palabras: 0  |  🔤 Caracteres: 0  |  📐 Fórmulas: 0  |  📋 Tablas: 0  |  🖼️ Imágenes: 0",
        fg=COLOR_TEXT_MUTED, bg=COLOR_INSET, font=FONT_HEAD
    )
    lbl_viewer_stats.pack(anchor="w")

    # Barra interactiva de búsqueda en el visor (Ctrl+F)
    card_search = make_card(p2)
    card_search.pack(fill="x", pady=(0, 8))

    search_frame = tk.Frame(card_search, bg=COLOR_CARD, padx=16, pady=6)
    search_frame.pack(fill="x")

    tk.Label(search_frame, text="🔍 Buscar:", fg=COLOR_TEXT_MUTED, bg=COLOR_CARD, font=FONT_HEAD).pack(side="left", padx=(0, 6))
    search_var = tk.StringVar()
    entry_search = tk.Entry(search_frame, textvariable=search_var, font=FONT_CODE, width=24, bg=COLOR_INPUT_BG, fg=COLOR_TEXT_PRIMARY, insertbackground=COLOR_ACCENT_BLUE, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER)
    entry_search.pack(side="left", padx=(0, 8), ipady=2)

    search_matches = []
    current_match_idx = -1

    def do_search(direction=1):
        nonlocal search_matches, current_match_idx
        q = search_var.get().strip()
        viewer_text.tag_remove("search_highlight", "1.0", "end")
        viewer_text.tag_remove("search_current", "1.0", "end")
        if not q:
            lbl_search_info.config(text="")
            search_matches = []
            current_match_idx = -1
            return

        search_matches = []
        start = "1.0"
        while True:
            pos = viewer_text.search(q, start, stopindex="end", nocase=True)
            if not pos:
                break
            end_pos = f"{pos}+{len(q)}c"
            viewer_text.tag_add("search_highlight", pos, end_pos)
            search_matches.append((pos, end_pos))
            start = end_pos

        if not search_matches:
            lbl_search_info.config(text="0 coincidencias", fg=COLOR_ACCENT_RED)
            current_match_idx = -1
            return

        if current_match_idx == -1:
            current_match_idx = 0
        else:
            current_match_idx = (current_match_idx + direction) % len(search_matches)

        cur_start, cur_end = search_matches[current_match_idx]
        viewer_text.tag_add("search_current", cur_start, cur_end)
        viewer_text.see(cur_start)
        lbl_search_info.config(
            text=f"✓ {current_match_idx + 1} / {len(search_matches)} coincidencias",
            fg=COLOR_ACCENT_GREEN
        )

    btn_prev = create_btn(search_frame, "◀ Anterior", lambda: do_search(-1), bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_SMALL, padx=10, pady=3)
    btn_prev.pack(side="left", padx=(0, 4))

    btn_next = create_btn(search_frame, "Siguiente ▶", lambda: do_search(1), bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_SMALL, padx=10, pady=3)
    btn_next.pack(side="left", padx=(0, 6))

    def clear_search():
        search_var.set("")
        do_search(0)
        entry_search.focus_set()

    btn_clear = create_btn(search_frame, "✖ Limpiar", clear_search, bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_SMALL, padx=10, pady=3)
    btn_clear.pack(side="left", padx=(0, 8))

    lbl_search_info = tk.Label(search_frame, text="", bg=COLOR_CARD, font=FONT_SMALL)
    lbl_search_info.pack(side="left", padx=4)

    entry_search.bind("<Return>", lambda e: do_search(1))
    entry_search.bind("<Shift-Return>", lambda e: do_search(-1))
    search_var.trace_add("write", lambda *args: do_search(0))

    root.bind("<Control-f>", lambda e: (notebook.select(tab_viewer), entry_search.focus_set(), entry_search.select_range(0, 'end')))

    # Área de visualización de Markdown con syntax highlighting ligero
    viewer_text = ScrolledText(p2, font=FONT_CODE, bg=COLOR_INPUT_BG, fg=COLOR_TEXT_PRIMARY, insertbackground=COLOR_ACCENT_BLUE, wrap="word", bd=0, highlightthickness=1, highlightbackground=COLOR_CARD_BORDER)
    viewer_text.pack(fill="both", expand=True)

    # Configuración de estilos visuales
    viewer_text.tag_config("h1", foreground=COLOR_ACCENT_CYAN, font=(FONT_FAMILY, 12, "bold"))
    viewer_text.tag_config("h2", foreground=COLOR_ACCENT_BLUE, font=(FONT_FAMILY, 11, "bold"))
    viewer_text.tag_config("h3", foreground="#60a5fa", font=(FONT_FAMILY, 10, "bold"))
    viewer_text.tag_config("math", foreground="#ffd60a", font=(FONT_CODE[0], 10, "bold"))
    viewer_text.tag_config("quote", foreground=COLOR_TEXT_MUTED)
    viewer_text.tag_config("table", foreground=COLOR_ACCENT_GREEN)
    viewer_text.tag_config("hr", foreground="#3a3a3c")
    viewer_text.tag_config("search_highlight", background="#78350f", foreground="#fef08a")
    viewer_text.tag_config("search_current", background=COLOR_ACCENT_GREEN, foreground="#ffffff")

    def highlight_markdown_syntax():
        content = viewer_text.get("1.0", "end-1c")
        lines = content.split("\n")
        in_math_block = False

        for i, line in enumerate(lines):
            line_idx = f"{i+1}.0"
            line_end = f"{i+1}.end"
            stripped = line.strip()

            if stripped.startswith("$$"):
                viewer_text.tag_add("math", line_idx, line_end)
                in_math_block = not in_math_block if stripped == "$$" else False
                continue
            if in_math_block:
                viewer_text.tag_add("math", line_idx, line_end)
                continue

            if stripped.startswith("# "):
                viewer_text.tag_add("h1", line_idx, line_end)
            elif stripped.startswith("## "):
                viewer_text.tag_add("h2", line_idx, line_end)
            elif stripped.startswith("### "):
                viewer_text.tag_add("h3", line_idx, line_end)
            elif stripped.startswith(">"):
                viewer_text.tag_add("quote", line_idx, line_end)
            elif stripped.startswith("|"):
                viewer_text.tag_add("table", line_idx, line_end)
            elif stripped in ("---", "***", "___"):
                viewer_text.tag_add("hr", line_idx, line_end)

    def load_content_into_viewer(target_file: Path, scroll_to_line: int = None, highlight_word: str = None):
        try:
            content = target_file.read_text(encoding="utf-8")
            viewer_text.config(state="normal")
            viewer_text.delete("1.0", "end")
            viewer_text.insert("1.0", content)
            highlight_markdown_syntax()
            viewer_text.config(state="disabled")

            words = len(content.split())
            chars = len(content)
            math_count = len(re.findall(r"\$\$|\$", content)) // 2
            tables_count = len(re.findall(r"\| :---", content))
            img_count = len(re.findall(r"!\[.*?\]\(.*?\)", content))

            lbl_viewer_stats.config(
                text=f"📊 Palabras: {words:,}  |  🔤 Caracteres: {chars:,}  |  📐 Fórmulas: {math_count}  |  📋 Tablas: {tables_count}  |  🖼️ Imágenes: {img_count}"
            )
            if highlight_word:
                search_var.set(highlight_word)
                do_search(0)
            elif search_var.get().strip():
                do_search(0)

            if scroll_to_line:
                viewer_text.see(f"{scroll_to_line}.0")
        except Exception as e:
            viewer_text.config(state="normal")
            viewer_text.delete("1.0", "end")
            viewer_text.insert("1.0", f"Error al cargar archivo: {str(e)}")
            viewer_text.config(state="disabled")

    # ==================================================================
    # PESTAÑA 3: CENTRO DE RECURSOS DEL CURSO Y ASISTENTE NOTEBOOKLM
    # ==================================================================
    canvas_res = tk.Canvas(tab_resources, bg=COLOR_CANVAS, highlightthickness=0, bd=0)
    scrollbar_res = ttk.Scrollbar(tab_resources, orient="vertical", command=canvas_res.yview)
    p3 = tk.Frame(canvas_res, bg=COLOR_CANVAS, padx=4, pady=4)

    p3.bind("<Configure>", lambda e: canvas_res.configure(scrollregion=canvas_res.bbox("all")))
    canvas_window = canvas_res.create_window((0, 0), window=p3, anchor="nw")
    canvas_res.bind("<Configure>", lambda e: canvas_res.itemconfig(canvas_window, width=e.width))
    canvas_res.configure(yscrollcommand=scrollbar_res.set)

    def _on_mousewheel_res(event):
        if event.delta:
            canvas_res.yview_scroll(int(-1 * (event.delta / 120)), "units")
    p3.bind("<Enter>", lambda e: canvas_res.bind_all("<MouseWheel>", _on_mousewheel_res))
    p3.bind("<Leave>", lambda e: canvas_res.unbind_all("<MouseWheel>"))

    scrollbar_res.pack(side="right", fill="y")
    canvas_res.pack(side="left", fill="both", expand=True)

    # Localizador de archivos generados
    def find_resource_file(filename):
        dst = out_var.get().strip()
        candidates = []
        if dst:
            d = Path(dst)
            candidates.append(d / filename)
            candidates.append(d.parent / filename)
        candidates.append(Path("dist_course_md") / filename)
        candidates.append(Path(".") / filename)
        for c in candidates:
            if c.exists() and c.is_file():
                return c
        return None

    def load_resource_in_viewer(filename):
        p = find_resource_file(filename)
        if p:
            notebook.select(tab_viewer)
            refresh_viewer_list()
            try:
                combo_viewer.set(p.name)
            except Exception:
                pass
            load_content_into_viewer(p)
            lbl_copy_msg.config(text=f"✅ Cargado: {p.name}", fg=COLOR_ACCENT_CYAN)
            root.after(3000, lambda: lbl_copy_msg.config(text=""))
        else:
            messagebox.showwarning(
                "Recurso no encontrado",
                f"El archivo '{filename}' aún no ha sido generado.\n\n"
                f"Haz clic en 'Convertir Todo el Curso' o asegúrate de que la carpeta de salida "
                f"apunte al directorio correcto."
            )

    def open_resource_in_editor(filename):
        p = find_resource_file(filename)
        if p:
            if sys.platform == "win32":
                os.startfile(str(p))
            else:
                subprocess.run(["xdg-open", str(p)])
        else:
            messagebox.showwarning("Archivo no encontrado", f"No se encontró el archivo '{filename}'.")

    def copy_resource_to_clipboard(filename, label_name):
        p = find_resource_file(filename)
        if p:
            try:
                content = p.read_text(encoding="utf-8")
                root.clipboard_clear()
                root.clipboard_append(content)
                lbl_res_status.config(text=f"✅ ¡{label_name} copiado al portapapeles! ({len(content):,} car.)", fg=COLOR_ACCENT_GREEN)
                root.after(3500, update_resources_status)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo leer el archivo: {e}")
        else:
            messagebox.showwarning("Archivo no encontrado", f"No se encontró el archivo '{filename}'.")

    def open_resource_folder(filename):
        p = find_resource_file(filename)
        folder = p.parent if p else (Path(out_var.get().strip()) if out_var.get().strip() else Path("dist_course_md"))
        if folder.exists():
            if sys.platform == "win32":
                os.startfile(str(folder))
            else:
                subprocess.run(["xdg-open", str(folder)])
        else:
            messagebox.showwarning("Carpeta no encontrada", f"La carpeta '{folder}' aún no existe.")

    def show_anki_guide():
        guide = (
            "📌 CÓMO IMPORTAR LAS FLASHCARDS EN ANKI:\n\n"
            "Opción 1: Paquete Nativo .apkg (¡Recomendado en 1 clic!)\n"
            "• Haz clic en '📦 Importar Paquete Anki (.apkg)' o haz doble clic sobre el archivo '_Flashcards_Examen.apkg'.\n"
            "• Se abrirá Anki e importará directamente las 500 tarjetas con diseño Apple Dark Mode y soporte de fórmulas MathJax.\n\n"
            "Opción 2: Archivo TSV Universal\n"
            "• Abre Anki -> Menú Archivo -> Importar -> Selecciona '_Flashcards_Examen.tsv'.\n"
            "• Asegúrate de que el separador sea 'Tab' y la casilla 'Permitir HTML' esté marcada."
        )
        messagebox.showinfo("Guía de Flashcards Anki", guide)

    def open_anki_package():
        p = find_resource_file("_Flashcards_Examen.apkg")
        if p and p.exists():
            if sys.platform == "win32":
                os.startfile(str(p))
            else:
                subprocess.run(["xdg-open", str(p)])
        else:
            # Si no existe, intentar compilarlo si existe in_dir
            target_dir = Path(out_var.get().strip()) if out_var.get().strip() else Path("dist_course_md")
            in_dir = Path(in_var.get().strip()) if in_var.get().strip() else Path("C:/Users/dmart/Documents/OpenCode")
            if in_dir.exists():
                lbl_res_status.config(text="⏳ Compilando paquete Anki .apkg...", fg=COLOR_ACCENT_AMBER)
                root.update_idletasks()
                generate_course_flashcards_tsv(target_dir, in_dir)
                p = target_dir / "_Flashcards_Examen.apkg"
                if p.exists():
                    if sys.platform == "win32":
                        os.startfile(str(p))
                    else:
                        subprocess.run(["xdg-open", str(p)])
                    lbl_res_status.config(text="✅ ¡Paquete .apkg compilado y abierto en Anki!", fg=COLOR_ACCENT_GREEN)
                    return
            messagebox.showwarning(
                "Paquete Anki no encontrado",
                "El paquete Anki '_Flashcards_Examen.apkg' aún no ha sido generado.\n\n"
                "Ejecuta 'Convertir Todo el Curso' para compilarlo automáticamente con las 500 tarjetas."
            )

    def open_spotlight_modal():
        spotlight_win = tk.Toplevel(root)
        spotlight_win.title(" Spotlight Course Search")
        spotlight_win.geometry("740x500")
        spotlight_win.configure(bg=COLOR_CANVAS)
        spotlight_win.transient(root)
        spotlight_win.grab_set()

        try:
            x = root.winfo_x() + (root.winfo_width() - 740) // 2
            y = root.winfo_y() + (root.winfo_height() - 500) // 2
            spotlight_win.geometry(f"+{max(10, x)}+{max(10, y)}")
        except Exception:
            pass

        s_box = tk.Frame(spotlight_win, bg=COLOR_CARD, padx=16, pady=12, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER)
        s_box.pack(fill="x", padx=16, pady=14)

        tk.Label(s_box, text="🔍", font=(FONT_FAMILY, 15), fg=COLOR_ACCENT_BLUE, bg=COLOR_CARD).pack(side="left", padx=(0, 10))

        s_entry = tk.Entry(s_box, font=(FONT_FAMILY, 13), bg=COLOR_CARD, fg=COLOR_TEXT_PRIMARY, insertbackground="#ffffff", bd=0, relief="flat")
        s_entry.pack(side="left", fill="x", expand=True)
        s_entry.focus_set()

        tk.Label(s_box, text="ESC para salir  •  ↵ para abrir", font=FONT_SMALL, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD).pack(side="right", padx=(8, 0))

        lbl_s_status = tk.Label(spotlight_win, text="Escribe para buscar fórmulas, conceptos y preguntas en todo el curso...", font=FONT_SMALL, fg=COLOR_TEXT_MUTED, bg=COLOR_CANVAS)
        lbl_s_status.pack(anchor="w", padx=20, pady=(0, 6))

        res_frame = tk.Frame(spotlight_win, bg=COLOR_CARD, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER)
        res_frame.pack(fill="both", expand=True, padx=16, pady=(0, 14))

        res_scroll = ttk.Scrollbar(res_frame, orient="vertical")
        res_list = tk.Listbox(
            res_frame, font=(FONT_MONO, 10), bg=COLOR_CARD, fg=COLOR_TEXT_PRIMARY,
            selectbackground=COLOR_ACCENT_BLUE, selectforeground="#ffffff",
            activestyle="none", bd=0, highlightthickness=0, yscrollcommand=res_scroll.set
        )
        res_scroll.config(command=res_list.yview)
        res_scroll.pack(side="right", fill="y")
        res_list.pack(side="left", fill="both", expand=True, padx=6, pady=6)

        search_results = []

        def trigger_search(*args):
            nonlocal search_results
            q = s_entry.get().strip()
            res_list.delete(0, "end")
            if len(q) < 2:
                lbl_s_status.config(text="Escribe al menos 2 caracteres...")
                search_results = []
                return

            target_dir = Path(out_var.get().strip()) if out_var.get().strip() else Path("dist_course_md")
            if not target_dir.exists():
                target_dir = Path(".")

            search_results = search_course_content(target_dir, q, max_results=40)
            lbl_s_status.config(text=f"Encontradas {len(search_results)} coincidencias para '{q}'")
            for r in search_results:
                res_list.insert("end", f"[{r['topic']}] {r['file']} (L{r['line']}): {r['snippet']}")
            if search_results:
                res_list.selection_set(0)

        s_entry.bind("<KeyRelease>", trigger_search)

        def jump_to_result(event=None):
            sel = res_list.curselection()
            if not sel or not search_results:
                return
            chosen = search_results[sel[0]]
            spotlight_win.destroy()

            notebook.select(tab_viewer)
            refresh_viewer_list()
            try:
                combo_viewer.set(chosen["path"].name)
            except Exception:
                pass
            search_var.set(s_entry.get().strip())
            load_content_into_viewer(chosen["path"], scroll_to_line=chosen["line"], highlight_word=s_entry.get().strip())
            lbl_copy_msg.config(text=f"🔍 Abierto {chosen['path'].name} en línea {chosen['line']}", fg=COLOR_ACCENT_CYAN)
            root.after(3500, lambda: lbl_copy_msg.config(text=""))

        res_list.bind("<Double-Button-1>", jump_to_result)
        s_entry.bind("<Return>", jump_to_result)
        res_list.bind("<Return>", jump_to_result)
        spotlight_win.bind("<Escape>", lambda e: spotlight_win.destroy())

    def open_exam_simulator_modal():
        in_val = in_var.get().strip()
        in_dir = Path(in_val) if in_val else Path("C:/Users/dmart/Documents/OpenCode")
        if not in_dir.exists():
            in_dir = Path("C:/Users/dmart/Documents/OpenCode")
        if not in_dir.exists():
            in_dir = Path(".")

        all_quizzes = load_all_course_quizzes(in_dir)
        if not all_quizzes:
            default_opencode = Path("C:/Users/dmart/Documents/OpenCode")
            if default_opencode.exists() and default_opencode != in_dir:
                all_quizzes = load_all_course_quizzes(default_opencode)

        if not all_quizzes:
            target_dir = Path(out_var.get().strip()) if out_var.get().strip() else Path("dist_course_md")
            tsv_p = target_dir / "_Flashcards_Examen.tsv"
            if not tsv_p.exists():
                tsv_p = Path("dist_course_md/_Flashcards_Examen.tsv")
            if tsv_p.exists():
                all_quizzes = load_quizzes_from_tsv(tsv_p)

        if not all_quizzes:
            messagebox.showwarning(
                "Simulador de Examen",
                "No se han encontrado preguntas de test en los archivos HTML del curso ni en las flashcards TSV.\n\n"
                "Asegúrate de que la ruta de entrada contenga los archivos 'entrenament.html' o ejecuta la conversión del curso."
            )
            return

        sim_win = tk.Toplevel(root)
        sim_win.title(" Simulador Oficial de Examen · Sistemes de Mesura (EEBE · UPC)")
        sim_win.geometry("860x720")
        sim_win.minsize(800, 640)
        sim_win.configure(bg=COLOR_CANVAS)
        sim_win.transient(root)
        sim_win.grab_set()

        try:
            x = root.winfo_x() + (root.winfo_width() - 860) // 2
            y = root.winfo_y() + (root.winfo_height() - 720) // 2
            sim_win.geometry(f"+{max(10, x)}+{max(10, y)}")
        except Exception:
            pass

        main_container = tk.Frame(sim_win, bg=COLOR_CANVAS, padx=20, pady=20)
        main_container.pack(fill="both", expand=True)

        current_questions = []
        user_answers = []
        current_idx = 0

        def render_config_screen():
            for w in main_container.winfo_children():
                w.destroy()

            head_box = tk.Frame(main_container, bg=COLOR_CARD, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER, padx=20, pady=16)
            head_box.pack(fill="x", pady=(0, 16))

            tk.Label(head_box, text=" Simulador Oficial de Examen · Sistemes de Mesura", font=(FONT_FAMILY, 17, "bold"), fg=COLOR_TEXT_PRIMARY, bg=COLOR_CARD).pack(anchor="w")
            tk.Label(
                head_box,
                text="Universitat Politècnica de Catalunya (EEBE)  •  Baremo oficial: +1.00 acierto, -0.33 fallo, 0.00 en blanco.",
                font=FONT_SUBTITLE, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD
            ).pack(anchor="w", pady=(4, 0))

            cfg_card = tk.Frame(main_container, bg=COLOR_CARD, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER, padx=24, pady=20)
            cfg_card.pack(fill="both", expand=True)

            tk.Label(cfg_card, text="Configuración del Simulacro", font=FONT_TITLE, fg=COLOR_TEXT_PRIMARY, bg=COLOR_CARD).pack(anchor="w", pady=(0, 14))

            tk.Label(cfg_card, text="Materia o Tema a Evaluar:", font=FONT_HEAD, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD).pack(anchor="w", pady=(6, 4))
            
            topics_options = ["Todos los Temas (500 preguntas del curso)"]
            for i in range(1, 11):
                topics_options.append(f"Tema {i} (50 preguntas oficiales)")

            topic_combo = ttk.Combobox(cfg_card, values=topics_options, state="readonly", font=FONT_BODY)
            topic_combo.current(0)
            topic_combo.pack(fill="x", pady=(0, 14))

            tk.Label(cfg_card, text="Número de Preguntas del Examen:", font=FONT_HEAD, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD).pack(anchor="w", pady=(6, 4))
            
            count_combo = ttk.Combobox(cfg_card, values=["10 preguntas (Test Rápido)", "20 preguntas (Simulacro Oficial Parcial)", "30 preguntas (Simulacro Final Exhaustivo)", "50 preguntas (Tema Completo)"], state="readonly", font=FONT_BODY)
            count_combo.current(1)
            count_combo.pack(fill="x", pady=(0, 20))

            def start_test():
                nonlocal current_questions, user_answers, current_idx
                sel_topic = topic_combo.current()
                if sel_topic == 0:
                    pool = all_quizzes.copy()
                else:
                    pool = [q for q in all_quizzes if q.get("tema_num") == sel_topic]

                sel_count_idx = count_combo.current()
                desired_count = [10, 20, 30, 50][sel_count_idx]
                
                random.shuffle(pool)
                current_questions = pool[:min(desired_count, len(pool))]
                user_answers = []
                current_idx = 0
                render_question_screen()

            create_btn(cfg_card, "🚀 Comenzar Examen Ahora", start_test, bg=COLOR_ACCENT_BLUE, hover_bg=COLOR_ACCENT_HOVER, font=(FONT_FAMILY, 12, "bold"), padx=24, pady=10).pack(anchor="w", pady=(10, 0))

        def render_question_screen():
            for w in main_container.winfo_children():
                w.destroy()

            if current_idx >= len(current_questions):
                render_results_screen()
                return

            q_data = current_questions[current_idx]
            q_num = current_idx + 1
            q_total = len(current_questions)

            _, cor, wro, bla, curr_grade = score_exam(user_answers)
            top_bar = tk.Frame(main_container, bg=COLOR_CANVAS)
            top_bar.pack(fill="x", pady=(0, 12))

            tk.Label(
                top_bar,
                text=f"Pregunta {q_num} de {q_total}",
                font=(FONT_FAMILY, 15, "bold"), fg=COLOR_TEXT_PRIMARY, bg=COLOR_CANVAS
            ).pack(side="left")

            tk.Label(
                top_bar,
                text=f"[{q_data.get('tema_label', 'Tema')}]",
                font=(FONT_FAMILY, 10, "bold"), fg=COLOR_ACCENT_CYAN, bg="#112530", padx=10, pady=3
            ).pack(side="left", padx=10)

            tk.Label(
                top_bar,
                text=f"Nota Provisoria: {curr_grade:.2f} / 10.0 (Aciertos: {cor}  |  Fallos: {wro}  |  Blanco: {bla})",
                font=FONT_HEAD, fg=COLOR_TEXT_MUTED, bg=COLOR_CANVAS
            ).pack(side="right")

            card_q = tk.Frame(main_container, bg=COLOR_CARD, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER, padx=22, pady=18)
            card_q.pack(fill="both", expand=True, pady=(0, 12))

            statement_lbl = tk.Label(
                card_q, text=q_data["q"], font=(FONT_FAMILY, 13, "bold"),
                fg="#ffffff", bg=COLOR_CARD, justify="left", wraplength=760
            )
            statement_lbl.pack(anchor="w", pady=(0, 16))

            if q_data.get("ref"):
                tk.Label(card_q, text=f"Referencia de estudio: {q_data['ref']}", font=FONT_SMALL, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD).pack(anchor="w", pady=(0, 16))

            choices_frame = tk.Frame(card_q, bg=COLOR_CARD)
            choices_frame.pack(fill="x", pady=(0, 14))

            fb_frame = tk.Frame(card_q, bg=COLOR_INSET, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER, padx=16, pady=12)

            btn_v = None
            btn_f = None
            btn_blank = None
            btn_next = None

            def handle_answer(choice):
                ans_dict = {
                    "question": q_data["q"],
                    "tema": q_data.get("tema_label", "Tema"),
                    "correct": q_data["a"],
                    "user_choice": choice,
                    "justification": q_data.get("j", "")
                }
                user_answers.append(ans_dict)

                btn_v.config(state="disabled", cursor="default")
                btn_f.config(state="disabled", cursor="default")
                btn_blank.config(state="disabled", cursor="default")

                correct_val = q_data["a"].upper()
                is_correct = (choice == correct_val or (choice == "V" and correct_val in ["V", "VERTADER", "VERDADERO"]) or (choice == "F" and correct_val in ["F", "FALS", "FALSO"]))

                if choice == "BLANK":
                    status_text = "⚪ Pregunta dejada en blanco (0.00 puntos)"
                    status_col = COLOR_TEXT_MUTED
                elif is_correct:
                    status_text = "✅ ¡CORRECTO! (+1.00 punto UPC)"
                    status_col = COLOR_ACCENT_GREEN
                else:
                    status_text = "❌ INCORRECTO (-0.33 puntos UPC)"
                    status_col = COLOR_ACCENT_RED

                fb_frame.pack(fill="x", pady=(10, 0))
                tk.Label(fb_frame, text=status_text, font=(FONT_FAMILY, 12, "bold"), fg=status_col, bg=COLOR_INSET).pack(anchor="w")
                
                correct_str = "VERTADER (V)" if correct_val in ["V", "VERTADER", "VERDADERO"] else "FALS (F)"
                tk.Label(fb_frame, text=f"Respuesta oficial: {correct_str}", font=FONT_HEAD, fg=COLOR_TEXT_PRIMARY, bg=COLOR_INSET).pack(anchor="w", pady=(4, 6))

                if q_data.get("j"):
                    tk.Label(
                        fb_frame, text=f"Justificación técnica:\n{q_data['j']}",
                        font=FONT_BODY, fg="#d1d1d6", bg=COLOR_INSET, justify="left", wraplength=720
                    ).pack(anchor="w")

                btn_next.pack(side="right", pady=10)
                sim_win.bind("<Return>", lambda e: advance_question())
                sim_win.bind("<space>", lambda e: advance_question())

            def advance_question():
                nonlocal current_idx
                sim_win.unbind("<Return>")
                sim_win.unbind("<space>")
                current_idx += 1
                render_question_screen()

            btn_v = create_btn(choices_frame, "✅ VERTADER (V)", lambda: handle_answer("V"), bg="#1b4332", hover_bg="#2d6a4f", font=(FONT_FAMILY, 11, "bold"), padx=20, pady=8)
            btn_v.pack(side="left", padx=(0, 10))

            btn_f = create_btn(choices_frame, "❌ FALS (F)", lambda: handle_answer("F"), bg="#49111c", hover_bg="#721c24", font=(FONT_FAMILY, 11, "bold"), padx=20, pady=8)
            btn_f.pack(side="left", padx=(0, 10))

            btn_blank = create_btn(choices_frame, "⚪ Dejar en blanco", lambda: handle_answer("BLANK"), bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_HEAD, padx=16, pady=8)
            btn_blank.pack(side="left")

            nav_bar = tk.Frame(main_container, bg=COLOR_CANVAS)
            nav_bar.pack(fill="x")

            btn_next = create_btn(nav_bar, "Siguiente Pregunta ➔", advance_question, bg=COLOR_ACCENT_BLUE, hover_bg=COLOR_ACCENT_HOVER, font=(FONT_FAMILY, 11, "bold"), padx=20, pady=6)

        def render_results_screen():
            for w in main_container.winfo_children():
                w.destroy()

            tot, cor, wro, bla, grade = score_exam(user_answers)

            res_card = tk.Frame(main_container, bg=COLOR_CARD, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER, padx=28, pady=24)
            res_card.pack(fill="both", expand=True)

            if grade >= 9.0:
                badge_text = "🏆 EXCELENTE · MATRÍCULA DE HONOR"
                badge_col = COLOR_ACCENT_AMBER
            elif grade >= 7.0:
                badge_text = "🌟 NOTABLE"
                badge_col = COLOR_ACCENT_GREEN
            elif grade >= 5.0:
                badge_text = "✅ APROBADO"
                badge_col = COLOR_ACCENT_CYAN
            else:
                badge_text = "⚠️ SUSPENSO (Necesita Repaso)"
                badge_col = COLOR_ACCENT_RED

            tk.Label(res_card, text=badge_text, font=(FONT_FAMILY, 13, "bold"), fg=badge_col, bg=COLOR_CARD).pack(anchor="w")
            tk.Label(res_card, text=f"{grade:.2f} / 10.0", font=(FONT_FAMILY, 34, "bold"), fg=COLOR_TEXT_PRIMARY, bg=COLOR_CARD).pack(anchor="w", pady=(4, 12))

            grid = tk.Frame(res_card, bg=COLOR_INSET, padx=16, pady=12, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER)
            grid.pack(fill="x", pady=(0, 16))

            tk.Label(grid, text=f"• Total Preguntas: {tot}", font=FONT_HEAD, fg=COLOR_TEXT_PRIMARY, bg=COLOR_INSET).grid(row=0, column=0, sticky="w", padx=10, pady=3)
            tk.Label(grid, text=f"• Aciertos (+1.0 pto): {cor}", font=FONT_HEAD, fg=COLOR_ACCENT_GREEN, bg=COLOR_INSET).grid(row=0, column=1, sticky="w", padx=10, pady=3)
            tk.Label(grid, text=f"• Fallos (-0.33 pto): {wro}", font=FONT_HEAD, fg=COLOR_ACCENT_RED, bg=COLOR_INSET).grid(row=1, column=0, sticky="w", padx=10, pady=3)
            tk.Label(grid, text=f"• En Blanco (0.0 pto): {bla}", font=FONT_HEAD, fg=COLOR_TEXT_MUTED, bg=COLOR_INSET).grid(row=1, column=1, sticky="w", padx=10, pady=3)

            failed = [a for a in user_answers if a.get("user_choice") != a.get("correct") and a.get("user_choice") != "BLANK"]
            if failed:
                tk.Label(res_card, text=f"Preguntas Falladas a Repasar ({len(failed)}):", font=FONT_HEAD, fg=COLOR_ACCENT_RED, bg=COLOR_CARD).pack(anchor="w", pady=(4, 4))
                f_scroll = ttk.Scrollbar(res_card, orient="vertical")
                f_list = tk.Listbox(
                    res_card, font=(FONT_FAMILY, 10), bg=COLOR_INSET, fg="#ffffff",
                    selectbackground=COLOR_ACCENT_BLUE, height=6, bd=0, yscrollcommand=f_scroll.set
                )
                f_scroll.config(command=f_list.yview)
                f_scroll.pack(side="right", fill="y")
                f_list.pack(fill="x", pady=(0, 16))
                for f_item in failed:
                    f_list.insert("end", f"[{f_item['tema']}] {f_item['question'][:75]}... (Oficial: {f_item['correct']})")

            btn_box = tk.Frame(res_card, bg=COLOR_CARD)
            btn_box.pack(fill="x", pady=(10, 0))

            create_btn(btn_box, "🔄 Nuevo Examen", render_config_screen, bg=COLOR_ACCENT_BLUE, hover_bg=COLOR_ACCENT_HOVER, font=FONT_HEAD, padx=16, pady=8).pack(side="left", padx=(0, 8))
            create_btn(btn_box, "📋 Copiar Resultados", lambda: copy_results(grade, cor, wro, bla), bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_HEAD, padx=16, pady=8).pack(side="left", padx=(0, 8))
            create_btn(btn_box, "✕ Cerrar", sim_win.destroy, bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_HEAD, padx=16, pady=8).pack(side="left")

            def copy_results(g, c, w, b):
                rep = f"Simulacro Examen Sistemes de Mesura (UPC EEBE)\nNota: {g:.2f}/10.0\nAciertos: {c} | Fallos: {w} | Blanco: {b}"
                root.clipboard_clear()
                root.clipboard_append(rep)
                messagebox.showinfo("Copiado", "Resumen de calificación copiado al portapapeles.")

        render_config_screen()

    # 1. Tarjeta Superior: Encabezado y Estado del Curso
    card_res_head = make_card(p3)
    card_res_head.pack(fill="x", pady=(0, 8))

    head_res_inner = tk.Frame(card_res_head, bg=COLOR_CARD, padx=16, pady=12)
    head_res_inner.pack(fill="x")

    tk.Label(
        head_res_inner,
        text="🎓 Biblioteca Central del Curso · Sistemes de Mesura",
        font=FONT_TITLE, fg=COLOR_TEXT_PRIMARY, bg=COLOR_CARD
    ).pack(anchor="w")

    tk.Label(
        head_res_inner,
        text="Colección completa de recursos optimizados para NotebookLM, Obsidian y preparación de exámenes.",
        font=FONT_SUBTITLE, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD
    ).pack(anchor="w", pady=(2, 8))

    res_status_bar = tk.Frame(head_res_inner, bg=COLOR_INSET, padx=14, pady=6, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER)
    res_status_bar.pack(fill="x")

    lbl_res_status = tk.Label(res_status_bar, text="Escaneando recursos disponibles...", font=FONT_HEAD, fg=COLOR_TEXT_MUTED, bg=COLOR_INSET)
    lbl_res_status.pack(side="left")

    def update_resources_status():
        target_dir = Path(out_var.get().strip()) if out_var.get().strip() else Path("dist_course_md")
        if not target_dir.exists():
            target_dir = Path(".")
        md_count = len(list(target_dir.glob("*.md"))) if target_dir.exists() else 0
        has_index = (target_dir / "_Gran_Indice_Sistemes_de_Mesura.md").exists() or Path("dist_course_md/_Gran_Indice_Sistemes_de_Mesura.md").exists()
        has_glossary = (target_dir / "_Glosario_Conceptos_Clave.md").exists() or Path("dist_course_md/_Glosario_Conceptos_Clave.md").exists()
        has_flashcards = (target_dir / "_Flashcards_Examen.tsv").exists() or Path("dist_course_md/_Flashcards_Examen.tsv").exists()

        badges = []
        if has_index: badges.append("✓ Gran Índice")
        if has_glossary: badges.append("✓ Glosario A-Z")
        if has_flashcards: badges.append("✓ 500 Flashcards Anki")

        if badges:
            lbl_res_status.config(
                text=f"🟢 Recursos listos: {md_count} archivos MD detectados  |  " + "  •  ".join(badges),
                fg=COLOR_ACCENT_GREEN
            )
        else:
            lbl_res_status.config(
                text=f"🟡 No se detectan recursos consolidados en '{target_dir.name}'. Haz clic en 'Convertir Todo el Curso' para generarlos.",
                fg=COLOR_ACCENT_AMBER
            )

    create_btn(res_status_bar, "🔄 Refrescar", update_resources_status, bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_SMALL, padx=10, pady=3).pack(side="right")

    # 2. Métricas Clave del Curso (Apple KPIs Grid)
    kpi_frame = tk.Frame(p3, bg=COLOR_CANVAS)
    kpi_frame.pack(fill="x", pady=(0, 8))

    kpis = [
        ("10", "Temas del Curso", "Sensores, Ruido, Conversores", COLOR_ACCENT_CYAN),
        ("81", "Documentos MD", "Teoría, problemas y tests", COLOR_ACCENT_PURPLE),
        ("3,356", "Fórmulas LaTeX", "Ecuaciones 100% blindadas", COLOR_ACCENT_AMBER),
        ("500", "Preguntas Examen", "Con solución justificada", COLOR_ACCENT_GREEN)
    ]

    for i, (title, sub1, sub2, col) in enumerate(kpis):
        k_card = tk.Frame(kpi_frame, bg=COLOR_CARD, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER, padx=14, pady=10)
        k_card.pack(side="left", fill="both", expand=True, padx=(0 if i == 0 else 6, 0))
        tk.Label(k_card, text=title, font=(FONT_FAMILY, 16, "bold"), fg=col, bg=COLOR_CARD).pack(anchor="w")
        tk.Label(k_card, text=sub1, font=FONT_HEAD, fg=COLOR_TEXT_PRIMARY, bg=COLOR_CARD).pack(anchor="w", pady=(2, 0))
        tk.Label(k_card, text=sub2, font=FONT_SMALL, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD).pack(anchor="w")

    # 3. Tarjetas de Acciones Principales
    # CARD A: Gran Índice General
    card_idx = make_card(p3, "📖 Gran Índice General del Curso")
    card_idx.pack(fill="x", pady=(0, 8))
    idx_inner = tk.Frame(card_idx, bg=COLOR_CARD, padx=16, pady=8)
    idx_inner.pack(fill="x")

    tk.Label(
        idx_inner,
        text="Archivo: _Gran_Indice_Sistemes_de_Mesura.md\n"
             "Mapa de contenidos integral con enlaces a cada documento por tema, desglose analítico de fórmulas, "
             "problemas resueltos y banco de preguntas.",
        font=FONT_BODY, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD, justify="left"
    ).pack(anchor="w", pady=(0, 6))

    idx_actions = tk.Frame(idx_inner, bg=COLOR_CARD)
    idx_actions.pack(fill="x")
    create_btn(idx_actions, "👁️ Abrir en Visor", lambda: load_resource_in_viewer("_Gran_Indice_Sistemes_de_Mesura.md"), bg=COLOR_ACCENT_BLUE, hover_bg=COLOR_ACCENT_HOVER, font=FONT_HEAD).pack(side="left", padx=(0, 6))
    create_btn(idx_actions, "📝 Abrir en Editor", lambda: open_resource_in_editor("_Gran_Indice_Sistemes_de_Mesura.md"), bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_HEAD).pack(side="left", padx=(0, 6))
    create_btn(idx_actions, "📋 Copiar Contenido", lambda: copy_resource_to_clipboard("_Gran_Indice_Sistemes_de_Mesura.md", "Gran Índice"), bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_HEAD).pack(side="left")

    # CARD B: Glosario de Conceptos Clave
    card_glo = make_card(p3, "📚 Glosario Central de Conceptos Clave A-Z")
    card_glo.pack(fill="x", pady=(0, 8))
    glo_inner = tk.Frame(card_glo, bg=COLOR_CARD, padx=16, pady=8)
    glo_inner.pack(fill="x")

    tk.Label(
        glo_inner,
        text="Archivo: _Glosario_Conceptos_Clave.md\n"
             "Diccionario técnico ordenado alfabéticamente con más de 120 definiciones técnicas extraídas de las "
             "unidades teóricas (CMRR, Aliasing, Galgas extensométricas, Ruido Johnson, Termopares, etc.).",
        font=FONT_BODY, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD, justify="left"
    ).pack(anchor="w", pady=(0, 6))

    glo_actions = tk.Frame(glo_inner, bg=COLOR_CARD)
    glo_actions.pack(fill="x")
    create_btn(glo_actions, "👁️ Abrir en Visor", lambda: load_resource_in_viewer("_Glosario_Conceptos_Clave.md"), bg=COLOR_ACCENT_BLUE, hover_bg=COLOR_ACCENT_HOVER, font=FONT_HEAD).pack(side="left", padx=(0, 6))
    create_btn(glo_actions, "📝 Abrir en Editor", lambda: open_resource_in_editor("_Glosario_Conceptos_Clave.md"), bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_HEAD).pack(side="left", padx=(0, 6))
    create_btn(glo_actions, "📋 Copiar para NotebookLM", lambda: copy_resource_to_clipboard("_Glosario_Conceptos_Clave.md", "Glosario Central"), bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_HEAD).pack(side="left")

    # CARD C: Formulario Oficial de Examen
    card_form = make_card(p3, "📐 Formulario Oficial de Examen (Temas 1 al 10)")
    card_form.pack(fill="x", pady=(0, 8))
    form_inner = tk.Frame(card_form, bg=COLOR_CARD, padx=16, pady=8)
    form_inner.pack(fill="x")

    tk.Label(
        form_inner,
        text="Archivo: _Formulario_Oficial_Examen.md\n"
             "Guía compacta con las fórmulas fundamentales del curso (Sensibilidad, Wheatstone, INA, Ruido Johnson, "
             "Sallen-Key, SNR, ENOB, GUM) preparadas para repaso rápido y resolución en NotebookLM.",
        font=FONT_BODY, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD, justify="left"
    ).pack(anchor="w", pady=(0, 6))

    form_actions = tk.Frame(form_inner, bg=COLOR_CARD)
    form_actions.pack(fill="x")
    create_btn(form_actions, "👁️ Abrir en Visor", lambda: load_resource_in_viewer("_Formulario_Oficial_Examen.md"), bg=COLOR_ACCENT_BLUE, hover_bg=COLOR_ACCENT_HOVER, font=FONT_HEAD).pack(side="left", padx=(0, 6))
    create_btn(form_actions, "📝 Abrir en Editor", lambda: open_resource_in_editor("_Formulario_Oficial_Examen.md"), bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_HEAD).pack(side="left", padx=(0, 6))
    create_btn(form_actions, "📋 Copiar Formulario", lambda: copy_resource_to_clipboard("_Formulario_Oficial_Examen.md", "Formulario Oficial"), bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_HEAD).pack(side="left")

    # CARD D: Flashcards Anki (Nativo .apkg y .tsv)
    card_fl = make_card(p3, "🃏 Banco de 500 Flashcards de Examen (Anki .apkg / TSV)")
    card_fl.pack(fill="x", pady=(0, 8))
    fl_inner = tk.Frame(card_fl, bg=COLOR_CARD, padx=16, pady=8)
    fl_inner.pack(fill="x")

    tk.Label(
        fl_inner,
        text="Archivos: _Flashcards_Examen.apkg (1-Clic Anki con Dark Mode y MathJax) y _Flashcards_Examen.tsv\n"
             "500 tarjetas con las preguntas de autoevaluación y cuestionarios oficiales de Moodle. "
             "Formato interactivo con anverso (pregunta) y reverso (respuesta correcta + justificación física).",
        font=FONT_BODY, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD, justify="left"
    ).pack(anchor="w", pady=(0, 6))

    fl_actions = tk.Frame(fl_inner, bg=COLOR_CARD)
    fl_actions.pack(fill="x")
    create_btn(fl_actions, "📦 Importar en Anki (.apkg)", open_anki_package, bg=COLOR_ACCENT_BLUE, hover_bg=COLOR_ACCENT_HOVER, font=FONT_HEAD).pack(side="left", padx=(0, 6))
    create_btn(fl_actions, "📂 Abrir Carpeta", lambda: open_resource_folder("_Flashcards_Examen.apkg"), bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_HEAD).pack(side="left", padx=(0, 6))
    create_btn(fl_actions, "ℹ️ Guía Anki", show_anki_guide, bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_HEAD).pack(side="left", padx=(0, 6))
    create_btn(fl_actions, "📋 Copiar TSV", lambda: copy_resource_to_clipboard("_Flashcards_Examen.tsv", "Flashcards TSV"), bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_HEAD).pack(side="left")

    # CARD E: Simulador Oficial de Examen UPC
    card_sim = make_card(p3, "🎓 Simulador Oficial de Examen UPC (Test Runner)")
    card_sim.pack(fill="x", pady=(0, 8))
    sim_inner = tk.Frame(card_sim, bg=COLOR_CARD, padx=16, pady=8)
    sim_inner.pack(fill="x")

    tk.Label(
        sim_inner,
        text="Entorno interactivo para poner a prueba tus conocimientos antes del examen real:\n"
             "• Banco oficial con las 500 preguntas de autoevaluación de los 10 temas.\n"
             "• Criterio oficial de calificación UPC: +1.00 por acierto, -0.33 por fallo, 0.00 en blanco.\n"
             "• Corrección inmediata con desglose de la respuesta correcta y justificación técnica.",
        font=FONT_BODY, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD, justify="left"
    ).pack(anchor="w", pady=(0, 6))

    sim_actions = tk.Frame(sim_inner, bg=COLOR_CARD)
    sim_actions.pack(fill="x")
    create_btn(sim_actions, "⚡ Iniciar Simulador de Examen UPC", open_exam_simulator_modal, bg=COLOR_ACCENT_GREEN, hover_bg=COLOR_ACCENT_GREEN_HOVER, font=(FONT_FAMILY, 11, "bold"), padx=20, pady=7).pack(side="left")

    # CARD D: Suite NotebookLM & Prompts Avanzados
    card_nlm = make_card(p3, "🤖 Asistente de Estudio con NotebookLM")
    card_nlm.pack(fill="x", pady=(0, 8))
    nlm_inner = tk.Frame(card_nlm, bg=COLOR_CARD, padx=16, pady=8)
    nlm_inner.pack(fill="x")

    tk.Label(
        nlm_inner,
        text="Conecta estos archivos con Google NotebookLM para obtener un tutor interactivo con citas exactas:\n"
             "1. Sube a NotebookLM los archivos .md (o el Cuaderno Maestro unificado).\n"
             "2. Copia y pega los prompts predefinidos a continuación para iniciar tus sesiones de estudio.",
        font=FONT_BODY, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD, justify="left"
    ).pack(anchor="w", pady=(0, 6))

    nlm_actions = tk.Frame(nlm_inner, bg=COLOR_CARD)
    nlm_actions.pack(fill="x")

    def copy_tutor_prompt():
        pr = (
            "Actúa como un profesor universitario experto y riguroso de la asignatura 'Sistemes de Mesura' (UPC). "
            "Basándote estrictamente en los documentos cargados, explícame los conceptos clave, "
            "plantea preguntas desafiantes para comprobar mi entendimiento y corrígeme en base a las deducciones matemáticas."
        )
        root.clipboard_clear()
        root.clipboard_append(pr)
        lbl_res_status.config(text="✅ ¡Prompt de Tutor copiado al portapapeles!", fg=COLOR_ACCENT_CYAN)
        root.after(3000, update_resources_status)

    create_btn(nlm_actions, "🌐 Abrir Google NotebookLM", lambda: webbrowser.open("https://notebooklm.google.com/"), bg=COLOR_ACCENT_GREEN, hover_bg=COLOR_ACCENT_GREEN_HOVER, font=FONT_HEAD).pack(side="left", padx=(0, 6))
    create_btn(nlm_actions, "📋 Copiar Prompt de Tutor", copy_tutor_prompt, bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_HEAD).pack(side="left")

    root.after(100, update_resources_status)

    # ==================================================================
    # LÓGICA DE EJECUCIÓN DEL WORKER
    # ==================================================================
    def execute():
        nonlocal is_running
        if mode_var.get() == "all_course":
            execute_all_course()
            return
        src = in_var.get().strip()
        dst = out_var.get().strip()
        if not src or not dst:
            messagebox.showerror("Error", "Debes especificar las rutas de origen y destino.")
            return

        cancel_event.clear()
        is_running = True
        progress_bar["value"] = 0
        lbl_progress_text.config(text="")
        btn_exec.config(state="disabled")
        btn_cancel.config(state="normal")
        btn_open.pack_forget()
        btn_go_viewer.pack_forget()

        rw_links = rewrite_links_var.get()
        inc_meta = include_meta_var.get()
        inc_yaml = include_yaml_var.get()
        gen_toc = generate_toc_var.get()
        ext_b64 = extract_b64_var.get()
        inc_sheet = formula_sheet_var.get()
        do_master = master_doc_var.get()
        do_dash = dashboard_var.get()
        mode = mode_var.get()

        def worker():
            start_t = time.time()
            try:
                if mode == "single":
                    log(f"Convirtiendo archivo: {Path(src).name}", "info")
                    stats = convert_single_file(
                        src, dst,
                        rewrite_links=rw_links,
                        include_meta=inc_meta,
                        include_yaml=inc_yaml,
                        generate_toc=gen_toc,
                        include_formula_sheet=inc_sheet,
                        extract_b64=ext_b64
                    )
                    elapsed = time.time() - start_t
                    progress_bar["value"] = 100
                    lbl_progress_text.config(text="100% completado")
                    log(f"¡Éxito! Generado en {elapsed:.2f}s [{stats.get('encoding')}]: {dst}", "success")
                    log(f"Métricas: {stats['math']} fórmulas, {stats['tables']} tablas, {stats['diagrams']} diagramas.", "info")

                    root.after(0, lambda: refresh_viewer_list())
                    root.after(0, lambda: btn_open.pack(side="right", padx=(6, 0)))
                    root.after(0, lambda: btn_go_viewer.pack(side="right", padx=(6, 0)))
                    root.after(0, lambda: messagebox.showinfo(
                        "Completado",
                        f"Archivo generado con éxito en:\n{dst}\n\n"
                        f"Fórmulas: {stats['math']} | Tablas: {stats['tables']}\n\n"
                        f"Puedes previsualizarlo, buscar términos o copiarlo en la pestaña 'Visor Markdown'."
                    ))
                else:
                    log(f"Iniciando escaneo de lote en: {src}...", "info")

                    def on_progress(curr, total, fname, file_stats):
                        pct = (curr / total) * 100
                        progress_bar["value"] = pct
                        lbl_progress_text.config(text=f"[{curr}/{total}] {fname}")
                        log(f"[{curr}/{total}] {fname} -> {file_stats['math']} fórmulas, {file_stats['tables']} tablas", "success")

                    total, stats, gen_files = process_batch(
                        src, dst,
                        progress_callback=on_progress,
                        rewrite_links=rw_links,
                        include_meta=inc_meta,
                        include_yaml=inc_yaml,
                        generate_toc=gen_toc,
                        include_formula_sheet=inc_sheet,
                        create_master_doc=do_master,
                        create_dashboard=do_dash,
                        extract_b64=ext_b64,
                        cancel_event=cancel_event
                    )

                    elapsed = time.time() - start_t
                    if cancel_event.is_set():
                        log(f"Proceso cancelado. Se convirtieron {total} archivos.", "warn")
                        root.after(0, lambda: messagebox.showwarning("Cancelado", f"Conversión detenida.\nSe procesaron {total} archivos."))
                    elif total == 0:
                        log("No se encontraron archivos HTML en la carpeta seleccionada.", "warn")
                        root.after(0, lambda: messagebox.showwarning("Sin archivos", "No se encontraron archivos .html o .htm."))
                    else:
                        log(f"¡Lote finalizado en {elapsed:.2f}s! {total} archivos convertidos.", "success")
                        if "master_document" in stats:
                            log(f"📚 Cuaderno Maestro generado: {stats['master_document']}", "success")
                        if "dashboard" in stats:
                            log(f"📊 Reporte Analítico generado: {stats['dashboard']}", "success")
                        log(f"Total global: {stats['math']} fórmulas LaTeX, {stats['tables']} tablas GFM, {stats['diagrams']} diagramas.", "info")
                        log("💡 Puedes previsualizar, buscar con Ctrl+F y copiar cualquier documento con 1 clic en la pestaña 'Visor Markdown'.", "info")

                        root.after(0, lambda: refresh_viewer_list())
                        root.after(0, lambda: btn_open.pack(side="right", padx=(6, 0)))
                        root.after(0, lambda: btn_go_viewer.pack(side="right", padx=(6, 0)))

                        msg_extra = ""
                        if "master_document" in stats:
                            msg_extra += f"\n📚 Cuaderno Maestro: {stats['master_document']}"
                        if "dashboard" in stats:
                            msg_extra += f"\n📊 Reporte Analítico: {stats['dashboard']}"

                        root.after(0, lambda: messagebox.showinfo(
                            "Proceso Completado",
                            f"¡Lote finalizado con éxito en {elapsed:.2f}s!\n\n"
                            f"Archivos convertidos: {total}\n"
                            f"Fórmulas LaTeX: {stats['math']}\n"
                            f"Tablas GFM 2D: {stats['tables']}\n"
                            f"Diagramas preservados: {stats['diagrams']}"
                            f"{msg_extra}\n\n"
                            f"¡Listo para usar en NotebookLM, Obsidian o LLMs!"
                        ))
            except Exception as e:
                log(f"ERROR: {str(e)}", "error")
                root.after(0, lambda: messagebox.showerror("Error Inesperado", f"Ocurrió un error:\n{str(e)}"))
            finally:
                btn_exec.config(state="normal")
                btn_cancel.config(state="disabled")

        threading.Thread(target=worker, daemon=True).start()

    def execute_all_course():
        nonlocal is_running
        src = in_var.get().strip()
        dst = out_var.get().strip()

        if not src or not dst:
            messagebox.showerror("Error", "Debes especificar la carpeta raíz del curso (que contiene los temas) y la carpeta de destino.")
            return

        cancel_event.clear()
        is_running = True
        progress_bar["value"] = 0
        lbl_progress_text.config(text="")
        btn_exec.config(state="disabled")
        btn_all_course.config(state="disabled")
        btn_cancel.config(state="normal")
        btn_open.pack_forget()
        btn_go_viewer.pack_forget()

        rw_links = rewrite_links_var.get()
        inc_meta = include_meta_var.get()
        inc_yaml = include_yaml_var.get()
        gen_toc = generate_toc_var.get()
        ext_b64 = extract_b64_var.get()
        inc_sheet = formula_sheet_var.get()
        do_master = master_doc_var.get()
        do_dash = dashboard_var.get()

        def course_worker():
            start_t = time.time()
            try:
                log("🚀 Iniciando conversión integral de todos los temas del curso...", "info")

                def on_course_prog(step_text, fname, curr_t, total_t):
                    pct = ((curr_t) / total_t) * 100
                    progress_bar["value"] = pct
                    lbl_progress_text.config(text=f"{step_text} {fname}")
                    log(f"{step_text} {fname}", "info")

                total, stats, gen_files = process_all_course_temas(
                    src, dst,
                    progress_callback=on_course_prog,
                    rewrite_links=rw_links,
                    include_meta=inc_meta,
                    include_yaml=inc_yaml,
                    generate_toc=gen_toc,
                    include_formula_sheet=inc_sheet,
                    create_master_doc=do_master,
                    create_dashboard=do_dash,
                    extract_b64=ext_b64,
                    cancel_event=cancel_event
                )

                elapsed = time.time() - start_t
                progress_bar["value"] = 100
                lbl_progress_text.config(text="100% Curso completado")

                if cancel_event.is_set():
                    log("Conversión del curso cancelada por el usuario.", "warn")
                else:
                    log(f"¡CURSO COMPLETO FINALIZADO en {elapsed:.2f}s!", "success")
                    log(f"Total: {total} archivos convertidos en {stats['topics_count']} temas.", "success")
                    log(f"📐 Fórmulas LaTeX: {stats['math']} | 📋 Tablas: {stats['tables']} | 🧠 Preguntas Examen: {stats['quiz_questions']}", "success")
                    if "grand_index" in stats:
                        log(f"🎓 Gran Índice General: {stats['grand_index']}", "success")

                    root.after(0, lambda: refresh_viewer_list())
                    root.after(0, lambda: btn_open.pack(side="right", padx=(6, 0)))
                    root.after(0, lambda: btn_go_viewer.pack(side="right", padx=(6, 0)))

                    root.after(0, lambda: messagebox.showinfo(
                        "Curso Completo Convertido",
                        f"¡Todos los temas ({stats['topics_count']} temas, {total} archivos) convertidos con éxito en {elapsed:.2f}s!\n\n"
                        f"• Fórmulas Matemáticas: {stats['math']:,}\n"
                        f"• Preguntas y Soluciones de Examen: {stats['quiz_questions']}\n"
                        f"• Palabras Totales: {stats['total_words']:,}\n"
                        f"• Gran Índice Generado: {stats.get('grand_index', '')}\n\n"
                        f"¡Listo para importar directamente a NotebookLM u Obsidian!"
                    ))
            except Exception as e:
                log(f"ERROR EN CURSO: {str(e)}", "error")
                root.after(0, lambda: messagebox.showerror("Error", f"Error durante la conversión del curso:\n{str(e)}"))
            finally:
                btn_exec.config(state="normal")
                btn_all_course.config(state="normal")
                btn_cancel.config(state="disabled")

        threading.Thread(target=course_worker, daemon=True).start()

    btn_exec = create_btn(
        btn_frame, "⚡ Convertir Lote", execute,
        bg=COLOR_ACCENT_BLUE, hover_bg=COLOR_ACCENT_HOVER, fg="white", font=FONT_HEAD, padx=20, pady=8
    )
    btn_exec.pack(side="left", fill="x", expand=True)

    btn_all_course = create_btn(
        btn_frame, "🎓 Convertir Todo el Curso (10 Temas)", execute_all_course,
        bg=COLOR_ACCENT_GREEN, hover_bg=COLOR_ACCENT_GREEN_HOVER, fg="white", font=FONT_HEAD, padx=18, pady=8
    )
    btn_all_course.pack(side="left", padx=(8, 0))

    btn_cancel.pack(side="left", padx=(8, 0))

    # Atajos de teclado globales (Spotlight Ctrl+K)
    root.bind_all("<Control-k>", lambda e: open_spotlight_modal())
    root.bind_all("<Control-K>", lambda e: open_spotlight_modal())

    # Drag and Drop nativo de Windows
    def on_files_dropped(paths):
        if not paths:
            return
        p = Path(paths[0])
        if p.is_dir():
            in_var.set(str(p))
            if any((p / f"Tema {i}").exists() or (p / f"Tema_{i:02d}").exists() or (p / f"Tema_{i}").exists() for i in range(1, 11)):
                mode_var.set("course")
                out_var.set("dist_course_md")
                log(f"📥 Drag & Drop: Carpeta de curso detectada '{p.name}'. Modo 'Curso Completo' fijado.", "info")
            else:
                mode_var.set("batch")
                out_var.set("dist_md")
                log(f"📥 Drag & Drop: Carpeta detectada '{p.name}'. Modo 'Lote' fijado.", "info")
            update_mode_ui()
        elif p.is_file():
            if p.suffix.lower() in [".html", ".htm"]:
                mode_var.set("single")
                in_var.set(str(p))
                out_var.set(str(p.parent / f"{p.stem}.md"))
                update_mode_ui()
                log(f"📥 Drag & Drop: Archivo HTML detectado '{p.name}'. Modo 'Archivo Único' fijado.", "info")
            else:
                log(f"⚠️ El archivo arrastrado no es HTML ({p.name})", "warn")

    root.after(250, lambda: setup_windows_drag_and_drop(root, on_files_dropped))

    root.mainloop()


# ----------------------------------------------------------------------
# 9. PUNTO DE ENTRADA CLI CON SOPORTE COMPLETO DE FLAGS Y PRESETS
# ----------------------------------------------------------------------

def print_help():
    print("""
Uso: conversor_html_notebooklm.exe <origen> <destino> [opciones]
     conversor_html_notebooklm.exe --all-temas <carpeta_curso> <carpeta_destino> [opciones]

Argumentos:
  origen                  Ruta a un archivo HTML o a una carpeta con archivos HTML.
  destino                 Ruta al archivo Markdown resultante (.md) o a la carpeta destino.
  -i, --input <ruta>      Ruta de entrada alternativa por parámetro con nombre.
  -o, --output <ruta>     Ruta de destino alternativa por parámetro con nombre.

Opciones y Modos:
  --all-temas             Procesa secuencialmente todos los temas (Tema 1..Tema 10),
                          generando los Cuadernos Maestros y el Gran Índice General del curso.
  --preset <nombre>       Aplica un perfil preconfigurado:
                            - notebooklm: Enlaces, TOC, Metadatos, Formulario, Cuaderno Maestro y Reporte.
                            - obsidian:   Enlaces, TOC, Metadatos, YAML Frontmatter, Formulario y Reporte.
                            - github:     Enlaces, TOC, Metadatos estándar.
  --merge                 Genera un Cuaderno Maestro unificado (_Cuaderno_Maestro.md) en lotes.
  --dashboard             Genera un Reporte Analítico del lote (_Reporte_Analitico.md).
  --no-dashboard          Desactiva la generación del reporte analítico.
  --formula-sheet         Genera una tabla resumen de ecuaciones al final de cada documento.
  --no-formula-sheet      Desactiva la generación del formulario resumen.
  --yaml                  Inserta cabecera YAML Frontmatter al inicio de los documentos.
  --no-rewrite-links      No reescribe los enlaces locales (.html -> .md).
  --no-meta               No incluye la tarjeta de metadatos (Autor, Fecha, Fuente).
  --no-toc                No genera el índice de contenidos (TOC).
  --no-extract-b64        No extrae las imágenes Base64 a archivos físicos en assets/.
  -h, --help              Muestra este mensaje de ayuda.
""")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        run_gui()
    elif "-h" in sys.argv or "--help" in sys.argv:
        print_help()
    else:
        args = sys.argv[1:]
        src = None
        dst = None

        if "-i" in args:
            src = args[args.index("-i") + 1]
        elif "--input" in args:
            src = args[args.index("--input") + 1]

        if "-o" in args:
            dst = args[args.index("-o") + 1]
        elif "--output" in args:
            dst = args[args.index("--output") + 1]

        if not src or not dst:
            positionals = []
            skip = False
            for idx, a in enumerate(args):
                if skip:
                    skip = False
                    continue
                if a in ["-i", "--input", "-o", "--output", "--preset"]:
                    skip = True
                    continue
                if not a.startswith("-"):
                    positionals.append(a)
            if len(positionals) >= 2:
                src = positionals[0]
                dst = positionals[1]
            elif len(positionals) == 1 and not src:
                src = positionals[0]

        if not src or not dst:
            print_help()
            sys.exit(1)

        # Configuración base por defecto (NotebookLM)
        rw_links = True
        inc_meta = True
        inc_yaml = False
        gen_toc = True
        ext_b64 = True
        inc_sheet = True
        do_master = True
        do_dash = True
        is_all_course = "--all-temas" in args

        # Soporte para presets
        if "--preset" in args:
            idx = args.index("--preset")
            if idx + 1 < len(args):
                preset_arg = args[idx + 1].lower()
                if preset_arg == "notebooklm":
                    rw_links, inc_meta, inc_yaml, gen_toc, ext_b64, inc_sheet, do_master, do_dash = True, True, False, True, True, True, True, True
                elif preset_arg == "obsidian":
                    rw_links, inc_meta, inc_yaml, gen_toc, ext_b64, inc_sheet, do_master, do_dash = True, True, True, True, True, True, False, True
                elif preset_arg == "github":
                    rw_links, inc_meta, inc_yaml, gen_toc, ext_b64, inc_sheet, do_master, do_dash = True, True, False, True, True, False, False, False

        # Sobrescrituras individuales por flags explícitas
        if "--no-rewrite-links" in args: rw_links = False
        if "--no-meta" in args: inc_meta = False
        if "--yaml" in args: inc_yaml = True
        if "--no-toc" in args: gen_toc = False
        if "--no-extract-b64" in args: ext_b64 = False
        if "--formula-sheet" in args: inc_sheet = True
        if "--no-formula-sheet" in args: inc_sheet = False
        if "--merge" in args: do_master = True
        if "--dashboard" in args: do_dash = True
        if "--no-dashboard" in args: do_dash = False

        if is_all_course:
            print(f"🎓 Iniciando conversión completa del curso desde: {src} ...")
            total, stats, gen_files = process_all_course_temas(
                src, dst,
                rewrite_links=rw_links,
                include_meta=inc_meta,
                include_yaml=inc_yaml,
                generate_toc=gen_toc,
                include_formula_sheet=inc_sheet,
                create_master_doc=do_master,
                create_dashboard=do_dash,
                extract_b64=ext_b64
            )
            print(f"¡Curso completo finalizado! {total} archivos convertidos en {stats['topics_count']} temas.")
            print(f"Fórmulas LaTeX totales: {stats['math']:,}")
            print(f"Preguntas de examen con solución: {stats['quiz_questions']:,}")
            if "grand_index" in stats:
                print(f"Gran Índice General: {stats['grand_index']}")
            if "glossary" in stats:
                print(f"Glosario Central A-Z: {stats['glossary']}")
            if "flashcards" in stats:
                print(f"Flashcards Anki TSV: {stats['flashcards']}")
        elif os.path.isfile(src):
            stats = convert_single_file(
                src, dst,
                rewrite_links=rw_links,
                include_meta=inc_meta,
                include_yaml=inc_yaml,
                generate_toc=gen_toc,
                include_formula_sheet=inc_sheet,
                extract_b64=ext_b64
            )
            print(f"Archivo convertido exitosamente: {dst}")
            print(f"Métricas: {stats.get('math', 0)} fórmulas, {stats.get('tables', 0)} tablas, {stats.get('diagrams', 0)} diagramas.")
        else:
            total, stats, gen_files = process_batch(
                src, dst,
                rewrite_links=rw_links,
                include_meta=inc_meta,
                include_yaml=inc_yaml,
                generate_toc=gen_toc,
                include_formula_sheet=inc_sheet,
                create_master_doc=do_master,
                create_dashboard=do_dash,
                extract_b64=ext_b64
            )
            print(f"Lote finalizado: {total} archivos convertidos.")
            if "master_document" in stats:
                print(f"Cuaderno Maestro generado: {stats['master_document']}")
            if "dashboard" in stats:
                print(f"Reporte Analítico generado: {stats['dashboard']}")
            print(f"Métricas globales: {stats.get('math', 0)} fórmulas, {stats.get('tables', 0)} tablas, {stats.get('diagrams', 0)} diagramas, {stats.get('quiz_questions', 0)} preguntas examen.")
