import PyPDF2

tempalte = PyPDF2.PdfFileReader(open('super.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
output = PyPDF2.PdfFileWriter()

for i in range(tempalte.getNumPages()):
    page = tempalte.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermark_output.pdf', 'wb') as file:
        output.write(file)