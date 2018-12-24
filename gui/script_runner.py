import multiprocessing
import os
from tkinter import *
from runpy import run_path


def make_app():
    app = Tk()
    Label(app, text='Script Runner').pack()
    Listbox(app, name='lbox', bg='#f2f2f2').pack(fill=BOTH, expand=True)
    Button(app, text='Run', command=run_script).pack()
    Button(app, text='Stop', command=stop_script).pack()
    app.geometry('300x400')
    return app


def list_scripts():
    listbox = app.children['lbox']
    files = os.listdir()
    for f in files:
        if f.endswith('.py'):
            listbox.insert(END, f)


def run_script():
    print('begin runner')

    listbox = app.children['lbox']
    select_path = listbox.get(ACTIVE)

    p = multiprocessing.Process(name='runner', target=lambda: run_path(select_path))
    p.start()


def stop_script():
    for p in multiprocessing.active_children():
        if p.name == 'runner':
            p.terminate()
    print('stop runner')


def watcher():
    print(multiprocessing.active_children())
    app.after(1000, watcher)


app = make_app()
app.after(0, watcher)
app.after(1000, list_scripts)
app.mainloop()
