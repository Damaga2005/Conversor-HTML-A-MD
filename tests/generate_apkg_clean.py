import genanki
import re
from pathlib import Path

# Apple Pro Model
model_id = 1607392319
deck_id = 2059400110

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

deck = genanki.Deck(deck_id, "Sistemes de Mesura (EEBE · UPC)")

lines = Path("dist_course_md/_Flashcards_Examen.tsv").read_text(encoding="utf-8").splitlines()
count = 0
for l in lines:
    if not l or l.startswith("#"):
        continue
    parts = l.split("\t")
    if len(parts) < 2:
        continue
    front, back = parts[0], parts[1]
    tag_str = parts[2] if len(parts) > 2 else "Sistemes_de_Mesura"
    
    is_v = "VERTADER" in back.upper()
    ans = "✅ VERTADER (V)" if is_v else "❌ FALS (F)"
    ans_class = "answer-v" if is_v else "answer-f"
    
    m_j = re.search(r"Justificaci.*?T.*?cnica:</b><br>(.*?)(?:<br><br><small|$)", back, re.DOTALL | re.I)
    just = m_j.group(1).strip() if m_j else back
    
    m_r = re.search(r"Refer.*?ncia:\s*(.*?)</", back, re.I)
    ref = m_r.group(1).strip() if m_r else ""
    if ref:
        just += f"<br><br><small style='color:#86868b;'><i>Referència: {ref}</i></small>"
        
    tags_list = tag_str.split()
    
    note = genanki.Note(
        model=model,
        fields=[front, ans, ans_class, just, tag_str],
        tags=tags_list
    )
    deck.add_note(note)
    count += 1

pkg = genanki.Package(deck)
target = Path("dist_course_md/_Flashcards_Examen.apkg")
pkg.write_to_file(str(target))
print(f"Generated {count} flashcards in {target} (Size: {target.stat().st_size} bytes)")
