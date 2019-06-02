# extracting_text.py
from PyPDF2 import PdfFileReader


def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        # get the first page
        page = pdf.getPage(0)
        print(page)
        print('Page type: {}'.format(str(type(page))))
        text = page.extractText()
        print(text)


if __name__ == '__main__':
    path = 'reportlab-sample.pdf'
    text_extractor("E:\\E&Y\\Challenge_4_-_CA_Automation\\Challenge 4 - CA Automation"
                                            "\\Underlying Documents\\fw9.pdf")