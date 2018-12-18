import os
from tkinter import *

app = Tk()

label = Label(text='All hidden files', font=('Hack', 25, 'bold'))
label.pack()

listbox = Listbox(bg='#0099ff', fg='#007788')
listbox.pack(fill=BOTH, expand=True)

path = '/Users/zac/'
files = os.listdir(path)
for f in files:
    if f.startswith('.'):
        listbox.insert(END, f)

app.mainloop()
