import sys, os, time, re
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.scrolledtext import ScrolledText
from pathlib import Path

# Test script to verify the new GUI structure and styling
import pytest

def test_modern_gui_structure():
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
        pytest.skip(f"Tkinter not available or headless environment: {e}")

    try:
        root.title("Conversor HTML a Markdown Ultra-Fiel · Edición Universitaria")
        root.geometry("960x780")
        root.minsize(880, 680)
        root.configure(bg="#0b0f19")

        style = ttk.Style()
        style.theme_use("clam")

        # Theme styling
        style.configure("Modern.TNotebook", background="#0b0f19", borderwidth=0)
        style.configure("Modern.TNotebook.Tab", background="#151d30", foreground="#94a3b8", padding=[16, 9], font=("Segoe UI", 9, "bold"), borderwidth=0)
        style.map("Modern.TNotebook.Tab",
            background=[("selected", "#1e293b"), ("active", "#1e293b")],
            foreground=[("selected", "#60a5fa"), ("active", "#f8fafc")]
        )
        style.configure("Modern.Horizontal.TProgressbar", background="#6366f1", troughcolor="#151d30", borderwidth=0, thickness=10)
        style.configure("Modern.TCombobox", fieldbackground="#151d30", background="#1e293b", foreground="#f8fafc", arrowcolor="#a5b4fc", borderwidth=1)
        style.map("Modern.TCombobox", fieldbackground=[("readonly", "#151d30")])

        # Verify UI components create cleanly
        header_frame = tk.Frame(root, bg="#0f172a", padx=24, pady=14)
        header_frame.pack(fill="x")
        tk.Label(header_frame, text="Conversor HTML a Markdown Ultra-Fiel", fg="white", bg="#0f172a", font=("Segoe UI", 15, "bold")).pack(anchor="w")

        notebook = ttk.Notebook(root, style="Modern.TNotebook")
        notebook.pack(fill="both", expand=True, padx=16, pady=12)

        tab_convert = tk.Frame(notebook, bg="#0b0f19")
        tab_viewer = tk.Frame(notebook, bg="#0b0f19")
        tab_resources = tk.Frame(notebook, bg="#0b0f19")

        notebook.add(tab_convert, text=" 🚀 Conversión ")
        notebook.add(tab_viewer, text=" 👁️ Visor Markdown & NotebookLM ")
        notebook.add(tab_resources, text=" 🗂️ Recursos del Curso ")
    finally:
        root.destroy()
