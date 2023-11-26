# This is a sample Python script.
import create_zip
import download_files
import os


def work_with_zip():
    os.mkdir("tmp")
    #загружаем файлы в папку tmp
    download_files.download_txt()
    download_files.download_pdf()
    download_files.download_xlsx()


    #создаем архив
    create_zip.create()

    #распаковываем архив
    create_zip.extract()


if __name__ == '__main__':
    work_with_zip()

