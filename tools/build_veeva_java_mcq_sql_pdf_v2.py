from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Preformatted, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "Veeva_Java_MCQ_SQL_Revision_v2.md"
OUT = ROOT / "Veeva_Java_MCQ_SQL_Revision_v2.pdf"


def escape(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline_format(text: str) -> str:
    text = escape(text)
    text = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', text)
    if text.startswith("Answer:"):
        return f'<font color="#0b6b3a"><b>{text}</b></font>'
    if text.startswith("Explanation:") or text.startswith("Pattern:"):
        return f'<font color="#3f4f5f">{text}</font>'
    return text


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.grey)
    canvas.drawString(0.55 * inch, 0.38 * inch, "Veeva Java MCQ and SQL Revision")
    canvas.drawRightString(A4[0] - 0.55 * inch, 0.38 * inch, f"Page {doc.page}")
    canvas.restoreState()


def main():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="TitleCustom",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=19,
            leading=23,
            alignment=TA_CENTER,
            spaceAfter=13,
            textColor=colors.HexColor("#17324d"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="H1Custom",
            parent=styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=18,
            spaceBefore=13,
            spaceAfter=8,
            textColor=colors.HexColor("#17324d"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="H2Custom",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=11.5,
            leading=15,
            spaceBefore=9,
            spaceAfter=5,
            textColor=colors.HexColor("#1f6f78"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyCustom",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8.6,
            leading=11.1,
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="OptionCustom",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8.35,
            leading=10.5,
            leftIndent=13,
            firstLineIndent=-9,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="AnswerCustom",
            parent=styles["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=8.6,
            leading=11,
            textColor=colors.HexColor("#0b6b3a"),
            backColor=colors.HexColor("#eef8f1"),
            borderPadding=4,
            spaceBefore=3,
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CodeCustom",
            parent=styles["Code"],
            fontName="Courier",
            fontSize=6.6,
            leading=8.25,
            backColor=colors.HexColor("#f6f7f8"),
            borderColor=colors.HexColor("#d8dee4"),
            borderWidth=0.3,
            borderPadding=5,
            spaceBefore=4,
            spaceAfter=6,
        )
    )

    story = []
    in_code = False
    code_lines = []

    for line in SRC.read_text(encoding="utf-8").splitlines():
        if line.startswith("```"):
            if not in_code:
                in_code = True
                code_lines = []
            else:
                story.append(Preformatted("\n".join(code_lines), styles["CodeCustom"]))
                in_code = False
            continue

        if in_code:
            code_lines.append(line)
            continue

        stripped = line.strip()
        if not stripped:
            story.append(Spacer(1, 2.5))
        elif line.startswith("# "):
            story.append(Paragraph(inline_format(line[2:].strip()), styles["TitleCustom"]))
        elif line.startswith("## "):
            story.append(Paragraph(inline_format(line[3:].strip()), styles["H1Custom"]))
        elif line.startswith("### "):
            story.append(Paragraph(inline_format(line[4:].strip()), styles["H2Custom"]))
        elif re.match(r"^[A-D]\. ", line):
            story.append(Paragraph(inline_format(line), styles["OptionCustom"]))
        elif line.startswith("Answer:"):
            story.append(Paragraph(inline_format(line), styles["AnswerCustom"]))
        elif line.startswith("- "):
            story.append(Paragraph(inline_format("- " + line[2:]), styles["OptionCustom"]))
        else:
            story.append(Paragraph(inline_format(line), styles["BodyCustom"]))

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        rightMargin=0.52 * inch,
        leftMargin=0.52 * inch,
        topMargin=0.52 * inch,
        bottomMargin=0.6 * inch,
    )
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(OUT)


if __name__ == "__main__":
    main()

