import sys, os, time, re, json, threading, subprocess
from pathlib import Path
from collections import defaultdict
from typing import Optional
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, font as tkfont
from tkinter.scrolledtext import ScrolledText
import pytest

def test_modular_gui_layout():
    # Ensure Tcl/Tk env vars if not set
    tcl_dir = Path(sys.base_prefix) / "tcl"
    if tcl_dir.exists():
        os.environ.setdefault("TCL_LIBRARY", str(tcl_dir / "tcl8.6"))
        os.environ.setdefault("TK_LIBRARY", str(tcl_dir / "tk8.6"))

    try:
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass

    try:
        root = tk.Tk()
    except Exception as e:
        pytest.skip(f"Tkinter/Tcl not available in test runner environment: {e}")

    try:
        root.title("Conversor HTML a Markdown Ultra-Fiel · Edición Universitaria")
        root.geometry("980x820")
        root.minsize(900, 720)
        root.configure(bg="#0b0f19")

        # Font definitions
        FONT_FAMILY = "Segoe UI"
        for f in ["Segoe UI Variable Display", "Segoe UI", "Helvetica Neue", "Arial"]:
            if f in tkfont.families():
                FONT_FAMILY = f
                break

        FONT_TITLE = (FONT_FAMILY, 14, "bold")
        FONT_SUBTITLE = (FONT_FAMILY, 9)
        FONT_HEAD = (FONT_FAMILY, 9, "bold")
        FONT_BODY = (FONT_FAMILY, 9)
        FONT_CODE = ("Consolas", 9)
        FONT_SMALL = (FONT_FAMILY, 8)

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Modern.TNotebook", background="#0b0f19", borderwidth=0)
        style.configure("Modern.TNotebook.Tab", background="#151d30", foreground="#94a3b8", padding=[18, 10], font=(FONT_FAMILY, 9, "bold"), borderwidth=0)
        style.map("Modern.TNotebook.Tab",
            background=[("selected", "#1e293b"), ("active", "#1e293b")],
            foreground=[("selected", "#60a5fa"), ("active", "#f8fafc")]
        )
        style.configure("Modern.Horizontal.TProgressbar", background="#6366f1", troughcolor="#0b1120", borderwidth=0, thickness=8)
        style.configure("Modern.TCombobox", fieldbackground="#0b1120", background="#1e293b", foreground="#f8fafc", arrowcolor="#a5b4fc", borderwidth=1)
        style.map("Modern.TCombobox", fieldbackground=[("readonly", "#0b1120")])

        def create_btn(parent, text, command, bg="#1e293b", fg="#f8fafc", hover_bg="#334155", font=FONT_HEAD, **kwargs):
            b = tk.Button(parent, text=text, command=command, bg=bg, fg=fg, activebackground=hover_bg, activeforeground=fg, font=font, cursor="hand2", relief="flat", bd=0, padx=12, pady=6, **kwargs)
            b.bind("<Enter>", lambda e: b.config(bg=hover_bg) if b["state"] != "disabled" else None)
            b.bind("<Leave>", lambda e: b.config(bg=bg) if b["state"] != "disabled" else None)
            return b

        def make_card(parent, title=""):
            c = tk.Frame(parent, bg="#151d30", bd=1, relief="solid", highlightthickness=1, highlightbackground="#222f47")
            if title:
                tk.Label(c, text=title, font=FONT_HEAD, fg="#a5b4fc", bg="#151d30").pack(anchor="w", padx=14, pady=(10, 4))
            return c

        card = make_card(root, "Panel de Prueba")
        btn = create_btn(card, "Probar", lambda: None)
        btn.pack()
        card.pack()
    finally:
        root.destroy()
