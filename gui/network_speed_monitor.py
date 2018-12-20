from time import sleep

import psutil
from tkinter import *


# This commented script will list your NIC(network interface card) name, like en0, en1
# import psutil
# addrs=psutil.net_if_addrs()
# print(addrs.keys())

def make_app():
    app = Tk()
    app.geometry('300x150')
    app.config(bg='#303030')
    Label(text='Speed Monitor', font=('Hack', 25, 'bold'), bg='#303030', fg='#1ef3ed').pack()
    Label(name='lb2', text='-kb/s', font=('Hack', 20, 'bold'), bg='#303030', fg='white').pack()
    return app


def test_speed():
    s1 = psutil.net_io_counters(pernic=True)['en0']
    sleep(5)
    s2 = psutil.net_io_counters(pernic=True)['en0']
    result = s2.bytes_recv - s1.bytes_recv
    return str(result / 1024) + 'kb/s'


def update_ui(do):
    data = do()
    lb2 = app.children['lb2']
    lb2.config(text=data)
    app.after(1000, lambda: update_ui(do))


app = make_app()
app.after(1000, lambda: update_ui(test_speed))
app.mainloop()
