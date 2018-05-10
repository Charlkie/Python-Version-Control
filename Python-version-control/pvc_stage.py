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
import sys
import hashlib
import gzip
import shutil
from random import randint as r

class Stage(PVC):
	"""The main class for staging things in pvc."""
	def __init__(self, list_args):
		"""The initialiser for pvc stage."""
		if not os.path.exists(os.getcwd()+'/.pvc'):
			raise IOError("Repository has not been initialized, try -- pvc init")
		self.files = list_args
		self.staged = []
		self.argv = sys.argv
		self.hash = hashlib.sha1()
		#integers 1-10 and letters A-Z
		self.char = [[str(i) for i in range(10)],[chr(x) for x in range(65,91)]]
		self.taken = []
		PVC.__init__(self)



	def add(self):
		not_found = []
		for file in self.argv[2:]:
			if os.path.exists(self.dir+'/'+file) == True:
				print('-added', file)
				Stage.hash(self, file)
			else: not_found.append(file)
		if len(not_found) > 0:
			print('pvc was unable to find these files:',
					', '.join([file for file in not_found]))

	def hash(self, file):
		name = self.dir+'/'+file
		with open(name, 'rb') as f:
			while True:
				content = f.read(self.blocksize)
				if not content:
					break
				self.hash.update(data)
		content_hash = self.hash.hexdigest()
		if not os.path.exists(self.repo+'/objects/'+content_hash[0:2]):
			Stage.blob(self, content_hash, file)

	def blob(self, hash, file):
		path = os.path.join(self.repo+'/objects/',hash[0:2])
		os.makedirs(path)
		# Compresing the files
		with open(file, 'rb') as f_in, gzip.open(path+'/'+hash[2:-1],"wb") as f_out:
			shutil.copyfileobj(f_in, f_out)

if __name__ == '__main__':
	stage = Stage(['*'])
	stage.add()
	# stage.create_blob(folders, added_files)








	# def save_dir(self, file, path, dir_files, files):
	# 	for _file in os.listdir(path):
	# 		new_path = path+'/'+_file
	# 		if os.path.isdir(new_path) == True:
	# 			Stage.save_dir(self, _file, new_path, {}, [])
	# 		else:
	# 			files.append(_file)
	# 	dir_files[file] = files
	# 	self.staged.append(dir_files)
	#
	# def add(self):
	# 	if self.files[0] == '*':
	# 		for file in os.listdir(self.dir):
	# 			if os.path.isdir(file) == True:
	# 				if file != '.pvc' and file !='.git':
	# 					dir_files = {}
	# 					files = []
	# 					Stage.save_dir(self, file, self.dir+'/'+file, dir_files, files)
	# 			else:
	# 				self.staged.append(file)
	# 		print(self.staged)
	# 	else:
	# 		for file in self.files:
	# 			self.staged[file] = os.path.isdir(file)
