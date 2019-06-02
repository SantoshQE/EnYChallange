# get_doc_info.py
from PyPDF2 import PdfFileReader


def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
    print(info)
    author = info.author
    creator = info.creator
    producer = info.producer
    subject = info.subject
    title = info.title


if __name__ == '__main__':
    path = 'reportlab-sample.pdf'
    get_info("E:\\E&Y\\Challenge_4_-_CA_Automation\\Challenge 4 - CA Automation\\Underlying Documents\\1680237818.pdf")
