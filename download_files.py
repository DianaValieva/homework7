import requests
from requests import Response
import os


def download_txt():
    content = requests.get(url="https://github.com/DianaValieva/test_python/raw/main/License%20free.txt").content
    with open(os.path.join('tmp',"text_test.txt"), 'wb') as file:
        file.write(content)

def download_pdf():
    content = requests.get(url='https://raw.githubusercontent.com/DianaValieva/test_python'
                               '/9150ccf18871fdda28ffc72d132179cbdb2c5982/insurance_rules.pdf').content
    with open(os.path.join('tmp', "pdf_test.pdf"), 'wb') as file:
        file.write(content)


def download_xlsx():
    content = requests.get(url='https://github.com/DianaValieva/test_python/raw/main/test_xlsx.xlsx').content
    with open(os.path.join('tmp', "xls_test.xlsx"), 'wb') as file:
        file.write(content)