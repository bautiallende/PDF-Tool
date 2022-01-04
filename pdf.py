import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_conbiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write("New File Name.pdf")

inputs = ["PDF URL + NAME.pdf"
          ]
pdf_conbiner(inputs)

