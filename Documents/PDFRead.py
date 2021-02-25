import PyPDF2

pdfFile = open('.\\Documents\\meetingminutes.pdf', 'rb')

reader = PyPDF2.PdfFileReader(pdfFile)

#
numPages = reader.numPages

page = reader.getPage(0)
page.extractText()

for pageNum in range(numPages):
    print(reader.getPage(pageNum).extractText())

