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

    def test(self):
        hash = hash.Hash_Obj()
        #keep these
        hash.hash_obj_dir(".pyvcs/objects", folders)
        added_files=['test.txt']
        folders= [(hash.hash_file(file)[0:2],hash.hash_file(file)[2:-1]) for file in added_files]
        print(folders[0][0])
        hash.create_blob(folders, added_files)
        #keep these
        #print(input("file to decode: "))

init = Init()
init.init()
# init.create_dir()
