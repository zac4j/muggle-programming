import os
import shutil

path = '/Users/zac/Downloads/zip/'


def scan_file():
    files = os.listdir(path)
    for f in files:
        if f.endswith('.zip'):
            print("ZacLog: Found zip file!")
            return f


def unzip_file(f):
    folder_name = f.split('.')[0]
    target_path = path + folder_name
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    shutil.unpack_archive(path + f, target_path)


def delete_file(f):
    os.remove(f)


zip_file = scan_file()
if zip_file:
    unzip_file(zip_file)
    delete_file(path + zip_file)
else:
    print("ZacLog: No zip file found!")
