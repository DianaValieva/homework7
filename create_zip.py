from zipfile import ZipFile
from constants import CURRENT_DIR



import zipfile, os

def create():
    tmp_dir = os.path.join(CURRENT_DIR, "tmp")
    files = os.listdir(tmp_dir)
    with zipfile.ZipFile('test.zip', mode='w', \
                         compression=zipfile.ZIP_DEFLATED) as zf:
        for file in files:
            add_file = os.path.join("tmp", file)
            zf.write(add_file)


def extract():
    with ZipFile('test.zip') as zf:
        zf.extractall("tmp2")
