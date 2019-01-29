import webbrowser
from time import ctime

from script.read_config import CONFIGS
import os
import threading


class ReadManager:

    def __init__(self, config):
        self.read_time = config['time']
        self.folder_path = config['folder_path']
        self.urls = self.urls_parse(self.folder_path)

    def is_valid_time(self):
        return self.read_time == ctime().split()[-2]

    def urls_parse(self, path):
        urls = []
        for f in os.listdir(path):
            if not f.startswith('.'):
                path = path + f
                with open(path, 'r') as raw_url:
                    url = raw_url.read().split('URL=')[-1].strip('\n')
                    urls.append(url)
            return urls

    def send_to_browser(self):
        for url in self.urls:
            webbrowser.open_new_tab(url)

    def run(self):

        def _run():
            while True:
                if self.is_valid_time():
                    print('ZacLog: send url to browser')
                    self.send_to_browser()

        t = threading.Thread(target=_run)
        t.daemon = True
        t.start()


managers = [ReadManager(c) for c in CONFIGS]
for manager in managers:
    print('ZacLog:', manager.urls)
    manager.run()
