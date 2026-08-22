from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Preformatted, SimpleDocTemplate, Spacer

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "Veeva_SQL_Queries_And_Spiral_Traversal.md"
OUT = ROOT / "Veeva_SQL_Queries_And_Spiral_Traversal.pdf"

def escape(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def inline_format(text: str) -> str:
    text = escape(text)
    text = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', text)
    if text.startswith("Pattern:") or text.startswith("Time:") or text.startswith("Space:"):
        return f'<font color="#3f4f5f">{text}</font>'
    return text

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.grey)
    canvas.drawString(0.52 * inch, 0.36 * inch, "Veeva SQL Queries and Spiral Traversal")
    canvas.drawRightString(A4[0] - 0.52 * inch, 0.36 * inch, f"Page {doc.page}")
    canvas.restoreState()

def main():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="TitleS", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=18, leading=22, alignment=TA_CENTER, spaceAfter=12, textColor=colors.HexColor("#17324d")))
    styles.add(ParagraphStyle(name="H1S", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=12.5, leading=15.5, spaceBefore=9, spaceAfter=5, textColor=colors.HexColor("#1f6f78")))
    styles.add(ParagraphStyle(name="H2S", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=10.5, leading=13, spaceBefore=7, spaceAfter=4, textColor=colors.HexColor("#17324d")))
    styles.add(ParagraphStyle(name="BodyS", parent=styles["BodyText"], fontName="Helvetica", fontSize=8.3, leading=10.6, spaceAfter=2.5))
    styles.add(ParagraphStyle(name="BulletS", parent=styles["BodyText"], fontName="Helvetica", fontSize=8.1, leading=10.2, leftIndent=12, firstLineIndent=-8, spaceAfter=2))
    styles.add(ParagraphStyle(name="CodeS", parent=styles["Code"], fontName="Courier", fontSize=6.2, leading=7.8, backColor=colors.HexColor("#f6f7f8"), borderColor=colors.HexColor("#d8dee4"), borderWidth=0.25, borderPadding=4, spaceBefore=3, spaceAfter=5))

    story = []
    in_code = False
    code_lines = []
    for line in SRC.read_text(encoding="utf-8").splitlines():
        if line.startswith("```"):
            if not in_code:
                in_code = True
                code_lines = []
            else:
                story.append(Preformatted("\n".join(code_lines), styles["CodeS"]))
                in_code = False
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not line.strip():
            story.append(Spacer(1, 2))
        elif line.startswith("# "):
            story.append(Paragraph(inline_format(line[2:].strip()), styles["TitleS"]))
        elif line.startswith("## "):
            story.append(Paragraph(inline_format(line[3:].strip()), styles["H1S"]))
        elif line.startswith("### "):
            story.append(Paragraph(inline_format(line[4:].strip()), styles["H2S"]))
        elif line.startswith("- "):
            story.append(Paragraph(inline_format(line), styles["BulletS"]))
        else:
            story.append(Paragraph(inline_format(line), styles["BodyS"]))

    doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=0.50*inch, leftMargin=0.50*inch, topMargin=0.50*inch, bottomMargin=0.58*inch)
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(OUT)

if __name__ == "__main__":
    main()
