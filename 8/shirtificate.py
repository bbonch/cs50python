from fpdf import FPDF, Align

name = input("Name: ")

pdf = FPDF(orientation="portrait", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(40, 10, "CS50 shirtificate", align=Align.C, center=True)
pdf.image("shirtificate.png", Align.C, 40)
pdf.set_text_color(255, 255, 255)
pdf.cell(40, 150, f"{name} took CS50", align=Align.C, center=True)
pdf.output("shirtificate.pdf")
