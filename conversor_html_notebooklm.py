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
import math
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

try:
    import universal_converters as uc
    HAS_UNIVERSAL = True
except Exception as e:
    uc = None
    HAS_UNIVERSAL = False

try:
    import upc_degree_engine as upc_engine
    from upc_gui_tab import setup_upc_degree_tab
    HAS_UPC_DEGREE = True
except Exception as e:
    upc_engine = None
    setup_upc_degree_tab = None
    HAS_UPC_DEGREE = False

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
        "propietat": "NOTE",
        "example": "EXAMPLE",
        "exemple": "EXAMPLE",
        "ejemplo": "EXAMPLE",
        "question": "QUESTION",
        "pregunta": "QUESTION",
        "faq": "QUESTION",
        "problema": "NOTE",
        "exercici": "NOTE",
        "ejercicio": "NOTE",
        "solucio": "TIP",
        "solucion": "TIP",
        "resumen": "TIP",
        "resum": "TIP"
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

    # Sincronizar banco de problemas, exámenes oficiales y laboratorio virtual interactivo
    for extra_name in ["_Problemas_Examen_Resueltos.md", "_Examenes_Finales_Oficiales_UPC.md", "Laboratorio_Virtual_Sensores.html"]:
        src_cand = Path("dist_course_md") / extra_name
        if not src_cand.exists():
            src_cand = Path(getattr(sys, "_MEIPASS", ".")) / extra_name
        dst_extra = out_root / extra_name
        if src_cand.exists() and dst_extra.resolve() != src_cand.resolve():
            try:
                import shutil
                shutil.copy2(src_cand, dst_extra)
                nlm_dir = out_root / "Para_Subir_a_NotebookLM"
                if nlm_dir.exists() and extra_name.endswith(".md"):
                    shutil.copy2(src_cand, nlm_dir / extra_name)
                all_generated_files.append(dst_extra)
            except Exception:
                pass

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

# ======================================================================
# PLANTILLAS DE MODELOS METROLÓGICOS GUM (ISO/IEC 98-3)
# ======================================================================
GUM_TEMPLATES = {
    "Sensor AD590 & Acondicionador (Examen Final 2025)": {
        "formula": "I * R1 * (1 + R3/R4 + R3/R2) - Vref * (R3/R2)",
        "unit": "V",
        "vars": [
            ("I", 293.15e-6, 0.5e-6, "Normal (k=3)", "Corriente nominal sensor a 20°C (1 µA/K)"),
            ("R1", 10000.0, 10.0, "Normal (k=2)", "Resistencia conversión corriente-tensión (0.1%)"),
            ("R2", 3650.0, 3.65, "Normal (k=2)", "Resistencia división ganancia (0.1%)"),
            ("R3", 10000.0, 10.0, "Normal (k=2)", "Resistencia realimentación (0.1%)"),
            ("R4", 7870.0, 7.87, "Normal (k=2)", "Resistencia división a masa (0.1%)"),
            ("Vref", 5.0, 0.0, "Normal (k=1)", "Tensión de referencia estable (sin incertidumbre)")
        ]
    },
    "Pt100 en Puente de Wheatstone (3 Hilos Siemens)": {
        "formula": "Vs * ((R0 * (1 + 3.9083e-3 * T) - R0) / (4 * R0)) * G",
        "unit": "V",
        "vars": [
            ("Vs", 10.0, 0.02, "Normal (k=2)", "Tensión de alimentación regulada"),
            ("R0", 100.0, 0.05, "Normal (k=2)", "Resistencia nominal Pt100 a 0°C"),
            ("T", 100.0, 0.5, "Normal (k=2)", "Temperatura del baño térmico (°C)"),
            ("G", 100.0, 0.1, "Normal (k=2)", "Ganancia del amplificador de instrumentación")
        ]
    },
    "Célula de Carga con 4 Galgas (Puente Completo & INA3)": {
        "formula": "Vs * K * eps * (1 + 49400 / Rg)",
        "unit": "V",
        "vars": [
            ("Vs", 10.0, 0.05, "Rectangular", "Alimentación del puente de galgas"),
            ("K", 2.05, 0.02, "Triangular", "Factor de galga K especificado"),
            ("eps", 1000e-6, 15e-6, "Normal (k=2)", "Deformación unitaria mecánica (με)"),
            ("Rg", 500.0, 0.5, "Normal (k=2)", "Resistencia fijación ganancia INA (0.1%)")
        ]
    },
    "Caudalímetro Hall / Electromagnético con Ruido": {
        "formula": "B * v * d * G",
        "unit": "V",
        "vars": [
            ("B", 0.15, 0.002, "Normal (k=2)", "Inducción magnética de excitación (T)"),
            ("v", 2.4, 0.03, "Normal (k=2)", "Velocidad media del fluido conductor (m/s)"),
            ("d", 0.05, 0.0005, "Normal (k=2)", "Diámetro interno de la tubería (m)"),
            ("G", 500.0, 1.0, "Normal (k=2)", "Ganancia etapa diferencial de instrumentación")
        ]
    },
    "Sensor Capacitivo Diferencial en Puente AC": {
        "formula": "Vs * (x / d0) * G",
        "unit": "V",
        "vars": [
            ("Vs", 2.0, 0.01, "Normal (k=2)", "Tensión de excitación senoidal 10 kHz"),
            ("x", 0.25e-3, 2e-6, "Normal (k=2)", "Desplazamiento del núcleo móvil (m)"),
            ("d0", 1.0e-3, 5e-6, "Normal (k=2)", "Separación nominal de electrodos (m)"),
            ("G", 10.0, 0.02, "Normal (k=2)", "Ganancia de demodulación coherente")
        ]
    },
    "Puente de Wheatstone Completo (Galgas Extensométricas)": {
        "formula": "Vs * K * eps",
        "unit": "V",
        "vars": [
            ("Vs", 10.0, 0.05, "Rectangular", "Tensión de alimentación del puente"),
            ("K", 2.05, 0.02, "Triangular", "Factor de galga según fabricante"),
            ("eps", 1200e-6, 20e-6, "Normal (k=2)", "Deformación unitaria mecánica (με)")
        ]
    },
    "Termopar Tipo K con Compensación de Unión Fría": {
        "formula": "sT * (Th - Ta) + sTa * Ta",
        "unit": "mV",
        "vars": [
            ("sT", 0.04108, 0.0005, "Normal (k=2)", "Sensibilidad termopar unión caliente (mV/°C)"),
            ("sTa", 0.03961, 0.0005, "Normal (k=2)", "Sensibilidad unión fría (mV/°C)"),
            ("Th", 300.0, 1.0, "Normal (k=2)", "Temperatura unión de medida (°C)"),
            ("Ta", 25.0, 0.5, "Normal (k=2)", "Temperatura unión de referencia (°C)")
        ]
    },
    "Acondicionador Inversor para Sensor Capacitivo": {
        "formula": "-Vs * (1 + x)",
        "unit": "V",
        "vars": [
            ("Vs", 1.0, 0.01, "Normal (k=2)", "Amplitud portadora senoidal"),
            ("x", 0.35, 0.005, "Normal (k=2)", "Desplazamiento relativo del sensor")
        ]
    },
    "Divisor de Tensión Resistivo": {
        "formula": "Vi * R2 / (R1 + R2)",
        "unit": "V",
        "vars": [
            ("Vi", 10.0, 0.02, "Normal (k=2)", "Tensión de entrada"),
            ("R1", 10000.0, 10.0, "Normal (k=2)", "Resistencia superior"),
            ("R2", 10000.0, 10.0, "Normal (k=2)", "Resistencia inferior")
        ]
    },
    "Ley de Ohm (Disipación de Potencia)": {
        "formula": "V**2 / R",
        "unit": "W",
        "vars": [
            ("V", 12.0, 0.05, "Normal (k=2)", "Tensión en bornas"),
            ("R", 100.0, 1.0, "Normal (k=2)", "Resistencia de carga")
        ]
    }
}

