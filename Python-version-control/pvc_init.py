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

class Init(PVC):
	"""The class for pvc-initialise"""
	def __init__(self):
		"""initialiser method for initialiser."""
		self.init_files = ['config', 'description', 'HEAD']
		PVC.__init__(self)

	def init_repo(self):
		# TESTING everything inside 1st if statement
		if os.path.exists(self.repo) == True:
			shutil.rmtree(self.repo+'/')
			print('Deleted currrent repository')
		# Creates initial directories and folders
		if os.path.exists(self.repo) == False:
			os.makedirs(self.repo)
			for folder in self.folders:
				os.makedirs(self.repo+'/'+folder)
			for file in self.init_files:
				f = open(self.repo+'/'+file, 'w+'); f.close()
			print("Initialized empty repository in"+self.repo)
		else:
			print("PCV already exists")




"""Testing for initialiser"""
if __name__ == "__main__":
	init = Init()
	init.init_repo()
