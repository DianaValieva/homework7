# This is a sample Python script.
import create_zip
import download_files
import os


def download_files_in_tmp():
    #загружаем файлы в папку tmp
    download_files.download_txt()
    download_files.download_pdf()
    download_files.download_xlsx()



if __name__ == '__main__':
    download_files_in_tmp()

