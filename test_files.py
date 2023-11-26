import os
from zipfile import ZipFile
from constants import TMP_DIR
from PyPDF2 import PdfReader
from openpyxl import load_workbook

def test_text():
    tmp = os.path.join(TMP_DIR, "tmp")

    with open(os.path.join(tmp, "text_test.txt")) as file:
        readfile = file.read()
        assert "You are free to use this image" in readfile, "txt-file не прошел валидацию"


def test_pdf():
    tmp = os.path.join(TMP_DIR, "tmp")

    reader = PdfReader(os.path.join(tmp, "pdf_test.pdf"))
    number_of_pdf_pages = len(reader.pages)
    page = reader.pages[0]
    pdftext = page.extract_text()
    assert number_of_pdf_pages == 39
    assert "Права и обязанности сторон" in pdftext, "PDF-file не прошел валидацию"

def test_xlsx():
    tmp = os.path.join(TMP_DIR, "tmp")
    workbook = load_workbook(os.path.join(tmp, "xls_test.xlsx"))
    sheet = workbook.active
    assert "Этапы тестирования" == sheet.cell(row=5, column=1).value, "xlsx-file не прошел валидацию"
