from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Preformatted, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "Veeva_Last_Night_Prep.md"
OUT = ROOT / "Veeva_Last_Night_Prep.pdf"


def escape(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline_format(text: str) -> str:
    text = escape(text)
    return re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', text)


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.grey)
    canvas.drawString(0.55 * inch, 0.38 * inch, "Veeva Technical Assessment Prep")
    canvas.drawRightString(A4[0] - 0.55 * inch, 0.38 * inch, f"Page {doc.page}")
    canvas.restoreState()


def main():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="PrepTitle",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=18,
            leading=22,
            alignment=TA_CENTER,
            spaceAfter=14,
            textColor=colors.HexColor("#1f3a5f"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="PrepH1",
            parent=styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=18,
            spaceBefore=12,
            spaceAfter=8,
            textColor=colors.HexColor("#1f3a5f"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="PrepH2",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=11.5,
            leading=15,
            spaceBefore=9,
            spaceAfter=5,
            textColor=colors.HexColor("#2f5d62"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="PrepBody",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="PrepList",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8.7,
            leading=11.2,
            leftIndent=12,
            firstLineIndent=-8,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="PrepCode",
            parent=styles["Code"],
            fontName="Courier",
            fontSize=7.4,
            leading=9.2,
            backColor=colors.HexColor("#f5f5f5"),
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
                story.append(Preformatted("\n".join(code_lines), styles["PrepCode"]))
                in_code = False
            continue

        if in_code:
            code_lines.append(line)
            continue

        stripped = line.strip()
        if not stripped:
            story.append(Spacer(1, 3))
        elif line.startswith("# "):
            story.append(Paragraph(inline_format(line[2:].strip()), styles["PrepTitle"]))
        elif line.startswith("## "):
            story.append(Paragraph(inline_format(line[3:].strip()), styles["PrepH1"]))
        elif line.startswith("### "):
            story.append(Paragraph(inline_format(line[4:].strip()), styles["PrepH2"]))
        elif re.match(r"^\d+\. ", line):
            story.append(Paragraph(inline_format(line), styles["PrepList"]))
        elif line.startswith("- "):
            story.append(Paragraph(inline_format("- " + line[2:]), styles["PrepList"]))
        else:
            story.append(Paragraph(inline_format(line), styles["PrepBody"]))

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        rightMargin=0.55 * inch,
        leftMargin=0.55 * inch,
        topMargin=0.55 * inch,
        bottomMargin=0.6 * inch,
    )
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(OUT)


if __name__ == "__main__":
    main()
