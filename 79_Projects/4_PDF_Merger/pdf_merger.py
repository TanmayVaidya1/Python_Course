import PyPDF2
pdfiles = [ 
           "C:\\Users\\tanma\\OneDrive\\Desktop\\Python Course\\79_Projects\\4_PDF_Merger\\1.pdf",
           "C:\\Users\\tanma\\OneDrive\\Desktop\\Python Course\\79_Projects\\4_PDF_Merger\\2.pdf", 
           "C:\\Users\\tanma\\OneDrive\\Desktop\\Python Course\\79_Projects\\4_PDF_Merger\\sample.pdf"]
Merger = PyPDF2.PdfMerger()

for filename in pdfiles:
        pdfFile = open(filename, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFile)
        Merger.append(pdfReader)

pdfFile.close()
Merger.write('C:\\Users\\tanma\\OneDrive\\Desktop\\Python Course\\79_Projects\\4_PDF_Merger\\merged.pdf')