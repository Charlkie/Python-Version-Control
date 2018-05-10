"""
Python-version-control-stage.

This file controls the staging function of PVC,
staging allows you to select which files you want
to commit to your repo. this can help when you don't
want some files in your repo

Use case:
use the command -
C:\path\to\your\repo> pvc stage [filename1, filename2]
- to selectively choose files or -,
C:\path\to\your\repo> pvc stage *
- to stage all the files that have changed since last commit

optional methods:
-f :: force - ignores any errors and forces the code through
-m :: messege - adds a title to your repo, Defaults to "my_new_repo"
"""

from pvc_main import PVC
import os

class Stage(PVC):
	"""The main class for staging things in pvc."""
	def __init__(self, list_args):
		"""The initialiser for pvc stage."""
		self.files = list_args
		self.staged = []
		PVC.__init__(self)

	def save_dir(self, file, path, dir_files, files):
		for _file in os.listdir(path):
			new_path = path+'/'+_file
			if os.path.isdir(new_path) == True:
				print(_file,'is a directory')
				Stage.save_dir(self, _file, new_path, {}, [])
			else:
				files.append(_file)
				print(_file,'is a file')
		dir_files[file] = files
		self.staged.append(dir_files)


	def add(self):
		if self.files[0] == '*':
			for file in os.listdir(self.dir):
				if os.path.isdir(file) == True:
					if file != '.pvc' and file !='.git':
						dir_files = {}
						files = []
						Stage.save_dir(self, file, self.dir+'/'+file, dir_files, files)
				else:
					self.staged.append(file)
			print(self.staged)
		else:
			for file in self.files:
				self.staged[file] = os.path.isdir(file)





if __name__ == '__main__':
	stage = Stage(['*'])
	stage.add()
