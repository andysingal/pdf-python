import PyPDF4
import os

def convert2txt(filename):
    # creating a pdf file object
    pdfFileObj = open(filename, 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF4.PdfFileReader(pdfFileObj)

    for i in range(0, pdfReader.numPages):
        content = ""
        content += pdfReader.getPage(i).extractText() + "\n"
        print(content)
        """    Locate all text drawing commands, in the order they are provided in the
               content stream, and extract the text.  This works well for some PDF
               files, but poorly for others, depending on the generator used.  This will
               be refined in the future.  Do not rely on the order of text coming out of
               this function, as it will change if this function is made more
               sophisticated.
               :return: a unicode string object.
               """
    # Note: we check all strings are TextStringObjects.  ByteStringObjects
    # are strings where the byte->string encoding was unknown, so adding
    # them to the text here would be gibberish.
    # closing the pdf file object
    pdfFileObj.close()


# rotate_pages.py
def rotate(filename):
    pdf_write = PyPDF4.PdfFileWriter()
    pdf_read = PyPDF4.PdfFileReader(filename)
    # Rotate page 90 degrees to the right
    page1 = pdf_read.getPage(0).rotateClockwise(90)
    page2 = pdf_read.getPage(1).rotateClockwise(90)
    pdf_write.addPage(page1)
    pdf_write.addPage(page2)
    # Add a page in normal orientation
    pdf_write.addPage(pdf_read.getPage(0))
    with open('rotate_pages.pdf', 'wb') as fh:
        pdf_write.write(fh)

def pdfmerger(paths, output):
    pdfwrite = PyPDF4.PdfFileWriter()
    for path in paths:
        pdfread = PyPDF4.PdfFileReader(path)
        for page in range(pdfread.getNumPages()):
            # Add each page to the writer object
            pdfwrite.addPage(pdfread.getPage(page))
    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdfwrite.write(out)

def create_watermark(input_pdf, output, watermark):
    watermark_obj = PyPDF4.PdfFileReader(watermark)
    watermark_page = watermark_obj.getPage(0)

    pdf_reader = PyPDF4.PdfFileReader(input_pdf)
    pdf_writer = PyPDF4.PdfFileWriter()

    # Watermark all the pages
    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    path = 'input/example.pdf'
    convert2txt(path)
    rotate(path)
    paths = ['input/example.pdf', 'rotate_pages.pdf']
    pdfmerger(paths, output = 'output/merger_example.pdf')
    create_watermark(path, output='output/watermark_out.pdf', watermark= 'input/watermark.pdf')
