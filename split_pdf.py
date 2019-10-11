import os
from PyPDF4 import PdfFileWriter, PdfFileReader
import tkinter
from tkinter import filedialog, simpledialog

# Create dialog window for file selection
root = tkinter.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(
    filetypes=[('.pdffiles', '.pdf')],
    title='Select an input pdf.'
)

# Parse result
directory, file_name = os.path.split(file_path)
file_name, extension = os.path.splitext(file_name)

# Open file
file = open(file_path, "rb")
input_pdf = PdfFileReader(file)

# Ask user for integer
page_number = simpledialog.askinteger(
    'User input',
    'Before what page should this file be split?'
)

# Split pdf
output = PdfFileWriter()
output_path = os.path.join(directory, file_name + '_part1' + extension)
for i in range(min(input_pdf.numPages, page_number - 1)):
    output.addPage(input_pdf.getPage(i))
with open(output_path, "wb") as outputStream:
    output.write(outputStream)
output = PdfFileWriter()
output_path = os.path.join(directory, file_name + '_part2' + extension)
for i in range(page_number, input_pdf.numPages):
    output.addPage(input_pdf.getPage(i))
with open(output_path, "wb") as outputStream:
    output.write(outputStream)
