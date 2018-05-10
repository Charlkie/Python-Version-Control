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

class Stage(PVC):
	"""The main class for staging things in pvc."""
	def __init__(self, list_args):
		"""The initialiser for pvc stage."""
		self.files = list_args
		self.staged = []
		self.argv = sys.argv
		self.h = hashlib.sha1()
		PVC.__init__(self)

	def sort(self):
		not_found = []
		for file in self.argv:
			if os.path.exists(self.dir+'/'+file) == True:
				Stage.hash(self, file)
			else:
				not_found.append(file)

	def hash(self, filename):
		print(filename)
		with open(filename, 'rb') as f:
			buf = f.read(self.blocksize)
			while len(buf) > 0:
				self.h.update(buf)
				buf = f.read(self.blocksize)
		hex= self.h.hexdigest()
		print(hex)
		return hex

	def create_blob(self, folders, files, root='.pvc/objects'):
		print("Busy making blob")
		for i in range(len(folders)):
			path = os.path.join(root,folders[i][0])
			os.makedirs(path)
			# Compresing the files
			with open(files[i], 'rb') as f_in, gzip.open(path+'/'+folders[i][1],"wb") as f_out:
				shutil.copyfileobj(f_in, f_out)

	def test(self):
		"""The testing method for pvc-init."""
		hash = hash.Hash_Obj()
		# keep these
		hash.hash_obj_dir(".pyvcs/objects", folders)

		print(folders[0][0])
		hash.create_blob(folders, added_files)
		# keep these
		# print(input("file to decode: "))

if __name__ == '__main__':
	stage = Stage(['*'])
	stage.sort()
	# folders= [(stage.sort()[0:2],stage.sort()[2:-1]) for file in added_files]
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
