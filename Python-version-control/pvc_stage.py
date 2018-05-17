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
import tarfile
import shutil
from random import randint as r

class Stage(PVC):
	"""The main class for staging things in pvc."""
	def __init__(self, list_args):
		"""The initialiser for pvc stage."""
		self.files = list_args
		self.staged = []
		self.argv = sys.argv
		if not os.path.exists(os.getcwd()+'/.pvc'):
			print("Repository has not been initialized, try -- pvc init")
			sys.exit()
		PVC.__init__(self)

	def add(self):
		"""Main Function of pvc-stage."""
		not_found = []
		unstaged = 0
		for obj in self.argv[2:]:
			path = self.dir+'/'+obj
			if os.path.exists(path):
				if os.path.isfile(path):
					content_hash = Stage.hash_file(self, path)
				if not os.path.exists(self.repo+'/objects/'+content_hash[0:2]):
					if content_hash:
						Stage.blob(self, obj, content_hash)
					else: Stage.blob(self, obj)
				else: unstaged+=1
			else:
				not_found.append(obj)
			if unstaged == len(self.argv[2:]): print("Stage up too date! Make changes silly ;)")
		if len(not_found) > 0:
			print('pvc was unable to find these files:',
				  ', '.join([file for file in not_found]))

	"""Hashes the files with the sha1 hash"""
	def hash_file(self, filepath, obj="file"):
		hash = hashlib.sha1()
		with open(filepath, 'rb') as f:
			while True:
				block = f.read(self.blocksize)
				if not block:break
				hash.update(block)
			#if obj == "file": print("HASH",hash.hexdigest(),filepath)
			return hash.hexdigest()

	#THIS ONE ALSO
	def hash_reduce(self, hashlist):
		hash = hashlib.sha1()
		for val in sorted(hashlist):
			hash.update(val.encode('utf-8'))
		return hash.hexdigest()

	def blob(self, file, hash=False):
		"""Hash file container creation function."""
		path = os.path.join(self.repo+'/objects/', hash[0:2])
		os.makedirs(path)
		# Compresing the files
		if hash:
			with open(file, 'rb') as f, gzip.open(path+'/'+hash[2:-1], "wb") as zipped:
				shutil.copyfileobj(f, zipped)
		else:
			with tarfile.open(hash[2:-1], "w:gz") as tar:
				tar.add(file, arcname=os.path.basename(path))

if __name__ == '__main__':
	stage = Stage(['*']) #['#'] represents all command line arguments
	stage.add()
