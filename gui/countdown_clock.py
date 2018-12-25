from time import sleep
from tkinter import *
import threading

timer = {
    'total_time': 0
}


def make_app():
    _font = ['Hack', 25, 'bold']
    app = Tk()
    Label(app, text='CountDown Clock').pack()
    Label(app, name='time', text=0, font=_font).pack()
    Entry(name='input').pack()
    Button(app, name='btn', text='Run', command=count_down).pack()
    app.geometry('300x400')
    return app


def count_down():
    def _count():
        while timer['total_time']:
            timer['total_time'] -= 1
            print(timer['total_time'])
            sleep(1)

    t = threading.Thread(target=_count, name='t_timer')
    t.start()


def choreographer():
    def _update_button():
        button = app.children['btn']
        t_timer = [t for t in threading.enumerate() if t.name == 't_timer']
        if t_timer:
            button['state'] = 'disable'
        else:
            button['state'] = 'normal'

    def _get_time():
        entry = app.children['input']
        t_timer = [t for t in threading.enumerate() if t.name == 't_timer']
        if not t_timer and entry.get():
            timer['total_time'] = int(entry.get())

    def _update_time():
        time_text = app.children['time']
        time_text['text'] = timer['total_time']

    def _main():
        while True:
            print("Current running thread:")
            print(threading.enumerate())
            _get_time()
            _update_button()
            _update_time()

    t = threading.Thread(target=_main, name='t_choreographer')
    t.start()


app = make_app()
app.after(0, choreographer)
app.mainloop()
