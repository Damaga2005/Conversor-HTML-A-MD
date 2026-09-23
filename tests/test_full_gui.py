import sys, os, time, re, json, threading, subprocess
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.scrolledtext import ScrolledText
import pytest

def test_full_gui_layout():
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
        root.geometry("980x790")
        root.minsize(900, 700)
        root.configure(bg="#0b0f19")

        style = ttk.Style()
        style.theme_use("clam")

        # Theme styling
        style.configure("Modern.TNotebook", background="#0b0f19", borderwidth=0)
        style.configure("Modern.TNotebook.Tab", background="#151d30", foreground="#94a3b8", padding=[18, 10], font=("Segoe UI", 9, "bold"), borderwidth=0)
        style.map("Modern.TNotebook.Tab",
            background=[("selected", "#1e293b"), ("active", "#1e293b")],
            foreground=[("selected", "#60a5fa"), ("active", "#f8fafc")]
        )
        style.configure("Modern.Horizontal.TProgressbar", background="#6366f1", troughcolor="#0b1120", borderwidth=0, thickness=8)
        style.configure("Modern.TCombobox", fieldbackground="#0b1120", background="#1e293b", foreground="#f8fafc", arrowcolor="#a5b4fc", borderwidth=1)
        style.map("Modern.TCombobox", fieldbackground=[("readonly", "#0b1120")])

        # Helper for modern buttons
        def create_btn(parent, text, command, bg="#1e293b", fg="#f8fafc", hover_bg="#334155", font=("Segoe UI", 9, "bold"), **kwargs):
            b = tk.Button(parent, text=text, command=command, bg=bg, fg=fg, activebackground=hover_bg, activeforeground=fg, font=font, cursor="hand2", relief="flat", bd=0, padx=12, pady=6, **kwargs)
            b.bind("<Enter>", lambda e: b.config(bg=hover_bg) if b["state"] != "disabled" else None)
            b.bind("<Leave>", lambda e: b.config(bg=bg) if b["state"] != "disabled" else None)
            return b

        def make_card(parent, title=""):
            c = tk.Frame(parent, bg="#151d30", bd=1, relief="solid", highlightthickness=1, highlightbackground="#222f47")
            if title:
                tk.Label(c, text=title, font=("Segoe UI", 9, "bold"), fg="#a5b4fc", bg="#151d30").pack(anchor="w", padx=14, pady=(10, 4))
            return c

        # Header
        header_frame = tk.Frame(root, bg="#0f172a", padx=24, pady=12)
        header_frame.pack(fill="x")
        accent_line = tk.Frame(root, bg="#4f46e5", height=2)
        accent_line.pack(fill="x")

        h_left = tk.Frame(header_frame, bg="#0f172a")
        h_left.pack(side="left")
        tk.Label(h_left, text="⚡ Conversor HTML a Markdown Ultra-Fiel", fg="white", bg="#0f172a", font=("Segoe UI", 15, "bold")).pack(anchor="w")
        tk.Label(h_left, text="Máxima fidelidad matemática y estructural para NotebookLM, Claude, Gemini y Obsidian", fg="#94a3b8", bg="#0f172a", font=("Segoe UI", 9)).pack(anchor="w")

        h_right = tk.Frame(header_frame, bg="#0f172a")
        h_right.pack(side="right")
        tk.Label(h_right, text="🎓 UPC · Sistemes de Mesura", fg="#a5b4fc", bg="#1e293b", font=("Segoe UI", 8, "bold"), padx=8, pady=4).pack(side="left", padx=4)
        tk.Label(h_right, text="v2.5 Ultra", fg="#34d399", bg="#064e3b", font=("Segoe UI", 8, "bold"), padx=8, pady=4).pack(side="left", padx=4)

        nb = ttk.Notebook(root, style="Modern.TNotebook")
        nb.pack(fill="both", expand=True, padx=16, pady=12)

        t1 = tk.Frame(nb, bg="#0b0f19")
        t2 = tk.Frame(nb, bg="#0b0f19")
        t3 = tk.Frame(nb, bg="#0b0f19")

        nb.add(t1, text=" 🚀 Conversión ")
        nb.add(t2, text=" 👁️ Visor Markdown & NotebookLM ")
        nb.add(t3, text=" 🗂️ Recursos del Curso ")

        # Card 1: Mode and Presets
        c1 = make_card(t1, "⚙️ Modo de Operación y Perfil")
        c1.pack(fill="x", padx=12, pady=(10, 8))

        # Card 2: Paths
        c2 = make_card(t1, "📁 Rutas de Entrada y Salida")
        c2.pack(fill="x", padx=12, pady=4)

        # Card 3: Options
        c3 = make_card(t1, "🛠️ Opciones de Formato y Rigor")
        c3.pack(fill="x", padx=12, pady=4)

        # Card 4: Console & Actions
        c4 = make_card(t1, "💻 Consola de Actividad")
        c4.pack(fill="both", expand=True, padx=12, pady=4)
    finally:
        root.destroy()
