from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Preformatted, SimpleDocTemplate, Spacer

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "Veeva_Complete_MCQ_SQL_Coding_Revision.md"
OUT = ROOT / "Veeva_Complete_MCQ_SQL_Coding_Revision.pdf"

def escape(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def inline_format(text: str) -> str:
    text = escape(text)
    text = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', text)
    if text.startswith("Answer:"):
        return f'<font color="#0b6b3a"><b>{text}</b></font>'
    if text.startswith("Explanation:") or text.startswith("Pattern:") or text.startswith("Time:") or text.startswith("Space:"):
        return f'<font color="#3f4f5f">{text}</font>'
    return text

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.grey)
    canvas.drawString(0.50 * inch, 0.35 * inch, "Veeva Complete MCQ, SQL, and Coding Revision")
    canvas.drawRightString(A4[0] - 0.50 * inch, 0.35 * inch, f"Page {doc.page}")
    canvas.restoreState()

def main():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="TitleX", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=18, leading=22, alignment=TA_CENTER, spaceAfter=11, textColor=colors.HexColor("#17324d")))
    styles.add(ParagraphStyle(name="H1X", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=13, leading=16, spaceBefore=10, spaceAfter=6, textColor=colors.HexColor("#17324d")))
    styles.add(ParagraphStyle(name="H2X", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=10.5, leading=13, spaceBefore=7, spaceAfter=4, textColor=colors.HexColor("#1f6f78")))
    styles.add(ParagraphStyle(name="BodyX", parent=styles["BodyText"], fontName="Helvetica", fontSize=7.7, leading=9.8, spaceAfter=2.2))
    styles.add(ParagraphStyle(name="OptionX", parent=styles["BodyText"], fontName="Helvetica", fontSize=7.5, leading=9.5, leftIndent=12, firstLineIndent=-8, spaceAfter=1.7))
    styles.add(ParagraphStyle(name="AnswerX", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=7.7, leading=9.8, textColor=colors.HexColor("#0b6b3a"), backColor=colors.HexColor("#eef8f1"), borderPadding=3, spaceBefore=2, spaceAfter=2))
    styles.add(ParagraphStyle(name="CodeX", parent=styles["Code"], fontName="Courier", fontSize=5.35, leading=6.7, backColor=colors.HexColor("#f6f7f8"), borderColor=colors.HexColor("#d8dee4"), borderWidth=0.25, borderPadding=4, spaceBefore=3, spaceAfter=5))

    story = []
    in_code = False
    code_lines = []

    for line in SRC.read_text(encoding="utf-8").splitlines():
        if line.startswith("```"):
            if not in_code:
                in_code = True
                code_lines = []
            else:
                story.append(Preformatted("\n".join(code_lines), styles["CodeX"]))
                in_code = False
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not line.strip():
            story.append(Spacer(1, 1.8))
        elif line.startswith("# "):
            story.append(Paragraph(inline_format(line[2:].strip()), styles["TitleX"]))
        elif line.startswith("## "):
            story.append(Paragraph(inline_format(line[3:].strip()), styles["H1X"]))
        elif line.startswith("### "):
            story.append(Paragraph(inline_format(line[4:].strip()), styles["H2X"]))
        elif re.match(r"^[A-F]\. ", line) or line.startswith("- ") or re.match(r"^\d+\. ", line):
            story.append(Paragraph(inline_format(line), styles["OptionX"]))
        elif line.startswith("Answer:"):
            story.append(Paragraph(inline_format(line), styles["AnswerX"]))
        elif line.strip() == "---":
            story.append(Spacer(1, 6))
        else:
            story.append(Paragraph(inline_format(line), styles["BodyX"]))

    doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=0.45*inch, leftMargin=0.45*inch, topMargin=0.45*inch, bottomMargin=0.55*inch)
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(OUT)

if __name__ == "__main__":
    main()
