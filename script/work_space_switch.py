import os
from subprocess import call
from script.work_space_config import WORK_SPACE_CONFIG


class WorkSpace:

    def __init__(self, c):
        self.folders = c['folders']
        self.name = c['name']
        self.target = c['target']

    def switch(self):
        for f in os.listdir(self.target):
            if f.endswith('.wspc'):
                os.remove(self.target + f)

        # make link
        for source in self.folders:
            target = self.target + source.split('/')[-1] + '.wspc'
            command = ['ln', '-s', source, target]
            call(command)


workspaces = [WorkSpace(c) for c in WORK_SPACE_CONFIG]
print("Choose your workspace:")
choice = input()
for space in workspaces:
    if space.name == choice:
        space.switch()
