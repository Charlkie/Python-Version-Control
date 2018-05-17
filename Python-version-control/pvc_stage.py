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
import re
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
		self.files = list_args
		self.staged = []
		self.argv = sys.argv
		self.foo = "foo"
		self.hash = hashlib.sha1
		if not os.path.exists(os.getcwd()+'/.pvc'):
			print("Repository has not been initialized, try -- pvc init")
			sys.exit()
		PVC.__init__(self)

	def add(self):
		"""Main Function of pvc-stage."""
		not_found = []
		for obj in self.argv[2:]:
			print("object:", obj, end=" ")
			path = self.dir+'/'+obj
			if os.path.exists(path):
				if os.path.isfile(path):
					Stage.hash_obj(self, obj)
				else:
					Stage.hash_obj(self, obj, 'dir')
				#print('-added', obj)
			else:
				not_found.append(obj)
		if len(not_found) > 0:
			print('pvc was unable to find these files:',
									', '.join([file for file in not_found]))

	def hash_obj(self, obj, type="file"):
		"""Hash creation function."""
		name = self.dir+'/'+obj
		if type == "file":
			content_hash = Stage.hash_file(self, name)
			print("FILE", content_hash)
		else:
			print("DIRECTORY", end=" ")
			content_hash = Stage.hash_dir(self, name)
		#content_hash = Stage.hash_file(self, name) if type == 'file' else Stage.hash_dir(self, name) #dir
		# print("content_hash:",content_hash)
		if not os.path.exists(self.repo+'/objects/'+content_hash[0:2]):
			Stage.blob(self, content_hash, obj)

	#THIS ONE
	def hash_dir(self, dirname):
		hash_func = hashlib.sha1
		hash_val = []
		for root, dirs, files in os.walk(dirname, topdown=True, followlinks=False):
			if not re.search(r'/\.', root):
				for f in files:
					if not f.startswith('.') and not re.search(r'/\.', f):
						hash_val.extend([Stage.hash_file(self, os.path.join(root, f))])
				hash_val.extend([  ])
				print("HASH",Stage.hash_reduce(self, hash_val))
		return Stage.hash_reduce(self, hash_val)

	#Hash File
	def hash_file(self, filepath):
		with open(filepath, 'rb') as f:
			while True:
				block = f.read(self.blocksize)
				if not block:break
				self.hash().update(block)
			# print("directory: ",self.hash().hexdigest())
			return self.hash().hexdigest()

	#THIS ONE ALSO
	def hash_reduce(self, hashlist):
		for val in sorted(hashlist):
			self.hash().update(val.encode('utf-8'))
		return self.hash().hexdigest()

	def blob(self, hash, file):
		"""Hash file container creation function."""
		path = os.path.join(self.repo+'/objects/', hash[0:2])
		os.makedirs(path)
		# Compresing the files
		if os.path.isfile(file):
			with open(file, 'rb') as f_in, gzip.open(path+'/'+hash[2:-1], "wb") as f_out:
				shutil.copyfileobj(f_in, f_out)
		else: pass

if __name__ == '__main__':
	stage = Stage(['*'])
	stage.add()
