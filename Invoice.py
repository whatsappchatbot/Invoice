import sqlite3
from reportlab.lib.colors import HexColor
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import brown,grey,chocolate,black,turquoise
con=sqlite3.connect("Invoice.db") #Connect to the database
cobj=con.cursor() #Make object of the database
# print(cobj.execute("select COUNT(item) from Invoice"))
# con.commit()
c=int(input())
print(c)
def generate_pdf():
    pdf=canvas.Canvas("Invoice.pdf")
    pdf.setFillColor(HexColor('#e4f9f5'))
    path = pdf.beginPath()
    path.moveTo(0 * cm, 0 * cm)
    path.lineTo(0 * cm, 30 * cm)
    path.lineTo(25 * cm, 30 * cm)
    path.lineTo(25 * cm, 0 * cm)
    pdf.drawPath(path, True, True)
    pdf.drawInlineImage("logo.jpeg",350,650)
    pdf.setFont("Helvetica",30)
    pdf.setFillColor(HexColor("#7c9473"))
    pdf.setFontSize(40)
    pdf.drawCentredString(90,770,"INVOICE")
    pdf.setFont("Helvetica", 20)
    pdf.setFillColor(HexColor("#7c9473"))
    pdf.drawCentredString(80,730,"Invoice No:23153")
    pdf.drawCentredString(45, 690, "Address:")
    pdf.setFillColor(HexColor("#62959c"))
    pdf.drawCentredString(130,670,"100,near PICT,Pune-411043")
    # pdf.setFillColorRGB(0, 0, 255)
    pdf.drawCentredString(130,630,"GSTIN : 07AABCS1429B1Z")
    # pdf.setFillColorRGB(0, 0, 0)
    pdf.setFillColor(HexColor("#7c9473"))
    pdf.drawCentredString(90,590,"Customer Details:")
    pdf.drawCentredString(60,560,"Phone NO:")
    pdf.setFillColor(HexColor("#62959c"))
    pdf.drawCentredString(170, 560, "9307840886")
    pdf.setFillColor(HexColor("#7c9473"))
    pdf.drawCentredString(55, 530, "Id")
    pdf.drawCentredString(140, 530, "Item")
    pdf.drawCentredString(230, 530, "Price")
    pdf.drawCentredString(330, 530, "Quantity")
    pdf.drawCentredString(430, 530, "Total")
    # pdf.line(80,555,570,555)
    count=0
    total=0
    for i in range(1,c+1):
        cobj.execute("select * from Invoice where id='"+str(i)+"'")
        result=cobj.fetchall()
        pdf.setFillColor(HexColor("#62959c"))
        pdf.drawCentredString(55, 500-count, str(result[0][0]))
        pdf.drawCentredString(140, 500-count, str(result[0][1]))
        pdf.drawCentredString(230, 500-count, str(result[0][2]))
        pdf.drawCentredString(330, 500-count, str(result[0][3]))
        pdf.drawCentredString(430, 500-count, str(result[0][4]))
        total=total+result[0][4]
        count=count+30
    # pdf.line(40, 555, 40, 555-(count+30))
    # pdf.line(100, 555, 100, 555-(count+30))
    # pdf.line(190, 555, 190, 555-(count+30))
    # pdf.line(290, 555, 290, 555-(count+30))
    # pdf.line(410, 555, 410,555-(count+60))
    # pdf.line(520, 555, 520, 555-(count+60))
    pdf.drawCentredString(330,500-count,"Total")
    pdf.drawCentredString(430,500-count,str(total))
    pdf.save()
generate_pdf()
def insert_data():# For inserting the data in database
    for i in range(0,c):
        cobj.execute("INSERT INTO Invoice(id,item,price,quantity,total) VALUES(?,?,?,?,?)",(3,"Nirma","20","2","40"))
        con.commit()

insert_data()
# mainloop()