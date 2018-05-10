import subprocess as sb
import os

class Init():
    def __init__(self):
        self.dir = os.getcwd()
        self.repo = self.dir+".pvc"
        self.folders = ['objects','info','refs']
    def init(self):
        if os.path.exists(self.repo) == False:
            os.makedirs(self.repo)

    def create_dir(self):
        pass
        #os.makedirs(os.path.dirname('.pvc'))
        #for folder in self.folders:
            #os.makedirs(os.path.join('.pvc',folder))



init = Init()
init.init()
# init.create_dir()
