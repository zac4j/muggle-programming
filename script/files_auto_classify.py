import os
import shutil

path = '/Users/zac/Downloads/'

files = os.listdir(path)

for f in files:
    folder_name = path + f.split('.')[-1]
    print('ZacLog: folder name is : ' + folder_name)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        shutil.move(path + f, folder_name)
        print('ZacLog: create folder name: ' + folder_name)
    else:
        shutil.move(path + f, folder_name)
        print('ZacLog: move file to: ' + folder_name)
print('All files classify done!')
