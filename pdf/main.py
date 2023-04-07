from PyPDF2 import PdfReader

with open('BikeRentalSystem.pdf',"rb") as file:
    pdf_reader = PdfReader(file)
    print(len(pdf_reader.pages))
    page = pdf_reader.pages[1]
    text = page.extract_text()
    information = pdf_reader.getDocumentInfo()
    print(f"Author: {information.title}")