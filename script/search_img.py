import os

path = '/Users/zac/Pictures/100CANON'

files = os.listdir(path)
for f in files:
    if '2958' in f and f.endswith('.png'):
        print('Found it: ' + f)
print('File not found!')
