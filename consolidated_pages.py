#Install the library
pip install PyPDF2

#Import the function
from PyPDF2 import PdfMerger

#Call the function
merger = PdfMerger()

#Import built-in library
from os import listdir

#Ensure all files are stored in the same folder as the python file
#Saving folder path as 'path'
path=listdir('C://Users//Gia//Desktop//Consolidated PDF's)

#Saving all the file names with .pdf in a list
pdf=[]
for i in range(len(path)):
    if path[i].endswith('.pdf'):
     pdf.append(path[i])

#Iterate through the folder and extract all filenames with a .pdf extension
pdf
['Gia_Maxhuni_Resume.pdf', 'Gia_Maxhuni_Cover_Letter.pdf']

#Merging PDF files
for pdf_file in pdf:
    merger.append(pdf_file)

#Saving the file
merger.write("consolidated_pages.pdf")
merger.close()

