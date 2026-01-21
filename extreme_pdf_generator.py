from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import inch

def generate_extreme_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # --- PAGE 1: THE COLUMN CHAOS ---
    # Header - Using corrected method name: drawCentredString
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width/2, height - 50, "Global Industry Analysis 2025")
    
    # Section 1: Traditional 2-Column
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 80, "Section 1.1: Executive Summary")
    
    # Simulate a sidebar box that sits between columns
    c.setFillColor(colors.lightgrey)
    c.rect(200, height - 250, 210, 120, fill=1, stroke=0)
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(210, height - 150, "INSIGHT: KEY MARKET DRIVER")
    c.setFont("Helvetica-Oblique", 9)
    c.drawString(210, height - 170, "Vision-based parsing (Gold Standard)")
    c.drawString(210, height - 185, "is required to maintain context")
    c.drawString(210, height - 200, "integrity in multi-column PDF files.")

    # Left Column Text
    c.setFont("Helvetica", 10)
    y = height - 120
    lines_left = [
        "This report explores document",
        "processing. Traditional methods",
        "often fail when faced with",
        "complex spatial layouts. We",
        "observe that coordinate-based",
        "extraction cannot maintain",
        "the logical integrity of",
        "multi-column reports."
    ]
    for line in lines_left:
        c.drawString(50, y, line)
        y -= 15

    # Right Column Text (Shared Y-axis with left)
    y = height - 120
    lines_right = [
        "The primary risk remains the",
        "'Coordinate Mesh' problem.",
        "When text from Column A and B",
        "share a Y-axis, parsers merge",
        "them into a single, nonsensical",
        "string of characters, which",
        "ultimately breaks RAG accuracy",
        "and causes hallucinations."
    ]
    for line in lines_right:
        c.drawString(420, y, line)
        y -= 15

    # Footer
    c.setFont("Helvetica-Oblique", 8)
    c.drawCentredString(width/2, 30, "Strictly Confidential - Page 01 - System Generated Report")
    c.showPage()

    # --- PAGE 2: THE TABLE HELL (Merged Cells) ---
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Financial Comparative Matrix")
    
    # Complex Data with Merged Headers logic
    data = [
        ["Region", "2023 Performance", "", "2024 Projection", ""], 
        ["", "Revenue", "Growth", "Revenue", "Growth"],           
        ["North Am.", "$450M", "12%", "$510M", "14%"],
        ["EMEA", "$320M", "8%", "$340M", "9%"],
        ["APAC", "$610M", "22%", "$780M", "25%"],
        ["TOTAL", "$1,380M", "14%", "$1,630M", "16%"]
    ]

    t = Table(data, colWidths=[1.2*inch, 1*inch, 0.8*inch, 1*inch, 0.8*inch])
    t.setStyle(TableStyle([
        ('SPAN', (1, 0), (2, 0)), # Merge 2023 Performance
        ('SPAN', (3, 0), (4, 0)), # Merge 2024 Projection
        ('SPAN', (0, 0), (0, 1)), # Merge Region vertically
        ('BACKGROUND', (0, 0), (-1, 1), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 1), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 0), (-1, 1), 'Helvetica-Bold'),
    ]))
    
    t.wrapOn(c, 50, height - 250)
    t.drawOn(c, 50, height - 250)

    c.setFont("Helvetica", 10)
    c.drawString(50, height - 280, "Note: Spanned headers are the 'Final Boss' of PDF parsing.")
    c.drawString(50, 30, "Strictly Confidential - Page 02 - System Generated Report")
    c.showPage()

    # --- PAGE 3: ROTATION & NOISE ---
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Technical Schematic Notes")

    # Rotated Text
    c.saveState()
    c.translate(550, height - 300)
    c.rotate(90)
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.red)
    c.drawString(0, 0, "DANGER: HIGH FREQUENCY DATA OVERLAP")
    c.restoreState()

    # Sidebar Box
    c.setDash(1, 2)
    c.rect(50, height - 400, 500, 80)
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(60, height - 340, "APPENDIX A: SYSTEM METADATA")
    
    c.setFont("Helvetica", 9)
    c.drawString(60, height - 360, "UUID: 884-XJ-9920 | Hash: 0x992837475 | Owner: Admin_System_A")

    c.setFont("Helvetica", 10)
    c.drawString(50, 100, "Conclusion: This benchmark proves the superiority of Docling.")
    c.drawCentredString(width/2, 30, "Strictly Confidential - Page 03 - System Generated Report")
    c.save()
    print(f"File '{filename}' generated.")

if __name__ == "__main__":
    generate_extreme_pdf("extreme_rag_test.pdf")