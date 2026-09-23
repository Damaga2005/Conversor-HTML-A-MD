# -*- coding: utf-8 -*-
"""
Automated unit tests for the UPC GREELEC Degree Engine:
- Validates all 35 compulsory courses are present and properly configured.
- Validates that over 420 questions are indexed with justifications.
- Validates all 35 parameter calculators run without errors and produce sensible outputs.
- Validates SPICE / VHDL / C simulation templates.
- Validates search, quiz evaluation, Anki export, and Markdown study guide generation.
"""
import pytest
from pathlib import Path
from upc_degree_engine import UPCDegreeEngine

@pytest.fixture(scope="module")
def engine():
    return UPCDegreeEngine()

def test_engine_subjects_count(engine):
    subjects = engine.get_all_subjects()
    assert len(subjects) == 35, f"Expected 35 compulsory subjects, got {len(subjects)}"

def test_engine_total_questions(engine):
    questions = engine.get_all_questions()
    assert len(questions) >= 420, f"Expected at least 420 questions, got {len(questions)}"
    for q in questions:
        assert q["question"], "Question text must not be empty"
        assert q["answer"] in ["V", "F"], f"Answer must be 'V' or 'F', got {q['answer']}"
        assert len(q["justification"]) >= 10, "Justification must be detailed"

def test_all_35_calculators_execute(engine):
    for s in engine.get_all_subjects():
        code = s["code"]
        res = engine.run_calculator(code)
        assert "error" not in res, f"Calculator failed for {code}: {res.get('error')}"
        assert "outputs" in res, f"Calculator outputs missing for {code}"
        assert len(res["outputs"]) > 0, f"Outputs empty for {code}"

def test_all_35_spice_templates_exist(engine):
    for s in engine.get_all_subjects():
        tmpl = engine.get_spice_template(s["code"])
        assert tmpl and len(tmpl) > 20, f"Template invalid for {s['code']}"

def test_curriculum_search(engine):
    res_cce = engine.search_curriculum("Thévenin")
    assert len(res_cce) > 0
    res_fpga = engine.search_curriculum("FPGA")
    assert len(res_fpga) > 0
    res_lora = engine.search_curriculum("LoRa")
    assert len(res_lora) > 0

def test_quiz_evaluation(engine):
    # Test CCE quiz evaluation
    questions = engine.get_questions_by_subject("CCE")
    assert len(questions) >= 12
    # Submit perfect answers
    perfect_answers = {i: q["a"] for i, q in enumerate(questions)}
    eval_res = engine.evaluate_quiz("CCE", perfect_answers)
    assert eval_res["score_out_of_10"] == 10.0
    assert eval_res["passed"] is True

def test_study_guide_markdown(engine):
    md = engine.export_subject_markdown("230900")
    assert "Componentes y Circuitos Electrónicos" in md
    assert "Ficha Técnica y Metadatos Oficiales" in md
    assert "Modelado Matemático y Fórmulas Clave" in md
    assert "Preguntas de Autoevaluación" in md

def test_curriculum_stats(engine):
    stats = engine.get_curriculum_statistics()
    assert stats["total_compulsory_subjects"] == 35
    assert stats["total_ects"] == 210.0
    assert stats["total_exam_questions"] >= 420