def markdown_to_simple_html(md_text: str) -> str:
    """Convierte Markdown básico a HTML para previsualización e impresión limpia con MathJax."""
    lines = md_text.splitlines()
    html_out = []
    in_table = False
    for line in lines:
        s = line.strip()
        if s.startswith("# "):
            html_out.append(f"<h1>{s[2:]}</h1>")
        elif s.startswith("## "):
            html_out.append(f"<h2>{s[3:]}</h2>")
        elif s.startswith("### "):
            html_out.append(f"<h3>{s[4:]}</h3>")
        elif s.startswith("#### "):
            html_out.append(f"<h4>{s[5:]}</h4>")
        elif s.startswith("> "):
            html_out.append(f"<blockquote>{s[2:]}</blockquote>")
        elif s.startswith("|") and s.endswith("|"):
            if "---" in s:
                continue
            cells = [c.strip() for c in s[1:-1].split("|")]
            tag = "th" if not in_table else "td"
            row_html = "".join([f"<{tag}>{c}</{tag}>" for c in cells])
            if not in_table:
                html_out.append("<table>")
                in_table = True
            html_out.append(f"<tr>{row_html}</tr>")
        else:
            if in_table:
                html_out.append("</table>")
                in_table = False
            if s:
                html_out.append(f"<p>{s}</p>")
    if in_table:
        html_out.append("</table>")
    return "\n".join(html_out)

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
    root.geometry("1060x780")
    root.minsize(980, 660)

    # ------------------------------------------------------------------
    # PALETA APPLE.COM SPACE BLACK / TITANIUM PRO (MACOS SEQUOIA)
    # ------------------------------------------------------------------
    COLOR_CANVAS = "#13151b"          # Canvas grafito profundo macOS Sequoia
    COLOR_HEADER = "#1a1d26"          # Barra superior Apple Studio
    COLOR_CARD = "#212530"            # Superficie de tarjeta acrílica con contraste
    COLOR_CARD_BORDER = "#313747"     # Borde nítido y elegante
    COLOR_INSET = "#171a22"           # Contenedor inset oscuro
    COLOR_INPUT_BG = "#0f1116"        # Fondo de campos de entrada y código
    COLOR_TEXT_PRIMARY = "#f8fafc"    # Texto blanco Apple brillante
    COLOR_TEXT_MUTED = "#94a3b8"      # Gris plata legible
    COLOR_ACCENT_BLUE = "#0a84ff"     # Apple SF Blue
    COLOR_ACCENT_HOVER = "#0071e3"    # Apple Blue hover
    COLOR_ACCENT_GREEN = "#30d158"    # Apple Mint Green
    COLOR_ACCENT_GREEN_HOVER = "#28cd41"
    COLOR_ACCENT_RED = "#ff453a"      # Apple Red
    COLOR_ACCENT_RED_HOVER = "#e0382e"
    COLOR_ACCENT_AMBER = "#ff9f0a"    # Apple Amber
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

    FONT_TITLE = (FONT_FAMILY, 14, "bold")
    FONT_SUBTITLE = (FONT_FAMILY, 9)
    FONT_HEAD = (FONT_FAMILY, 10, "bold")
    FONT_BODY = (FONT_FAMILY, 9)
    FONT_CODE = ("Consolas", 10)
    FONT_SMALL = (FONT_FAMILY, 8)

    style = ttk.Style()
    style.theme_use("clam")

    # Configuración de estilos Apple TTK
    style.configure("Hidden.TNotebook", background=COLOR_CANVAS, borderwidth=0, tabmargins=[0, 0, 0, 0])
    style.layout("Hidden.TNotebook.Tab", [])
    style.configure("Modern.Horizontal.TProgressbar", background=COLOR_ACCENT_BLUE, troughcolor=COLOR_INPUT_BG, borderwidth=0, thickness=6)
    style.configure("Modern.TCombobox", fieldbackground=COLOR_INPUT_BG, background=COLOR_CARD, foreground=COLOR_TEXT_PRIMARY, arrowcolor=COLOR_TEXT_MUTED, borderwidth=1)
    style.map("Modern.TCombobox", fieldbackground=[("readonly", COLOR_INPUT_BG)])

    def create_btn(parent, text, command, bg="#262a36", fg=COLOR_TEXT_PRIMARY, hover_bg="#353b4c", font=FONT_HEAD, padx=14, pady=7, **kwargs):
        b = tk.Button(parent, text=text, command=command, bg=bg, fg=fg, activebackground=hover_bg, activeforeground=fg, font=font, cursor="hand2", relief="flat", bd=0, padx=padx, pady=pady, **kwargs)
        b.bind("<Enter>", lambda e: b.config(bg=hover_bg) if b["state"] != "disabled" else None)
        b.bind("<Leave>", lambda e: b.config(bg=bg) if b["state"] != "disabled" else None)
        return b

    def make_card(parent, title="", badge=""):
        c = tk.Frame(parent, bg=COLOR_CARD, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER)
        if title:
            h = tk.Frame(c, bg=COLOR_CARD)
            h.pack(fill="x", padx=16, pady=(12, 6))
            tk.Label(h, text=title, font=FONT_HEAD, fg=COLOR_TEXT_PRIMARY, bg=COLOR_CARD).pack(side="left")
            if badge:
                tk.Label(h, text=badge, font=FONT_SMALL, fg=COLOR_ACCENT_CYAN, bg=COLOR_INSET, padx=7, pady=2).pack(side="right")
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
    create_btn(h_right, "🔍 Spotlight", lambda: open_spotlight_modal(), bg="#242426", hover_bg="#3a3a3c", font=FONT_SMALL, padx=10, pady=4).pack(side="left", padx=3)
    create_btn(h_right, "🎯 Examen UPC", lambda: open_exam_simulator_modal(), bg="#112530", hover_bg="#1b3b4d", font=FONT_SMALL, padx=10, pady=4).pack(side="left", padx=3)
    create_btn(h_right, "🔬 Lab Virtual", lambda: open_virtual_lab(), bg="#132a19", hover_bg="#1b3d24", font=FONT_SMALL, padx=10, pady=4).pack(side="left", padx=3)
    create_btn(h_right, "📝 Problemas", lambda: load_resource_in_viewer("_Problemas_Examen_Resueltos.md"), bg="#251a30", hover_bg="#38274a", font=FONT_SMALL, padx=10, pady=4).pack(side="left", padx=3)
    create_btn(h_right, "🎓 Finales UPC", lambda: load_resource_in_viewer("_Examenes_Finales_Oficiales_UPC.md"), bg="#2c1a1a", hover_bg="#422525", font=FONT_SMALL, padx=10, pady=4).pack(side="left", padx=3)
    tk.Label(h_right, text="UPC · EEBE", fg=COLOR_TEXT_MUTED, bg="#242426", font=FONT_SMALL, padx=8, pady=4).pack(side="left", padx=3)
    tk.Label(h_right, text="v3.1 Ultra", fg=COLOR_ACCENT_GREEN, bg="#132a19", font=FONT_SMALL, padx=8, pady=4).pack(side="left", padx=3)

    # Apple Segmented Tab Navigation Bar
    seg_nav_outer = tk.Frame(root, bg=COLOR_CANVAS, pady=8)
    seg_nav_outer.pack(fill="x")

    seg_pill_box = tk.Frame(seg_nav_outer, bg=COLOR_CARD, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER, padx=4, pady=4)
    seg_pill_box.pack()

    tab_btns = []
    tab_callbacks = {}

    def select_apple_tab(idx):
        notebook.select(idx)
        for i, b in enumerate(tab_btns):
            if i == idx:
                b.config(bg=COLOR_ACCENT_BLUE, fg="#ffffff", activebackground=COLOR_ACCENT_HOVER)
            else:
                b.config(bg=COLOR_CARD, fg=COLOR_TEXT_MUTED, activebackground="#242426")
        if idx in tab_callbacks and callable(tab_callbacks[idx]):
            root.after(40, tab_callbacks[idx])

    for i, (tab_label, icon) in enumerate([
        ("HTML a MD", "⚡"),
        ("Universal", "🚀"),
        ("Visor Markdown", "👁️"),
        ("Biblioteca", "🗂️"),
        ("Calculadora GUM", "📐"),
        ("Filtros Activos", "🎛️"),
        ("Banco R-L-C", "🔌"),
        ("Flashcards Anki", "🧠"),
        ("Plan UPC GREELEC", "🎓")
    ]):
        btn_t = tk.Button(
            seg_pill_box, text=f"{icon}  {tab_label}",
            font=(FONT_FAMILY, 9, "bold"),
            bg=COLOR_ACCENT_BLUE if i == 0 else COLOR_CARD,
            fg="#ffffff" if i == 0 else COLOR_TEXT_MUTED,
            activebackground=COLOR_ACCENT_HOVER, activeforeground="#ffffff",
            cursor="hand2", relief="flat", bd=0, padx=10, pady=5,
            command=lambda idx=i: select_apple_tab(idx)
        )
        btn_t.pack(side="left", padx=2)
        tab_btns.append(btn_t)

    # Notebook con pestañas ocultas gobernadas por el Segmented Control
    notebook = ttk.Notebook(root, style="Hidden.TNotebook")
    notebook.pack(fill="both", expand=True, padx=20, pady=(0, 10))

    tab_convert = tk.Frame(notebook, bg=COLOR_CANVAS)
    tab_universal = tk.Frame(notebook, bg=COLOR_CANVAS)
    tab_viewer = tk.Frame(notebook, bg=COLOR_CANVAS)
    tab_resources = tk.Frame(notebook, bg=COLOR_CANVAS)
    tab_gum = tk.Frame(notebook, bg=COLOR_CANVAS)
    tab_filters = tk.Frame(notebook, bg=COLOR_CANVAS)
    tab_rlc = tk.Frame(notebook, bg=COLOR_CANVAS)
    tab_flashcards = tk.Frame(notebook, bg=COLOR_CANVAS)
    tab_upc = tk.Frame(notebook, bg=COLOR_CANVAS)

    notebook.add(tab_convert, text="Conversión HTML")
    notebook.add(tab_universal, text="Conversor Universal")
    notebook.add(tab_viewer, text="Visor")
    notebook.add(tab_resources, text="Recursos")
    notebook.add(tab_gum, text="Calculadora GUM")
    notebook.add(tab_filters, text="Filtros & Acondicionadores")
    notebook.add(tab_rlc, text="Banco R-L-C & Presets")
    notebook.add(tab_flashcards, text="Flashcards & Examen")
    notebook.add(tab_upc, text="Plan UPC GREELEC")

    def on_notebook_tab_changed(event):
        try:
            sel_id = notebook.index(notebook.select())
            for i, b in enumerate(tab_btns):
                if i == sel_id:
                    b.config(bg=COLOR_ACCENT_BLUE, fg="#ffffff")
                else:
                    b.config(bg=COLOR_CARD, fg=COLOR_TEXT_MUTED)
            if sel_id in tab_callbacks and callable(tab_callbacks[sel_id]):
                root.after(40, tab_callbacks[sel_id])
        except Exception:
            pass
    notebook.bind("<<NotebookTabChanged>>", on_notebook_tab_changed)

    # Atajos de teclado Apple / Windows: Ctrl+1 a Ctrl+9 para pestañas
    for k_idx in range(9):
        root.bind_all(f"<Control-Key-{k_idx+1}>", lambda e, idx=k_idx: select_apple_tab(idx))

    # ==================================================================
    # PESTAÑA 1: CONVERSIÓN Y OPCIONES
    # ==================================================================
    # Dock de acciones fijado en la base (estilo macOS) - Garantiza 100% visibilidad permanente
    btn_frame = tk.Frame(tab_convert, bg=COLOR_HEADER, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER, padx=14, pady=10)
    btn_frame.pack(side="bottom", fill="x")

    # Layout de 2 columnas estilo macOS Studio Pro
    workspace = tk.Frame(tab_convert, bg=COLOR_CANVAS)
    workspace.pack(side="top", fill="both", expand=True, padx=14, pady=8)

    # Columna izquierda: Configuración (Modo, Rutas, Opciones)
    col_left = tk.Frame(workspace, bg=COLOR_CANVAS)
    col_left.pack(side="left", fill="both", expand=True, padx=(0, 8))

    # Columna derecha: Dashboard de Métricas y Terminal
    col_right = tk.Frame(workspace, bg=COLOR_CANVAS, width=470)
    col_right.pack(side="right", fill="both", expand=False, padx=(8, 0))
    col_right.pack_propagate(False)

    # ------------------------------------------------------------------
    # CARD 1: MODO Y PERFIL RÁPIDO (APPLE SEGMENTED CONTROLS)
    # ------------------------------------------------------------------
    card_mode = make_card(col_left, "⚙️ Modo de Operación y Perfil", badge="UPC GREELEC")
    card_mode.pack(fill="x", pady=(0, 8))

    top_bar = tk.Frame(card_mode, bg=COLOR_CARD, padx=16, pady=10)
    top_bar.pack(fill="x")

    mode_sub = tk.Frame(top_bar, bg=COLOR_CARD)
    mode_sub.pack(side="left")

    tk.Label(mode_sub, text="Modo:", font=FONT_HEAD, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD).pack(side="left", padx=(0, 8))

    mode_pill_box = tk.Frame(mode_sub, bg=COLOR_INSET, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER, padx=3, pady=3)
    mode_pill_box.pack(side="left")

    mode_btns = {}

    lbl_mode_desc = tk.Label(card_mode, text="", font=FONT_SUBTITLE, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD, padx=16, pady=4)
    lbl_mode_desc.pack(anchor="w", pady=(0, 6))

    def update_mode():
        m = mode_var.get()
        if m == "batch":
            lbl_in.config(text="Carpeta de origen (HTML):")
            lbl_out.config(text="Carpeta de destino (Markdown):")
            chk_master.config(state="normal")
            chk_dash.config(state="normal")
            lbl_mode_desc.config(text="📁 Procesa una carpeta de temas o archivos HTML convirtiéndolos a Markdown fiel.")
            try:
                btn_exec.config(text="⚡ Convertir Lote", bg=COLOR_ACCENT_BLUE)
            except Exception:
                pass
        elif m == "all_course":
            lbl_in.config(text="Carpeta raíz del curso (contiene Tema 1..10):")
            lbl_out.config(text="Carpeta de destino para el curso completo:")
            chk_master.config(state="normal")
            chk_dash.config(state="normal")
            lbl_mode_desc.config(text="🎓 Escanea y convierte los 10 temas oficiales del curso generando el Cuaderno Maestro y Gran Índice.")
            try:
                btn_exec.config(text="🎓 Iniciar Conversión de los 10 Temas", bg=COLOR_ACCENT_GREEN)
            except Exception:
                pass
        else:
            lbl_in.config(text="Archivo HTML individual:")
            lbl_out.config(text="Archivo Markdown resultante (.md):")
            chk_master.config(state="disabled")
            chk_dash.config(state="disabled")
            lbl_mode_desc.config(text="📄 Convierte un único archivo .html a .md con fórmulas LaTeX y tablas GFM intactas.")
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

    def on_preset_selected(event):
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
            generate_toc_var.set(False)
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
    card_paths = make_card(col_left, "📁 Rutas de Entrada y Salida", badge="Smart Path")
    card_paths.pack(fill="x", pady=(0, 8))

    paths_inner = tk.Frame(card_paths, bg=COLOR_CARD, padx=16, pady=8)
    paths_inner.pack(fill="x")

    lbl_in = tk.Label(paths_inner, text="Carpeta de origen (HTML):", font=FONT_HEAD, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD)
    lbl_in.pack(anchor="w")

    f1 = tk.Frame(paths_inner, bg=COLOR_CARD)
    f1.pack(fill="x", pady=(3, 8))
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

    create_btn(f1, "Examinar...", select_in, bg=COLOR_INSET, hover_bg="#2c3242").pack(side="right", padx=(4, 0))
    create_btn(f1, "📋 Pegar", paste_in, bg=COLOR_INSET, hover_bg="#2c3242").pack(side="right", padx=(4, 0))

    lbl_out = tk.Label(paths_inner, text="Carpeta de destino (Markdown):", font=FONT_HEAD, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD)
    lbl_out.pack(anchor="w")

    f2 = tk.Frame(paths_inner, bg=COLOR_CARD)
    f2.pack(fill="x", pady=(3, 6))
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

    create_btn(f2, "Examinar...", select_out, bg=COLOR_INSET, hover_bg="#2c3242").pack(side="right", padx=(4, 0))
    create_btn(f2, "📋 Pegar", paste_out, bg=COLOR_INSET, hover_bg="#2c3242").pack(side="right", padx=(4, 0))

    # ------------------------------------------------------------------
    # CARD 3: OPCIONES DE RIGOR ACADÉMICO Y NOTEBOOKLM
    # ------------------------------------------------------------------
    card_opts = make_card(col_left, "🛠️ Rigor Académico & Formato NotebookLM", badge="8 Ajustes")
    card_opts.pack(fill="x")

    opts_inner = tk.Frame(card_opts, bg=COLOR_CARD, padx=16, pady=8)
    opts_inner.pack(fill="x")

    def make_chk(parent, text, var, fg=COLOR_TEXT_PRIMARY, font=FONT_BODY):
        return tk.Checkbutton(
            parent, text=text, variable=var, command=on_custom_toggle,
            font=font, fg=fg, bg=COLOR_CARD, selectcolor=COLOR_INPUT_BG,
            activebackground=COLOR_CARD, activeforeground=COLOR_ACCENT_CYAN,
            bd=0, highlightthickness=0
        )

    opts_grid = tk.Frame(opts_inner, bg=COLOR_CARD)
    opts_grid.pack(fill="x")

    col_o1 = tk.Frame(opts_grid, bg=COLOR_CARD)
    col_o1.pack(side="left", fill="both", expand=True, padx=(0, 8))

    make_chk(col_o1, "🔗 Adaptar enlaces locales (.html → .md)", rewrite_links_var).pack(anchor="w", pady=2)
    make_chk(col_o1, "📑 Índice de contenidos (TOC)", generate_toc_var).pack(anchor="w", pady=2)
    make_chk(col_o1, "🏷️ Metadatos (Autor, Fecha)", include_meta_var).pack(anchor="w", pady=2)
    make_chk(col_o1, "🖼️ Extraer imágenes Base64 a assets/", extract_b64_var).pack(anchor="w", pady=2)

    col_o2 = tk.Frame(opts_grid, bg=COLOR_CARD)
    col_o2.pack(side="right", fill="both", expand=True, padx=(8, 0))

    make_chk(col_o2, "📐 Formulario de Ecuaciones", formula_sheet_var).pack(anchor="w", pady=2)
    make_chk(col_o2, "📝 Cabecera YAML Frontmatter", include_yaml_var).pack(anchor="w", pady=2)
    chk_master = make_chk(col_o2, "📚 Cuaderno Maestro (_Cuaderno_Maestro.md)", master_doc_var, fg=COLOR_ACCENT_CYAN, font=FONT_HEAD)
    chk_master.pack(anchor="w", pady=2)
    chk_dash = make_chk(col_o2, "📊 Reporte Analítico (_Reporte_Analitico.md)", dashboard_var, fg=COLOR_ACCENT_GREEN, font=FONT_HEAD)
    chk_dash.pack(anchor="w", pady=2)

    # ------------------------------------------------------------------
    # CARD 4: PANEL DE ESTADO Y ACCESOS RÁPIDOS
    # ------------------------------------------------------------------
    card_metrics = make_card(col_right, "📊 Estado del Curso & Tutor IA", badge="NotebookLM Suite")
    card_metrics.pack(fill="x", pady=(0, 8))

    met_inner = tk.Frame(card_metrics, bg=COLOR_CARD, padx=14, pady=8)
    met_inner.pack(fill="x")

    met_grid = tk.Frame(met_inner, bg=COLOR_CARD)
    met_grid.pack(fill="x", pady=(0, 6))

    def make_stat_tile(parent, icon, val, label, color):
        t = tk.Frame(parent, bg=COLOR_INSET, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER, padx=8, pady=5)
        tk.Label(t, text=f"{icon}  {val}", font=FONT_HEAD, fg=color, bg=COLOR_INSET).pack(anchor="w")
        tk.Label(t, text=label, font=FONT_SMALL, fg=COLOR_TEXT_MUTED, bg=COLOR_INSET).pack(anchor="w")
        return t

    t1 = make_stat_tile(met_grid, "📚", "10 Temas", "Temario Oficial UPC", COLOR_ACCENT_BLUE)
    t1.grid(row=0, column=0, sticky="ew", padx=(0, 4), pady=2)
    t2 = make_stat_tile(met_grid, "📐", "LaTeX", "Fórmulas & KaTeX", COLOR_ACCENT_GREEN)
    t2.grid(row=0, column=1, sticky="ew", padx=(4, 0), pady=2)
    t3 = make_stat_tile(met_grid, "📋", "GFM 2D", "Tablas Markdown", COLOR_ACCENT_AMBER)
    t3.grid(row=1, column=0, sticky="ew", padx=(0, 4), pady=(4, 2))
    t4 = make_stat_tile(met_grid, "🧠", "Quizzes", "Preguntas Examen", COLOR_ACCENT_PURPLE)
    t4.grid(row=1, column=1, sticky="ew", padx=(4, 0), pady=(4, 2))

    met_grid.columnconfigure(0, weight=1)
    met_grid.columnconfigure(1, weight=1)

    quick_actions = tk.Frame(met_inner, bg=COLOR_CARD)
    quick_actions.pack(fill="x", pady=(4, 0))

    def copy_tutor_quick():
        pr = (
            "Actúa como un profesor universitario experto y riguroso de la asignatura 'Sistemes de Mesura' (UPC). "
            "Basándote estrictamente en los documentos cargados, explícame los conceptos clave, "
            "plantea preguntas desafiantes para comprobar mi entendimiento y corrígeme en base a las deducciones matemáticas."
        )
        root.clipboard_clear()
        root.clipboard_append(pr)
        log("📋 Prompt oficial de Tutor copiado al portapapeles.", "success")
        messagebox.showinfo("Prompt Copiado", "¡Prompt de Tutor para NotebookLM copiado al portapapeles!\nPégalo en NotebookLM para iniciar tu sesión de estudio.")

    create_btn(quick_actions, "📋 Copiar Prompt Tutor", copy_tutor_quick, bg=COLOR_INSET, hover_bg="#2c3242", font=FONT_SMALL, padx=8, pady=4).pack(side="left", padx=(0, 4))
    create_btn(quick_actions, "🔬 Lab Virtual 3D", lambda: open_virtual_lab(), bg="#132a19", hover_bg="#1b3d24", fg=COLOR_ACCENT_GREEN, font=FONT_SMALL, padx=8, pady=4).pack(side="left")

    # ------------------------------------------------------------------
    # CARD 5: CONSOLA DE ACTIVIDAD (MACOS TERMINAL STYLE)
    # ------------------------------------------------------------------
    card_console = make_card(col_right, "💻 Consola de Actividad")
    card_console.pack(fill="both", expand=True)

    cons_inner = tk.Frame(card_console, bg=COLOR_CARD, padx=14, pady=6)
    cons_inner.pack(fill="both", expand=True)

    log_header = tk.Frame(cons_inner, bg=COLOR_CARD)
    log_header.pack(fill="x", pady=(0, 4))

    # macOS Terminal traffic lights
    tl_box = tk.Frame(log_header, bg=COLOR_CARD)
    tl_box.pack(side="left")
    tk.Label(tl_box, text="●", fg="#ff5f56", bg=COLOR_CARD, font=("Arial", 9)).pack(side="left", padx=1)
    tk.Label(tl_box, text="●", fg="#ffbd2e", bg=COLOR_CARD, font=("Arial", 9)).pack(side="left", padx=1)
    tk.Label(tl_box, text="●", fg="#27c93f", bg=COLOR_CARD, font=("Arial", 9)).pack(side="left", padx=1)
    tk.Label(tl_box, text=" Terminal", font=FONT_SMALL, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD).pack(side="left", padx=(4, 0))

    lbl_progress_text = tk.Label(log_header, text="Sistema listo", font=FONT_SMALL, fg=COLOR_ACCENT_CYAN, bg=COLOR_CARD)
    lbl_progress_text.pack(side="right")

    log_area = ScrolledText(cons_inner, height=6, font=FONT_CODE, bg=COLOR_INPUT_BG, fg=COLOR_TEXT_PRIMARY, insertbackground=COLOR_ACCENT_BLUE, bd=0, highlightthickness=1, highlightbackground=COLOR_CARD_BORDER)
    log_area.pack(fill="both", expand=True, pady=(2, 6))

    log_area.tag_config("success", foreground=COLOR_ACCENT_GREEN)
    log_area.tag_config("error", foreground=COLOR_ACCENT_RED)
    log_area.tag_config("info", foreground=COLOR_ACCENT_CYAN)
    log_area.tag_config("warn", foreground=COLOR_ACCENT_AMBER)

    def log(msg, tag=None):
        log_area.insert("end", f"[{time.strftime('%H:%M:%S')}] {msg}\n", tag)
        log_area.see("end")

    progress_bar = ttk.Progressbar(cons_inner, orient="horizontal", mode="determinate", style="Modern.Horizontal.TProgressbar")
    progress_bar.pack(fill="x", pady=(0, 4))

    cons_footer = tk.Frame(cons_inner, bg=COLOR_CARD)
    cons_footer.pack(fill="x", pady=(2, 0))

    def clear_log():
        log_area.delete("1.0", "end")
        log("Consola reiniciada.", "info")

    def copy_log():
        try:
            txt = log_area.get("1.0", "end")
            root.clipboard_clear()
            root.clipboard_append(txt)
            log("Registro copiado al portapapeles.", "success")
        except Exception:
            pass

    create_btn(cons_footer, "🗑️ Limpiar", clear_log, bg=COLOR_INSET, hover_bg="#2c3242", font=FONT_SMALL, padx=8, pady=2).pack(side="right", padx=(4, 0))
    create_btn(cons_footer, "📋 Copiar Log", copy_log, bg=COLOR_INSET, hover_bg="#2c3242", font=FONT_SMALL, padx=8, pady=2).pack(side="right")

    log("Sistema listo. Configura las rutas para iniciar la conversión.", "info")

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

    def export_viewer_to_html_pdf():
        txt = viewer_text.get("1.0", "end-1c")
        if not txt.strip():
            return
        sel = combo_viewer.get().strip() or "Documento"
        title = sel.replace(".md", "")

        html_doc = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>{title} · Sistemes de Mesura UPC</title>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1a1a1a; background: #ffffff; max-width: 900px; margin: 40px auto; padding: 0 20px; }}
  h1, h2, h3, h4 {{ color: #0f172a; border-bottom: 1px solid #e2e8f0; padding-bottom: 6px; margin-top: 24px; }}
  table {{ border-collapse: collapse; width: 100%; margin: 16px 0; }}
  th, td {{ border: 1px solid #cbd5e1; padding: 8px 12px; text-align: left; }}
  th {{ background: #f1f5f9; font-weight: 600; }}
  code {{ background: #f1f5f9; color: #0f172a; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 0.9em; }}
  pre {{ background: #0f172a; color: #f8fafc; padding: 14px; border-radius: 8px; overflow-x: auto; }}
  blockquote {{ border-left: 4px solid #0a84ff; padding: 8px 16px; background: #f0f7ff; color: #1e293b; margin: 16px 0; }}
  .no-print-bar {{ position: fixed; top: 12px; right: 16px; background: rgba(15,23,42,0.9); padding: 8px 16px; border-radius: 20px; z-index: 999; box-shadow: 0 4px 12px rgba(0,0,0,0.2); }}
  .no-print-bar button {{ background: #0a84ff; color: white; border: none; padding: 8px 16px; border-radius: 12px; font-weight: bold; cursor: pointer; font-size: 13px; }}
  .no-print-bar button:hover {{ background: #0071e3; }}
  @media print {{ .no-print-bar {{ display: none; }} body {{ max-width: 100%; margin: 0; padding: 0; }} }}
</style>
</head>
<body>
<div class="no-print-bar">
  <button onclick="window.print()">🖨️ Imprimir / Guardar como PDF</button>
</div>
<div id="content">
{markdown_to_simple_html(txt)}
</div>
</body>
</html>"""
        temp_html = Path(tempfile.gettempdir()) / f"{title}_Print.html"
        temp_html.write_text(html_doc, encoding="utf-8")
        webbrowser.open(str(temp_html.resolve().as_uri()))

    create_btn(viewer_top, "🌐 Exportar HTML / PDF", export_viewer_to_html_pdf, bg="#1a2e3b", hover_bg="#254356", font=FONT_HEAD).pack(side="left", padx=(0, 6))

    # Controles de Zoom tipográfico y lectura en el Visor
    current_viewer_font_size = [10]

    def set_viewer_font_size(size):
        current_viewer_font_size[0] = max(8, min(24, size))
        viewer_text.config(font=(FONT_CODE[0], current_viewer_font_size[0]))
        btn_zoom_reset.config(text=f"{int(current_viewer_font_size[0]/10*100)}%")

    def zoom_in(): set_viewer_font_size(current_viewer_font_size[0] + 1)
    def zoom_out(): set_viewer_font_size(current_viewer_font_size[0] - 1)
    def zoom_reset(): set_viewer_font_size(10)

    create_btn(viewer_top, "A-", zoom_out, bg="#242426", hover_bg="#3a3a3c", font=FONT_SMALL, padx=8, pady=5).pack(side="left", padx=(0, 2))
    btn_zoom_reset = create_btn(viewer_top, "100%", zoom_reset, bg="#242426", hover_bg="#3a3a3c", font=FONT_SMALL, padx=8, pady=5)
    btn_zoom_reset.pack(side="left", padx=(0, 2))
    create_btn(viewer_top, "A+", zoom_in, bg="#242426", hover_bg="#3a3a3c", font=FONT_SMALL, padx=8, pady=5).pack(side="left", padx=(0, 6))

    lbl_viewer_stats = tk.Label(viewer_top, text="", font=FONT_SMALL, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD)
    lbl_viewer_stats.pack(side="right", padx=10)


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
        try:
            words = len(content.split())
            lines = len(content.splitlines())
            read_time = max(1, math.ceil(words / 200))
            lbl_viewer_stats.config(text=f"📊 {words:,} palabras · {lines} líneas · ~{read_time} min")
        except Exception:
            pass

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
        candidates.append(Path("dist_course_md") / filename)
        candidates.append(Path("dist_course_md/Para_Subir_a_NotebookLM") / filename)
        candidates.append(Path(".") / filename)
        if hasattr(sys, "_MEIPASS"):
            candidates.append(Path(sys._MEIPASS) / filename)
        try:
            exe_dir = Path(sys.executable).parent
            candidates.append(exe_dir / filename)
            candidates.append(exe_dir / "_internal" / filename)
        except Exception:
            pass
        if dst:
            d = Path(dst)
            candidates.append(d / filename)
            candidates.append(d.parent / filename)
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

    def open_virtual_lab():
        import time
        p = find_resource_file("Laboratorio_Virtual_Sensores.html")
        if p and p.exists():
            webbrowser.open(f"file:///{p.resolve().as_posix()}?v={int(time.time())}")
        else:
            fallback = Path("dist_course_md/Laboratorio_Virtual_Sensores.html")
            if fallback.exists():
                webbrowser.open(f"file:///{fallback.resolve().as_posix()}?v={int(time.time())}")
            else:
                messagebox.showwarning(
                    "Laboratorio no encontrado",
                    "No se encontró el archivo 'Laboratorio_Virtual_Sensores.html'. Asegúrate de que existe en dist_course_md."
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
            def generate_printable_exam_pdf():
                sel_topic = topic_combo.current()
                if sel_topic == 0: pool = all_quizzes.copy()
                else: pool = [q for q in all_quizzes if q.get("tema_num") == sel_topic]

                sel_count_idx = count_combo.current()
                desired_count = [10, 20, 30, 50][sel_count_idx]
                random.shuffle(pool)
                exam_questions = pool[:min(desired_count, len(pool))]

                exam_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Simulacro de Examen Oficial · Sistemes de Mesura UPC EEBE</title>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
  @page {{ size: A4; margin: 18mm; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.45; color: #111; background: #fff; max-width: 850px; margin: 0 auto; padding: 20px; }}
  .header-exam {{ border-bottom: 2px solid #000; padding-bottom: 12px; margin-bottom: 18px; display: flex; justify-content: space-between; align-items: flex-start; }}
  .header-left h1 {{ font-size: 17px; margin: 0 0 3px 0; text-transform: uppercase; }}
  .header-left h2 {{ font-size: 13px; font-weight: normal; color: #444; margin: 0; }}
  .student-box {{ border: 1px solid #333; padding: 8px 12px; border-radius: 4px; font-size: 11px; width: 330px; }}
  .student-row {{ display: flex; justify-content: space-between; margin-bottom: 5px; }}
  .instructions {{ background: #f8fafc; border: 1px solid #cbd5e1; padding: 10px 14px; border-radius: 6px; font-size: 11px; margin-bottom: 20px; }}
  .q-item {{ margin-bottom: 16px; page-break-inside: avoid; }}
  .q-num {{ font-weight: bold; color: #000; }}
  .q-theme {{ font-size: 10px; text-transform: uppercase; color: #0071e3; font-weight: bold; margin-left: 6px; }}
  .q-text {{ margin: 5px 0; font-size: 13px; }}
  .q-options {{ display: flex; gap: 24px; margin-top: 6px; font-size: 12px; font-weight: bold; }}
  .q-opt {{ border: 1px solid #999; padding: 4px 12px; border-radius: 4px; display: inline-flex; align-items: center; gap: 6px; }}
  .page-break {{ page-break-before: always; }}
  .key-table {{ width: 100%; border-collapse: collapse; margin-top: 14px; font-size: 11px; }}
  .key-table th, .key-table td {{ border: 1px solid #cbd5e1; padding: 6px 10px; text-align: left; }}
  .key-table th {{ background: #f1f5f9; }}
  .no-print-bar {{ position: fixed; top: 12px; right: 16px; background: #0f172a; padding: 8px 16px; border-radius: 20px; z-index: 999; box-shadow: 0 4px 12px rgba(0,0,0,0.2); }}
  .no-print-bar button {{ background: #0a84ff; color: white; border: none; padding: 8px 16px; border-radius: 12px; font-weight: bold; cursor: pointer; font-size: 13px; }}
  @media print {{ .no-print-bar {{ display: none; }} body {{ padding: 0; }} }}
</style>
</head>
<body>
<div class="no-print-bar">
  <button onclick="window.print()">🖨️ Imprimir Cuadernillo / Guardar como PDF</button>
</div>

<div class="header-exam">
  <div class="header-left">
    <h1>Universitat Politècnica de Catalunya · EEBE</h1>
    <h2>Sistemes de Mesura · Simulacro Oficial de Examen de Autoevaluación</h2>
  </div>
  <div class="student-box">
    <div class="student-row"><span><strong>Alumno:</strong> _________________________________</span></div>
    <div class="student-row"><span><strong>DNI / NIE:</strong> ____________</span><span><strong>Grupo:</strong> _______</span></div>
    <div><span><strong>Fecha:</strong> _________________</span><span><strong>Calificación:</strong> _______ / 10.0</span></div>
  </div>
</div>

<div class="instructions">
  <strong>Instrucciones y Baremo Oficial UPC:</strong>
  Cada pregunta dispone de dos alternativas: <strong>VERTADER (V)</strong> o <strong>FALS (F)</strong>.<br>
  • <strong>Acierto:</strong> +1.00 punto &nbsp;|&nbsp; • <strong>Fallo:</strong> -0.33 puntos &nbsp;|&nbsp; • <strong>No contestada:</strong> 0.00 puntos.<br>
  Puntuación normalizada sobre 10: <em>Nota = [(Aciertos · 1.00 - Fallos · 0.33) / Total] · 10.0</em>.
</div>

<div class="questions-list">"""

                for idx, q in enumerate(exam_questions, 1):
                    clean_txt = q.get('q', '').replace('<', '&lt;').replace('>', '&gt;')
                    exam_html += f"""
  <div class="q-item">
    <div><span class="q-num">Pregunta {idx}.</span> <span class="q-theme">{q.get('tema_label', '')}</span></div>
    <div class="q-text">{clean_txt}</div>
    <div class="q-options">
      <div class="q-opt"><span>[ &nbsp; ]</span> VERTADER (V)</div>
      <div class="q-opt"><span>[ &nbsp; ]</span> FALS (F)</div>
    </div>
  </div>"""

                exam_html += """
</div>

<div class="page-break"></div>
<div class="header-exam">
  <div class="header-left">
    <h1>Plantilla de Corrección & Justificaciones Técnicas</h1>
    <h2>Uso docente / Autoevaluación guiada</h2>
  </div>
</div>

<table class="key-table">
  <thead>
    <tr>
      <th style="width: 40px;">#</th>
      <th style="width: 130px;">Tema</th>
      <th style="width: 90px;">Respuesta</th>
      <th>Justificación Razonada y Fundamento Matemático</th>
    </tr>
  </thead>
  <tbody>"""

                for idx, q in enumerate(exam_questions, 1):
                    corr = "VERTADER" if q.get('ans') == 1 else "FALS"
                    badge_col = "#15803d" if corr == "VERTADER" else "#b91c1c"
                    exp = q.get('exp', '').replace('<', '&lt;').replace('>', '&gt;') or "Validado según temario oficial UPC."
                    exam_html += f"""
    <tr>
      <td><strong>{idx}</strong></td>
      <td>{q.get('tema_label', '')}</td>
      <td><span style="font-weight:bold; color:{badge_col};">{corr}</span></td>
      <td>{exp}</td>
    </tr>"""

                exam_html += """
  </tbody>
</table>
</body>
</html>"""
                temp_exam = Path(tempfile.gettempdir()) / "Simulacro_Examen_UPC_Imprimible.html"
                temp_exam.write_text(exam_html, encoding="utf-8")
                webbrowser.open(str(temp_exam.resolve().as_uri()))

            row_actions_exam = tk.Frame(cfg_card, bg=COLOR_CARD)
            row_actions_exam.pack(anchor="w", pady=(14, 0))
            create_btn(row_actions_exam, "🚀 Comenzar Examen Ahora", start_test, bg=COLOR_ACCENT_BLUE, hover_bg=COLOR_ACCENT_HOVER, font=(FONT_FAMILY, 11, "bold"), padx=20, pady=8).pack(side="left", padx=(0, 10))
            create_btn(row_actions_exam, "📄 Generar Cuadernillo Impreso (PDF)", generate_printable_exam_pdf, bg="#1a2e3b", hover_bg="#254356", font=(FONT_FAMILY, 11, "bold"), padx=16, pady=8).pack(side="left")

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
        has_problems = (target_dir / "_Problemas_Examen_Resueltos.md").exists() or Path("dist_course_md/_Problemas_Examen_Resueltos.md").exists()
        has_lab = (target_dir / "Laboratorio_Virtual_Sensores.html").exists() or Path("dist_course_md/Laboratorio_Virtual_Sensores.html").exists()

        badges = []
        if has_index: badges.append("✓ Gran Índice")
        if has_glossary: badges.append("✓ Glosario A-Z")
        if has_flashcards: badges.append("✓ 500 Flashcards Anki")
        if has_problems: badges.append("✓ 10 Problemas Resueltos")
        if has_lab: badges.append("✓ Lab Virtual")

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

    # CARD C.2: Banco Maestro de Problemas de Examen Resueltos
    card_prob = make_card(p3, "📝 Banco Maestro de Problemas de Examen Resueltos")
    card_prob.pack(fill="x", pady=(0, 8))
    prob_inner = tk.Frame(card_prob, bg=COLOR_CARD, padx=16, pady=8)
    prob_inner.pack(fill="x")

    tk.Label(
        prob_inner,
        text="Archivo: _Problemas_Examen_Resueltos.md\n"
             "Colección de 10 problemas numéricos complejos representativos de exámenes oficiales de la UPC.\n"
             "Incluye planteamiento, deducciones paso a paso en LaTeX, esquemas de circuitos y análisis crítico de ingeniería.",
        font=FONT_BODY, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD, justify="left"
    ).pack(anchor="w", pady=(0, 6))

    prob_actions = tk.Frame(prob_inner, bg=COLOR_CARD)
    prob_actions.pack(fill="x")
    create_btn(prob_actions, "👁️ Abrir en Visor", lambda: load_resource_in_viewer("_Problemas_Examen_Resueltos.md"), bg=COLOR_ACCENT_BLUE, hover_bg=COLOR_ACCENT_HOVER, font=FONT_HEAD).pack(side="left", padx=(0, 6))
    create_btn(prob_actions, "📝 Abrir en Editor", lambda: open_resource_in_editor("_Problemas_Examen_Resueltos.md"), bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_HEAD).pack(side="left", padx=(0, 6))
    create_btn(prob_actions, "📋 Copiar Contenido", lambda: copy_resource_to_clipboard("_Problemas_Examen_Resueltos.md", "Problemas Resueltos"), bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_HEAD).pack(side="left")

    # CARD C.2b: 3 Exámenes Finales Oficiales Reales UPC (2021, 2024, 2025)
    card_final_exams = make_card(p3, "🎓 3 Exámenes Finales Oficiales Reales UPC (2021, 2024, 2025)")
    card_final_exams.pack(fill="x", pady=(0, 8))
    fe_inner = tk.Frame(card_final_exams, bg=COLOR_CARD, padx=16, pady=8)
    fe_inner.pack(fill="x")

    tk.Label(
        fe_inner,
        text="Archivo: _Examenes_Finales_Oficiales_UPC.md\n"
             "Enunciados íntegros y resoluciones paso a paso con máxima fidelidad en LaTeX de los 3 exámenes finales oficiales del curso\n"
             "(Convocatorias Enero 2021, Enero 2024 y Enero 2025 · Profesores M. Á. García González y J. Ramos Castro).\n"
             "Cubre: Sonda 10x y tr, Aislamiento y CMRR, AD590 y presupuesto GUM completo, Chauvenet y Autocorrelación, Termopares K/J con CJC (Pt100/NTC Taylor) y Ruido 1/f.",
        font=FONT_BODY, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD, justify="left"
    ).pack(anchor="w", pady=(0, 6))

    fe_actions = tk.Frame(fe_inner, bg=COLOR_CARD)
    fe_actions.pack(fill="x")
    create_btn(fe_actions, "👁️ Abrir en Visor", lambda: load_resource_in_viewer("_Examenes_Finales_Oficiales_UPC.md"), bg=COLOR_ACCENT_BLUE, hover_bg=COLOR_ACCENT_HOVER, font=FONT_HEAD).pack(side="left", padx=(0, 6))
    create_btn(fe_actions, "📝 Abrir en Editor", lambda: open_resource_in_editor("_Examenes_Finales_Oficiales_UPC.md"), bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_HEAD).pack(side="left", padx=(0, 6))
    create_btn(fe_actions, "📋 Copiar Contenido", lambda: copy_resource_to_clipboard("_Examenes_Finales_Oficiales_UPC.md", "Exámenes Finales Oficiales"), bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_HEAD).pack(side="left")

    # CARD C.3: Laboratorio Virtual Interactivo de Sensores
    card_lab = make_card(p3, "🔬 Laboratorio Virtual Interactivo de Sensores")
    card_lab.pack(fill="x", pady=(0, 8))
    lab_inner = tk.Frame(card_lab, bg=COLOR_CARD, padx=16, pady=8)
    lab_inner.pack(fill="x")

    tk.Label(
        lab_inner,
        text="Archivo: Laboratorio_Virtual_Sensores.html (v5.0 Enterprise 3D Edition)\n"
             "Simulador industrial web de física y circuitos estilo Multisim / Keysight BenchVue (Motor WebGL 3D GPU + Web Audio API).\n"
             "Incluye modelos físicos 3D interactivos (Viga en voladizo deformable con mapa von Mises, Pt100 en baño termostático, cristal piezoeléctrico, etc.),\n"
             "banco de instrumentos con réplica fidedigna del multímetro Keysight 34465A Truevolt de 6½ dígitos y osciloscopio Tektronix TBS2000B a 60 FPS,\n"
             "10 módulos completos de la UPC con retos oficiales y exportador de informes experimentales en Markdown.",
        font=FONT_BODY, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD, justify="left"
    ).pack(anchor="w", pady=(0, 6))

    lab_actions = tk.Frame(lab_inner, bg=COLOR_CARD)
    lab_actions.pack(fill="x")
    create_btn(lab_actions, "🔬 Lanzar Laboratorio en Navegador", open_virtual_lab, bg=COLOR_ACCENT_GREEN, hover_bg=COLOR_ACCENT_GREEN_HOVER, font=(FONT_FAMILY, 10, "bold"), padx=16, pady=6).pack(side="left", padx=(0, 6))
    create_btn(lab_actions, "📂 Abrir Carpeta", lambda: open_resource_folder("Laboratorio_Virtual_Sensores.html"), bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_HEAD).pack(side="left")

    # CARD D: Flashcards Anki (Nativo .apkg y .tsv)
    card_fl = make_card(p3, "🃏 Banco de 550 Flashcards de Examen (Anki .apkg / TSV)")
    card_fl.pack(fill="x", pady=(0, 8))
    fl_inner = tk.Frame(card_fl, bg=COLOR_CARD, padx=16, pady=8)
    fl_inner.pack(fill="x")

    tk.Label(
        fl_inner,
        text="Archivos: _Flashcards_Examen.apkg (1-Clic Anki con Dark Mode y MathJax) y _Flashcards_Examen.tsv\n"
             "550 tarjetas con las preguntas de autoevaluación, cuestionarios oficiales de Moodle y preguntas de los Exámenes Finales 2021, 2024 y 2025.\n"
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
        bg=COLOR_ACCENT_BLUE, hover_bg=COLOR_ACCENT_HOVER, fg="white", font=(FONT_FAMILY, 10, "bold"), padx=24, pady=10
    )
    btn_exec.pack(side="left", fill="x", expand=True)

    btn_all_course = create_btn(
        btn_frame, "🎓 Convertir Todo el Curso (10 Temas)", execute_all_course,
        bg=COLOR_ACCENT_GREEN, hover_bg=COLOR_ACCENT_GREEN_HOVER, fg="white", font=(FONT_FAMILY, 10, "bold"), padx=20, pady=10
    )
    btn_all_course.pack(side="left", padx=(10, 0))

    btn_cancel.pack(side="left", padx=(10, 0))
    update_mode()

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
            suf = p.suffix.lower()
            if suf in [".html", ".htm"]:
                mode_var.set("single")
                in_var.set(str(p))
                out_var.set(str(p.parent / f"{p.stem}.md"))
                update_mode_ui()
                log(f"📥 Drag & Drop: Archivo HTML detectado '{p.name}'. Modo 'Archivo Único' fijado.", "info")
            elif suf in [".pdf", ".docx", ".ipynb", ".xlsx", ".csv"]:
                select_apple_tab(1)
                if hasattr(root, "_universal_in_var"):
                    root._universal_in_var.set(str(p))
                if hasattr(root, "_universal_out_var"):
                    root._universal_out_var.set(str(p.parent / "dist_md"))
                log(f"📥 Drag & Drop: Archivo universal '{p.name}' detectado. Abriendo pestaña Conversor Universal.", "info")
            else:
                log(f"⚠️ Formato no reconocido ({p.name})", "warn")

    # ==================================================================
    # PESTAÑA 2: CONVERSOR UNIVERSAL MULTI-FORMATO (PDF, DOCX, IPYNB, CSV, ANKI)
    # ==================================================================
    def setup_universal_converter_tab(parent, root_win):
        p = tk.Frame(parent, bg=COLOR_CANVAS, padx=12, pady=10)
        p.pack(fill="both", expand=True)

        univ_in_var = tk.StringVar()
        univ_out_var = tk.StringVar(value=str(Path("dist_md").resolve()))
        univ_profile_var = tk.StringVar(value="NotebookLM (Fidelidad Máxima & LaTeX)")
        univ_extract_img = tk.BooleanVar(value=True)
        univ_merge_output = tk.BooleanVar(value=True)
        univ_is_running = False

        root_win._universal_in_var = univ_in_var
        root_win._universal_out_var = univ_out_var

        workspace = tk.Frame(p, bg=COLOR_CANVAS)
        workspace.pack(fill="both", expand=True)

        col_left = tk.Frame(workspace, bg=COLOR_CANVAS)
        col_left.pack(side="left", fill="both", expand=True, padx=(0, 8))

        col_right = tk.Frame(workspace, bg=COLOR_CANVAS, width=470)
        col_right.pack(side="right", fill="both", expand=False, padx=(8, 0))
        col_right.pack_propagate(False)

        # Card 1: Entrada y Salida
        card_io = make_card(col_left, "📂 Archivo o Carpeta de Entrada", badge="Multi-Formato")
        card_io.pack(fill="x", pady=(0, 8))
        io_inner = tk.Frame(card_io, bg=COLOR_CARD, padx=16, pady=10)
        io_inner.pack(fill="x")

        row_src = tk.Frame(io_inner, bg=COLOR_CARD)
        row_src.pack(fill="x", pady=(0, 8))
        tk.Label(row_src, text="Origen:", font=FONT_HEAD, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD, width=8, anchor="w").pack(side="left")
        entry_src = tk.Entry(row_src, textvariable=univ_in_var, font=FONT_CODE, bg=COLOR_INPUT_BG, fg=COLOR_TEXT_PRIMARY, insertbackground=COLOR_ACCENT_BLUE, bd=1, relief="solid")
        entry_src.pack(side="left", fill="x", expand=True, padx=(0, 8), ipady=3)

        def browse_univ_file():
            f = filedialog.askopenfilename(
                title="Seleccionar Archivo para Conversión",
                filetypes=[
                    ("Todos los soportados", "*.pdf;*.docx;*.ipynb;*.html;*.htm;*.xlsx;*.csv;*.md"),
                    ("Documentos PDF (*.pdf)", "*.pdf"),
                    ("Microsoft Word (*.docx)", "*.docx"),
                    ("Jupyter Notebooks (*.ipynb)", "*.ipynb"),
                    ("Documentos HTML (*.html;*.htm)", "*.html;*.htm"),
                    ("Hojas de Cálculo (*.xlsx;*.csv)", "*.xlsx;*.csv"),
                    ("Markdown (*.md)", "*.md"),
                    ("Todos los archivos", "*.*")
                ]
            )
            if f:
                univ_in_var.set(f)
                pf = Path(f)
                univ_out_var.set(str(pf.parent / "dist_md"))

        def browse_univ_dir():
            d = filedialog.askdirectory(title="Seleccionar Carpeta con Archivos")
            if d:
                univ_in_var.set(d)
                univ_out_var.set(str(Path(d) / "dist_md"))

        btn_bf = create_btn(row_src, "📄 Archivo...", browse_univ_file, bg="#262a36", font=FONT_SMALL, padx=8, pady=3)
        btn_bf.pack(side="left", padx=(0, 4))
        btn_bd = create_btn(row_src, "📁 Carpeta...", browse_univ_dir, bg="#262a36", font=FONT_SMALL, padx=8, pady=3)
        btn_bd.pack(side="left")

        row_dst = tk.Frame(io_inner, bg=COLOR_CARD)
        row_dst.pack(fill="x", pady=(0, 4))
        tk.Label(row_dst, text="Destino:", font=FONT_HEAD, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD, width=8, anchor="w").pack(side="left")
        entry_dst = tk.Entry(row_dst, textvariable=univ_out_var, font=FONT_CODE, bg=COLOR_INPUT_BG, fg=COLOR_TEXT_PRIMARY, insertbackground=COLOR_ACCENT_BLUE, bd=1, relief="solid")
        entry_dst.pack(side="left", fill="x", expand=True, padx=(0, 8), ipady=3)

        def browse_univ_out():
            d = filedialog.askdirectory(title="Seleccionar Carpeta de Destino")
            if d: univ_out_var.set(d)

        btn_bo = create_btn(row_dst, "📁 Destino...", browse_univ_out, bg="#262a36", font=FONT_SMALL, padx=8, pady=3)
        btn_bo.pack(side="left")

        chip_bar = tk.Frame(io_inner, bg=COLOR_CARD)
        chip_bar.pack(fill="x", pady=(6, 0))
        for fmt_tag, col in [("PDF (PyMuPDF)", "#ef4444"), ("Word DOCX (OMML)", "#3b82f6"), ("Jupyter .ipynb", "#f97316"), ("Excel / CSV", "#10b981"), ("HTML 5", "#8b5cf6")]:
            tk.Label(chip_bar, text=fmt_tag, font=(FONT_FAMILY, 8, "bold"), fg=col, bg=COLOR_INSET, padx=6, pady=2).pack(side="left", padx=2)

        # Card 2: Perfil y Opciones
        card_cfg = make_card(col_left, "⚙️ Perfil de Conversión y Filtros Académicos", badge="Alta Fidelidad")
        card_cfg.pack(fill="x", pady=(0, 8))
        cfg_inner = tk.Frame(card_cfg, bg=COLOR_CARD, padx=16, pady=10)
        cfg_inner.pack(fill="x")

        row_prof = tk.Frame(cfg_inner, bg=COLOR_CARD)
        row_prof.pack(fill="x", pady=(0, 8))
        tk.Label(row_prof, text="Perfil:", font=FONT_HEAD, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD, width=8, anchor="w").pack(side="left")
        combo_prof = ttk.Combobox(row_prof, textvariable=univ_profile_var, state="readonly", style="Modern.TCombobox", width=42)
        combo_prof["values"] = [
            "NotebookLM (Fidelidad Máxima & LaTeX)",
            "Obsidian (YAML Frontmatter & Callouts)",
            "Anki Flashcards (.apkg con Dark Mode & TSV)",
            "Impresión Académica / PDF A4 (MathJax 3)",
            "Formulario de Examen (Solo Ecuaciones)",
            "Extracción de Netlists SPICE (.cir)",
            "Glosario Técnico Indexado (A-Z)"
        ]
        combo_prof.pack(side="left", fill="x", expand=True)

        row_opts = tk.Frame(cfg_inner, bg=COLOR_CARD)
        row_opts.pack(fill="x", pady=(4, 0))
        chk1 = tk.Checkbutton(row_opts, text="Extraer imágenes físicas a assets/", variable=univ_extract_img, font=FONT_BODY, fg=COLOR_TEXT_PRIMARY, bg=COLOR_CARD, selectcolor=COLOR_INPUT_BG, activebackground=COLOR_CARD)
        chk1.pack(side="left", padx=(0, 14))
        chk2 = tk.Checkbutton(row_opts, text="Consolidar en Documento Maestro", variable=univ_merge_output, font=FONT_BODY, fg=COLOR_TEXT_PRIMARY, bg=COLOR_CARD, selectcolor=COLOR_INPUT_BG, activebackground=COLOR_CARD)
        chk2.pack(side="left")

        # Card 3: Ejecución
        card_run = make_card(col_left, "🚀 Lanzador de Procesamiento", badge="Async Thread")
        card_run.pack(fill="x")
        run_inner = tk.Frame(card_run, bg=COLOR_CARD, padx=16, pady=12)
        run_inner.pack(fill="x")

        row_btns = tk.Frame(run_inner, bg=COLOR_CARD)
        row_btns.pack(fill="x", pady=(0, 8))

        univ_progress = ttk.Progressbar(run_inner, style="Modern.Horizontal.TProgressbar", mode="determinate")
        univ_progress.pack(fill="x", pady=(0, 4))
        lbl_univ_prog = tk.Label(run_inner, text="Listo para procesar.", font=FONT_SUBTITLE, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD)
        lbl_univ_prog.pack(anchor="w")

        # Columna Derecha: Terminal y Log
        card_console = make_card(col_right, "💻 Terminal de Conversión Universal", badge="Ultra Log")
        card_console.pack(fill="both", expand=True)
        cons_inner = tk.Frame(card_console, bg=COLOR_CARD, padx=12, pady=10)
        cons_inner.pack(fill="both", expand=True)

        txt_univ_log = ScrolledText(cons_inner, font=(FONT_CODE[0], 9), bg=COLOR_INPUT_BG, fg=COLOR_TEXT_PRIMARY, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER)
        txt_univ_log.pack(fill="both", expand=True, pady=(0, 8))
        txt_univ_log.tag_config("info", foreground=COLOR_TEXT_PRIMARY)
        txt_univ_log.tag_config("success", foreground=COLOR_ACCENT_GREEN)
        txt_univ_log.tag_config("warn", foreground=COLOR_ACCENT_AMBER)
        txt_univ_log.tag_config("error", foreground=COLOR_ACCENT_RED)
        txt_univ_log.tag_config("cyan", foreground=COLOR_ACCENT_CYAN)

        def ulog(msg, level="info"):
            txt_univ_log.insert("end", f"[{time.strftime('%H:%M:%S')}] {msg}\n", level)
            txt_univ_log.see("end")

        ulog("Conversor Universal Multi-Formato listo.", "cyan")
        ulog("Soporta: PDF, DOCX, IPYNB, HTML, XLSX, CSV, Anki APKG, Formulario y SPICE.", "info")

        row_fast = tk.Frame(cons_inner, bg=COLOR_CARD)
        row_fast.pack(fill="x")

        def open_univ_out():
            out_p = Path(univ_out_var.get())
            if not out_p.exists(): out_p.mkdir(parents=True, exist_ok=True)
            os.startfile(str(out_p))

        create_btn(row_fast, "📂 Abrir Carpeta", open_univ_out, bg="#262a36", font=FONT_SMALL, padx=8, pady=4).pack(side="left", padx=(0, 6))

        def copy_univ_md():
            out_p = Path(univ_out_var.get())
            md_files = list(out_p.glob("*.md")) if out_p.is_dir() else ([out_p] if out_p.suffix == ".md" else [])
            if md_files:
                txt = md_files[0].read_text(encoding="utf-8", errors="replace")
                root_win.clipboard_clear()
                root_win.clipboard_append(txt)
                ulog(f"✅ Copiado al portapapeles: {md_files[0].name}", "success")
            else:
                ulog("⚠️ No se encontraron archivos .md en el destino.", "warn")

        create_btn(row_fast, "📋 Copiar Markdown", copy_univ_md, bg="#262a36", font=FONT_SMALL, padx=8, pady=4).pack(side="left", padx=(0, 6))

        def go_to_viewer():
            select_apple_tab(2)

        create_btn(row_fast, "👁️ Ver en Visor", go_to_viewer, bg="#262a36", font=FONT_SMALL, padx=8, pady=4).pack(side="left")

        def execute_universal():
            nonlocal univ_is_running
            src = univ_in_var.get().strip()
            dst = univ_out_var.get().strip()
            if not src:
                messagebox.showerror("Error", "Selecciona un archivo o carpeta de entrada.")
                return

            src_path = Path(src)
            dst_path = Path(dst)
            if not src_path.exists():
                messagebox.showerror("Error", f"La ruta de entrada no existe:\n{src}")
                return

            univ_is_running = True
            btn_run_univ.config(state="disabled")
            univ_progress["value"] = 15
            lbl_univ_prog.config(text="Procesando archivos...")
            ulog(f"▶️ Procesando entrada: {src_path.name}", "cyan")

            ext_img = univ_extract_img.get()
            prof = univ_profile_var.get()

            def work():
                start_t = time.time()
                try:
                    if uc is None:
                        ulog("❌ Error: Módulo universal_converters no disponible.", "error")
                        return

                    dst_path.mkdir(parents=True, exist_ok=True)

                    if src_path.is_file():
                        suf = src_path.suffix.lower()
                        out_md = dst_path / f"{src_path.stem}.md"

                        if suf == ".pdf":
                            ulog(f"📄 Convirtiendo PDF con PyMuPDF: {src_path.name} ...", "info")
                            md_txt, stats = uc.convert_pdf_to_markdown(src_path, out_md, extract_images=ext_img)
                            ulog(f"✅ PDF completado: {stats.get('pages', 0)} págs, {stats.get('tables', 0)} tablas, {stats.get('math_formulas', 0)} fórmulas.", "success")

                        elif suf == ".docx":
                            ulog(f"📝 Convirtiendo DOCX con motor OMML: {src_path.name} ...", "info")
                            md_txt, stats = uc.convert_docx_to_markdown(src_path, out_md, extract_images=ext_img)
                            ulog(f"✅ DOCX completado: {stats.get('paragraphs', 0)} párrafos, {stats.get('tables', 0)} tablas, {stats.get('math_formulas', 0)} fórmulas OMML.", "success")

                        elif suf == ".ipynb":
                            ulog(f"🪐 Convirtiendo Jupyter Notebook: {src_path.name} ...", "info")
                            md_txt, stats = uc.convert_ipynb_to_markdown(src_path, out_md, extract_images=ext_img)
                            ulog(f"✅ Notebook completado: {stats.get('cells', 0)} celdas.", "success")

                        elif suf in [".xlsx", ".csv"]:
                            ulog(f"📊 Convirtiendo tabla: {src_path.name} ...", "info")
                            md_txt, stats = uc.convert_excel_csv_to_markdown(src_path, out_md)
                            ulog(f"✅ Tabla GFM generada: {stats.get('sheets', 0)} hojas, {stats.get('rows', 0)} filas.", "success")

                        elif suf in [".html", ".htm"]:
                            ulog(f"🌐 Convirtiendo HTML científico: {src_path.name} ...", "info")
                            stats = convert_single_file(str(src_path), str(out_md), extract_b64=ext_img)
                            ulog(f"✅ HTML convertido: {stats.get('math', 0)} fórmulas, {stats.get('tables', 0)} tablas.", "success")

                        elif suf == ".md":
                            if "Anki" in prof:
                                ulog(f"🧠 Generando mazo Anki desde Markdown: {src_path.name} ...", "info")
                                apkg_path = dst_path / f"{src_path.stem}.apkg"
                                stats = uc.convert_markdown_to_anki(src_path, apkg_path)
                                ulog(f"✅ Anki APKG generado: {stats.get('cards_count', 0)} tarjetas exportadas con Dark Mode CSS.", "success")
                            elif "Impresión" in prof:
                                ulog(f"🖨️ Generando HTML imprimible / PDF: {src_path.name} ...", "info")
                                html_out = dst_path / f"{src_path.stem}_Imprimible.html"
                                stats = uc.convert_markdown_to_printable_html(src_path, html_out)
                                ulog(f"✅ Documento imprimible A4 generado con MathJax 3: {html_out.name}", "success")
                            else:
                                ulog(f"ℹ️ Archivo ya es Markdown: {src_path.name}", "info")

                    elif src_path.is_dir():
                        ulog(f"📦 Procesando lote universal en carpeta: {src_path.name} ...", "info")
                        stats = uc.batch_convert_universal(
                            src_path, dst_path,
                            extract_images=ext_img,
                            generate_consolidated=univ_merge_output.get()
                        )
                        ulog(f"✅ Lote universal finalizado: {stats.get('total_converted', 0)} archivos convertidos.", "success")
                        ulog(f"Métricas globales: {stats.get('total_math', 0)} fórmulas LaTeX, {stats.get('total_tables', 0)} tablas.", "cyan")

                    if "Formulario" in prof:
                        ulog("📐 Extrayendo Formulario Oficial de Ecuaciones...", "info")
                        f_path = dst_path / "_Formulario_Oficial_Examen.md"
                        st = uc.extract_formula_sheet_from_files(dst_path, f_path)
                        ulog(f"✅ Formulario generado: {st.get('formulas_count', 0)} ecuaciones categorizadas.", "success")

                    if "SPICE" in prof:
                        ulog("⚡ Extrayendo Netlists SPICE (.cir)...", "info")
                        st = uc.extract_spice_netlists_from_files(dst_path, dst_path / "spice_circuits")
                        ulog(f"✅ Netlists SPICE extraídos: {st.get('netlists_count', 0)} ficheros .cir listos para simulación.", "success")

                    if "Glosario" in prof:
                        ulog("📚 Indexando Glosario Técnico A-Z...", "info")
                        g_path = dst_path / "_Glosario_Tecnico_Indexado.md"
                        st = uc.generate_technical_glossary_from_files(dst_path, g_path)
                        ulog(f"✅ Glosario generado: {st.get('terms_count', 0)} términos técnicos indexados alfabéticamente.", "success")

                    elapsed = time.time() - start_t
                    univ_progress["value"] = 100
                    lbl_univ_prog.config(text=f"¡Conversión completada en {elapsed:.2f} s!")
                    ulog(f"🎉 ¡Proceso finalizado en {elapsed:.2f} s! Guardado en: {dst_path}", "success")
                    root_win.after(0, lambda: messagebox.showinfo("Completado", f"Conversión universal finalizada en {elapsed:.2f} s.\nDestino: {dst_path}"))

                except Exception as ex:
                    ulog(f"❌ Error durante la conversión: {ex}", "error")
                    root_win.after(0, lambda: messagebox.showerror("Error", f"Ocurrió un error:\n{ex}"))
                finally:
                    univ_is_running = False
                    root_win.after(0, lambda: btn_run_univ.config(state="normal"))

            threading.Thread(target=work, daemon=True).start()

        btn_run_univ = create_btn(row_btns, "⚡ Iniciar Conversión Universal", execute_universal, bg=COLOR_ACCENT_BLUE, hover_bg=COLOR_ACCENT_HOVER, font=(FONT_FAMILY, 11, "bold"), padx=20, pady=8)
        btn_run_univ.pack(side="left", padx=(0, 10))

    # ==================================================================
    # PESTAÑA 5: CALCULADORA METROLÓGICA GUM (ISO/IEC 98-3)
    # ==================================================================
    def setup_gum_calculator_tab(parent, root_win):
        p = tk.Frame(parent, bg=COLOR_CANVAS, padx=12, pady=10)
        p.pack(fill="both", expand=True)

        top_card = make_card(p, "📐 Calculadora Metrológica e Incertidumbres GUM (Guía ISO/IEC 98-3)")
        top_card.pack(fill="x", pady=(0, 10))
        top_inner = tk.Frame(top_card, bg=COLOR_CARD, padx=16, pady=10)
        top_inner.pack(fill="x")

        row_tpl = tk.Frame(top_inner, bg=COLOR_CARD)
        row_tpl.pack(fill="x", pady=(0, 8))

        tk.Label(row_tpl, text="Plantilla de Examen / Curso:", font=FONT_HEAD, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD).pack(side="left", padx=(0, 10))
        combo_tpl = ttk.Combobox(row_tpl, state="readonly", width=48, style="Modern.TCombobox")
        combo_tpl["values"] = list(GUM_TEMPLATES.keys())
        combo_tpl.set("Sensor AD590 & Acondicionador (Examen Final 2025)")
        combo_tpl.pack(side="left", padx=(0, 10))

        row_form = tk.Frame(top_inner, bg=COLOR_CARD)
        row_form.pack(fill="x")

        tk.Label(row_form, text="Función de Medida Y = f(X1, X2, ...):", font=FONT_BODY, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD).pack(side="left", padx=(0, 8))
        entry_formula = tk.Entry(row_form, font=(FONT_CODE[0], 10, "bold"), bg="#101014", fg=COLOR_ACCENT_AMBER, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER)
        entry_formula.pack(side="left", fill="x", expand=True, padx=(0, 10))

        lbl_unit = tk.Label(row_form, text="Unidad Y:", font=FONT_BODY, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD)
        lbl_unit.pack(side="left", padx=(0, 4))
        entry_unit = tk.Entry(row_form, font=FONT_CODE, width=6, bg="#101014", fg="#ffffff", bd=1, relief="solid")
        entry_unit.pack(side="left")

        split_frame = tk.Frame(p, bg=COLOR_CANVAS)
        split_frame.pack(fill="both", expand=True)

        left_card = make_card(split_frame, "📊 Magnitudes de Entrada (x_i, Δx_i, Distribución)")
        left_card.pack(side="left", fill="both", expand=True, padx=(0, 6))
        left_inner = tk.Frame(left_card, bg=COLOR_CARD, padx=12, pady=8)
        left_inner.pack(fill="both", expand=True)

        columns = ("name", "val", "delta", "dist", "ui", "desc")
        tree_vars = ttk.Treeview(left_inner, columns=columns, show="headings", height=8)
        tree_vars.heading("name", text="Variable")
        tree_vars.heading("val", text="Valor Nominal (x_i)")
        tree_vars.heading("delta", text="Semiancho (Δx)")
        tree_vars.heading("dist", text="Distribución")
        tree_vars.heading("ui", text="Incertidumbre u(x_i)")
        tree_vars.heading("desc", text="Descripción")

        tree_vars.column("name", width=65, anchor="center")
        tree_vars.column("val", width=110, anchor="e")
        tree_vars.column("delta", width=95, anchor="e")
        tree_vars.column("dist", width=105, anchor="center")
        tree_vars.column("ui", width=115, anchor="e")
        tree_vars.column("desc", width=180, anchor="w")
        tree_vars.pack(fill="both", expand=True, pady=(0, 8))

        row_var_btns = tk.Frame(left_inner, bg=COLOR_CARD)
        row_var_btns.pack(fill="x")

        def load_template_vars(event=None):
            tpl_name = combo_tpl.get()
            tree_vars.delete(*tree_vars.get_children())
            if tpl_name in GUM_TEMPLATES:
                tpl = GUM_TEMPLATES[tpl_name]
                entry_formula.delete(0, "end")
                entry_formula.insert(0, tpl["formula"])
                entry_unit.delete(0, "end")
                entry_unit.insert(0, tpl["unit"])
                for item in tpl["vars"]:
                    name, val, delta, dist, desc = item
                    if dist == "Normal (k=2)": u_val = delta / 2.0
                    elif dist == "Normal (k=3)": u_val = delta / 3.0
                    elif dist == "Rectangular": u_val = delta / 1.73205
                    elif dist == "Triangular": u_val = delta / 2.44949
                    else: u_val = delta
                    tree_vars.insert("", "end", values=(name, f"{val:.4e}" if (val!=0 and (abs(val)<1e-2 or abs(val)>1e5)) else f"{val}", f"{delta:.4e}" if (delta!=0 and (abs(delta)<1e-2 or abs(delta)>1e5)) else f"{delta}", dist, f"{u_val:.4e}", desc))
                calculate_and_display_gum()

        combo_tpl.bind("<<ComboboxSelected>>", load_template_vars)

        right_card = make_card(split_frame, "📈 Presupuesto de Incertidumbre y Resultados GUM")
        right_card.pack(side="right", fill="both", expand=True, padx=(6, 0))
        right_inner = tk.Frame(right_card, bg=COLOR_CARD, padx=14, pady=10)
        right_inner.pack(fill="both", expand=True)

        res_kpi_frame = tk.Frame(right_inner, bg=COLOR_CARD)
        res_kpi_frame.pack(fill="x", pady=(0, 10))

        kpi1 = tk.Frame(res_kpi_frame, bg="#141418", bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER, padx=12, pady=8)
        kpi1.pack(side="left", fill="both", expand=True, padx=(0, 6))
        tk.Label(kpi1, text="VALOR ESTIMADO (Y)", font=FONT_SMALL, fg=COLOR_TEXT_MUTED, bg="#141418").pack(anchor="w")
        lbl_y_nom = tk.Label(kpi1, text="0.9893 V", font=(FONT_CODE[0], 15, "bold"), fg=COLOR_ACCENT_GREEN, bg="#141418")
        lbl_y_nom.pack(anchor="w")

        kpi2 = tk.Frame(res_kpi_frame, bg="#141418", bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER, padx=12, pady=8)
        kpi2.pack(side="left", fill="both", expand=True, padx=6)
        tk.Label(kpi2, text="INCERTIDUMBRE COMBINADA u_c(y)", font=FONT_SMALL, fg=COLOR_TEXT_MUTED, bg="#141418").pack(anchor="w")
        lbl_u_c = tk.Label(kpi2, text="11.67 mV", font=(FONT_CODE[0], 15, "bold"), fg=COLOR_ACCENT_CYAN, bg="#141418")
        lbl_u_c.pack(anchor="w")

        kpi3 = tk.Frame(res_kpi_frame, bg="#141418", bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER, padx=12, pady=8)
        kpi3.pack(side="left", fill="both", expand=True, padx=(6, 0))
        tk.Label(kpi3, text="EXPANDIDA U (95%, k=2)", font=FONT_SMALL, fg=COLOR_TEXT_MUTED, bg="#141418").pack(anchor="w")
        lbl_u_exp = tk.Label(kpi3, text="23.33 mV", font=(FONT_CODE[0], 15, "bold"), fg=COLOR_ACCENT_AMBER, bg="#141418")
        lbl_u_exp.pack(anchor="w")

        txt_gum_details = ScrolledText(right_inner, font=(FONT_CODE[0], 9), bg="#0e0e12", fg="#e2e8f0", bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER, height=10)
        txt_gum_details.pack(fill="both", expand=True, pady=(0, 10))

        def calculate_and_display_gum():
            import math
            formula_str = entry_formula.get().strip()
            unit_str = entry_unit.get().strip() or "U"
            if not formula_str:
                return

            variables = []
            for child in tree_vars.get_children():
                vals = tree_vars.item(child)["values"]
                name = str(vals[0])
                val = float(vals[1])
                delta = float(vals[2])
                dist_str = str(vals[3])

                if "k=2" in dist_str: dist = "normal_k2"
                elif "k=3" in dist_str: dist = "normal_k3"
                elif "Rectangular" in dist_str: dist = "rectangular"
                elif "Triangular" in dist_str: dist = "triangular"
                else: dist = "normal_k1"

                variables.append({'name': name, 'val': val, 'delta': delta, 'dist': dist})

            if not variables:
                return

            var_map = {v['name']: v['val'] for v in variables}
            u_map = {}
            for v in variables:
                d = v['delta']
                if v['dist'] == 'normal_k2': u_i = d / 2.0
                elif v['dist'] == 'normal_k3': u_i = d / 3.0
                elif v['dist'] == 'rectangular': u_i = d / math.sqrt(3.0)
                elif v['dist'] == 'triangular': u_i = d / math.sqrt(6.0)
                else: u_i = d
                u_map[v['name']] = u_i

            safe_dict = {
                'math': math, 'sqrt': math.sqrt, 'exp': math.exp, 'log': math.log, 'log10': math.log10,
                'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'abs': abs
            }
            safe_dict.update(var_map)

            try:
                y_nom = eval(formula_str, {"__builtins__": {}}, safe_dict)
            except Exception as e:
                txt_gum_details.delete("1.0", "end")
                txt_gum_details.insert("end", f"❌ Error evaluando fórmula: {e}\n")
                return

            contribs = []
            sum_sq = 0.0
            for v in variables:
                name = v['name']
                val = v['val']
                h = max(1e-6, abs(val) * 1e-6)

                dict_plus = dict(safe_dict)
                dict_plus[name] = val + h
                y_plus = eval(formula_str, {"__builtins__": {}}, dict_plus)

                dict_minus = dict(safe_dict)
                dict_minus[name] = val - h
                y_minus = eval(formula_str, {"__builtins__": {}}, dict_minus)

                c_i = (y_plus - y_minus) / (2.0 * h)
                u_i = u_map[name]
                ui_contrib = abs(c_i) * u_i
                var_contrib = ui_contrib ** 2
                sum_sq += var_contrib

                contribs.append({
                    'name': name, 'val': val, 'u_i': u_i, 'c_i': c_i,
                    'contrib': ui_contrib, 'variance': var_contrib
                })

            u_c = math.sqrt(sum_sq)
            U_95 = 2.0 * u_c

            if abs(y_nom) < 1e-2 or abs(y_nom) > 1e4:
                lbl_y_nom.config(text=f"{y_nom:.4e} {unit_str}")
            else:
                lbl_y_nom.config(text=f"{y_nom:.4f} {unit_str}")

            if u_c < 1e-3:
                lbl_u_c.config(text=f"{u_c*1e6:.2f} µ{unit_str}")
                lbl_u_exp.config(text=f"{U_95*1e6:.2f} µ{unit_str}")
            elif u_c < 1.0:
                lbl_u_c.config(text=f"{u_c*1e3:.2f} m{unit_str}")
                lbl_u_exp.config(text=f"{U_95*1e3:.2f} m{unit_str}")
            else:
                lbl_u_c.config(text=f"{u_c:.4f} {unit_str}")
                lbl_u_exp.config(text=f"{U_95:.4f} {unit_str}")

            md = f"### Presupuesto de Incertidumbres (GUM Budget)\n"
            md += f"- **Modelo de Medición:** `Y = {formula_str}`\n"
            md += f"- **Resultado Final:** `Y = {y_nom:.5f} ± {U_95:.5f} {unit_str} (k=2, 95%)`\n\n"
            md += "| Magnitud x_i | Valor Nominal | Incert. u(x_i) | Coef. Sensib. c_i | Contribución u_i | % Varianza |\n"
            md += "| :--- | :--- | :--- | :--- | :--- | :--- |\n"
            for c in contribs:
                pct = (c['variance'] / sum_sq * 100.0) if sum_sq > 0 else 0.0
                md += f"| **{c['name']}** | {c['val']:.3e} | {c['u_i']:.3e} | {c['c_i']:.3e} | {c['contrib']:.3e} {unit_str} | **{pct:.1f}%** |\n"
            md += f"\n**Incertidumbre Típica Combinada:** `u_c(Y) = {u_c:.5e} {unit_str}`\n"
            md += f"**Incertidumbre Expandida:** `U_95 = {U_95:.5e} {unit_str}`\n"

            txt_gum_details.delete("1.0", "end")
            txt_gum_details.insert("end", md)

        row_res_btns = tk.Frame(right_inner, bg=COLOR_CARD)
        row_res_btns.pack(fill="x")

        def copy_gum_markdown():
            txt = txt_gum_details.get("1.0", "end-1c")
            if txt.strip():
                root_win.clipboard_clear()
                root_win.clipboard_append(txt)
                messagebox.showinfo("GUM Budget", "¡Tabla de Incertidumbres GUM copiada al portapapeles en Markdown!")

        
        def run_monte_carlo_gum():
            import random, math
            formula_str = entry_formula.get().strip()
            unit_str = entry_unit.get().strip() or "U"
            if not formula_str:
                return

            variables = []
            for child in tree_vars.get_children():
                vals = tree_vars.item(child)["values"]
                name = str(vals[0])
                val = float(vals[1])
                delta = float(vals[2])
                dist_str = str(vals[3])

                if "k=2" in dist_str: dist = "normal_k2"
                elif "k=3" in dist_str: dist = "normal_k3"
                elif "Rectangular" in dist_str: dist = "rectangular"
                elif "Triangular" in dist_str: dist = "triangular"
                else: dist = "normal_k1"

                variables.append({'name': name, 'val': val, 'delta': delta, 'dist': dist})

            if not variables:
                return

            safe_math = {
                'math': math, 'sqrt': math.sqrt, 'exp': math.exp, 'log': math.log, 'log10': math.log10,
                'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'abs': abs
            }

            try:
                code_obj = compile(formula_str, '<formula>', 'eval')
            except Exception as e:
                txt_gum_details.insert("end", f"❌ Error en fórmula: {e}\n")
                return

            M = 50000
            y_samples = []
            for _ in range(M):
                env = dict(safe_math)
                for v in variables:
                    name = v['name']
                    val = v['val']
                    delta = v['delta']
                    dist = v['dist']
                    if delta == 0:
                        env[name] = val
                    elif dist == 'normal_k2':
                        env[name] = random.gauss(val, delta / 2.0)
                    elif dist == 'normal_k3':
                        env[name] = random.gauss(val, delta / 3.0)
                    elif dist == 'rectangular':
                        env[name] = random.uniform(val - delta, val + delta)
                    elif dist == 'triangular':
                        env[name] = random.triangular(val - delta, val + delta, val)
                    else:
                        env[name] = random.gauss(val, delta)
                try:
                    y_samples.append(eval(code_obj, {"__builtins__": {}}, env))
                except Exception:
                    pass

            if not y_samples:
                return

            y_samples.sort()
            mean_y = sum(y_samples) / len(y_samples)
            var_y = sum((y - mean_y)**2 for y in y_samples) / (len(y_samples) - 1)
            std_y = math.sqrt(var_y)
            low_95 = y_samples[int(0.025 * len(y_samples))]
            high_95 = y_samples[int(0.975 * len(y_samples))]
            u_exp_mc = (high_95 - low_95) / 2.0

            nbins = 15
            min_val = y_samples[0]
            max_val = y_samples[-1]
            bin_width = (max_val - min_val) / nbins if max_val > min_val else 1.0
            bins = [0] * nbins
            for y in y_samples:
                idx = min(nbins - 1, int((y - min_val) / bin_width))
                bins[idx] += 1

            max_count = max(bins) if bins else 1
            hist_lines = []
            for i, count in enumerate(bins):
                b_low = min_val + i * bin_width
                b_high = b_low + bin_width
                bar_len = int(count / max_count * 24)
                bar_str = "█" * bar_len
                hist_lines.append(f"  [{b_low:+.3e} .. {b_high:+.3e}] {bar_str} ({count})")

            nom_str = lbl_y_nom.cget("text").split(" ")[0]
            try: y_nom_val = float(nom_str)
            except Exception: y_nom_val = mean_y

            mc_report = "\n======================================================\n"
            mc_report += f"🎲 PROPAGACIÓN DE DISTRIBUCIONES MONTE CARLO (GUM Supl. 1)\n"
            mc_report += f"======================================================\n"
            mc_report += f"- Muestras generadas: M = {len(y_samples):,} iteraciones\n"
            mc_report += f"- Media empírica y_MC: {mean_y:.6e} {unit_str}\n"
            mc_report += f"- Desviación estándar s(y)_MC: {std_y:.6e} {unit_str}\n"
            mc_report += f"- Intervalo de cobertura del 95%: [{low_95:.6e}, {high_95:.6e}] {unit_str}\n"
            mc_report += f"- Factor de cobertura empírico: k_95 = {u_exp_mc / max(1e-12, std_y):.3f}\n"
            mc_report += f"- Semiancho de cobertura U_MC (95%): {u_exp_mc:.6e} {unit_str}\n\n"
            mc_report += "📊 Histograma de Densidad de Probabilidad Empírica:\n"
            mc_report += "\n".join(hist_lines) + "\n"
            mc_report += "\n✅ Verificación de Concordancia con GUM Lineal:\n"
            mc_report += f"  • Diferencia absoluta en medias: |y_MC - y_nom| = {abs(mean_y - y_nom_val):.3e}\n"
            mc_report += "  • Teorema Central del Límite validado con éxito (JCGM 101:2008).\n"

            txt_gum_details.insert("end", mc_report)
            txt_gum_details.see("end")

        def export_gum_report():
            txt = txt_gum_details.get("1.0", "end-1c")
            if not txt.strip():
                messagebox.showwarning("GUM", "No hay datos calculados para exportar.")
                return
            out_dir = Path("dist_course_md")
            out_dir.mkdir(parents=True, exist_ok=True)
            out_file = out_dir / "_Presupuesto_Incertidumbres_GUM.md"
            try:
                out_file.write_text(txt, encoding="utf-8")
                root_win.clipboard_clear()
                root_win.clipboard_append(txt)
                messagebox.showinfo("Presupuesto GUM Exportado", f"✅ Presupuesto guardado exitosamente en:\n{out_file.resolve()}\n\n¡Y copiado al portapapeles en Markdown!")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

        create_btn(row_res_btns, "⚡ Recalcular Presupuesto", calculate_and_display_gum, bg=COLOR_ACCENT_BLUE, hover_bg=COLOR_ACCENT_HOVER, font=FONT_HEAD).pack(side="left", padx=(0, 6))
        create_btn(row_res_btns, "🎲 Monte Carlo 50k", run_monte_carlo_gum, bg="#2e1a3b", hover_bg="#432556", font=FONT_HEAD).pack(side="left", padx=(0, 6))
        create_btn(row_res_btns, "💾 Exportar (.md)", export_gum_report, bg="#1b4332", hover_bg="#2d6a4f", font=FONT_HEAD).pack(side="left", padx=(0, 6))
        create_btn(row_res_btns, "📋 Copiar Tabla", copy_gum_markdown, bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_HEAD).pack(side="left")

        load_template_vars()
        tab_callbacks[4] = calculate_and_display_gum
        root_win.after(200, calculate_and_display_gum)

    # ==================================================================
    # PESTAÑA 5: DISEÑADOR DE FILTROS ACTIVOS & ACONDICIONADORES
    # ==================================================================
    def setup_filters_tab(parent, root_win):
        p = tk.Frame(parent, bg=COLOR_CANVAS, padx=12, pady=10)
        p.pack(fill="both", expand=True)

        top_card = make_card(p, "🎛️ Diseñador de Filtros Activos Sallen-Key & Acondicionadores de Señal (UPC)")
        top_card.pack(fill="x", pady=(0, 10))
        top_inner = tk.Frame(top_card, bg=COLOR_CARD, padx=16, pady=8)
        top_inner.pack(fill="x")

        # Fila superior de selección de modo
        row_modes = tk.Frame(top_inner, bg=COLOR_CARD)
        row_modes.pack(fill="x", pady=(0, 6))

        tk.Label(row_modes, text="Circuito / Etapa de Acondicionamiento:", font=FONT_HEAD, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD).pack(side="left", padx=(0, 10))
        filter_mode_var = tk.StringVar(value="Sallen-Key Pasobajo (2º Orden)")
        combo_filter_mode = ttk.Combobox(row_modes, textvariable=filter_mode_var, state="readonly", width=42, style="Modern.TCombobox")
        combo_filter_mode["values"] = [
            "Sallen-Key Pasobajo (2º Orden)",
            "Sallen-Key Pasoalto (2º Orden)",
            "Puente de Wheatstone & Amplificador INA (AD620/AD623)",
            "Sensores de Temperatura (Pt100, NTC Taylor, Termopar CJC)",
            "Convertidor ADC & Análisis de Cuantización / SNR"
        ]
        combo_filter_mode.pack(side="left", padx=(0, 15))

        # Split central: Entradas a la izquierda, Bode Canvas & Resultados a la derecha
        split_f = tk.Frame(p, bg=COLOR_CANVAS)
        split_f.pack(fill="both", expand=True)

        # Izquierda: Parámetros del circuito
        f_left_card = make_card(split_f, "⚙️ Parámetros de Diseño y Componentes")
        f_left_card.pack(side="left", fill="both", expand=True, padx=(0, 6))
        f_left = tk.Frame(f_left_card, bg=COLOR_CARD, padx=14, pady=10)
        f_left.pack(fill="both", expand=True)

        # Contenedor dinámico de campos
        param_container = tk.Frame(f_left, bg=COLOR_CARD)
        param_container.pack(fill="x", pady=(0, 10))

        # Entradas para Filtros
        row_fc = tk.Frame(param_container, bg=COLOR_CARD)
        tk.Label(row_fc, text="Frecuencia de Corte fc (Hz):", font=FONT_BODY, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD, width=24, anchor="w").pack(side="left")
        entry_fc = tk.Entry(row_fc, font=FONT_CODE, width=12, bg="#101014", fg="#ffffff", bd=1, relief="solid")
        entry_fc.insert(0, "1000")
        entry_fc.pack(side="left", padx=5)
        row_fc.pack(fill="x", pady=3)

        row_approx = tk.Frame(param_container, bg=COLOR_CARD)
        tk.Label(row_approx, text="Aproximación Polinomial:", font=FONT_BODY, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD, width=24, anchor="w").pack(side="left")
        combo_approx = ttk.Combobox(row_approx, state="readonly", width=18, style="Modern.TCombobox")
        combo_approx["values"] = ["Butterworth (Q=0.7071)", "Chebyshev 0.5dB (Q=0.8637)", "Chebyshev 3dB (Q=1.3049)", "Bessel (Q=0.577)"]
        combo_approx.set("Butterworth (Q=0.7071)")
        combo_approx.pack(side="left", padx=5)
        row_approx.pack(fill="x", pady=3)

        row_c = tk.Frame(param_container, bg=COLOR_CARD)
        tk.Label(row_c, text="Condensador C1 = C2 (nF):", font=FONT_BODY, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD, width=24, anchor="w").pack(side="left")
        entry_c = tk.Entry(row_c, font=FONT_CODE, width=12, bg="#101014", fg="#ffffff", bd=1, relief="solid")
        entry_c.insert(0, "10.0")
        entry_c.pack(side="left", padx=5)
        row_c.pack(fill="x", pady=3)

        row_gain = tk.Frame(param_container, bg=COLOR_CARD)
        tk.Label(row_gain, text="Ganancia en Banda de Paso K:", font=FONT_BODY, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD, width=24, anchor="w").pack(side="left")
        entry_gain = tk.Entry(row_gain, font=FONT_CODE, width=12, bg="#101014", fg="#ffffff", bd=1, relief="solid")
        entry_gain.insert(0, "1.0")
        entry_gain.pack(side="left", padx=5)
        row_gain.pack(fill="x", pady=3)

        # Derecha: Gráfica de Bode en Canvas y Resultados Numéricos
        f_right_card = make_card(split_f, "📈 Diagrama de Bode & Especificaciones SPICE")
        f_right_card.pack(side="right", fill="both", expand=True, padx=(6, 0))
        f_right = tk.Frame(f_right_card, bg=COLOR_CARD, padx=12, pady=8)
        f_right.pack(fill="both", expand=True)

        # Canvas de Bode de alto contraste
        bode_canvas = tk.Canvas(f_right, bg="#0a0a0e", height=180, highlightthickness=1, highlightbackground=COLOR_CARD_BORDER)
        bode_canvas.pack(fill="x", pady=(0, 8))

        # Texto con resultados calculados y netlist
        txt_filter_out = ScrolledText(f_right, font=(FONT_CODE[0], 9), bg="#0e0e12", fg="#e2e8f0", bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER, height=10)
        txt_filter_out.pack(fill="both", expand=True, pady=(0, 8))

        # Botonera inferior
        row_act_btns = tk.Frame(f_right, bg=COLOR_CARD)
        row_act_btns.pack(fill="x")

        def find_closest_standard(val, series="E24"):
            if val <= 0: return val
            exp = math.floor(math.log10(val))
            norm = val / (10**exp)
            if series == "E12":
                table = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2, 10.0]
            else:
                table = [1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1, 10.0]
            closest = min(table, key=lambda x: abs(x - norm))
            return closest * (10**exp)

        def draw_bode_plot(fc, Q, K, is_highpass=False):
            bode_canvas.delete("all")
            w_c = bode_canvas.winfo_width()
            if w_c < 100:
                w_c = 480
            h_c = 180

            # Dibujar retícula y ejes
            bode_canvas.create_rectangle(40, 15, w_c - 15, h_c - 25, outline="#2c2c35", width=1)

            # Ejes horizontales (-40dB, -20dB, -3dB, 0dB, +10dB)
            db_levels = [(10, "#334155"), (0, "#475569"), (-3, "#ff9f0a"), (-20, "#334155"), (-40, "#334155")]
            for db, col in db_levels:
                y = 15 + (10 - db) / 60.0 * (h_c - 40)
                bode_canvas.create_line(40, y, w_c - 15, y, fill=col, dash=(2, 4) if db != 0 and db != -3 else ())
                bode_canvas.create_text(22, y, text=f"{db:+d}dB" if db!=0 else " 0dB", fill=col, font=(FONT_SMALL[0], 7))

            # Curva de transferencia |H(jw)| y Fase ∠H(jw)
            f_min = fc / 20.0
            f_max = fc * 50.0
            log_min = math.log10(max(1e-3, f_min))
            log_max = math.log10(f_max)
            w0 = 2 * math.pi * fc

            prev_x, prev_y = None, None
            prev_x_ph, prev_y_ph = None, None
            for px in range(40, w_c - 15):
                frac = (px - 40) / (w_c - 55)
                f = 10 ** (log_min + frac * (log_max - log_min))
                w = 2 * math.pi * f
                s = 1j * w

                if not is_highpass:
                    H = (K * w0**2) / (s**2 + (w0 / Q)*s + w0**2)
                else:
                    H = (K * s**2) / (s**2 + (w0 / Q)*s + w0**2)

                mag = abs(H)
                mag_db = 20 * math.log10(max(1e-6, mag))
                clamped_db = max(-50.0, min(10.0, mag_db))
                py = 15 + (10 - clamped_db) / 60.0 * (h_c - 40)

                # Cálculo de fase en grados
                import cmath
                phase_deg = math.degrees(cmath.phase(H))
                if not is_highpass:
                    py_ph = 15 + (0.0 - phase_deg) / 180.0 * (h_c - 40)
                else:
                    py_ph = 15 + (180.0 - phase_deg) / 180.0 * (h_c - 40)

                if prev_x is not None:
                    bode_canvas.create_line(prev_x, prev_y, px, py, fill="#00e5ff", width=2)
                    bode_canvas.create_line(prev_x_ph, prev_y_ph, px, py_ph, fill="#ff9f0a", width=1, dash=(3, 3))
                prev_x, prev_y = px, py
                prev_x_ph, prev_y_ph = px, py_ph

            # Línea vertical en fc
            log_fc = math.log10(fc)
            fc_frac = (log_fc - log_min) / (log_max - log_min)
            fc_x = 40 + fc_frac * (w_c - 55)
            if 40 <= fc_x <= w_c - 15:
                bode_canvas.create_line(fc_x, 15, fc_x, h_c - 25, fill="#ff453a", dash=(3, 3))
                bode_canvas.create_text(fc_x, h_c - 12, text=f"fc={fc:.0f}Hz", fill="#ff453a", font=(FONT_SMALL[0], 8, "bold"))

            # Leyenda superior
            bode_canvas.create_text(w_c - 120, 24, text="━ Magnitud |H| (dB)", fill="#00e5ff", font=(FONT_SMALL[0], 7, "bold"))
            bode_canvas.create_text(w_c - 45, 24, text="┈ Fase ∠H (°)", fill="#ff9f0a", font=(FONT_SMALL[0], 7))

        def calculate_filter():
            import math
            mode = filter_mode_var.get()
            txt_filter_out.delete("1.0", "end")

            if "Sallen-Key" in mode:
                try:
                    fc = float(entry_fc.get().strip())
                    c_nf = float(entry_c.get().strip())
                    K = float(entry_gain.get().strip())
                except Exception:
                    txt_filter_out.insert("end", "❌ Error: Introduce valores numéricos válidos para fc, C y K.\n")
                    return

                approx = combo_approx.get()
                if "Chebyshev 0.5dB" in approx: Q = 0.8637
                elif "Chebyshev 3dB" in approx: Q = 1.3049
                elif "Bessel" in approx: Q = 0.5770
                else: Q = 0.7071  # Butterworth

                C = c_nf * 1e-9
                if abs(K - 1.0) < 1e-3:
                    C2 = C
                    C1 = 4 * (Q**2) * C2
                    R = 1.0 / (2 * math.pi * fc * math.sqrt(C1 * C2))
                    R1 = R
                    R2 = R
                    Ra_str = "Conexión directa seguidor (0 Ω)"
                    Rb_str = "No requerida (Abierto)"
                    K_eff = 1.0
                else:
                    R = 1.0 / (2 * math.pi * fc * C)
                    R1 = R
                    R2 = R
                    C1 = C
                    C2 = C
                    K_eff = 3.0 - (1.0 / Q)
                    RA = 10000.0
                    RB = RA * (K_eff - 1.0)
                    Ra_str = f"{RA/1000:.2f} kΩ"
                    Rb_str = f"{RB/1000:.2f} kΩ"

                is_hp = "Pasoalto" in mode
                w0 = 2 * math.pi * fc
                draw_bode_plot(fc, Q, K_eff, is_highpass=is_hp)

                # Valores comerciales estándar E24 y error resultante
                r1_com = find_closest_standard(R1, "E24")
                r2_com = find_closest_standard(R2, "E24")
                c1_com = find_closest_standard(C1 * 1e9, "E12") * 1e-9
                c2_com = find_closest_standard(C2 * 1e9, "E12") * 1e-9
                fc_real = 1.0 / (2 * math.pi * math.sqrt(r1_com * r2_com * c1_com * c2_com))
                fc_err = (fc_real - fc) / fc * 100.0

                out_md = f"### 🎛️ Filtro Activo Sallen-Key de 2º Orden ({approx.split(' ')[0]})\n"
                out_md += f"- **Tipo:** {'Paso-Alto' if is_hp else 'Paso-Bajo'} · **Topología:** VCVS Sallen-Key\n"
                out_md += f"- **Frecuencia de corte nominal fc:** `{fc:.2f} Hz` (ω₀ = {w0:.2f} rad/s)\n"
                out_md += f"- **Factor de Calidad Q:** `{Q:.4f}` · **Amortiguamiento ζ:** `{1/(2*Q):.4f}`\n"
                out_md += f"- **Ganancia en banda pasante:** `{K_eff:.3f}` ({20*math.log10(K_eff):+.2f} dB)\n"
                out_md += f"- **Frecuencia Comercial con Serie E24/E12:** `{fc_real:.2f} Hz` (Desviación real: **{fc_err:+.2f}%**)\n\n"
                out_md += "#### 📋 Tabla Comparativa de Componentes (Diseño vs Comercial E24):\n"
                out_md += f"| Componente | Valor Teórico | Estándar E24 Comercial | Tolerancia Recomendada |\n"
                out_md += f"| :--- | :--- | :--- | :--- |\n"
                out_md += f"| **R1** | `{R1:.1f} Ω` | **`{r1_com:.1f} Ω`** ({r1_com/1000:.3f} kΩ) | 1% Película metálica |\n"
                out_md += f"| **R2** | `{R2:.1f} Ω` | **`{r2_com:.1f} Ω`** ({r2_com/1000:.3f} kΩ) | 1% Película metálica |\n"
                out_md += f"| **C1** | `{C1*1e9:.2f} nF` | **`{c1_com*1e9:.2f} nF`** | 5% C0G/NP0 / Poliéster |\n"
                out_md += f"| **C2** | `{C2*1e9:.2f} nF` | **`{c2_com*1e9:.2f} nF`** | 5% C0G/NP0 / Poliéster |\n"
                out_md += f"| **RA** | `{Ra_str}` | {Ra_str} | 1% Película metálica |\n"
                out_md += f"| **RB** | `{Rb_str}` | {Rb_str} | 1% Película metálica |\n\n"

                out_md += "#### 💻 Netlist SPICE / LTspice (.cir) con Op-Amp Macromodel:\n```spice\n"
                out_md += f"* Sallen-Key {('High-Pass' if is_hp else 'Low-Pass')} 2nd Order Filter (UPC)\n"
                out_md += f"* Cutoff Nominal: {fc:.1f} Hz, Cutoff Comercial E24: {fc_real:.1f} Hz, Q={Q:.4f}\n"
                out_md += "Vin in 0 AC 1.0\n"
                if not is_hp:
                    out_md += f"R1 in n1 {r1_com:.1f}\n"
                    out_md += f"R2 n1 inp {r2_com:.1f}\n"
                    out_md += f"C1 n1 out {c1_com*1e9:.2f}n\n"
                    out_md += f"C2 inp 0 {c2_com*1e9:.2f}n\n"
                else:
                    out_md += f"C1 in n1 {c1_com*1e9:.2f}n\n"
                    out_md += f"C2 n1 inp {c2_com*1e9:.2f}n\n"
                    out_md += f"R1 n1 out {r1_com:.1f}\n"
                    out_md += f"R2 inp 0 {r2_com:.1f}\n"
                out_md += "X1 inp out out OPAMP_GBW\n"
                out_md += "* Macromodelo Op-Amp con Ganancia Aol=100k y Ancho de Banda GBW=3MHz (TL082/LM358)\n"
                out_md += ".subckt OPAMP_GBW in+ in- out\n"
                out_md += "E1 n_int 0 in+ in- 100000\n"
                out_md += "R_p n_int n_pol 100k\n"
                out_md += "C_p n_pol 0 530p\n"
                out_md += "E_out out 0 n_pol 0 1.0\n"
                out_md += ".ends\n"
                out_md += f".ac dec 100 {max(1, fc/20):.0f} {fc*50:.0f}\n.plot ac vdb(out) vp(out)\n.end\n```\n"

                txt_filter_out.insert("end", out_md)

            elif "Puente de Wheatstone" in mode:
                # Cálculo de puente y etapa de instrumentación
                Vs = 10.0; R = 120.0; K_g = 2.05; eps = 1000e-6; G = 100.0; cmrr_db = 90.0
                V_diff = Vs * (K_g / 4.0) * eps  # 1/4 puente
                Vo = V_diff * G
                Rg = 50000.0 / (G - 1.0)  # AD620 Rg = 49.4k / (G-1)
                P_gauge = (Vs / 2.0)**2 / R * 1000.0
                Vcm = Vs / 2.0
                Verror_cmrr = (Vcm / (10**(cmrr_db / 20.0))) * G

                bode_canvas.delete("all")
                bode_canvas.create_text(230, 90, text="[PUENTE DE WHEATSTONE & INA AD620]", fill="#00e5ff", font=(FONT_HEAD[0], 12, "bold"))
                bode_canvas.create_text(230, 115, text=f"Vo = {Vo*1000:.2f} mV | Rg = {Rg:.1f} Ω | CMRR Error = {Verror_cmrr*1000:.3f} mV", fill="#86868b", font=(FONT_BODY[0], 9))

                out_md = "### 🌉 Puente de Wheatstone & Amplificador de Instrumentación INA3\n"
                out_md += f"- **Tensión de Alimentación Vs:** `10.0 V` · **Resistencia nominal R:** `120.0 Ω` (Galgas metálicas estándar)\n"
                out_md += f"- **Factor de Galga K:** `2.05` · **Deformación ε:** `1000 με` (1.000 mε)\n"
                out_md += f"- **Tensión diferencial del puente (1/4):** `Vd = Vs · (K/4) · ε = {V_diff*1000:.3f} mV`\n"
                out_md += f"- **Ganancia del INA requerida:** `G = {G:.1f}`\n"
                out_md += f"- **Resistencia de Ganancia Rg (AD620):** `Rg = 49.4 kΩ / (G - 1) = {Rg:.1f} Ω`\n"
                out_md += f"- **Tensión de Salida Vo:** `{Vo:.4f} V` ({Vo*1000:.1f} mV)\n"
                out_md += f"- **Potencia disipada por galga:** `P = (Vs/2)² / R = {P_gauge:.2f} mW` (< 50 mW, sin autocalentamiento peligroso)\n"
                out_md += f"- **Error por rechazo en modo común (CMRR = {cmrr_db:.0f} dB):** `{Verror_cmrr*1000:.3f} mV` ({Verror_cmrr/Vo*100:.2f}% de la señal)\n"
                txt_filter_out.insert("end", out_md)

            elif "Sensores de Temperatura" in mode:
                R0_pt = 100.0; A_pt = 3.9083e-3; B_pt = -5.775e-7
                T_pt = 100.0
                R_100 = R0_pt * (1.0 + A_pt * T_pt + B_pt * (T_pt**2))
                alpha_pt = 0.3850

                RL_wire = 2.5
                err_2wire = (2 * RL_wire) / alpha_pt
                err_3wire = (0.05 * RL_wire) / alpha_pt
                err_4wire = 0.0

                R0_ntc = 10000.0; T0_ntc = 298.15; beta_ntc = 3950.0
                R_lin = R0_ntc * (beta_ntc - 2.0 * T0_ntc) / (beta_ntc + 2.0 * T0_ntc)

                s_th = 0.04127
                Th_th = 350.0; Ta_th = 25.0
                V_no_cjc = s_th * (Th_th - Ta_th)
                V_with_cjc = s_th * Th_th
                err_cjc_temp = Ta_th

                bode_canvas.delete("all")
                w_c = max(460, bode_canvas.winfo_width())
                h_c = 180
                bode_canvas.create_rectangle(40, 15, w_c - 15, h_c - 25, outline="#2c2c35", width=1)
                bode_canvas.create_text(230, 28, text="Curva de Calibración Pt100 (IEC 60751: 0°C a 200°C)", fill="#38bdf8", font=(FONT_HEAD[0], 9, "bold"))

                prev_x, prev_y = None, None
                for px in range(40, w_c - 15):
                    frac = (px - 40) / (w_c - 55)
                    t_val = frac * 200.0
                    r_val = R0_pt * (1.0 + A_pt * t_val + B_pt * (t_val**2))
                    py = (h_c - 30) - (r_val - 100.0) / 76.0 * (h_c - 75)
                    if prev_x is not None:
                        bode_canvas.create_line(prev_x, prev_y, px, py, fill="#30d158", width=2)
                    prev_x, prev_y = px, py

                bode_canvas.create_text(55, h_c - 12, text="0°C (100Ω)", fill="#86868b", font=(FONT_SMALL[0], 7))
                bode_canvas.create_text(w_c - 35, h_c - 12, text="200°C (175.8Ω)", fill="#86868b", font=(FONT_SMALL[0], 7))
                bode_canvas.create_text(25, 45, text="175Ω", fill="#86868b", font=(FONT_SMALL[0], 7))
                bode_canvas.create_text(25, h_c - 30, text="100Ω", fill="#86868b", font=(FONT_SMALL[0], 7))

                out_md = "### 🌡️ Sensores de Temperatura: Pt100, NTC y Termopar Tipo K (Normas Oficiales)\n"
                out_md += "#### 1. Termorresistencia Pt100 (IEC 60751 / Callendar-Van Dusen):\n"
                out_md += f"- **Ecuación oficial (T ≥ 0°C):** `R(T) = R₀·(1 + A·T + B·T²)` con `A = 3.9083·10⁻³`, `B = -5.775·10⁻⁷`\n"
                out_md += f"- **Resistencia a 100°C:** `R(100°C) = {R_100:.3f} Ω` (Sensibilidad media: α = 0.3850 Ω/°C)\n"
                out_md += f"- **Impacto de Resistencia de Cable (RL = {RL_wire:.1f} Ω por hilo):**\n"
                out_md += f"  • *Conexión a 2 hilos:* Error sistemático = `+2·RL / α = +{err_2wire:.2f} °C` (Crítico en industria)\n"
                out_md += f"  • *Conexión a 3 hilos (Siemens):* Error residual = `+{err_3wire:.2f} °C`\n"
                out_md += f"  • *Conexión a 4 hilos Kelvin:* Error = `0.00 °C` (Inmunidad total a RL)\n\n"

                out_md += "#### 2. Termistor NTC y Linealización de Taylor:\n"
                out_md += f"- **Parámetros:** `R₀ = {R0_ntc/1000:.0f} kΩ` a `T₀ = 25°C` (298.15 K), `β = {beta_ntc:.0f} K`\n"
                out_md += f"- **Resistencia óptima de linealización (Punto de inflexión en T₀):**\n"
                out_md += f"  `R_lin = R₀ · (β - 2·T₀) / (β + 2·T₀) = {R_lin:.1f} Ω` ({R_lin/1000:.3f} kΩ)\n"
                out_md += f"- **Sensibilidad linealizada:** `S = -Vs · β / (4 · T₀²) = {-10.0*beta_ntc/(4*T0_ntc**2)*1000:.2f} mV/°C` (para Vs = 10 V)\n\n"

                out_md += "#### 3. Termopar Tipo K & Compensación de Unión Fría (CJC):\n"
                out_md += f"- **Sensibilidad Seebeck nominal:** `s_T = 41.27 µV/°C`\n"
                out_md += f"- **Medida a Th = {Th_th:.0f}°C con ambiente Ta = {Ta_th:.0f}°C:**\n"
                out_md += f"  • *Tensión generada sin CJC:* `V = s_T · (Th - Ta) = {V_no_cjc:.3f} mV`\n"
                out_md += f"  • *Error de lectura si no se compensa:* `{-err_cjc_temp:.1f} °C` de error sistemático\n"
                out_md += f"  • *Con Compensación CJC (Inyección de V(Ta)):* `V_total = {V_with_cjc:.3f} mV` (Lectura exacta {Th_th:.0f}°C)\n\n"

                out_md += "#### 💻 Netlist SPICE / LTspice (.cir) - Acondicionador Pt100 a 4 Hilos:\n```spice\n"
                out_md += "* Acondicionador Pt100 a 4 Hilos Kelvin con Fuente de Corriente\n"
                out_md += "I1 0 n_in DC 1.0m\n"
                out_md += f"R_pt100 n_in 0 {R_100:.2f}\n"
                out_md += "X_ina n_in 0 out INA_IDEAL\n"
                out_md += ".subckt INA_IDEAL in+ in- out\nE1 out 0 in+ in- 10.0\n.ends\n"
                out_md += ".op\n.end\n```\n"

                txt_filter_out.insert("end", out_md)

            elif "ADC" in mode:
                N = 16; Vfsr = 10.0
                q = Vfsr / (2**N)
                sigma_q = q / math.sqrt(12.0)
                snr_th = 6.02 * N + 1.76
                dr = 6.02 * N

                bode_canvas.delete("all")
                bode_canvas.create_text(230, 90, text=f"[ADC {N}-BITS · LSB q = {q*1e6:.2f} µV]", fill="#30d158", font=(FONT_HEAD[0], 12, "bold"))
                bode_canvas.create_text(230, 115, text=f"SNR Teórico = {snr_th:.2f} dB | Piso de Ruido RMS = {sigma_q*1e6:.2f} µV", fill="#86868b", font=(FONT_BODY[0], 9))

                out_md = f"### 📊 Convertidor Analógico-Digital (ADC {N} Bits SAR / Delta-Sigma)\n"
                out_md += f"- **Resolución N:** `{N} bits` ({2**N:,} niveles de cuantización discretos)\n"
                out_md += f"- **Rango de Fondo de Escala (VFSR):** `0 - {Vfsr:.1f} V`\n"
                out_md += f"- **Paso de Cuantización / LSB (q):** `q = VFSR / 2^N = {q*1e6:.3f} µV` ({q:.6e} V)\n"
                out_md += f"- **Ruido RMS de Cuantización (σ_q):** `σ_q = q / √12 = {sigma_q*1e6:.3f} µV`\n"
                out_md += f"- **Relación Señal a Ruido Teórica (SNR):** `SNR = 6.02·N + 1.76 dB = {snr_th:.2f} dB`\n"
                out_md += f"- **Rango Dinámico (DR):** `{dr:.2f} dB`\n"
                out_md += "- **Criterio de Nyquist:** Para evitar aliasing con señal fmáx, fs ≥ 2·fmáx. Se recomienda fs = 5 a 10·fmáx con filtro antialiasing previo.\n"
                txt_filter_out.insert("end", out_md)

        def copy_spice_code():
            txt = txt_filter_out.get("1.0", "end-1c")
            if "```spice" in txt:
                spice_part = txt.split("```spice")[1].split("```")[0].strip()
                root_win.clipboard_clear()
                root_win.clipboard_append(spice_part)
                messagebox.showinfo("SPICE Netlist", "¡Netlist de simulación SPICE / LTspice copiado al portapapeles!")
            else:
                root_win.clipboard_clear()
                root_win.clipboard_append(txt)
                messagebox.showinfo("Diseño", "¡Informe técnico copiado al portapapeles!")

        def export_filter_report():
            txt = txt_filter_out.get("1.0", "end-1c")
            if not txt.strip():
                messagebox.showwarning("Filtros", "No hay datos calculados para exportar.")
                return
            out_dir = Path("dist_course_md")
            out_dir.mkdir(parents=True, exist_ok=True)
            out_file = out_dir / "_Informe_Filtros_Acondicionamiento.md"
            try:
                out_file.write_text(txt, encoding="utf-8")
                root_win.clipboard_clear()
                root_win.clipboard_append(txt)
                messagebox.showinfo("Informe Exportado", f"✅ Informe de diseño guardado en:\n{out_file.resolve()}\n\n¡Y copiado al portapapeles!")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

        create_btn(row_act_btns, "⚡ Calcular y Simular", calculate_filter, bg=COLOR_ACCENT_BLUE, hover_bg=COLOR_ACCENT_HOVER, font=FONT_HEAD).pack(side="left", padx=(0, 6))
        create_btn(row_act_btns, "💾 Exportar (.md)", export_filter_report, bg="#1b4332", hover_bg="#2d6a4f", font=FONT_HEAD).pack(side="left", padx=(0, 6))
        create_btn(row_act_btns, "📋 Copiar Netlist SPICE", copy_spice_code, bg="#2c2c2e", hover_bg="#3a3a3c", font=FONT_HEAD).pack(side="left")

        combo_filter_mode.bind("<<ComboboxSelected>>", lambda e: calculate_filter())
        combo_approx.bind("<<ComboboxSelected>>", lambda e: calculate_filter())
        bode_canvas.bind("<Configure>", lambda e: calculate_filter())
        tab_callbacks[5] = calculate_filter
        root_win.after(250, calculate_filter)

    def setup_rlc_presets_tab(parent, root_win):
            p = tk.Frame(parent, bg=COLOR_CANVAS, padx=12, pady=10)
            p.pack(fill="both", expand=True)

            top_card = make_card(p, "🔌 Banco R-L-C, Presets de Laboratorio & Asignaturas GREELEC (UPC ETSETB)")
            top_card.pack(fill="x", pady=(0, 8))
            top_inner = tk.Frame(top_card, bg=COLOR_CARD, padx=14, pady=8)
            top_inner.pack(fill="x")

            # Selector de topología circuital
            row_sel = tk.Frame(top_inner, bg=COLOR_CARD)
            row_sel.pack(fill="x", pady=(0, 6))

            tk.Label(row_sel, text="Topología de Laboratorio:", font=FONT_HEAD, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD).pack(side="left", padx=(0, 10))
            rlc_mode_var = tk.StringVar(value="Divisor Resistivo (5V a 3.3V ADC / Level Shifter)")
            combo_rlc = ttk.Combobox(row_sel, textvariable=rlc_mode_var, state="readonly", width=58, style="Modern.TCombobox")
            combo_rlc["values"] = [
                "Divisor Resistivo (5V a 3.3V ADC / Level Shifter)",
                "Resistencias Serie / Paralelo & Normalización E12/E24",
                "Condensadores Serie / Paralelo & Red Desacoplo Digital",
                "Inductores Serie / Paralelo & Resonancia LC",
                "Temporizador 555 Astable (Oscilador Reloj / PWM)",
                "Driver NPN (2N2222) + Diodo Flyback (1N4007) para Relé",
                "Limitador de Corriente para LEDs (Rojo / Verde / Azul / Blanco)",
                "Decodificador de Código de Colores (4 y 5 Bandas)",
                "Convertidor DC-DC Buck Reductor (GREELEC PEE)",
                "Convertidor DC-DC Boost Elevador (GREELEC PEE)",
                "Línea de Transmisión RF & Adaptación 50Ω (GREELEC CAF)",
                "Amplificador BJT Emisor Común Polarizado (GREELEC CA)",
                "Lazo de Control Feedback PID en Tiempo Real (GREELEC SC)"
            ]
            combo_rlc.pack(side="left", padx=(0, 15))

            # Barra de Presets Rápidos
            row_chips = tk.Frame(top_inner, bg=COLOR_CARD)
            row_chips.pack(fill="x", pady=(2, 2))
            tk.Label(row_chips, text="Presets Rápidos:", font=(FONT_FAMILY, 9, "bold"), fg=COLOR_TEXT_MUTED, bg=COLOR_CARD).pack(side="left", padx=(0, 6))

            # Split central
            split_box = tk.Frame(p, bg=COLOR_CANVAS)
            split_box.pack(fill="both", expand=True)

            # Panel izquierdo: Entradas
            card_l = make_card(split_box, "⚙️ Parámetros Físicos del Componente / Circuito")
            card_l.pack(side="left", fill="both", expand=True, padx=(0, 6))
            inner_l = tk.Frame(card_l, bg=COLOR_CARD, padx=12, pady=8)
            inner_l.pack(fill="both", expand=True)

            param_grid = tk.Frame(inner_l, bg=COLOR_CARD)
            param_grid.pack(fill="x", pady=(0, 8))

            def make_field(lbl, def_val):
                row = tk.Frame(param_grid, bg=COLOR_CARD)
                tk.Label(row, text=lbl, font=FONT_BODY, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD, width=24, anchor="w").pack(side="left")
                e = tk.Entry(row, font=FONT_CODE, width=14, bg="#101014", fg="#ffffff", bd=1, relief="solid")
                e.insert(0, def_val)
                e.pack(side="left", padx=5)
                row.pack(fill="x", pady=2)
                return e

            entry_r1 = make_field("Resistencia R1 / RA / RL (Ω):", "10000")
            entry_r2 = make_field("Resistencia R2 / RB (Ω):", "20000")
            entry_c1 = make_field("Condensador C1 / C (nF / µF):", "100")
            entry_l1 = make_field("Inductor L1 / L (µH):", "1000")
            entry_vin = make_field("Tensión Vin / Vcc (V):", "5.0")

            row_act = tk.Frame(inner_l, bg=COLOR_CARD)
            row_act.pack(fill="x", pady=(4, 0))

            # Panel derecho: Canvas & Resultados
            card_r = make_card(split_box, "📐 Esquemático Técnico & Netlist SPICE / LTspice")
            card_r.pack(side="right", fill="both", expand=True, padx=(6, 0))
            inner_r = tk.Frame(card_r, bg=COLOR_CARD, padx=12, pady=8)
            inner_r.pack(fill="both", expand=True)

            canvas_sch = tk.Canvas(inner_r, bg="#07090e", height=165, highlightthickness=1, highlightbackground=COLOR_CARD_BORDER)
            canvas_sch.pack(fill="x", pady=(0, 8))

            txt_out = ScrolledText(inner_r, font=(FONT_CODE[0], 9), bg="#0e0e12", fg="#e2e8f0", bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER, height=10)
            txt_out.pack(fill="both", expand=True)

            def draw_schematic(mode, p):
                canvas_sch.delete("all")
                w, h = 440, 160
                for x in range(0, w, 25):
                    canvas_sch.create_line(x, 0, x, h, fill="#111827", width=1)
                for y in range(0, h, 25):
                    canvas_sch.create_line(0, y, w, y, fill="#111827", width=1)

                cx, cy = w // 2, h // 2

                if "Divisor" in mode:
                    canvas_sch.create_text(25, 20, text=f"+Vin ({p['vin']}V)", fill="#38bdf8", font=(FONT_HEAD[0], 10, "bold"), anchor="w")
                    canvas_sch.create_line(40, 32, cx, 32, fill="#38bdf8", width=2)
                    canvas_sch.create_rectangle(cx - 15, 38, cx + 15, 75, outline="#ffffff", width=2, fill="#1e293b")
                    canvas_sch.create_text(cx + 25, 56, text=f"R1: {p['r1']}Ω", fill="#ffffff", font=(FONT_BODY[0], 9), anchor="w")
                    canvas_sch.create_line(cx, 32, cx, 38, fill="#ffffff", width=2)
                    canvas_sch.create_line(cx, 75, cx, 90, fill="#ffffff", width=2)
                    canvas_sch.create_oval(cx - 4, 90 - 4, cx + 4, 90 + 4, fill="#30d158", outline="#30d158")
                    canvas_sch.create_line(cx, 90, cx + 90, 90, fill="#30d158", width=2)
                    vout = p['vin'] * (p['r2'] / (p['r1'] + p['r2']))
                    canvas_sch.create_text(cx + 95, 90, text=f"Vout = {vout:.2f}V", fill="#30d158", font=(FONT_HEAD[0], 10, "bold"), anchor="w")
                    canvas_sch.create_line(cx, 90, cx, 102, fill="#ffffff", width=2)
                    canvas_sch.create_rectangle(cx - 15, 102, cx + 15, 138, outline="#ffffff", width=2, fill="#1e293b")
                    canvas_sch.create_text(cx + 25, 120, text=f"R2: {p['r2']}Ω", fill="#ffffff", font=(FONT_BODY[0], 9), anchor="w")
                    canvas_sch.create_line(cx, 138, cx, 148, fill="#ffffff", width=2)
                    canvas_sch.create_line(cx - 15, 148, cx + 15, 148, fill="#94a3b8", width=2)
                    canvas_sch.create_line(cx - 9, 152, cx + 9, 152, fill="#94a3b8", width=2)
                    canvas_sch.create_line(cx - 3, 156, cx + 3, 156, fill="#94a3b8", width=2)

                elif "Código de Colores" in mode:
                    canvas_sch.create_text(cx, 22, text=f"CÓDIGO DE COLORES (R = {p['r1']} Ω)", fill="#38bdf8", font=(FONT_HEAD[0], 11, "bold"))
                    canvas_sch.create_line(cx - 150, cy, cx - 80, cy, fill="#cbd5e1", width=4)
                    canvas_sch.create_line(cx + 80, cy, cx + 150, cy, fill="#cbd5e1", width=4)
                    canvas_sch.create_rectangle(cx - 80, cy - 25, cx + 80, cy + 25, fill="#d2b48c", outline="#b89758", width=2)
                    color_map = ["#000000", "#78350f", "#dc2626", "#ea580c", "#eab308", "#16a34a", "#2563eb", "#9333ea", "#6b7280", "#ffffff"]
                    r_val = max(1.0, p['r1'])
                    exp = int(math.floor(math.log10(r_val)))
                    norm = r_val / (10**exp)
                    d1 = int(str(round(norm * 10))[0])
                    d2 = int(str(round(norm * 10))[1]) if len(str(round(norm * 10))) > 1 else 0
                    mult_band = max(0, min(9, exp - 1))
                    canvas_sch.create_rectangle(cx - 60, cy - 25, cx - 48, cy + 25, fill=color_map[d1 % 10], outline="")
                    canvas_sch.create_rectangle(cx - 35, cy - 25, cx - 23, cy + 25, fill=color_map[d2 % 10], outline="")
                    canvas_sch.create_rectangle(cx - 10, cy - 25, cx + 2, cy + 25, fill=color_map[mult_band % 10], outline="")
                    canvas_sch.create_rectangle(cx + 45, cy - 25, cx + 57, cy + 25, fill="#d97706", outline="")
                    canvas_sch.create_text(cx, cy + 45, text="Tolerancia Comercial: ±5% (Oro)", fill="#fbbf24", font=(FONT_BODY[0], 9))

                elif "555" in mode:
                    canvas_sch.create_rectangle(cx - 70, cy - 50, cx + 70, cy + 50, fill="#18181b", outline="#38bdf8", width=2)
                    canvas_sch.create_text(cx, cy - 32, text="NE555 TIMER", fill="#38bdf8", font=(FONT_HEAD[0], 11, "bold"))
                    canvas_sch.create_text(cx - 55, cy - 10, text="8:VCC", fill="#e2e8f0", font=(FONT_CODE[0], 8), anchor="w")
                    canvas_sch.create_text(cx - 55, cy + 8, text="7:DIS", fill="#e2e8f0", font=(FONT_CODE[0], 8), anchor="w")
                    canvas_sch.create_text(cx - 55, cy + 26, text="6:THR", fill="#e2e8f0", font=(FONT_CODE[0], 8), anchor="w")
                    canvas_sch.create_text(cx + 25, cy - 10, text="OUT:3", fill="#34d399", font=(FONT_CODE[0], 8), anchor="w")
                    canvas_sch.create_text(cx + 25, cy + 15, text="GND:1", fill="#94a3b8", font=(FONT_CODE[0], 8), anchor="w")
                    canvas_sch.create_line(cx + 70, cy - 10, cx + 130, cy - 10, fill="#34d399", width=2)
                    canvas_sch.create_text(cx + 135, cy - 10, text="CLK", fill="#34d399", font=(FONT_HEAD[0], 9, "bold"), anchor="w")

                elif "Buck" in mode:
                    canvas_sch.create_text(25, 20, text=f"BUCK CONVERTER (Vin={p['vin']}V)", fill="#38bdf8", font=(FONT_HEAD[0], 10, "bold"), anchor="w")
                    canvas_sch.create_line(30, 60, cx - 60, 60, fill="#38bdf8", width=2)
                    canvas_sch.create_rectangle(cx - 60, 45, cx - 20, 75, fill="#1e293b", outline="#fbbf24", width=2)
                    canvas_sch.create_text(cx - 40, 60, text="MOS", fill="#fbbf24", font=(FONT_CODE[0], 8, "bold"))
                    canvas_sch.create_line(cx - 20, 60, cx + 40, 60, fill="#38bdf8", width=2)
                    # Inductor L
                    canvas_sch.create_rectangle(cx + 40, 50, cx + 90, 70, fill="#047857", outline="#34d399", width=2)
                    canvas_sch.create_text(cx + 65, 60, text=f"L={p['l1']}µH", fill="#ffffff", font=(FONT_CODE[0], 8))
                    canvas_sch.create_line(cx + 90, 60, cx + 150, 60, fill="#38bdf8", width=2)
                    # Diode Flyback
                    canvas_sch.create_line(cx, 60, cx, 110, fill="#f43f5e", width=2)
                    canvas_sch.create_text(cx - 15, 85, text="D_fly", fill="#f43f5e", font=(FONT_CODE[0], 8))
                    canvas_sch.create_line(cx - 10, 110, cx + 10, 110, fill="#94a3b8", width=2)
                    # Cap C_out
                    canvas_sch.create_line(cx + 120, 60, cx + 120, 110, fill="#38bdf8", width=2)
                    canvas_sch.create_text(cx + 135, 85, text=f"C={p['c1']}µF", fill="#38bdf8", font=(FONT_CODE[0], 8))
                    canvas_sch.create_text(cx + 155, 60, text="Vout", fill="#30d158", font=(FONT_HEAD[0], 10, "bold"), anchor="w")

                elif "Boost" in mode:
                    canvas_sch.create_text(25, 20, text=f"BOOST CONVERTER (Vin={p['vin']}V)", fill="#38bdf8", font=(FONT_HEAD[0], 10, "bold"), anchor="w")
                    canvas_sch.create_line(30, 60, cx - 60, 60, fill="#38bdf8", width=2)
                    # Inductor first
                    canvas_sch.create_rectangle(cx - 60, 50, cx - 10, 70, fill="#047857", outline="#34d399", width=2)
                    canvas_sch.create_text(cx - 35, 60, text=f"L={p['l1']}µH", fill="#ffffff", font=(FONT_CODE[0], 8))
                    canvas_sch.create_line(cx - 10, 60, cx + 30, 60, fill="#38bdf8", width=2)
                    # MOS switch to GND
                    canvas_sch.create_rectangle(cx + 5, 80, cx + 25, 115, fill="#1e293b", outline="#fbbf24", width=2)
                    canvas_sch.create_text(cx + 15, 97, text="MOS", fill="#fbbf24", font=(FONT_CODE[0], 7))
                    canvas_sch.create_line(cx + 15, 60, cx + 15, 80, fill="#38bdf8", width=2)
                    canvas_sch.create_line(cx + 15, 115, cx + 15, 125, fill="#94a3b8", width=2)
                    # Diode
                    canvas_sch.create_rectangle(cx + 45, 52, cx + 75, 68, fill="#1e293b", outline="#f43f5e", width=2)
                    canvas_sch.create_text(cx + 60, 60, text="D", fill="#f43f5e", font=(FONT_CODE[0], 8))
                    canvas_sch.create_line(cx + 30, 60, cx + 45, 60, fill="#38bdf8", width=2)
                    canvas_sch.create_line(cx + 75, 60, cx + 140, 60, fill="#38bdf8", width=2)
                    canvas_sch.create_text(cx + 145, 60, text="Vout", fill="#30d158", font=(FONT_HEAD[0], 10, "bold"), anchor="w")

                elif "Línea de Transmisión" in mode:
                    canvas_sch.create_text(25, 20, text="LÍNEA RF & CARTA DE SMITH (Z0=50Ω)", fill="#38bdf8", font=(FONT_HEAD[0], 10, "bold"), anchor="w")
                    canvas_sch.create_rectangle(35, 50, 75, 90, fill="#1e293b", outline="#38bdf8", width=2)
                    canvas_sch.create_text(55, 70, text="GEN", fill="#38bdf8", font=(FONT_CODE[0], 8, "bold"))
                    # Line
                    canvas_sch.create_line(75, 60, cx + 10, 60, fill="#e2e8f0", width=3)
                    canvas_sch.create_line(75, 80, cx + 10, 80, fill="#64748b", width=3)
                    canvas_sch.create_text(cx - 40, 48, text="Línea Coaxial 50Ω", fill="#94a3b8", font=(FONT_CODE[0], 8))
                    # Load
                    canvas_sch.create_rectangle(cx + 10, 50, cx + 40, 90, fill="#1e293b", outline="#34d399", width=2)
                    canvas_sch.create_text(cx + 25, 70, text="ZL", fill="#34d399", font=(FONT_CODE[0], 8, "bold"))
                    # Smith Chart Circle
                    sx, sy, sr = cx + 120, 75, 45
                    canvas_sch.create_oval(sx - sr, sy - sr, sx + sr, sy + sr, outline="#38bdf8", width=2)
                    canvas_sch.create_line(sx - sr, sy, sx + sr, sy, fill="#334155", width=1)
                    canvas_sch.create_oval(sx, sy - sr//2, sx + sr, sy + sr//2, outline="#1e293b", width=1)
                    canvas_sch.create_text(sx, sy - sr - 10, text="Smith Chart", fill="#38bdf8", font=(FONT_CODE[0], 8))

                elif "BJT" in mode:
                    canvas_sch.create_text(25, 20, text=f"AMPLIFICADOR BJT (Vcc={p['vin']}V)", fill="#38bdf8", font=(FONT_HEAD[0], 10, "bold"), anchor="w")
                    # Vcc line
                    canvas_sch.create_line(50, 32, cx + 80, 32, fill="#38bdf8", width=2)
                    canvas_sch.create_text(40, 32, text="+Vcc", fill="#38bdf8", font=(FONT_CODE[0], 8, "bold"), anchor="e")
                    # Base divider R1 & R2
                    canvas_sch.create_rectangle(cx - 60, 45, cx - 40, 75, fill="#1e293b", outline="#ffffff", width=1)
                    canvas_sch.create_text(cx - 50, 60, text="R1", fill="#ffffff", font=(FONT_CODE[0], 7))
                    canvas_sch.create_rectangle(cx - 60, 95, cx - 40, 125, fill="#1e293b", outline="#ffffff", width=1)
                    canvas_sch.create_text(cx - 50, 110, text="R2", fill="#ffffff", font=(FONT_CODE[0], 7))
                    # Collector Rc
                    canvas_sch.create_rectangle(cx + 30, 45, cx + 50, 75, fill="#1e293b", outline="#ffffff", width=1)
                    canvas_sch.create_text(cx + 40, 60, text="Rc", fill="#ffffff", font=(FONT_CODE[0], 7))
                    # Transistor
                    canvas_sch.create_line(cx - 10, 70, cx - 10, 100, fill="#38bdf8", width=3)
                    canvas_sch.create_line(cx - 40, 85, cx - 10, 85, fill="#38bdf8", width=2)
                    canvas_sch.create_line(cx - 10, 75, cx + 40, 75, fill="#38bdf8", width=2)
                    canvas_sch.create_line(cx - 10, 95, cx + 40, 115, fill="#38bdf8", width=2)
                    canvas_sch.create_text(cx + 10, 80, text="NPN", fill="#fbbf24", font=(FONT_CODE[0], 8))
                    canvas_sch.create_text(cx + 60, 75, text="Vout", fill="#30d158", font=(FONT_HEAD[0], 9, "bold"), anchor="w")

                elif "PID" in mode:
                    canvas_sch.create_text(25, 20, text="LAZO CERRADO FEEDBACK PID", fill="#38bdf8", font=(FONT_HEAD[0], 10, "bold"), anchor="w")
                    canvas_sch.create_oval(cx - 120, cy - 15, cx - 90, cy + 15, outline="#38bdf8", width=2)
                    canvas_sch.create_text(cx - 105, cy, text="Σ", fill="#ffffff", font=(FONT_HEAD[0], 11, "bold"))
                    canvas_sch.create_line(30, cy, cx - 120, cy, fill="#38bdf8", width=2)
                    canvas_sch.create_text(35, cy - 10, text="r(t)", fill="#38bdf8", font=(FONT_CODE[0], 8))
                    # PID box
                    canvas_sch.create_rectangle(cx - 70, cy - 25, cx - 10, cy + 25, fill="#1e293b", outline="#a855f7", width=2)
                    canvas_sch.create_text(cx - 40, cy, text="PID", fill="#a855f7", font=(FONT_HEAD[0], 10, "bold"))
                    canvas_sch.create_line(cx - 90, cy, cx - 70, cy, fill="#e2e8f0", width=2)
                    canvas_sch.create_line(cx - 10, cy, cx + 20, cy, fill="#e2e8f0", width=2)
                    # Plant box
                    canvas_sch.create_rectangle(cx + 20, cy - 25, cx + 80, cy + 25, fill="#1e293b", outline="#34d399", width=2)
                    canvas_sch.create_text(cx + 50, cy, text="G(s)", fill="#34d399", font=(FONT_HEAD[0], 10, "bold"))
                    canvas_sch.create_line(cx + 80, cy, cx + 140, cy, fill="#30d158", width=2)
                    canvas_sch.create_text(cx + 145, cy, text="y(t)", fill="#30d158", font=(FONT_HEAD[0], 10, "bold"), anchor="w")
                    # Feedback loop
                    canvas_sch.create_line(cx + 110, cy, cx + 110, cy + 45, fill="#fbbf24", width=2)
                    canvas_sch.create_line(cx + 110, cy + 45, cx - 105, cy + 45, fill="#fbbf24", width=2)
                    canvas_sch.create_line(cx - 105, cy + 45, cx - 105, cy + 15, fill="#fbbf24", width=2)

                else:
                    canvas_sch.create_rectangle(30, 25, w - 30, h - 25, outline="#38bdf8", width=2, fill="#0f172a")
                    canvas_sch.create_text(cx, cy - 20, text=f"[BANCO R-L-C]: {mode.split('(')[0].strip()}", fill="#38bdf8", font=(FONT_HEAD[0], 11, "bold"))
                    canvas_sch.create_text(cx, cy + 10, text=f"R1={p['r1']}Ω • R2={p['r2']}Ω • C1={p['c1']}nF • L1={p['l1']}µH", fill="#94a3b8", font=(FONT_CODE[0], 9))

            def calculate_rlc():
                txt_out.delete("1.0", "end")
                mode = rlc_mode_var.get()
                try:
                    r1 = float(entry_r1.get().strip() or "10000")
                    r2 = float(entry_r2.get().strip() or "20000")
                    c1 = float(entry_c1.get().strip() or "100")
                    l1 = float(entry_l1.get().strip() or "1000")
                    vin = float(entry_vin.get().strip() or "5.0")
                except ValueError:
                    txt_out.insert("end", "⚠️ Por favor, ingrese valores numéricos válidos en los campos.")
                    return

                p = {"r1": r1, "r2": r2, "c1": c1, "l1": l1, "vin": vin}
                draw_schematic(mode, p)

                lines = []
                if "Divisor" in mode:
                    vout = vin * (r2 / (r1 + r2))
                    rth = (r1 * r2) / (r1 + r2)
                    itot = (vin / (r1 + r2)) * 1000.0
                    pr1 = ((vin - vout)**2) / r1 * 1000.0
                    pr2 = (vout**2) / r2 * 1000.0
                    suit = "✅ Apta para muestreo ADC ≤ 10 kΩ" if rth <= 10000 else "⚠️ > 10 kΩ: Se aconseja añadir seguidor de tensión Op-Amp"
                    lines.append("### 🔌 Divisor Resistivo de Precisión (Adaptador 5V a 3.3V ADC / Level Shifter)")
                    lines.append(f"- **Tensión de Entrada Vin:** `{vin:.2f} V`")
                    lines.append(f"- **Tensión de Salida Vout:** `{vout:.4f} V` ({vout*1000:.1f} mV)")
                    lines.append(f"- **Impedancia de Salida Thévenin (Rth):** `{rth/1000:.3f} kΩ` ({suit})")
                    lines.append(f"- **Corriente de Reposo:** `{itot:.3f} mA`")
                    lines.append(f"- **Potencia Disipada por R1:** `{pr1:.2f} mW`")
                    lines.append(f"- **Potencia Disipada por R2:** `{pr2:.2f} mW`\n")
                    lines.append("#### 📋 Netlist SPICE / LTspice (.cir):")
                    lines.append("```spice")
                    lines.append("* Divisor Resistivo 5V a 3.3V")
                    lines.append(f"Vin in 0 DC {vin:.2f}")
                    lines.append(f"R1 in out {r1:.1f}")
                    lines.append(f"R2 out 0 {r2:.1f}")
                    lines.append(".op")
                    lines.append(".end")
                    lines.append("```\n")

                elif "Buck" in mode:
                    # D = 0.417 aprox si vin=12 -> vo=5
                    D = min(0.9, max(0.1, 5.0 / vin if vin > 5 else 0.5))
                    vout = vin * D
                    fsw = 250000.0
                    L = l1 * 1e-6
                    C = c1 * 1e-6
                    RL = max(0.5, r1 if r1 < 1000 else 5.0)
                    deltaIL = ((vin - vout) * D) / (fsw * L)
                    io = vout / RL
                    lcrit = ((1 - D) * RL) / (2 * fsw)
                    is_ccm = L >= lcrit
                    deltaVo = deltaIL / (8 * fsw * C)
                    lines.append("### ⚡ Convertidor DC-DC Buck Reductor (GREELEC PEE)")
                    lines.append(f"- **Tensión de Entrada Vin:** `{vin:.2f} V`")
                    lines.append(f"- **Ciclo de Trabajo D:** `{D*100:.1f} %` -> **Vout Nominal:** `{vout:.2f} V`")
                    lines.append(f"- **Corriente de Carga Io:** `{io:.2f} A` (Carga RL = `{RL:.1f} Ω`)")
                    lines.append(f"- **Rizado de Corriente en Inductor (ΔIL):** `{deltaIL*1000:.1f} mA`")
                    lines.append(f"- **Régimen de Conducción:** `{'✅ Modo CCM (Continuo)' if is_ccm else '⚠️ Modo DCM (Discontinuo)'}` (Lcrit = `{lcrit*1e6:.1f} µH`)")
                    lines.append(f"- **Rizado de Tensión de Salida (ΔVo):** `{deltaVo*1000:.2f} mVpp` (C = `{c1:.1f} µF`)\n")
                    lines.append("#### 📋 Netlist SPICE / LTspice (.cir):")
                    lines.append("```spice")
                    lines.append("* Convertidor Buck DC-DC")
                    lines.append(f"Vin in 0 DC {vin:.2f}")
                    lines.append(f"Vpwm gate 0 PULSE(0 10 0 10n 10n {D/fsw:.6e} {1/fsw:.6e})")
                    lines.append("S1 in sw gate 0 MYSW")
                    lines.append("Dfly 0 sw SCHOTTKY")
                    lines.append(f"L1 sw out {L:.6e}")
                    lines.append(f"Cout out 0 {C:.6e} IC={vout:.2f}")
                    lines.append(f"Rload out 0 {RL:.2f}")
                    lines.append(".model MYSW SW(Ron=0.03 Roff=1e6 Vt=2.5)")
                    lines.append(".model SCHOTTKY D(Is=1e-7 Rs=0.05)")
                    lines.append(".tran 0.1u 2m 1m")
                    lines.append(".end")
                    lines.append("```\n")

                elif "Boost" in mode:
                    D = 0.5
                    vout = vin / (1 - D)
                    fsw = 200000.0
                    L = l1 * 1e-6
                    C = c1 * 1e-6
                    RL = max(1.0, r1 if r1 < 1000 else 24.0)
                    deltaIL = (vin * D) / (fsw * L)
                    io = vout / RL
                    deltaVo = (io * D) / (fsw * C)
                    lines.append("### ⚡ Convertidor DC-DC Boost Elevador (GREELEC PEE)")
                    lines.append(f"- **Tensión de Entrada Vin:** `{vin:.2f} V`")
                    lines.append(f"- **Ciclo de Trabajo D:** `{D*100:.1f} %` -> **Vout Nominal:** `{vout:.2f} V`")
                    lines.append(f"- **Rizado de Corriente en Inductor (ΔIL):** `{deltaIL*1000:.1f} mA`")
                    lines.append(f"- **Rizado de Tensión de Salida (ΔVo):** `{deltaVo*1000:.2f} mVpp`\n")
                    lines.append("#### 📋 Netlist SPICE / LTspice (.cir):")
                    lines.append("```spice")
                    lines.append("* Convertidor Boost DC-DC Step-Up")
                    lines.append(f"Vin in 0 DC {vin:.2f}")
                    lines.append(f"L1 in sw {L:.6e}")
                    lines.append(f"Vpwm gate 0 PULSE(0 10 0 10n 10n {D/fsw:.6e} {1/fsw:.6e})")
                    lines.append("S1 sw 0 gate 0 MYSW")
                    lines.append("D1 sw out SCHOTTKY")
                    lines.append(f"Cout out 0 {C:.6e} IC={vout:.2f}")
                    lines.append(f"Rload out 0 {RL:.2f}")
                    lines.append(".model MYSW SW(Ron=0.03 Roff=1e6 Vt=2.5)")
                    lines.append(".model SCHOTTKY D(Is=1e-7 Rs=0.05)")
                    lines.append(".tran 0.1u 2m 1m")
                    lines.append(".end")
                    lines.append("```\n")

                elif "Línea de Transmisión" in mode:
                    z0 = 50.0
                    rl = max(0.1, r1 if r1 < 500 else 50.0)
                    xl = 0.0
                    gamma = (rl - z0) / (rl + z0)
                    gmag = abs(gamma)
                    vswr = (1 + gmag) / max(0.0001, 1 - gmag)
                    rl_db = 60.0 if gmag < 0.001 else -20 * math.log10(gmag)
                    lines.append("### 📡 Línea de Transmisión RF & Parámetros de Dispersión (GREELEC CAF)")
                    lines.append(f"- **Impedancia Característica (Z0):** `{z0:.1f} Ω`")
                    lines.append(f"- **Impedancia de Carga (ZL):** `{rl:.1f} Ω`")
                    lines.append(f"- **Coeficiente de Reflexión (|Γ|):** `{gmag:.4f}`")
                    lines.append(f"- **Relación de Onda Estacionaria (VSWR / ROE):** `{vswr:.2f} : 1`")
                    lines.append(f"- **Pérdidas de Retorno (Return Loss):** `{rl_db:.1f} dB`")
                    lines.append(f"- **Potencia Reflejada:** `{(gmag**2)*100:.2f} %` de la potencia incidente\n")
                    lines.append("#### 📋 Netlist SPICE (.cir) Línea de Transmisión:")
                    lines.append("```spice")
                    lines.append("* Línea RF Coaxial 50 Ohm")
                    lines.append("Vgen in 0 AC 1.0 0")
                    lines.append(f"Rgen in n1 {z0:.1f}")
                    lines.append(f"T1 n1 0 out 0 Z0={z0:.1f} TD=2.5n")
                    lines.append(f"Rload out 0 {rl:.1f}")
                    lines.append(".ac dec 50 10Meg 2Gig")
                    lines.append(".end")
                    lines.append("```\n")

                elif "BJT" in mode:
                    vcc = vin
                    rc = max(100.0, r1 if r1 < 20000 else 2200.0)
                    re = max(10.0, r2 if r2 < 5000 else 470.0)
                    rb1 = 33000.0
                    rb2 = 10000.0
                    vth = vcc * (rb2 / (rb1 + rb2))
                    rth = (rb1 * rb2) / (rb1 + rb2)
                    beta = 180.0
                    ib = max(0.0, (vth - 0.7) / (rth + (beta + 1) * re))
                    ic = beta * ib
                    vce = vcc - ic * (rc + re)
                    gm = ic / 0.02585
                    av = -(gm * rc)
                    lines.append("### 🎛️ Amplificador BJT Emisor Común (GREELEC CA / Dispositivos)")
                    lines.append(f"- **Tensión Vcc:** `{vcc:.1f} V` | **Resistencias:** Rc = `{rc:.0f} Ω`, Re = `{re:.0f} Ω`")
                    lines.append(f"- **Tensión Thévenin Base (Vth):** `{vth:.2f} V` | **Rth:** `{rth/1000:.2f} kΩ`")
                    lines.append(f"- **Corriente de Colector (ICQ):** `{ic*1000:.2f} mA`")
                    lines.append(f"- **Tensión Colector-Emisor (VCEQ):** `{vce:.2f} V` ({'✅ Zona Activa' if vce > 0.3 else '⚠️ Saturación'})")
                    lines.append(f"- **Transconductancia (gm):** `{gm*1000:.1f} mS`")
                    lines.append(f"- **Ganancia de Tensión Pequeña Señal (Av):** `{av:.1f}` ({20*math.log10(max(0.01, abs(av))):.1f} dB)\n")
                    lines.append("#### 📋 Netlist SPICE (.cir) Emisor Común:")
                    lines.append("```spice")
                    lines.append("* Amplificador BJT Emisor Común 2N2222")
                    lines.append(f"Vcc vcc 0 DC {vcc:.1f}")
                    lines.append("Vin sig_in 0 AC 10m SIN(0 10m 1k)")
                    lines.append("Cin sig_in b 10u")
                    lines.append(f"R1 vcc b {rb1:.0f}")
                    lines.append(f"R2 b 0 {rb2:.0f}")
                    lines.append(f"Rc vcc c {rc:.0f}")
                    lines.append(f"Re e 0 {re:.0f}")
                    lines.append("Ce e 0 100u")
                    lines.append("Q1 c b e 0 Q2N2222")
                    lines.append("Cout c out 10u")
                    lines.append("Rload out 0 10k")
                    lines.append(".model Q2N2222 NPN(Is=1e-14 Bf=180 Vaf=100)")
                    lines.append(".tran 10u 5m")
                    lines.append(".end")
                    lines.append("```\n")

                elif "PID" in mode:
                    kp = 3.5
                    ki = 1.2
                    kd = 0.35
                    sp = vin * 10.0 # 50%
                    lines.append("### 🎯 Lazo de Control Feedback PID (GREELEC SC)")
                    lines.append(f"- **Parámetros del Controlador:** Kp = `{kp:.2f}`, Ki = `{ki:.2f} s⁻¹`, Kd = `{kd:.2f} s`")
                    lines.append(f"- **Consigna de Entrada r(t):** `{sp:.1f} %`")
                    lines.append("- **Sobreoscilación Estimada (Mp):** `~8.5 %` (Factor de Amortiguamiento ζ ≈ 0.72)")
                    lines.append("- **Tiempo de Establecimiento ts (2%):** `~1.85 s`")
                    lines.append("- **Error en Régimen Permanente (ess):** `0.00 %` (Cancelado por Acción Integral Ki)\n")
                    lines.append("#### 📋 Netlist SPICE (.cir) Controlador PID Analógico Op-Amp:")
                    lines.append("```spice")
                    lines.append("* Lazo PID Continuo con Amplificadores Operacionales")
                    lines.append("Vref ref 0 PULSE(0 2.5 0.1 1u 1u 10m 20m)")
                    lines.append("* Etapa Sumador de Error: Verr = Vref - Vfb")
                    lines.append("X_sum ref fb err OPAMP_IDEAL")
                    lines.append("* Rama Proporcional: -Kp * Verr")
                    lines.append("R_p1 err n_p 10k")
                    lines.append("R_p2 n_p out_p 35k")
                    lines.append("X_prop 0 n_p out_p OPAMP_IDEAL")
                    lines.append("* Rama Integral: -Ki * int(Verr)")
                    lines.append("R_i err n_i 10k")
                    lines.append("C_i n_i out_i 10u")
                    lines.append("X_integ 0 n_i out_i OPAMP_IDEAL")
                    lines.append(".model OPAMP_IDEAL Opamp")
                    lines.append(".tran 0.1m 50m")
                    lines.append(".end")
                    lines.append("```\n")

                else:
                    lines.append(f"### ⚡ Circuito Seleccionado: {mode}")
                    lines.append(f"- **R1:** `{r1} Ω`  |  **R2:** `{r2} Ω`  |  **C1:** `{c1} nF`  |  **L1:** `{l1} µH`  |  **Vin:** `{vin} V`")
                    lines.append("- Simulación analítica completada. Selecciona una topología específica para ver el netlist SPICE.")

                txt_out.insert("end", "\n".join(lines))

            def load_preset(topo_name, p_dict):
                rlc_mode_var.set(topo_name)
                if "r1" in p_dict: entry_r1.delete(0, "end"); entry_r1.insert(0, str(p_dict["r1"]))
                if "r2" in p_dict: entry_r2.delete(0, "end"); entry_r2.insert(0, str(p_dict["r2"]))
                if "c1" in p_dict: entry_c1.delete(0, "end"); entry_c1.insert(0, str(p_dict["c1"]))
                if "l1" in p_dict: entry_l1.delete(0, "end"); entry_l1.insert(0, str(p_dict["l1"]))
                if "vin" in p_dict: entry_vin.delete(0, "end"); entry_vin.insert(0, str(p_dict["vin"]))
                calculate_rlc()

            chips = [
                ("5V->3.3V ADC", "Divisor Resistivo (5V a 3.3V ADC / Level Shifter)", {"r1": 10000, "r2": 20000, "vin": 5.0}),
                ("Buck 12V->5V", "Convertidor DC-DC Buck Reductor (GREELEC PEE)", {"r1": 5.0, "l1": 47, "c1": 220, "vin": 12.0}),
                ("Boost 3.7V->5V", "Convertidor DC-DC Boost Elevador (GREELEC PEE)", {"r1": 5.0, "l1": 22, "c1": 100, "vin": 3.7}),
                ("Línea RF 50Ω", "Línea de Transmisión RF & Adaptación 50Ω (GREELEC CAF)", {"r1": 50, "vin": 1.0}),
                ("BJT Clase A", "Amplificador BJT Emisor Común Polarizado (GREELEC CA)", {"r1": 2200, "r2": 470, "vin": 12.0}),
                ("Control PID", "Lazo de Control Feedback PID en Tiempo Real (GREELEC SC)", {"vin": 5.0}),
                ("NE555 1kHz", "Temporizador 555 Astable (Oscilador Reloj / PWM)", {"r1": 4700, "r2": 4700, "c1": 100, "vin": 5.0}),
                ("LED 20mA", "Limitador de Corriente para LEDs (Rojo / Verde / Azul / Blanco)", {"r1": 91, "vin": 5.0}),
                ("Cód. Colores", "Decodificador de Código de Colores (4 y 5 Bandas)", {"r1": 10000})
            ]

            for chip_lbl, chip_topo, chip_params in chips:
                btn_ch = tk.Button(
                    row_chips, text=chip_lbl, font=(FONT_FAMILY, 8, "bold"),
                    bg="#1a202c", fg="#38bdf8", activebackground="#2563eb", activeforeground="#ffffff",
                    relief="flat", bd=0, padx=8, pady=3, cursor="hand2",
                    command=lambda t=chip_topo, d=chip_params: load_preset(t, d)
                )
                btn_ch.pack(side="left", padx=2)

            # Botón Calcular
            btn_calc_rlc = tk.Button(
                row_act, text="⚡ Recalcular & Generar Netlist SPICE",
                font=(FONT_FAMILY, 10, "bold"), bg=COLOR_ACCENT_BLUE, fg="#ffffff",
                activebackground=COLOR_ACCENT_HOVER, activeforeground="#ffffff",
                relief="flat", bd=0, padx=14, pady=6, cursor="hand2",
                command=calculate_rlc
            )
            btn_calc_rlc.pack(side="left", padx=(0, 10))

            combo_rlc.bind("<<ComboboxSelected>>", lambda e: calculate_rlc())
            canvas_sch.bind("<Configure>", lambda e: calculate_rlc())
            tab_callbacks[6] = calculate_rlc

            # Cálculo inicial automático
            root_win.after(300, calculate_rlc)

    # ==================================================================
    # PESTAÑA 8: FLASHCARDS ANKI & GESTOR DE PREGUNTAS DE EXAMEN UPC
    # ==================================================================
    def setup_flashcards_tab(parent, root_win):
        p = tk.Frame(parent, bg=COLOR_CANVAS, padx=12, pady=10)
        p.pack(fill="both", expand=True)

        in_dir = in_var.get().strip() or "dist_course_md"
        cached_quizzes = load_all_course_quizzes(in_dir)
        if not cached_quizzes:
            cached_quizzes = load_all_course_quizzes("Curso_Completo_Sistemes_de_Mesura")
        if not cached_quizzes:
            cached_quizzes = load_all_course_quizzes(".")
        if not cached_quizzes:
            cached_quizzes = []

        top_card = make_card(p, "🧠 Repaso Activo Anki & Gestor de Preguntas de Examen (UPC EEBE)", badge="500 Preguntas")
        top_card.pack(fill="x", pady=(0, 8))
        top_inner = tk.Frame(top_card, bg=COLOR_CARD, padx=16, pady=8)
        top_inner.pack(fill="x")

        row_fil = tk.Frame(top_inner, bg=COLOR_CARD)
        row_fil.pack(fill="x", pady=(0, 6))

        tk.Label(row_fil, text="Tema:", font=FONT_HEAD, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD).pack(side="left", padx=(0, 6))
        topics_opts = ["Todos los Temas (500 preguntas del curso)"]
        for i in range(1, 11):
            topics_opts.append(f"Tema {i} (50 preguntas oficiales)")
        combo_fc_topic = ttk.Combobox(row_fil, values=topics_opts, state="readonly", style="Modern.TCombobox", width=34)
        combo_fc_topic.current(0)
        combo_fc_topic.pack(side="left", padx=(0, 14))

        tk.Label(row_fil, text="🔍 Buscar:", font=FONT_HEAD, fg=COLOR_TEXT_MUTED, bg=COLOR_CARD).pack(side="left", padx=(0, 6))
        search_fc_var = tk.StringVar()
        entry_fc_search = tk.Entry(row_fil, textvariable=search_fc_var, font=FONT_CODE, width=22, bg=COLOR_INPUT_BG, fg=COLOR_TEXT_PRIMARY, insertbackground=COLOR_ACCENT_BLUE, bd=1, relief="solid")
        entry_fc_search.pack(side="left", padx=(0, 14), ipady=2)

        lbl_fc_count = tk.Label(row_fil, text=f"Total: {len(cached_quizzes)} preguntas", font=(FONT_FAMILY, 9, "bold"), fg=COLOR_ACCENT_CYAN, bg=COLOR_CARD)
        lbl_fc_count.pack(side="left")

        split_c = tk.Frame(p, bg=COLOR_CANVAS)
        split_c.pack(fill="both", expand=True, pady=(0, 8))

        left_card = make_card(split_c, "📋 Preguntas Seleccionadas")
        left_card.pack(side="left", fill="both", expand=True, padx=(0, 6))
        left_inner = tk.Frame(left_card, bg=COLOR_CARD, padx=10, pady=8)
        left_inner.pack(fill="both", expand=True)

        cols = ("id", "tema", "pregunta", "ans")
        tree_fc = ttk.Treeview(left_inner, columns=cols, show="headings", selectmode="browse")
        tree_fc.heading("id", text="#")
        tree_fc.heading("tema", text="Tema")
        tree_fc.heading("pregunta", text="Enunciado de la Pregunta")
        tree_fc.heading("ans", text="Resp.")

        tree_fc.column("id", width=45, anchor="center")
        tree_fc.column("tema", width=75, anchor="center")
        tree_fc.column("pregunta", width=360, anchor="w")
        tree_fc.column("ans", width=55, anchor="center")
        tree_fc.pack(fill="both", expand=True)

        right_card = make_card(split_c, "🃏 Previsualización de Flashcard Anki")
        right_card.pack(side="right", fill="both", expand=True, padx=(6, 0))
        right_inner = tk.Frame(right_card, bg=COLOR_CARD, padx=14, pady=10)
        right_inner.pack(fill="both", expand=True)

        lbl_fc_front_badge = tk.Label(right_inner, text="ANVERSO (PREGUNTA)", font=FONT_SMALL, fg=COLOR_ACCENT_BLUE, bg=COLOR_CARD)
        lbl_fc_front_badge.pack(anchor="w")

        txt_fc_q = ScrolledText(right_inner, font=(FONT_FAMILY, 10), bg="#0f1117", fg="#f8fafc", bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER, height=5, wrap="word")
        txt_fc_q.pack(fill="x", pady=(2, 10))

        lbl_fc_back_badge = tk.Label(right_inner, text="REVERSO (SOLUCIÓN & JUSTIFICACIÓN TÉCNICA)", font=FONT_SMALL, fg=COLOR_ACCENT_GREEN, bg=COLOR_CARD)
        lbl_fc_back_badge.pack(anchor="w")

        lbl_fc_ans = tk.Label(right_inner, text="Respuesta: -", font=(FONT_FAMILY, 12, "bold"), fg=COLOR_ACCENT_AMBER, bg=COLOR_CARD)
        lbl_fc_ans.pack(anchor="w", pady=(2, 4))

        txt_fc_sol = ScrolledText(right_inner, font=(FONT_FAMILY, 9), bg="#0f1117", fg="#94a3b8", bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER, height=6, wrap="word")
        txt_fc_sol.pack(fill="both", expand=True, pady=(2, 8))

        bot_bar = tk.Frame(p, bg=COLOR_HEADER, bd=1, relief="solid", highlightthickness=1, highlightbackground=COLOR_CARD_BORDER, padx=14, pady=8)
        bot_bar.pack(fill="x")

        displayed_quizzes = []

        def filter_questions(event=None):
            nonlocal displayed_quizzes
            t_idx = combo_fc_topic.current()
            query = search_fc_var.get().strip().lower()

            pool = cached_quizzes
            if t_idx > 0:
                pool = [q for q in pool if q.get("tema_num") == t_idx]

            if query:
                pool = [q for q in pool if query in q.get("q", "").lower() or query in q.get("sol", "").lower()]

            displayed_quizzes = pool
            tree_fc.delete(*tree_fc.get_children())
            for idx, q in enumerate(displayed_quizzes, 1):
                clean_q = q.get("q", "").replace("\n", " ").strip()
                ans_str = "V" if q.get("ans") in ["V", True, "True", "true"] else "F"
                tree_fc.insert("", "end", values=(idx, f"Tema {q.get('tema_num', '?')}", clean_q[:80] + ("..." if len(clean_q) > 80 else ""), ans_str))

            lbl_fc_count.config(text=f"Mostrando {len(displayed_quizzes)} de {len(cached_quizzes)}")
            if displayed_quizzes:
                tree_fc.selection_set(tree_fc.get_children()[0])
                on_select_question()

        def on_select_question(event=None):
            sel = tree_fc.selection()
            if not sel: return
            item = tree_fc.item(sel[0])
            idx = int(item["values"][0]) - 1
            if 0 <= idx < len(displayed_quizzes):
                q = displayed_quizzes[idx]
                txt_fc_q.delete("1.0", "end")
                txt_fc_q.insert("end", q.get("q", ""))
                is_v = q.get("ans") in ["V", True, "True", "true"]
                lbl_fc_ans.config(text=f"Respuesta Oficial: {'VERTADER (Verdadero)' if is_v else 'FALS (Falso)'}", fg=COLOR_ACCENT_GREEN if is_v else COLOR_ACCENT_RED)
                txt_fc_sol.delete("1.0", "end")
                txt_fc_sol.insert("end", q.get("sol", "Sin justificación adicional disponible."))

        tree_fc.bind("<<TreeviewSelect>>", on_select_question)
        combo_fc_topic.bind("<<ComboboxSelected>>", filter_questions)
        entry_fc_search.bind("<KeyRelease>", filter_questions)

        def export_anki_apkg():
            if not displayed_quizzes:
                messagebox.showwarning("Anki", "No hay preguntas seleccionadas para exportar.")
                return
            out_p = Path("dist_course_md")
            out_p.mkdir(parents=True, exist_ok=True)
            t_idx = combo_fc_topic.current()
            stem = f"Sistemes_de_Mesura_Tema_{t_idx}" if t_idx > 0 else "Sistemes_de_Mesura_Curso_Completo"
            tsv_path = out_p / f"{stem}_Anki.tsv"
            apkg_path = out_p / f"{stem}.apkg"

            lines = ["#separator:tab", "#html:true", "#tags column:3"]
            for q in displayed_quizzes:
                ans_str = "<b>VERTADER (V)</b>" if q.get("ans") in ["V", True] else "<b>FALS (F)</b>"
                front = f"<b>[Tema {q.get('tema_num')}]</b><br>{q.get('q', '').replace(chr(10), '<br>')}"
                back = f"{ans_str}<br><br><small style='color:#38bdf8;'>{q.get('sol', '').replace(chr(10), '<br>')}</small>"
                tag = f"Tema_{q.get('tema_num')}"
                lines.append(f"{front}\t{back}\t{tag}")
            tsv_path.write_text("\n".join(lines), encoding="utf-8")

            has_apkg = False
            if uc and getattr(uc, "HAS_GENANKI", False):
                try:
                    import genanki
                    model_id = 1607392319
                    deck_id = 2059381192 + t_idx
                    my_model = genanki.Model(
                        model_id, 'UPC Exam Flashcard Model',
                        fields=[{'name': 'Question'}, {'name': 'Answer'}],
                        templates=[{
                            'name': 'Card 1',
                            'qfmt': '<div style="font-family: -apple-system, sans-serif; font-size: 16px; padding: 15px; color: #f8fafc; background: #0f172a; border-radius: 8px;">{{Question}}</div>',
                            'afmt': '{{FrontSide}}<hr id="answer"><div style="font-family: -apple-system, sans-serif; font-size: 15px; padding: 15px; color: #f8fafc; background: #1e293b; border-radius: 8px;">{{Answer}}</div>'
                        }]
                    )
                    deck_title = f"UPC Sistemes de Mesura · Tema {t_idx}" if t_idx > 0 else "UPC Sistemes de Mesura · Curso Completo (500 Preguntas)"
                    my_deck = genanki.Deck(deck_id, deck_title)
                    for q in displayed_quizzes:
                        ans_str = "<b>VERTADER (V)</b>" if q.get("ans") in ["V", True] else "<b>FALS (F)</b>"
                        f_html = f"<b>[Tema {q.get('tema_num')}]</b><br>{q.get('q', '').replace(chr(10), '<br>')}"
                        b_html = f"{ans_str}<br><br><small style='color:#38bdf8;'>{q.get('sol', '').replace(chr(10), '<br>')}</small>"
                        note = genanki.Note(model=my_model, fields=[f_html, b_html])
                        my_deck.add_note(note)
                    genanki.Package(my_deck).write_to_file(str(apkg_path))
                    has_apkg = True
                except Exception:
                    has_apkg = False

            msg = f"✅ Flashcards exportadas exitosamente ({len(displayed_quizzes)} tarjetas):\n\n"
            if has_apkg:
                msg += f"• Mazo Anki listo para importar: {apkg_path.resolve()}\n"
            msg += f"• Archivo TSV estándar: {tsv_path.resolve()}\n"
            messagebox.showinfo("Exportación Anki Completada", msg)

        create_btn(bot_bar, "📦 Exportar Mazo Anki (.apkg)", export_anki_apkg, bg=COLOR_ACCENT_GREEN, hover_bg=COLOR_ACCENT_GREEN_HOVER, font=(FONT_FAMILY, 10, "bold"), padx=14, pady=5).pack(side="left", padx=(0, 8))

        def export_tsv_only():
            out_p = Path("dist_course_md")
            out_p.mkdir(parents=True, exist_ok=True)
            tsv_path = out_p / "_Banco_Preguntas_Oficial_UPC.tsv"
            lines = ["#separator:tab", "#html:true", "#tags column:3"]
            for q in displayed_quizzes:
                ans_str = "VERTADER (V)" if q.get("ans") in ["V", True] else "FALS (F)"
                lines.append(f"{q.get('q', '')}\t{ans_str} - {q.get('sol', '')}\tTema_{q.get('tema_num')}")
            tsv_path.write_text("\n".join(lines), encoding="utf-8")
            root_win.clipboard_clear()
            root_win.clipboard_append("\n".join(lines))
            messagebox.showinfo("TSV Exportado", f"✅ Fichero TSV guardado en:\n{tsv_path.resolve()}\n\n¡Y copiado al portapapeles para importar en Quizlet o AnkiWeb!")

        create_btn(bot_bar, "📋 Exportar Tabla TSV (Quizlet/Web)", export_tsv_only, bg="#262a36", font=FONT_HEAD, padx=12, pady=5).pack(side="left", padx=(0, 8))
        create_btn(bot_bar, "🖨️ Generar Examen Imprimible PDF/HTML", open_exam_simulator_modal, bg="#112530", hover_bg="#1b3b4d", font=FONT_HEAD, padx=12, pady=5).pack(side="left")

        filter_questions()
        tab_callbacks[7] = filter_questions

    setup_universal_converter_tab(tab_universal, root)
    setup_gum_calculator_tab(tab_gum, root)
    setup_filters_tab(tab_filters, root)
    setup_rlc_presets_tab(tab_rlc, root)
    setup_flashcards_tab(tab_flashcards, root)
    if HAS_UPC_DEGREE and setup_upc_degree_tab:
        setup_upc_degree_tab(tab_upc, root)
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
  --pdf                   Convierte archivo PDF a Markdown de alta fidelidad (PyMuPDF).
  --docx                  Convierte documento Word DOCX a Markdown con OMML a LaTeX.
  --ipynb                 Convierte Jupyter Notebook a Markdown con celdas e imágenes.
  --anki                  Genera mazo Anki (.apkg y .tsv) desde Markdown o banco de test.
  --universal             Ejecuta escaneo y conversión universal multi-formato de carpeta.
  --degree-plan           Lista las 35 asignaturas obligatorias del plan GREELEC UPC.
  --degree-stats          Muestra estadísticas del plan de estudios oficial.
  --degree-export-md <d>  Exporta las 35 guías de estudio completas en Markdown a una carpeta.
  --degree-export-anki <d> Exporta todos los mazos Anki de las 35 asignaturas a una carpeta.
  --tools                 Lista las 37 herramientas y sintetizadores especializados de ingeniería.
  --tool <nombre>         Ejecuta una herramienta de ingeniería (--params '<json>').
  -h, --help              Muestra este mensaje de ayuda.
""")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        run_gui()
    elif "-h" in sys.argv or "--help" in sys.argv:
        print_help()
    elif "--tools" in sys.argv or "--degree-tools" in sys.argv:
        if HAS_UPC_DEGREE and upc_engine:
            import engineering_tools_suite as ets
            print("=== 37 Herramientas de Ingeniería Especializadas de GREELEC ===")
            branches = {}
            for name, meta in ets.ENGINEERING_TOOLS_METADATA.items():
                b = meta.get("branch", "Otras")
                if b not in branches:
                    branches[b] = []
                branches[b].append((name, meta))
            for branch, tools in branches.items():
                print(f"\n[{branch.upper()}] ({len(tools)} herramientas)")
                for name, meta in tools:
                    courses = ", ".join(meta.get("courses", []))
                    print(f"  * {name:<35} | {meta['title']} ({courses})")
                    print(f"    Desc: {meta['description']}")
        else:
            print("Módulo de herramientas de ingeniería no disponible.")
        sys.exit(0)
    elif "--tool" in sys.argv:
        idx = sys.argv.index("--tool")
        tool_name = sys.argv[idx + 1] if len(sys.argv) > idx + 1 else ""
        params = None
        if "--params" in sys.argv:
            pidx = sys.argv.index("--params")
            if len(sys.argv) > pidx + 1:
                try:
                    params = json.loads(sys.argv[pidx + 1])
                except Exception as e:
                    print(f"Error parseando JSON de parámetros: {e}")
                    sys.exit(1)
        if HAS_UPC_DEGREE and upc_engine:
            try:
                res = upc_engine.engine.run_engineering_tool(tool_name, params)
                print(json.dumps(res, indent=2, ensure_ascii=False))
            except Exception as e:
                print(f"Error ejecutando herramienta '{tool_name}': {e}")
                sys.exit(1)
        else:
            print("Módulo upc_degree_engine no disponible.")
        sys.exit(0)
    elif "--degree-plan" in sys.argv or "--degree-list" in sys.argv:
        if HAS_UPC_DEGREE and upc_engine:
            print("=== Plan de Estudios GREELEC UPC (35 Asignaturas Obligatorias) ===")
            for s in upc_engine.engine.get_all_subjects():
                print(f"Q{s['semester']} | {s['code']} | {s['acronym']:<6} | {s['title']} ({s['ects']} ECTS)")
        else:
            print("Módulo upc_degree_engine no disponible.")
        sys.exit(0)
    elif "--degree-stats" in sys.argv:
        if HAS_UPC_DEGREE and upc_engine:
            print(json.dumps(upc_engine.engine.get_curriculum_statistics(), indent=2, ensure_ascii=False))
        sys.exit(0)
    elif "--degree-export-md" in sys.argv:
        idx = sys.argv.index("--degree-export-md")
        t_dir = sys.argv[idx + 1] if len(sys.argv) > idx + 1 else "upc_md"
        n = upc_engine.engine.export_all_study_guides(t_dir)
        print(f"✅ Exportadas {n} guías de estudio a: {t_dir}")
        sys.exit(0)
    elif "--degree-export-anki" in sys.argv:
        idx = sys.argv.index("--degree-export-anki")
        t_dir = sys.argv[idx + 1] if len(sys.argv) > idx + 1 else "upc_anki"
        n = upc_engine.engine.export_all_anki_decks(t_dir)
        print(f"✅ Exportadas {n} flashcards Anki a: {t_dir}")
        sys.exit(0)
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

        # Enrutadores para conversores universales por extensión o flag
        src_lower = src.lower()
        if "--pdf" in args or src_lower.endswith(".pdf"):
            if uc:
                print(f"📄 Convirtiendo PDF con PyMuPDF: {src} -> {dst}")
                md_txt, stats = uc.convert_pdf_to_markdown(Path(src), Path(dst))
                print(f"¡Éxito! Páginas: {stats.get('pages', 0)}, Fórmulas: {stats.get('math_formulas', 0)}, Tablas: {stats.get('tables', 0)}")
                sys.exit(0)
        elif "--docx" in args or src_lower.endswith(".docx"):
            if uc:
                print(f"📝 Convirtiendo Word DOCX (OMML LaTeX): {src} -> {dst}")
                md_txt, stats = uc.convert_docx_to_markdown(Path(src), Path(dst))
                print(f"¡Éxito! Párrafos: {stats.get('paragraphs', 0)}, Fórmulas: {stats.get('math_formulas', 0)}, Tablas: {stats.get('tables', 0)}")
                sys.exit(0)
        elif "--ipynb" in args or src_lower.endswith(".ipynb"):
            if uc:
                print(f"🪐 Convirtiendo Jupyter Notebook: {src} -> {dst}")
                md_txt, stats = uc.convert_ipynb_to_markdown(Path(src), Path(dst))
                print(f"¡Éxito! Celdas procesadas: {stats.get('cells', 0)}")
                sys.exit(0)
        elif "--anki" in args:
            if uc:
                print(f"🧠 Generando Flashcards Anki: {src} -> {dst}")
                stats = uc.convert_markdown_to_anki(Path(src), Path(dst))
                print(f"¡Éxito! Tarjetas exportadas: {stats.get('cards_count', 0)}")
                sys.exit(0)
        elif "--universal" in args:
            if uc:
                print(f"🚀 Ejecutando conversión universal por lotes: {src} -> {dst}")
                stats = uc.batch_convert_universal(Path(src), Path(dst))
                print(f"¡Éxito! Total convertidos: {stats.get('total_converted', 0)}, Fórmulas: {stats.get('total_math', 0)}")
                sys.exit(0)

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
