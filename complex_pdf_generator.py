from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle

def generate_complex_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # --- PAGE 1: THE MULTI-COLUMN TRAP ---
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Quarterly Strategy & Market Analysis")
    
    # Left Column
    c.setFont("Helvetica", 10)
    text_left = [
        "STRATEGIC GOALS:",
        "1. Increase market share by 15% in the EMEA region.",
        "2. Reduce operational overhead by optimizing the",
        "   supply chain logistics and warehouse management.",
        "3. Launch the new AI-driven product suite by Q4."
    ]
    y = height - 100
    for line in text_left:
        c.drawString(50, y, line)
        y -= 15

    # Right Column (Traditional parsers will merge these lines with the left column)
    text_right = [
        "MARKET RISKS:",
        "A. Increased competition from local low-cost providers.",
        "B. Potential regulatory changes in data privacy laws.",
        "C. Fluctuations in raw material pricing affecting",
        "   the overall manufacturing margin globally."
    ]
    y = height - 100
    for line in text_right:
        c.drawString(300, y, line)
        y -= 15

    # A "Sidebar" box in the middle that breaks flow
    c.setStrokeColor(colors.black)
    c.rect(150, height - 250, 250, 50, fill=0)
    c.setFont("Helvetica-Oblique", 9)
    c.drawString(160, height - 220, "CRITICAL NOTE: All projections are subject to")
    c.drawString(160, height - 235, "audit by the internal compliance committee.")

    # Page Footer (To see if it's stripped)
    c.setFont("Helvetica", 8)
    c.drawString(width/2 - 50, 30, "CONFIDENTIAL - INTERNAL USE ONLY - PAGE 1")

    c.showPage()

    # --- PAGE 2: THE TABLE TRAP ---
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Consolidated Financial Summary")

    # Data for a complex table
    data = [
        ["Metric", "FY 2022", "FY 2023", "% Change", "Status"],
        ["Total Revenue", "$1,240,000", "$1,450,000", "+16.9%", "Growth"],
        ["R&D Spend", "$340,000", "$510,000", "+50.0%", "Aggressive"],
        ["Net Income", "$120,000", "$95,000", "-20.8%", "Declining"],
        ["User Count", "45.2k", "102.1k", "+125.8%", "Scaling"]
    ]

    table = Table(data, colWidths=[100, 80, 80, 80, 80])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    table.wrapOn(c, 50, height - 200)
    table.drawOn(c, 50, height - 200)

    # Some text below the table
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 250, "Observations: Net income decreased due to massive R&D re-investment.")
    c.drawString(50, height - 265, "User growth indicates strong product-market fit despite margins.")

    # Page Footer
    c.setFont("Helvetica", 8)
    c.drawString(width/2 - 50, 30, "CONFIDENTIAL - INTERNAL USE ONLY - PAGE 2")

    c.save()
    print(f"File '{filename}' generated successfully.")

if __name__ == "__main__":
    generate_complex_pdf("complex_test.pdf")