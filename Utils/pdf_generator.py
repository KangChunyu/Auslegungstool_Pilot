# Utils/pdf_generator.py

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from io import BytesIO
import matplotlib.pyplot as plt
import tempfile


def generate_result_pdf(form_data, results):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    width, height = A4
    margin = 50
    y = height - margin

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(margin, y, "📄 Auswertung Bericht")
    y -= 40

    # Section 1: Form Data
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margin, y, "Benutzereingaben:")
    y -= 20

    for section, fields in form_data.items():
        c.setFont("Helvetica-Bold", 12)
        c.drawString(margin, y, section)
        y -= 15

        table_data = [["Feld", "Wert"]]
        for key, value in fields.items():
            table_data.append([key, str(value)])

        table = Table(table_data, colWidths=[200, 250])
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 6),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ]))

        w, h = table.wrapOn(c, width, height)
        if y - h < 100:
            c.showPage()
            y = height - margin

        table.drawOn(c, margin, y - h)
        y -= h + 30

    # Section 2: Results
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margin, y, "Berechnete Ergebnisse:")
    y -= 20

    for section, fields in results.items():
        c.setFont("Helvetica-Bold", 12)
        c.drawString(margin, y, section)
        y -= 15

        for key, value in fields.items():
            c.setFont("Helvetica", 10)
            c.drawString(margin + 10, y, f"{key}: {value}")
            y -= 12

            if y < 100:
                c.showPage()
                y = height - margin

        y -= 10

    # Section 3: Dummy Chart from matplotlib
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margin, y, "Beispielgrafik:")
    y -= 220  # Reserve space for chart

    # Generate chart with matplotlib
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        plt.figure(figsize=(5, 3))
        plt.plot([1, 2, 3, 4], [10, 20, 15, 25], marker='o')
        plt.title("Dummy Ergebnisdiagramm")
        plt.xlabel("Zeit")
        plt.ylabel("Wert")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(tmpfile.name)
        plt.close()

        c.drawImage(tmpfile.name, margin, y, width=400, height=200)

    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer
