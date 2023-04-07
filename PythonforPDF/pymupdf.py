# install fitz and PyMuPDF
import fitz  # this is pymupdf

with fitz.open("input/letter.pdf") as doc:
    text = ""
    for page in doc:
        text += page.getText()


print(text)