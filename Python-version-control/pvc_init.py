"""
Python-version-control-initialiser.

The code that gives you a fresh repo to put your code into.
Use the console command PVC init to generate a new repo at
the current location of your command line

Use case:
use the command -
C:\path\to\your\repo> pvc init
- to create a blank repo with the deafault name -
C:\path\to\your\repo> pvc init -m "My new repo"
- Creates a blank repo with a custom title

optional methods:
-f :: force - ignores any errors and forces the code through
-m :: messege - adds a title to your repo, Defaults to "my_new_repo"
"""


from pvc_main import PVC
import subprocess as sb
import os
import shutil #TESTING

shutil.rmtree('/folder_name')


class Init(PVC):
	"""The class for pvc-initialise"""
	def __init__(self):
		"""initialiser method for initialiser."""
		self.init_files = ['config', 'description', 'HEAD']
		PVC.__init__(self)

	def init_repo(self):
		#TESTING everything inside 1st if statement
		if os.path.exists(self.repo) == True:
			os.rmdir(self.repo+'/')
		if os.path.exists(self.repo) == False:
			os.makedirs(self.repo)
			for folder in self.folders:
				os.makedirs(self.repo+'/'+folder)
			for file in self.init_files:
				f = open(file, 'w')
				f.close()
				print("")

			print("Initialized empty repository in"+self.repo)
		else:
			print("PCV already exists")


	def test(self):
		"""The testing method for pvc-init."""
		hash = hash.Hash_Obj()
		#keep these
		hash.hash_obj_dir(".pyvcs/objects", folders)
		added_files=['test.txt']
		folders= [(hash.hash_file(file)[0:2],hash.hash_file(file)[2:-1]) for file in added_files]
		print(folders[0][0])
		hash.create_blob(folders, added_files)
		#keep these
		#print(input("file to decode: "))

"""Testing for initialiser"""
if __name__ == "__main__":
	init = Init()
	init.init_repo()
