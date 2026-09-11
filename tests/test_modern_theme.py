import sys, os
import tkinter as tk
from tkinter import ttk

# Test DPI awareness
try:
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except Exception:
    pass

root = tk.Tk()
root.title("Test Modern Theme")
root.geometry("400x300")
root.configure(bg="#0b0f19")

style = ttk.Style()
style.theme_use("clam")

# Configure Notebook
style.configure("Modern.TNotebook", background="#0b0f19", borderwidth=0)
style.configure("Modern.TNotebook.Tab", background="#151d30", foreground="#94a3b8", padding=[16, 8], font=("Segoe UI", 9, "bold"), borderwidth=0)
style.map("Modern.TNotebook.Tab",
    background=[("selected", "#1e293b"), ("active", "#1a243a")],
    foreground=[("selected", "#f8fafc"), ("active", "#e2e8f0")]
)

# Configure Progressbar
style.configure("Modern.Horizontal.TProgressbar", background="#6366f1", troughcolor="#151d30", borderwidth=0, thickness=8)

# Configure Combobox
style.configure("Modern.TCombobox", fieldbackground="#151d30", background="#1e293b", foreground="#f8fafc", arrowcolor="#a5b4fc", borderwidth=1)
style.map("Modern.TCombobox", fieldbackground=[("readonly", "#151d30")])

nb = ttk.Notebook(root, style="Modern.TNotebook")
tab1 = tk.Frame(nb, bg="#0b0f19")
tab2 = tk.Frame(nb, bg="#0b0f19")
nb.add(tab1, text="🚀 Conversión")
nb.add(tab2, text="👁️ Visor")
nb.pack(fill="both", expand=True, padx=10, pady=10)

pb = ttk.Progressbar(tab1, style="Modern.Horizontal.TProgressbar", orient="horizontal", mode="determinate", value=50)
pb.pack(fill="x", padx=20, pady=20)

cb = ttk.Combobox(tab1, style="Modern.TCombobox", values=["NotebookLM", "Obsidian", "GitHub"], state="readonly")
cb.set("NotebookLM")
cb.pack(padx=20, pady=10)

print("Theme configured successfully without errors!")
root.destroy()
