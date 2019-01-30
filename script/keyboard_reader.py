from pynput.keyboard import Listener, Controller, Key
import time
import threading


class ComboListener:

    def __init__(self):
        self.cur_keys = []
        self.keymap = {
            'aaa': 'aster',
            'bbb': 'good boy'
        }
        self._run()

    def _on_press(self, key):
        try:
            self.cur_keys.append(key.char)
        except AttributeError:
            self.cur_keys.append(key.name)

    def _run(self):
        l = Listener(on_press=self._on_press)
        l.daemon = True
        l.start()

        t = threading.Thread(target=self._clear)
        t.daemon = True
        t.start()

    def _clear(self):
        while True:
            time.sleep(0.7)
            self.cur_keys.clear()

    def get_combo(self):
        if len(self.cur_keys) >= 3:
            combo = self.cur_keys[-3]
            return combo

    def parse_combo(self):
        combo = self.get_combo()
        if combo:
            key = ''.join(combo)
            if key in self.keymap.keys():
                return self.keymap[key]


def send(content):
    for _ in range(3):
        c.press(Key.backspace)

    c.type(content)


cl = ComboListener()
c = Controller()

while True:
    combo = cl.parse_combo()
    if combo:
        print(combo)
        send(combo)
