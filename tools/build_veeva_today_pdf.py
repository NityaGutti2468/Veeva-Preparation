from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Preformatted, SimpleDocTemplate, Spacer

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "Veeva_Todays_Questions_Only.md"
OUT = ROOT / "Veeva_Todays_Questions_Only.pdf"

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
    canvas.drawString(0.52 * inch, 0.36 * inch, "Veeva Today's Questions Only")
    canvas.drawRightString(A4[0] - 0.52 * inch, 0.36 * inch, f"Page {doc.page}")
    canvas.restoreState()

def main():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="TitleT", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=18, leading=22, alignment=TA_CENTER, spaceAfter=12, textColor=colors.HexColor("#17324d")))
    styles.add(ParagraphStyle(name="H1T", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=13, leading=16, spaceBefore=10, spaceAfter=6, textColor=colors.HexColor("#17324d")))
    styles.add(ParagraphStyle(name="H2T", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=10.8, leading=13.2, spaceBefore=7, spaceAfter=4, textColor=colors.HexColor("#1f6f78")))
    styles.add(ParagraphStyle(name="BodyT", parent=styles["BodyText"], fontName="Helvetica", fontSize=8.2, leading=10.5, spaceAfter=2.5))
    styles.add(ParagraphStyle(name="OptionT", parent=styles["BodyText"], fontName="Helvetica", fontSize=8, leading=10.2, leftIndent=12, firstLineIndent=-8, spaceAfter=2))
    styles.add(ParagraphStyle(name="AnswerT", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=8.2, leading=10.5, textColor=colors.HexColor("#0b6b3a"), backColor=colors.HexColor("#eef8f1"), borderPadding=3, spaceBefore=2, spaceAfter=3))
    styles.add(ParagraphStyle(name="CodeT", parent=styles["Code"], fontName="Courier", fontSize=5.95, leading=7.45, backColor=colors.HexColor("#f6f7f8"), borderColor=colors.HexColor("#d8dee4"), borderWidth=0.25, borderPadding=4, spaceBefore=3, spaceAfter=5))

    story = []
    in_code = False
    code_lines = []
    for line in SRC.read_text(encoding="utf-8").splitlines():
        if line.startswith("```"):
            if not in_code:
                in_code = True
                code_lines = []
            else:
                story.append(Preformatted("\n".join(code_lines), styles["CodeT"]))
                in_code = False
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not line.strip():
            story.append(Spacer(1, 2))
        elif line.startswith("# "):
            story.append(Paragraph(inline_format(line[2:].strip()), styles["TitleT"]))
        elif line.startswith("## "):
            story.append(Paragraph(inline_format(line[3:].strip()), styles["H1T"]))
        elif line.startswith("### "):
            story.append(Paragraph(inline_format(line[4:].strip()), styles["H2T"]))
        elif re.match(r"^[A-D]\. ", line) or line.startswith("- "):
            story.append(Paragraph(inline_format(line), styles["OptionT"]))
        elif line.startswith("Answer:"):
            story.append(Paragraph(inline_format(line), styles["AnswerT"]))
        else:
            story.append(Paragraph(inline_format(line), styles["BodyT"]))

    doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=0.48*inch, leftMargin=0.48*inch, topMargin=0.48*inch, bottomMargin=0.58*inch)
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(OUT)

if __name__ == "__main__":
    main()
