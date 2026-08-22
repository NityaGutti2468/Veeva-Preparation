from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Preformatted, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "Veeva_Optimized_Coding_Set_Java.md"
OUT = ROOT / "Veeva_Optimized_Coding_Set_Java.pdf"


def escape(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline_format(text: str) -> str:
    text = escape(text)
    text = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', text)
    return text


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.grey)
    canvas.drawString(0.55 * inch, 0.38 * inch, "Veeva Optimized Coding Set - Java")
    canvas.drawRightString(A4[0] - 0.55 * inch, 0.38 * inch, f"Page {doc.page}")
    canvas.restoreState()


def main():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="CodeTitle",
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
            name="CodeH1",
            parent=styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=13,
            leading=16,
            spaceBefore=10,
            spaceAfter=6,
            textColor=colors.HexColor("#1f6f78"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="CodeBody",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8.5,
            leading=11,
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CodeBullet",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8.4,
            leading=10.6,
            leftIndent=13,
            firstLineIndent=-9,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CodeBlock",
            parent=styles["Code"],
            fontName="Courier",
            fontSize=6.45,
            leading=8.1,
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
                story.append(Preformatted("\n".join(code_lines), styles["CodeBlock"]))
                in_code = False
            continue

        if in_code:
            code_lines.append(line)
            continue

        stripped = line.strip()
        if not stripped:
            story.append(Spacer(1, 2.5))
        elif line.startswith("# "):
            story.append(Paragraph(inline_format(line[2:].strip()), styles["CodeTitle"]))
        elif line.startswith("## "):
            story.append(Paragraph(inline_format(line[3:].strip()), styles["CodeH1"]))
        elif line.startswith("- "):
            story.append(Paragraph(inline_format("- " + line[2:]), styles["CodeBullet"]))
        elif re.match(r"^\d+\. ", line):
            story.append(Paragraph(inline_format(line), styles["CodeBullet"]))
        else:
            story.append(Paragraph(inline_format(line), styles["CodeBody"]))

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
