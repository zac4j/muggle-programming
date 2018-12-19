# Compress image

from PIL import Image as Img
from tkinter.filedialog import *

info = {
    'path': []
}


def make_app():
    app = Tk()
    Label(app, text='Image Compressor').pack()
    Listbox(app, name='lbox', bg='#f2f2f2').pack(fill=BOTH, expand=True)
    Button(app, text='open', command=get_file).pack()
    Button(app, text='compress', command=compress_img).pack()
    app.geometry('300x400')
    return app


def get_file():
    f_names = askopenfilenames()
    lbox = app.children['lbox']
    info['path'] = f_names
    print(f_names)
    if info['path']:
        for name in f_names:
            print(name)
            lbox.insert(END, name.split('/')[-1])  # -1 -> the last item in array


def compress_img():
    for f_path in info['path']:
        out_path = '/Users/zac/Downloads/game_image/'
        name = f_path.split('/')[-1]
        image = Img.open(f_path)
        save_path = out_path + 'c' + name
        image.save(save_path, quality=60)
        print('compressed file save in : ' + save_path)


app = make_app()
app.mainloop()
