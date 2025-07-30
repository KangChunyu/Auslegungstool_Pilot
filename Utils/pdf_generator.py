from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from io import BytesIO
import matplotlib.pyplot as plt
import tempfile
import os


def generate_result_pdf(form_data, results, logo_path="Assets\\BuderusLogo.png", footer_path="Assets\\BuderusLogo.png"):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    margin = 50

    def add_logo_and_page_number(page_num):
        # Place Logo at Top Right
        if logo_path and os.path.exists(logo_path):
            logo_width = 40
            logo_height = 40
            c.drawImage(logo_path, width - logo_width -margin, height - logo_height -10, width=logo_width, height=logo_height)
            
            # Page number at bottom-center
        c.setFont("Helvetica", 8)
        c.drawCentredString(width / 2, 20, f"Seite {page_num}")

    page_number = 1

    # Title page
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(width / 2, height - 200, "Auswertung Bericht")
    if logo_path and os.path.exists(logo_path):
        c.drawImage(logo_path, width / 2 - 100, height / 2 - 100, width=200, height=200)
    add_logo_and_page_number(page_number)
    c.showPage()
    page_number += 1

    # Section 1: Form Data
    y = height - margin
    c.setFont("Helvetica-Bold", 20)
    c.drawString(margin, y, "Benutzereingaben:")
    y -= 40

    for section, fields in form_data.items():
        c.setFont("Helvetica-Bold", 14)
        c.drawString(margin, y, section)
        y -= 20

        table_data = [["Feld", "Wert"]]
        for key, value in fields.items():
            table_data.append([key, str(value)])

        table = Table(table_data, colWidths=[200, 250])
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#003366")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#f2f2f2")),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ]))

        w, h = table.wrapOn(c, width, height)
        if y - h < 100:
            add_logo_and_page_number(page_number)
            c.showPage()
            page_number += 1
            y = height - margin

        table.drawOn(c, margin, y - h)
        y -= h + 30

    # Section 2: Results
    c.setFont("Helvetica-Bold", 20)
    c.drawString(margin, y, "Berechnete Ergebnisse:")
    y -= 30

    for section, fields in results.items():
        c.setFont("Helvetica-Bold", 14)
        c.drawString(margin, y, section)
        y -= 20

        for key, value in fields.items():
            c.setFont("Helvetica", 10)
            c.drawString(margin + 10, y, f"{key}: {value}")
            y -= 12

            if y < 100:
                add_logo_and_page_number(page_number)
                c.showPage()
                page_number += 1
                y = height - margin

        y -= 10

    # Section 3: Chart
    c.setFont("Helvetica-Bold", 20)
    c.drawString(margin, y, "Beispielgrafik:")
    y -= 220

    # Using mkstemp to avoid Windows locking issues
    fd, tmp_path = tempfile.mkstemp(suffix=".png")
    os.close(fd)  # Close the file descriptor to avoid lock

    try:
        plt.figure(figsize=(5, 3))
        plt.plot([1, 2, 3, 4], [10, 20, 15, 25], marker='o')
        plt.title("Dummy Ergebnisdiagramm")
        plt.xlabel("Zeit")
        plt.ylabel("Wert")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(tmp_path)
        plt.close()

        c.drawImage(tmp_path, margin, y, width=400, height=200)
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

    add_logo_and_page_number(page_number)
    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer
