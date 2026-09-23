# -*- coding: utf-8 -*-
"""
UPC ETSETB - Grado en Ingeniería Electrónica de Telecomunicación (GREELEC)
Master Academic Knowledge & Simulation Engine (35 Compulsory Subjects)
======================================================================
Provides complete course metadata, official syllabi, mathematical models (LaTeX),
executable simulation/calculators, laboratory benches, SPICE netlists, and
over 420 official exam/self-assessment questions with technical rationales.
"""
from __future__ import annotations
import os
import sys
import re
import json
import math
import argparse
from pathlib import Path
from typing import Dict, List, Any, Tuple, Optional

# Path to master catalog data file
MASTER_DATA_PATH = Path(__file__).resolve().parent / "data" / "upc_curriculum_master.json"

class UPCDegreeEngine:
    """
    Comprehensive curriculum engine for GREELEC (UPC ETSETB).
    Integrates 35 compulsory courses, 420+ questions, calculators, and exports.
    """
    def __init__(self, data_path: Optional[str | Path] = None):
        self.data_path = Path(data_path) if data_path else MASTER_DATA_PATH
        self.subjects: Dict[str, Dict[str, Any]] = {}
        self._load_catalog()

    def _load_catalog(self) -> None:
        """Loads the full catalog from JSON."""
        if not self.data_path.exists():
            raise FileNotFoundError(f"Curriculum master file not found at: {self.data_path}")
        with open(self.data_path, "r", encoding="utf-8") as f:
            self.subjects = json.load(f)

    def get_all_subjects(self) -> List[Dict[str, Any]]:
        """Returns all 35 compulsory subjects sorted by semester and code."""
        return sorted(self.subjects.values(), key=lambda s: (s.get("semester", 1), s.get("code", "")))

    def get_subject_by_code(self, code: str) -> Optional[Dict[str, Any]]:
        """Retrieves a single subject by its official UPC code."""
        return self.subjects.get(str(code).strip())

    def get_subject_by_acronym(self, acronym: str) -> Optional[Dict[str, Any]]:
        """Retrieves a single subject by its acronym (e.g. 'CCE', 'DD', 'CA')."""
        acr = acronym.strip().upper()
        for s in self.subjects.values():
            if s.get("acronym", "").upper() == acr:
                return s
        return None

    def get_subjects_by_semester(self, semester: int) -> List[Dict[str, Any]]:
        """Returns all subjects taught in the specified semester (1 to 8)."""
        return [s for s in self.get_all_subjects() if s.get("semester") == semester]

    def search_curriculum(self, query: str) -> List[Dict[str, Any]]:
        """Full-text search across titles, acronyms, descriptions, contents, and formulas."""
        q = query.strip().lower()
        if not q:
            return self.get_all_subjects()
        matches = []
        for s in self.get_all_subjects():
            c_texts = [c if isinstance(c, str) else str(c) for c in s.get("contents", [])]
            f_texts = [f.get("name", "") if isinstance(f, dict) else str(f) for f in s.get("formulas", [])]
            text_corpus = " ".join([
                str(s.get("code", "")),
                str(s.get("acronym", "")),
                str(s.get("title", "")),
                str(s.get("description", "")),
                " ".join(c_texts),
                " ".join(f_texts),
                str(s.get("department", ""))
            ]).lower()
            if q in text_corpus:
                matches.append(s)
        return matches

    def get_all_questions(self) -> List[Dict[str, Any]]:
        """Returns a flat list of all 420+ technical questions with subject context."""
        out = []
        for s in self.get_all_subjects():
            for idx, q_item in enumerate(s.get("questions", []), start=1):
                out.append({
                    "subject_code": s["code"],
                    "subject_acronym": s["acronym"],
                    "subject_title": s["title"],
                    "question_idx": idx,
                    "question": q_item["q"],
                    "answer": q_item["a"],
                    "justification": q_item["j"]
                })
        return out

    def get_questions_by_subject(self, code_or_acronym: str) -> List[Dict[str, Any]]:
        """Returns the question set for a given subject."""
        s = self.get_subject_by_code(code_or_acronym) or self.get_subject_by_acronym(code_or_acronym)
        if not s:
            return []
        return s.get("questions", [])

    def evaluate_quiz(self, code_or_acronym: str, answers: Dict[int, str]) -> Dict[str, Any]:
        """
        Evaluates user answers for a subject quiz.
        answers: dictionary mapping question index (0-based) to 'V' or 'F'.
        """
        questions = self.get_questions_by_subject(code_or_acronym)
        if not questions:
            return {"error": f"Subject {code_or_acronym} not found or has no questions."}
        
        total = len(questions)
        correct = 0
        feedback = []
        
        for i, q in enumerate(questions):
            user_ans = answers.get(i, "").strip().upper()
            true_ans = q["a"].strip().upper()
            is_ok = (user_ans == true_ans)
            if is_ok:
                correct += 1
            feedback.append({
                "index": i + 1,
                "question": q["q"],
                "user_answer": user_ans,
                "correct_answer": true_ans,
                "is_correct": is_ok,
                "justification": q["j"]
            })
            
        score_10 = (correct / total) * 10.0 if total > 0 else 0.0
        return {
            "subject": code_or_acronym,
            "total_questions": total,
            "correct_answers": correct,
            "score_out_of_10": round(score_10, 2),
            "passed": score_10 >= 5.0,
            "details": feedback
        }

    def run_calculator(self, code_or_acronym: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Executes the parametric calculator associated with the course."""
        s = self.get_subject_by_code(code_or_acronym) or self.get_subject_by_acronym(code_or_acronym)
        if not s:
            return {"error": f"Subject {code_or_acronym} not found."}
        
        calc_fn_str = s.get("calc_fn", "")
        if not calc_fn_str:
            return {"error": f"No calculator function defined for {s['code']}."}
            
        calc_params = dict(s.get("calc_params", {}))
        if params:
            calc_params.update(params)
            
        # Execute calculator in safe isolated scope
        local_scope = {}
        try:
            exec(calc_fn_str, {"math": math}, local_scope)
            calc_func = local_scope.get("calc")
            if callable(calc_func):
                result = calc_func(calc_params)
                return {
                    "subject": f"{s['code']} - {s['acronym']}",
                    "inputs_used": calc_params,
                    "outputs": result
                }
            else:
                return {"error": "Calculator function signature invalid."}
        except Exception as e:
            return {"error": f"Calculation error: {str(e)}"}

    def get_spice_template(self, code_or_acronym: str) -> str:
        """Returns the laboratory SPICE netlist, VHDL, or C template for the course."""
        s = self.get_subject_by_code(code_or_acronym) or self.get_subject_by_acronym(code_or_acronym)
        if not s:
            return f"# Subject {code_or_acronym} not found."
        return s.get("spice_template", "# No template available.")

    def export_subject_markdown(self, code_or_acronym: str) -> str:
        """Generates an extensive study guide markdown document for NotebookLM or study."""
        s = self.get_subject_by_code(code_or_acronym) or self.get_subject_by_acronym(code_or_acronym)
        if not s:
            return f"# Asignatura {code_or_acronym} no encontrada."
            
        md = []
        md.append(f"# {s['code']} - {s['title']} ({s['acronym']})")
        md.append(f"**Grado en Ingeniería Electrónica de Telecomunicación (GREELEC)**  ")
        md.append(f"*Escuela Técnica Superior de Ingeniería de Telecomunicación de Barcelona (ETSETB - UPC)*\n")
        
        md.append("## 1. Ficha Técnica y Metadatos Oficiales")
        md.append(f"- **Código UPC**: `{s['code']}`")
        md.append(f"- **Acrónimo Oficial**: `{s['acronym']}`")
        md.append(f"- **Semestre**: Q{s['semester']} ({'Fase Inicial' if s['semester'] <= 2 else 'Fase Troncal / Especialización'})")
        md.append(f"- **Créditos ECTS**: {s['ects']} ECTS ({s.get('hours', '150 h')})")
        md.append(f"- **Departamento Responsable**: {s['department']}")
        md.append(f"- **Profesorado / Coordinación**: {s.get('responsible_professor', 'Profesorado EEL/TSC/DAC')}")
        md.append(f"- **Guía Docente Oficial en PDF**: [{s['code']}_guia_docent.pdf]({s.get('pdf_url', '')})\n")
        
        md.append("## 2. Descripción General y Requisitos")
        md.append(f"{s['description']}\n")
        
        md.append("## 3. Objetivos de Aprendizaje y Competencias")
        for obj in s.get("objectives", []):
            md.append(f"- {obj}")
        md.append("")
        
        md.append("## 4. Temario y Unidades de Contenido")
        for c in s.get("contents", []):
            md.append(f"- {c}")
        md.append("")
        
        md.append("## 5. Modelado Matemático y Fórmulas Clave (LaTeX)")
        for idx, f in enumerate(s.get("formulas", []), start=1):
            md.append(f"### 5.{idx} {f['name']}")
            md.append(f"$$\n{f['latex']}\n$$\n")
            
        md.append("## 6. Banco de Ensayos / Laboratorio Virtual")
        template = s.get("spice_template", "")
        lang = "spice" if "*" in template[:20] else ("vhdl" if "--" in template[:20] else "c")
        md.append(f"```{lang}\n{template}```\n")
        
        md.append("## 7. Preguntas de Autoevaluación y Examen con Justificación Técnica")
        for idx, q in enumerate(s.get("questions", []), start=1):
            md.append(f"#### Pregunta {idx}")
            md.append(f"**{q['q']}**")
            md.append(f"- **Respuesta**: `[{q['a']}]` ({'Verdadero' if q['a'] == 'V' else 'Falso'})")
            md.append(f"- **Justificación Teórica**: {q['j']}\n")
            
        md.append("## 8. Sistema de Evaluación y Bibliografía Recomendada")
        md.append(f"**Evaluación**: {s.get('evaluation', 'Evaluación continua y examen final.')}\n")
        md.append("**Bibliografía de Referencia**:")
        for b in s.get("bibliography", []):
            md.append(f"- {b}")
            
        return "\n".join(md)

    def export_all_study_guides(self, output_dir: str | Path) -> int:
        """Exports complete Markdown study guides for all 35 subjects into the specified directory."""
        out_path = Path(output_dir)
        out_path.mkdir(parents=True, exist_ok=True)
        count = 0
        for s in self.get_all_subjects():
            code = s["code"]
            acr = s["acronym"]
            fname = out_path / f"UPC_{code}_{acr}_Guia_Estudio.md"
            content = self.export_subject_markdown(code)
            with open(fname, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
        return count

    def export_anki_deck(self, code_or_acronym: str, output_file: str | Path) -> int:
        """Exports questions of a subject as TSV for Anki flashcards (Front\tBack)."""
        s = self.get_subject_by_code(code_or_acronym) or self.get_subject_by_acronym(code_or_acronym)
        if not s:
            return 0
        lines = []
        for q in s.get("questions", []):
            front = f"[{s['acronym']}] {q['q']}"
            verdict = "Verdadero (V)" if q['a'] == 'V' else "Falso (F)"
            back = f"<b>{verdict}</b><br><br><i>{q['j']}</i>"
            lines.append(f"{front}\t{back}")
        out_f = Path(output_file)
        out_f.parent.mkdir(parents=True, exist_ok=True)
        with open(out_f, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        return len(lines)

    def export_all_anki_decks(self, output_dir: str | Path) -> int:
        """Exports Anki flashcards for all 35 subjects + master combined deck."""
        out_path = Path(output_dir)
        out_path.mkdir(parents=True, exist_ok=True)
        total_cards = 0
        all_lines = []
        for s in self.get_all_subjects():
            code = s["code"]
            acr = s["acronym"]
            fname = out_path / f"Anki_{code}_{acr}.tsv"
            n = self.export_anki_deck(code, fname)
            total_cards += n
            for q in s.get("questions", []):
                front = f"[{s['acronym']}] {q['q']}"
                verdict = "Verdadero (V)" if q['a'] == 'V' else "Falso (F)"
                back = f"<b>{verdict}</b><br><br><i>{q['j']}</i>"
                all_lines.append(f"{front}\t{back}")
                
        # Combined deck
        with open(out_path / "Anki_UPC_GREELEC_Master_424_Questions.tsv", "w", encoding="utf-8") as f:
            f.write("\n".join(all_lines))
            
        return total_cards

    def generate_degree_cheatsheet(self) -> str:
        """Generates a master synthesis cheatsheet with all formulas and core concepts."""
        md = []
        md.append("# Cheatsheet Maestro: Grado en Ingeniería Electrónica de Telecomunicación (UPC GREELEC)")
        md.append("Compendio matemático, modelos físicos y fórmulas canónicas de las 35 asignaturas obligatorias.\n")
        
        for sem in range(1, 9):
            subjs = self.get_subjects_by_semester(sem)
            if not subjs:
                continue
            md.append(f"## Semestre Q{sem}")
            for s in subjs:
                md.append(f"### {s['code']} - {s['acronym']}: {s['title']}")
                for f in s.get("formulas", []):
                    md.append(f"- **{f['name']}**: ${f['latex']}$")
                md.append("")
        return "\n".join(md)

    def get_curriculum_statistics(self) -> Dict[str, Any]:
        """Returns analytical statistics of the curriculum."""
        subjs = self.get_all_subjects()
        total_ects = sum(s.get("ects", 0.0) for s in subjs)
        total_q = sum(len(s.get("questions", [])) for s in subjs)
        depts: Dict[str, int] = {}
        for s in subjs:
            d = s.get("department", "Otro")
            depts[d] = depts.get(d, 0) + 1
        return {
            "total_compulsory_subjects": len(subjs),
            "total_ects": total_ects,
            "total_exam_questions": total_q,
            "subjects_per_semester": {f"Q{i}": len(self.get_subjects_by_semester(i)) for i in range(1, 9)},
            "department_breakdown": depts
        }

# Global singleton engine instance
engine = UPCDegreeEngine()

# Standalone CLI interface
def main():
    parser = argparse.ArgumentParser(description="UPC ETSETB GREELEC Degree Engine CLI")
    parser.add_argument("--list", action="store_true", help="List all 35 compulsory subjects")
    parser.add_argument("--stats", action="store_true", help="Print curriculum statistics")
    parser.add_argument("--subject", type=str, help="Display subject details by code or acronym")
    parser.add_argument("--calc", type=str, help="Run calculator for subject code/acronym")
    parser.add_argument("--params", type=str, help="JSON string of parameters for calculator")
    parser.add_argument("--export-guides", type=str, help="Export all 35 study guides to target directory")
    parser.add_argument("--export-anki", type=str, help="Export Anki decks to target directory")
    parser.add_argument("--cheatsheet", action="store_true", help="Print degree formula cheatsheet")
    
    args = parser.parse_args()
    
    if args.list:
        print(f"=== Plan de Estudios GREELEC UPC (35 Asignaturas Obligatorias) ===")
        for s in engine.get_all_subjects():
            print(f"Q{s['semester']} | {s['code']} | {s['acronym']:<6} | {s['title']}")
        return

    if args.stats:
        stats = engine.get_curriculum_statistics()
        print(json.dumps(stats, indent=2, ensure_ascii=False))
        return

    if args.subject:
        s = engine.get_subject_by_code(args.subject) or engine.get_subject_by_acronym(args.subject)
        if s:
            print(engine.export_subject_markdown(s["code"]))
        else:
            print(f"Subject {args.subject} not found.")
        return

    if args.calc:
        params = json.loads(args.params) if args.params else None
        res = engine.run_calculator(args.calc, params)
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return

    if args.export_guides:
        n = engine.export_all_study_guides(args.export_guides)
        print(f"Exported {n} Markdown study guides to: {args.export_guides}")
        return

    if args.export_anki:
        n = engine.export_all_anki_decks(args.export_anki)
        print(f"Exported {n} Anki flashcards to: {args.export_anki}")
        return

    if args.cheatsheet:
        print(engine.generate_degree_cheatsheet())
        return

    parser.print_help()

if __name__ == "__main__":
    main()
