# -*- coding: utf-8 -*-
"""
UPC ETSETB GREELEC Degree Plan Workstation (Tab 9 for Conversor HTML a MD)
Interactive UI with course explorer, official syllabus, LaTeX formulas,
interactive parameter calculators, SPICE benches, and 424 exam quiz questions.
"""
from __future__ import annotations
import os
import sys
import json
import math
import webbrowser
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkinter.scrolledtext import ScrolledText

from upc_degree_engine import engine, UPCDegreeEngine

def setup_upc_degree_tab(parent_frame: tk.Frame, root: tk.Tk) -> None:
    """Sets up the complete UPC GREELEC Degree Plan Workstation UI."""
    # Palette matching Apple Dark Mode theme
    BG_CANVAS = "#18181a"
    BG_CARD = "#1f1f23"
    BG_INSET = "#141416"
    BG_BORDER = "#2e2e33"
    TXT_PRIMARY = "#f2f2f7"
    TXT_MUTED = "#98989f"
    ACCENT_BLUE = "#0a84ff"
    ACCENT_HOVER = "#0071e3"
    ACCENT_GREEN = "#30d158"
    ACCENT_ORANGE = "#ff9f0a"
    ACCENT_CYAN = "#64d2ff"
    FONT_FAMILY = "Segoe UI"

    # Container
    main_box = tk.Frame(parent_frame, bg=BG_CANVAS)
    main_box.pack(fill="both", expand=True, padx=14, pady=10)

    # 1. Header with Title & Degree Stats Badge
    header = tk.Frame(main_box, bg=BG_CANVAS)
    header.pack(fill="x", pady=(0, 10))

    title_box = tk.Frame(header, bg=BG_CANVAS)
    title_box.pack(side="left")

    tk.Label(
        title_box,
        text="🎓 Grado en Ingeniería Electrónica de Telecomunicación (UPC - ETSETB)",
        font=(FONT_FAMILY, 14, "bold"),
        fg=TXT_PRIMARY,
        bg=BG_CANVAS
    ).pack(anchor="w")

    stats = engine.get_curriculum_statistics()
    subtitle_text = f"Plan Oficial GREELEC · {stats['total_compulsory_subjects']} Asignaturas Obligatorias · {int(stats['total_ects'])} ECTS · {stats['total_exam_questions']} Preguntas de Examen con Justificación"
    tk.Label(
        title_box,
        text=subtitle_text,
        font=(FONT_FAMILY, 9),
        fg=TXT_MUTED,
        bg=BG_CANVAS
    ).pack(anchor="w", pady=(2, 0))

    # Top Action Buttons
    action_box = tk.Frame(header, bg=BG_CANVAS)
    action_box.pack(side="right")

    def export_all_md():
        out_dir = filedialog.askdirectory(title="Seleccionar carpeta para exportar las 35 guías de estudio")
        if out_dir:
            n = engine.export_all_study_guides(out_dir)
            messagebox.showinfo("Exportación Completada", f"✅ Se han generado {n} guías de estudio en Markdown en:\n{out_dir}")

    def export_all_anki():
        out_dir = filedialog.askdirectory(title="Seleccionar carpeta para exportar los mazos Anki")
        if out_dir:
            n = engine.export_all_anki_decks(out_dir)
            messagebox.showinfo("Exportación Anki", f"✅ Se han generado {n} tarjetas Anki (.tsv) en:\n{out_dir}")

    def open_virtual_lab():
        lab_file = Path(__file__).resolve().parent / "Laboratorio_Virtual_Sensores.html"
        if lab_file.exists():
            webbrowser.open(lab_file.as_uri())
        else:
            messagebox.showwarning("Laboratorio", "Archivo Laboratorio_Virtual_Sensores.html no encontrado.")

    def open_cheatsheet_window():
        cs_win = tk.Toplevel(root)
        cs_win.title("Cheatsheet Maestro de Fórmulas - UPC GREELEC")
        cs_win.geometry("900x700")
        cs_win.configure(bg=BG_CANVAS)
        
        st = ScrolledText(cs_win, bg=BG_INSET, fg=TXT_PRIMARY, insertbackground="#fff", font=(FONT_FAMILY, 10), wrap="word", padx=12, pady=12)
        st.pack(fill="both", expand=True, padx=14, pady=14)
        st.insert("1.0", engine.generate_degree_cheatsheet())
        st.config(state="disabled")

    def open_engineering_tools_window():
        et_win = tk.Toplevel(root)
        et_win.title("🛠️ Suite de Ingeniería Especializada GREELEC (37 Solvers) - UPC ETSETB")
        et_win.geometry("1100x750")
        et_win.configure(bg=BG_CANVAS)
        build_tools_workbench(et_win)

    def make_btn(p, txt, cmd, bg_col=BG_CARD, fg_col=TXT_PRIMARY, hover_col="#2a2a2e"):
        b = tk.Button(
            p, text=txt, command=cmd, font=(FONT_FAMILY, 9, "bold"),
            bg=bg_col, fg=fg_col, activebackground=hover_col, activeforeground=fg_col,
            relief="flat", bd=0, padx=10, pady=5, cursor="hand2"
        )
        b.bind("<Enter>", lambda e: b.config(bg=hover_col))
        b.bind("<Leave>", lambda e: b.config(bg=bg_col))
        return b

    make_btn(action_box, "🛠️ Suite 37 Solvers", open_engineering_tools_window, bg_col="#234229", hover_col="#2f5737").pack(side="left", padx=3)
    make_btn(action_box, "🔬 Laboratorio Virtual", open_virtual_lab, bg_col="#1a3b5c", hover_col="#205080").pack(side="left", padx=3)
    make_btn(action_box, "📋 Cheatsheet Fórmulas", open_cheatsheet_window).pack(side="left", padx=3)
    make_btn(action_box, "📚 Exportar 35 Guías .MD", export_all_md).pack(side="left", padx=3)
    make_btn(action_box, "🧠 Exportar Mazos Anki", export_all_anki).pack(side="left", padx=3)

    # 2. Filter & Search Bar
    filter_bar = tk.Frame(main_box, bg=BG_CARD, bd=1, relief="solid", highlightbackground=BG_BORDER, highlightthickness=1)
    filter_bar.pack(fill="x", pady=(0, 10), padx=2, ipady=6)

    tk.Label(filter_bar, text="🔍 Buscar:", font=(FONT_FAMILY, 9, "bold"), fg=TXT_PRIMARY, bg=BG_CARD).pack(side="left", padx=(12, 6))
    search_var = tk.StringVar()
    search_entry = tk.Entry(filter_bar, textvariable=search_var, font=(FONT_FAMILY, 9), bg=BG_INSET, fg=TXT_PRIMARY, insertbackground="#fff", bd=0, relief="flat", width=35)
    search_entry.pack(side="left", ipady=4, padx=(0, 16))

    tk.Label(filter_bar, text="📅 Semestre:", font=(FONT_FAMILY, 9, "bold"), fg=TXT_PRIMARY, bg=BG_CARD).pack(side="left", padx=(0, 6))
    semester_var = tk.StringVar(value="Todos los Semestres (Q1 - Q8)")
    semester_combo = ttk.Combobox(
        filter_bar,
        textvariable=semester_var,
        values=[
            "Todos los Semestres (Q1 - Q8)",
            "Semestre 1 (Q1)", "Semestre 2 (Q2)", "Semestre 3 (Q3)", "Semestre 4 (Q4)",
            "Semestre 5 (Q5)", "Semestre 6 (Q6)", "Semestre 7 (Q7)", "Semestre 8 (Q8)"
        ],
        state="readonly",
        width=25
    )
    semester_combo.pack(side="left", ipady=2, padx=(0, 16))

    lbl_count = tk.Label(filter_bar, text="35 asignaturas mostradas", font=(FONT_FAMILY, 9, "italic"), fg=TXT_MUTED, bg=BG_CARD)
    lbl_count.pack(side="right", padx=12)

    # 3. Master-Detail Split Layout
    paned = tk.PanedWindow(main_box, orient="horizontal", bg=BG_BORDER, sashwidth=4, bd=0)
    paned.pack(fill="both", expand=True)

    # Left Panel: Course Table
    left_frame = tk.Frame(paned, bg=BG_CARD, width=340)
    paned.add(left_frame, minsize=280)

    tk.Label(left_frame, text="Plan de Estudios Oficial", font=(FONT_FAMILY, 10, "bold"), fg=TXT_PRIMARY, bg=BG_CARD).pack(anchor="w", padx=10, pady=(8, 4))

    tree_cols = ("sem", "code", "acr", "title")
    tree = ttk.Treeview(left_frame, columns=tree_cols, show="headings", selectmode="browse")
    tree.heading("sem", text="Q")
    tree.heading("code", text="Código")
    tree.heading("acr", text="Acr.")
    tree.heading("title", text="Asignatura")

    tree.column("sem", width=36, anchor="center")
    tree.column("code", width=62, anchor="center")
    tree.column("acr", width=60, anchor="center")
    tree.column("title", width=180, anchor="w")

    tree_scroll = ttk.Scrollbar(left_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=tree_scroll.set)
    tree_scroll.pack(side="right", fill="y")
    tree.pack(fill="both", expand=True, padx=(4, 0), pady=(0, 4))

    # Right Panel: Workstation Tabs
    right_frame = tk.Frame(paned, bg=BG_CANVAS)
    paned.add(right_frame, minsize=600)

    # Workstation Header banner
    work_header = tk.Frame(right_frame, bg=BG_CARD, bd=1, relief="solid", highlightbackground=BG_BORDER, highlightthickness=1)
    work_header.pack(fill="x", padx=6, pady=(0, 6), ipady=6)

    lbl_selected_title = tk.Label(work_header, text="Selecciona una asignatura para comenzar", font=(FONT_FAMILY, 12, "bold"), fg=TXT_PRIMARY, bg=BG_CARD)
    lbl_selected_title.pack(anchor="w", padx=12, pady=(2, 0))

    lbl_selected_meta = tk.Label(work_header, text="", font=(FONT_FAMILY, 9), fg=TXT_MUTED, bg=BG_CARD)
    lbl_selected_meta.pack(anchor="w", padx=12)

    # Sub-notebook for selected subject
    sub_nb = ttk.Notebook(right_frame)
    sub_nb.pack(fill="both", expand=True, padx=6, pady=(0, 6))

    tab_syllabus = tk.Frame(sub_nb, bg=BG_CANVAS)
    tab_formulas = tk.Frame(sub_nb, bg=BG_CANVAS)
    tab_calc = tk.Frame(sub_nb, bg=BG_CANVAS)
    tab_tools = tk.Frame(sub_nb, bg=BG_CANVAS)
    tab_spice = tk.Frame(sub_nb, bg=BG_CANVAS)
    tab_quiz = tk.Frame(sub_nb, bg=BG_CANVAS)

    sub_nb.add(tab_syllabus, text="📋 Ficha & Temario")
    sub_nb.add(tab_formulas, text="📐 Fórmulas LaTeX")
    sub_nb.add(tab_calc, text="⚡ Calculadora")
    sub_nb.add(tab_tools, text="🛠️ Herramientas de Ingeniería (37)")
    sub_nb.add(tab_spice, text="🔌 Banco SPICE / HDL")
    sub_nb.add(tab_quiz, text="🎯 Examen & Quiz (12)")

    # --- Constructor de la Suite de Herramientas de Ingeniería ---
    def build_tools_workbench(container, default_tool_name=None):
        import engineering_tools_suite as ets
        
        wb_box = tk.Frame(container, bg=BG_CANVAS)
        wb_box.pack(fill="both", expand=True, padx=6, pady=6)

        # Top Control Bar
        ctrl_bar = tk.Frame(wb_box, bg=BG_CARD, bd=1, relief="solid", highlightbackground=BG_BORDER, highlightthickness=1)
        ctrl_bar.pack(fill="x", pady=(0, 6), ipady=5, padx=2)

        tk.Label(ctrl_bar, text="📁 Rama:", font=(FONT_FAMILY, 9, "bold"), fg=TXT_PRIMARY, bg=BG_CARD).pack(side="left", padx=(10, 4))
        
        branch_options = [
            "Todas las Ramas (37 herramientas)",
            "RF, Microondas y Telecomunicación",
            "Electrónica Analógica y Potencia",
            "Sistemas Digitales y Embebidos",
            "Tratamiento de Señal y Comunicaciones",
            "Física, Sensores y Control"
        ]
        branch_var = tk.StringVar(value=branch_options[0])
        branch_combo = ttk.Combobox(ctrl_bar, textvariable=branch_var, values=branch_options, state="readonly", width=30)
        branch_combo.pack(side="left", padx=(0, 12), ipady=2)

        tk.Label(ctrl_bar, text="🛠️ Herramienta:", font=(FONT_FAMILY, 9, "bold"), fg=TXT_PRIMARY, bg=BG_CARD).pack(side="left", padx=(0, 4))
        
        tool_names_all = list(ets.ALL_ENGINEERING_TOOLS.keys())
        tool_var = tk.StringVar(value=default_tool_name or tool_names_all[0])
        tool_combo = ttk.Combobox(ctrl_bar, textvariable=tool_var, state="readonly", width=36)
        tool_combo.pack(side="left", padx=(0, 10), ipady=2)

        # Split: Left (Inputs & Metadata) / Right (Outputs & Code)
        paned_tool = tk.PanedWindow(wb_box, orient="horizontal", bg=BG_BORDER, sashwidth=4, bd=0)
        paned_tool.pack(fill="both", expand=True)

        left_side = tk.Frame(paned_tool, bg=BG_CARD, bd=1, relief="solid", highlightbackground=BG_BORDER, highlightthickness=1)
        paned_tool.add(left_side, minsize=320)

        right_side = tk.Frame(paned_tool, bg=BG_CARD, bd=1, relief="solid", highlightbackground=BG_BORDER, highlightthickness=1)
        paned_tool.add(right_side, minsize=380)

        # Left Info Header
        info_header = tk.Frame(left_side, bg=BG_CARD)
        info_header.pack(fill="x", padx=10, pady=(8, 4))

        lbl_tool_title = tk.Label(info_header, text="", font=(FONT_FAMILY, 10, "bold"), fg=ACCENT_CYAN, bg=BG_CARD, wraplength=320, justify="left")
        lbl_tool_title.pack(anchor="w")

        lbl_tool_branch = tk.Label(info_header, text="", font=(FONT_FAMILY, 8, "bold"), fg=ACCENT_ORANGE, bg=BG_CARD)
        lbl_tool_branch.pack(anchor="w", pady=(2, 0))

        lbl_tool_courses = tk.Label(info_header, text="", font=(FONT_FAMILY, 8), fg=TXT_MUTED, bg=BG_CARD)
        lbl_tool_courses.pack(anchor="w")

        lbl_tool_desc = tk.Label(info_header, text="", font=(FONT_FAMILY, 8), fg=TXT_PRIMARY, bg=BG_CARD, wraplength=320, justify="left")
        lbl_tool_desc.pack(anchor="w", pady=(4, 6))

        tk.Label(left_side, text="Parámetros de Entrada:", font=(FONT_FAMILY, 9, "bold"), fg=TXT_PRIMARY, bg=BG_CARD).pack(anchor="w", padx=10, pady=(4, 2))

        params_scroll_canvas = tk.Canvas(left_side, bg=BG_CARD, highlightthickness=0)
        params_sb = ttk.Scrollbar(left_side, orient="vertical", command=params_scroll_canvas.yview)
        params_inner = tk.Frame(params_scroll_canvas, bg=BG_CARD)

        params_inner.bind("<Configure>", lambda e: params_scroll_canvas.configure(scrollregion=params_scroll_canvas.bbox("all")))
        params_scroll_canvas.create_window((0, 0), window=params_inner, anchor="nw")
        params_scroll_canvas.configure(yscrollcommand=params_sb.set)

        params_scroll_canvas.pack(side="top", fill="both", expand=True, padx=6)
        params_sb.pack(side="right", fill="y")

        param_inputs: dict[str, tk.StringVar] = {}

        # Button frame at bottom of left side
        btn_calc_frame = tk.Frame(left_side, bg=BG_CARD)
        btn_calc_frame.pack(fill="x", padx=10, pady=8)

        # Right Side Output
        out_top = tk.Frame(right_side, bg=BG_CARD)
        out_top.pack(fill="x", padx=10, pady=(8, 4))

        tk.Label(out_top, text="Resultados del Solver / Síntesis:", font=(FONT_FAMILY, 10, "bold"), fg=TXT_PRIMARY, bg=BG_CARD).pack(side="left")

        def copy_tool_output():
            txt = txt_tool_out.get("1.0", "end").strip()
            if txt:
                root.clipboard_clear()
                root.clipboard_append(txt)
                messagebox.showinfo("Portapapeles", "✅ Resultados copiados al portapapeles.")

        def save_tool_output():
            txt = txt_tool_out.get("1.0", "end").strip()
            if not txt:
                return
            tname = tool_var.get()
            fn = filedialog.asksaveasfilename(title="Guardar resultados de ingeniería", initialfile=f"{tname}_resultado.txt")
            if fn:
                with open(fn, "w", encoding="utf-8") as f:
                    f.write(txt)
                messagebox.showinfo("Guardado", f"✅ Fichero guardado en:\n{fn}")

        make_btn(out_top, "📋 Copiar", copy_tool_output).pack(side="right", padx=2)
        make_btn(out_top, "💾 Guardar...", save_tool_output).pack(side="right", padx=2)

        txt_tool_out = ScrolledText(right_side, bg=BG_INSET, fg=ACCENT_GREEN, insertbackground="#fff", font=("Consolas", 10), wrap="word", padx=10, pady=10)
        txt_tool_out.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        def execute_tool_solver():
            tname = tool_var.get()
            meta = ets.get_tool_metadata(tname)
            if not meta:
                return
            p_dict = {}
            for pk, pvar in param_inputs.items():
                val_str = pvar.get().strip()
                p_spec = meta["params"].get(pk, {})
                ptype = p_spec.get("type", "float")
                try:
                    if ptype == "float":
                        p_dict[pk] = float(val_str)
                    elif ptype == "int":
                        p_dict[pk] = int(val_str)
                    elif ptype == "list":
                        p_dict[pk] = json.loads(val_str)
                    else:
                        p_dict[pk] = val_str
                except Exception:
                    p_dict[pk] = val_str
            
            try:
                res = ets.run_engineering_tool(tname, p_dict)
                txt_tool_out.delete("1.0", "end")
                txt_tool_out.insert("end", f"=== {meta['title'].upper()} ===\n")
                txt_tool_out.insert("end", f"Rama: {meta['branch']} | Asignaturas: {', '.join(meta.get('courses', []))}\n")
                txt_tool_out.insert("end", "-" * 55 + "\n\n")
                
                for rk, rv in res.items():
                    if isinstance(rv, (dict, list)):
                        txt_tool_out.insert("end", f"▶ {rk}:\n{json.dumps(rv, indent=2, ensure_ascii=False)}\n\n")
                    elif isinstance(rv, str) and "\n" in rv:
                        txt_tool_out.insert("end", f"▶ {rk}:\n{rv}\n\n")
                    else:
                        txt_tool_out.insert("end", f"  • {rk:<30}: {rv}\n")
            except Exception as ex:
                txt_tool_out.delete("1.0", "end")
                txt_tool_out.insert("1.0", f"Error en solver: {ex}")

        make_btn(btn_calc_frame, "⚡ Calcular / Sintetizar", execute_tool_solver, bg_col=ACCENT_BLUE, hover_col=ACCENT_HOVER).pack(fill="x")

        def on_tool_change(new_tool_name):
            meta = ets.get_tool_metadata(new_tool_name)
            if not meta:
                return
            tool_var.set(new_tool_name)
            lbl_tool_title.config(text=meta["title"])
            lbl_tool_branch.config(text=f"RAMA: {meta['branch']}")
            lbl_tool_courses.config(text=f"Asignaturas: {', '.join(meta.get('courses', []))}")
            lbl_tool_desc.config(text=meta["description"])

            # Clean and rebuild parameter inputs
            for w in params_inner.winfo_children():
                w.destroy()
            param_inputs.clear()

            for pk, p_spec in meta.get("params", {}).items():
                p_row = tk.Frame(params_inner, bg=BG_CARD)
                p_row.pack(fill="x", pady=2)
                
                p_lbl = tk.Label(p_row, text=f"{p_spec.get('label', pk)}:", font=(FONT_FAMILY, 8), fg=TXT_PRIMARY, bg=BG_CARD, anchor="w", wraplength=190, justify="left")
                p_lbl.pack(side="left", fill="x", expand=True)

                def_val = p_spec.get("default", "")
                if isinstance(def_val, list):
                    def_str = json.dumps(def_val)
                else:
                    def_str = str(def_val) if def_val is not None else ""

                p_var = tk.StringVar(value=def_str)
                param_inputs[pk] = p_var

                p_entry = tk.Entry(p_row, textvariable=p_var, font=("Consolas", 9), bg=BG_INSET, fg=TXT_PRIMARY, insertbackground="#fff", bd=0, relief="flat", width=12)
                p_entry.pack(side="right", padx=4, ipady=1)

            execute_tool_solver()

        def update_tool_dropdown(*_):
            sel_b = branch_var.get()
            if "Todas" in sel_b:
                filtered_tools = list(ets.ALL_ENGINEERING_TOOLS.keys())
            else:
                filtered_tools = [k for k, v in ets.ENGINEERING_TOOLS_METADATA.items() if v.get("branch") == sel_b]
            tool_combo["values"] = filtered_tools
            if filtered_tools:
                if tool_var.get() not in filtered_tools:
                    tool_var.set(filtered_tools[0])
                on_tool_change(tool_var.get())

        branch_combo.bind("<<ComboboxSelected>>", update_tool_dropdown)
        tool_combo.bind("<<ComboboxSelected>>", lambda e: on_tool_change(tool_var.get()))

        update_tool_dropdown()
        if default_tool_name and default_tool_name in ets.ALL_ENGINEERING_TOOLS:
            tool_var.set(default_tool_name)
            on_tool_change(default_tool_name)

        return tool_var, on_tool_change

    tool_var_subnb, on_tool_change_subnb = build_tools_workbench(tab_tools)

    # --- Pestaña 1: Ficha & Temario ---
    txt_syllabus = ScrolledText(tab_syllabus, bg=BG_INSET, fg=TXT_PRIMARY, insertbackground="#fff", font=(FONT_FAMILY, 9), wrap="word", padx=10, pady=10)
    txt_syllabus.pack(fill="both", expand=True, padx=6, pady=6)

    # --- Pestaña 2: Fórmulas LaTeX ---
    f_box = tk.Frame(tab_formulas, bg=BG_CANVAS)
    f_box.pack(fill="both", expand=True, padx=6, pady=6)
    txt_formulas = ScrolledText(f_box, bg=BG_INSET, fg=ACCENT_CYAN, insertbackground="#fff", font=("Consolas", 10), wrap="word", padx=10, pady=10)
    txt_formulas.pack(fill="both", expand=True)

    # --- Pestaña 3: Calculadora ---
    calc_container = tk.Frame(tab_calc, bg=BG_CANVAS)
    calc_container.pack(fill="both", expand=True, padx=8, pady=8)

    calc_inputs_frame = tk.Frame(calc_container, bg=BG_CARD, bd=1, relief="solid", highlightbackground=BG_BORDER, highlightthickness=1)
    calc_inputs_frame.pack(side="left", fill="both", expand=True, padx=(0, 4), pady=2)

    tk.Label(calc_inputs_frame, text="Parámetros de Entrada", font=(FONT_FAMILY, 10, "bold"), fg=TXT_PRIMARY, bg=BG_CARD).pack(anchor="w", padx=10, pady=(8, 6))
    calc_entries_box = tk.Frame(calc_inputs_frame, bg=BG_CARD)
    calc_entries_box.pack(fill="both", expand=True, padx=10, pady=4)

    calc_outputs_frame = tk.Frame(calc_container, bg=BG_CARD, bd=1, relief="solid", highlightbackground=BG_BORDER, highlightthickness=1)
    calc_outputs_frame.pack(side="right", fill="both", expand=True, padx=(4, 0), pady=2)

    tk.Label(calc_outputs_frame, text="Resultados Calculados", font=(FONT_FAMILY, 10, "bold"), fg=TXT_PRIMARY, bg=BG_CARD).pack(anchor="w", padx=10, pady=(8, 6))
    txt_calc_res = ScrolledText(calc_outputs_frame, bg=BG_INSET, fg=ACCENT_GREEN, font=("Consolas", 10), wrap="word", padx=10, pady=10)
    txt_calc_res.pack(fill="both", expand=True, padx=8, pady=8)

    calc_param_vars: dict[str, tk.StringVar] = {}

    # --- Pestaña 4: SPICE / HDL ---
    spice_container = tk.Frame(tab_spice, bg=BG_CANVAS)
    spice_container.pack(fill="both", expand=True, padx=6, pady=6)

    spice_btn_bar = tk.Frame(spice_container, bg=BG_CANVAS)
    spice_btn_bar.pack(fill="x", pady=(0, 4))

    def copy_spice():
        root.clipboard_clear()
        root.clipboard_append(txt_spice.get("1.0", "end"))
        messagebox.showinfo("Portapapeles", "✅ Código SPICE/HDL copiado al portapapeles.")

    def save_spice():
        cur_code = selected_code.get()
        if not cur_code:
            return
        fn = filedialog.asksaveasfilename(title="Guardar código de laboratorio", initialfile=f"UPC_{cur_code}_bench.txt")
        if fn:
            with open(fn, "w", encoding="utf-8") as f:
                f.write(txt_spice.get("1.0", "end"))
            messagebox.showinfo("Guardado", f"✅ Fichero guardado en:\n{fn}")

    make_btn(spice_btn_bar, "📋 Copiar Código", copy_spice).pack(side="left", padx=(0, 4))
    make_btn(spice_btn_bar, "💾 Guardar Archivo...", save_spice).pack(side="left")

    txt_spice = ScrolledText(spice_container, bg=BG_INSET, fg="#ffcc66", insertbackground="#fff", font=("Consolas", 10), wrap="none", padx=10, pady=10)
    txt_spice.pack(fill="both", expand=True)

    # --- Pestaña 5: Quiz Interactivo ---
    quiz_container = tk.Frame(tab_quiz, bg=BG_CANVAS)
    quiz_container.pack(fill="both", expand=True, padx=6, pady=6)

    quiz_top = tk.Frame(quiz_container, bg=BG_CARD, bd=1, relief="solid", highlightbackground=BG_BORDER, highlightthickness=1)
    quiz_top.pack(fill="x", pady=(0, 6), ipady=4)

    lbl_quiz_status = tk.Label(quiz_top, text="Responde a las preguntas de examen oficial y pulsa Corregir.", font=(FONT_FAMILY, 9), fg=TXT_PRIMARY, bg=BG_CARD)
    lbl_quiz_status.pack(side="left", padx=10)

    quiz_ans_vars: dict[int, tk.StringVar] = {}

    quiz_scroll_frame = tk.Frame(quiz_container, bg=BG_CANVAS)
    quiz_scroll_frame.pack(fill="both", expand=True)

    quiz_canvas = tk.Canvas(quiz_scroll_frame, bg=BG_CANVAS, highlightthickness=0)
    quiz_sb = ttk.Scrollbar(quiz_scroll_frame, orient="vertical", command=quiz_canvas.yview)
    quiz_inner = tk.Frame(quiz_canvas, bg=BG_CANVAS)

    quiz_inner.bind("<Configure>", lambda e: quiz_canvas.configure(scrollregion=quiz_canvas.bbox("all")))
    quiz_canvas.create_window((0, 0), window=quiz_inner, anchor="nw")
    quiz_canvas.configure(yscrollcommand=quiz_sb.set)

    quiz_canvas.pack(side="left", fill="both", expand=True)
    quiz_sb.pack(side="right", fill="y")

    # State
    selected_code = tk.StringVar()

    def execute_calc_action():
        code = selected_code.get()
        if not code:
            return
        params = {}
        for k, v in calc_param_vars.items():
            try:
                params[k] = float(v.get())
            except ValueError:
                params[k] = v.get()
        res = engine.run_calculator(code, params)
        txt_calc_res.delete("1.0", "end")
        if "error" in res:
            txt_calc_res.insert("1.0", f"Error: {res['error']}")
        else:
            txt_calc_res.insert("end", f"=== RESULTADOS SIMULACIÓN ({res['subject']}) ===\n\n")
            for out_k, out_v in res["outputs"].items():
                txt_calc_res.insert("end", f"  • {out_k}: {out_v}\n")
            txt_calc_res.insert("end", "\nParámetros utilizados:\n")
            for in_k, in_v in res["inputs_used"].items():
                txt_calc_res.insert("end", f"    - {in_k} = {in_v}\n")

    def grade_quiz():
        code = selected_code.get()
        if not code:
            return
        answers = {i: quiz_ans_vars[i].get() for i in quiz_ans_vars}
        eval_res = engine.evaluate_quiz(code, answers)
        if "error" in eval_res:
            messagebox.showerror("Error", eval_res["error"])
            return
        score = eval_res["score_out_of_10"]
        correct = eval_res["correct_answers"]
        total = eval_res["total_questions"]
        state_txt = f"Nota: {score} / 10.0 ({correct} aciertos de {total}) - {'APROBADO ✅' if score >= 5.0 else 'SUSPENSO ❌'}"
        lbl_quiz_status.config(text=state_txt, fg=ACCENT_GREEN if score >= 5.0 else "#ff453a")
        
        # Color feedback on questions
        for item in eval_res["details"]:
            idx = item["index"] - 1
            if idx in quiz_feedback_labels:
                f_lbl = quiz_feedback_labels[idx]
                if item["is_correct"]:
                    f_lbl.config(text=f"✅ Correcto ({item['correct_answer']}): {item['justification']}", fg=ACCENT_GREEN)
                else:
                    f_lbl.config(text=f"❌ Incorrecto. Correcta: [{item['correct_answer']}]. {item['justification']}", fg="#ff9f0a")

    make_btn(quiz_top, "✅ Corregir Examen", grade_quiz, bg_col=ACCENT_BLUE, hover_col=ACCENT_HOVER).pack(side="right", padx=10)

    quiz_feedback_labels: dict[int, tk.Label] = {}

    def load_subject_details(code: str):
        s = engine.get_subject_by_code(code)
        if not s:
            return
        selected_code.set(code)
        lbl_selected_title.config(text=f"Q{s['semester']} · {s['code']} - {s['title']} ({s['acronym']})")
        lbl_selected_meta.config(text=f"{s['ects']} ECTS ({s.get('hours', '150 h')}) · {s['department']} · Prof: {s.get('responsible_professor', 'Coordinación')}")

        # Tab 1: Ficha & Temario
        txt_syllabus.delete("1.0", "end")
        txt_syllabus.insert("end", f"=== {s['title']} ({s['acronym']}) ===\n\n")
        txt_syllabus.insert("end", f"DESCRIPCIÓN:\n{s['description']}\n\n")
        txt_syllabus.insert("end", "OBJETIVOS DE APRENDIZAJE:\n")
        for obj in s.get("objectives", []):
            txt_syllabus.insert("end", f"  • {obj}\n")
        txt_syllabus.insert("end", "\nTEMARIO Y CONTENIDOS:\n")
        for c in s.get("contents", []):
            txt_syllabus.insert("end", f"  • {c}\n")
        txt_syllabus.insert("end", f"\nEVALUACIÓN:\n{s.get('evaluation', 'Evaluación continua.')}\n\n")
        txt_syllabus.insert("end", "BIBLIOGRAFÍA OFICIAL:\n")
        for b in s.get("bibliography", []):
            txt_syllabus.insert("end", f"  • {b}\n")
        txt_syllabus.insert("end", f"\nGuía Docente Oficial en PDF: {s.get('pdf_url', '')}\n")

        # Tab 2: Fórmulas
        txt_formulas.delete("1.0", "end")
        for idx, f in enumerate(s.get("formulas", []), start=1):
            txt_formulas.insert("end", f"[{idx}] {f['name']}\n")
            txt_formulas.insert("end", f"    {f['latex']}\n\n")

        # Tab 3: Calculadora
        for widget in calc_entries_box.winfo_children():
            widget.destroy()
        calc_param_vars.clear()
        for p_k, p_v in s.get("calc_params", {}).items():
            row = tk.Frame(calc_entries_box, bg=BG_CARD)
            row.pack(fill="x", pady=2)
            tk.Label(row, text=f"{p_k}:", width=18, anchor="w", font=(FONT_FAMILY, 9), fg=TXT_PRIMARY, bg=BG_CARD).pack(side="left")
            var = tk.StringVar(value=str(p_v))
            calc_param_vars[p_k] = var
            e = tk.Entry(row, textvariable=var, font=("Consolas", 9), bg=BG_INSET, fg=TXT_PRIMARY, insertbackground="#fff", bd=0, relief="flat", width=14)
            e.pack(side="left", padx=4, ipady=2)
        make_btn(calc_entries_box, "⚡ Calcular Parámetros", execute_calc_action, bg_col=ACCENT_BLUE, hover_col=ACCENT_HOVER).pack(pady=(10, 4))
        execute_calc_action()

        # Tab Herramientas de Ingeniería: auto-seleccionar solver relevante
        try:
            import engineering_tools_suite as ets
            matching_tool = None
            for t_name, t_meta in ets.ENGINEERING_TOOLS_METADATA.items():
                for c_str in t_meta.get("courses", []):
                    if s["code"] in c_str or s["acronym"] in c_str:
                        matching_tool = t_name
                        break
                if matching_tool:
                    break
            if matching_tool and on_tool_change_subnb:
                on_tool_change_subnb(matching_tool)
        except Exception:
            pass

        # Tab 4: SPICE / HDL
        txt_spice.delete("1.0", "end")
        txt_spice.insert("1.0", s.get("spice_template", ""))

        # Tab 5: Quiz
        for widget in quiz_inner.winfo_children():
            widget.destroy()
        quiz_ans_vars.clear()
        quiz_feedback_labels.clear()
        lbl_quiz_status.config(text=f"Autoevaluación de {s['acronym']} (12 preguntas oficiales)", fg=TXT_PRIMARY)

        for i, q in enumerate(s.get("questions", [])):
            q_card = tk.Frame(quiz_inner, bg=BG_CARD, bd=1, relief="solid", highlightbackground=BG_BORDER, highlightthickness=1)
            q_card.pack(fill="x", padx=6, pady=4, ipady=4)

            q_text_lbl = tk.Label(q_card, text=f"{i+1}. {q['q']}", font=(FONT_FAMILY, 9, "bold"), fg=TXT_PRIMARY, bg=BG_CARD, wraplength=520, justify="left")
            q_text_lbl.pack(anchor="w", padx=8, pady=(4, 2))

            ans_var = tk.StringVar(value="")
            quiz_ans_vars[i] = ans_var

            opts_frame = tk.Frame(q_card, bg=BG_CARD)
            opts_frame.pack(anchor="w", padx=8, pady=2)

            tk.Radiobutton(opts_frame, text="Verdadero (V)", variable=ans_var, value="V", font=(FONT_FAMILY, 9), fg=TXT_PRIMARY, bg=BG_CARD, selectcolor=BG_INSET, activebackground=BG_CARD, activeforeground=TXT_PRIMARY).pack(side="left", padx=(0, 14))
            tk.Radiobutton(opts_frame, text="Falso (F)", variable=ans_var, value="F", font=(FONT_FAMILY, 9), fg=TXT_PRIMARY, bg=BG_CARD, selectcolor=BG_INSET, activebackground=BG_CARD, activeforeground=TXT_PRIMARY).pack(side="left")

            fb_lbl = tk.Label(q_card, text="", font=(FONT_FAMILY, 8, "italic"), fg=TXT_MUTED, bg=BG_CARD, wraplength=520, justify="left")
            fb_lbl.pack(anchor="w", padx=8, pady=(2, 4))
            quiz_feedback_labels[i] = fb_lbl

    def populate_tree():
        for item in tree.get_children():
            tree.delete(item)
        query = search_var.get().strip()
        sem_filter = semester_var.get()
        sem_num = None
        if "Semestre" in sem_filter:
            try:
                sem_num = int(sem_filter.split("Semestre")[1].split("(")[0].strip())
            except Exception:
                pass

        if query:
            matched = engine.search_curriculum(query)
        else:
            matched = engine.get_all_subjects()

        if sem_num:
            matched = [s for s in matched if s.get("semester") == sem_num]

        lbl_count.config(text=f"{len(matched)} asignaturas encontradas")

        for s in matched:
            tree.insert("", "end", iid=s["code"], values=(s["semester"], s["code"], s["acronym"], s["title"]))

        # Select first item if exists
        children = tree.get_children()
        if children:
            first = children[0]
            tree.selection_set(first)
            load_subject_details(first)

    def on_tree_select(event):
        sel = tree.selection()
        if sel:
            load_subject_details(sel[0])

    tree.bind("<<TreeviewSelect>>", on_tree_select)
    search_var.trace_add("write", lambda *args: populate_tree())
    semester_combo.bind("<<ComboboxSelected>>", lambda e: populate_tree())

    # Initial population
    populate_tree()
