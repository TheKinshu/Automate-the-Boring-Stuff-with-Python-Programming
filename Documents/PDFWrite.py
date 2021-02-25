# Notes:
# You cannot create by itself with PyPDF2 but can create new PDF by combining PDF

import PyPDF2

# Open PDF and create usable variable
pdf1File = open('.\\Documents\\meetingminutes.pdf', 'rb')
pdf2File = open('.\\Documents\\meetingminutes2.pdf', 'rb')

# Create reader variable
reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

# Creates a PDF in memory
writer = PyPDF2.PdfFileWriter()

# Looping through pdf1
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

# Looping through pdf2
for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

# Creates an output file to store the new PDF
outputFile = open('.\\Documents\\combinedminutes.pdf', 'wb')
writer.write(outputFile) # Write the combine PDF into 1 PDF

# Closing all file reader
outputFile.close()
pdf1File.close()
pdf2File.close()