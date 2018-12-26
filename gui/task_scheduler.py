import multiprocessing
import threading
import time
from runpy import run_path
from time import sleep
from tkinter import *

data_store = []


def make_app():
    app = Tk()
    Button(name='add', text='add', command=make_task).pack(side=BOTTOM)
    app.geometry('300x400')
    return app


def make_task():
    _font = ['Hack', 18, 'bold']
    f = Frame(bg='#f2f2f2')
    Label(f, name='lb_file', text='Script name', bg='#f2f2f2', font=_font).pack(anchor='nw')  # anchor?
    Label(f, name='lb_time', text='Time', bg='#f2f2f2').pack(side=LEFT)
    Button(f, text=':', command=lambda: make_dialog(f)).pack(anchor='se')
    f.pack(fill=X)


def make_dialog(f):
    t = Toplevel(f)
    Label(t, text='FILE PATH').pack()
    Entry(t, name='file_input').pack()
    Label(t, text='START TIME').pack()
    Entry(t, name='time_input').pack()
    Button(t, text='save', command=lambda: (save(t), t.destroy())).pack()


def save(t):
    d = {}
    file_path = t.children['file_input'].get()
    start_time = t.children['time_input'].get()
    d['file_path'] = file_path
    d['start_time'] = start_time
    d['execute'] = False
    data_store.append(d)


def work_manager():
    def _test():
        print(data_store)

    def _refresh_tasks():
        tasks = [t[1] for t in app.children.items() if t[0] != 'add']
        for d, t in zip(data_store, tasks):
            t.children['lb_file']['text'] = d['file_path']
            t.children['lb_time']['text'] = d['start_time']

    def _task_executor():
        now = time.ctime().split()[-2]

        for d in data_store:
            if d['start_time'] <= now and not d['execute']:
                p = multiprocessing.Process(target=lambda: run_path(d['file_path']))
                p.start()
                d['execute'] = True

    def _main():
        while True:
            sleep(0.5)
            _test()
            _refresh_tasks()
            _task_executor()

    t = threading.Thread(target=_main, name='work_manager')
    t.start()


app = make_app()
app.after(0, work_manager)
app.mainloop()
