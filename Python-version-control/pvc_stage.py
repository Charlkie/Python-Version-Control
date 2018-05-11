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
			path = self.dir+'/'+file
			if os.path.exists(path) == True:
				if os.path.isfile(path) == True:
					print('-added', file)
					Stage.hash_file(self, file)
				else:
					Stage.hash_dir(self, file)
			else:
				not_found.append(file)
		if len(not_found) > 0:
			print('pvc was unable to find these files:',
					', '.join([file for file in not_found]))

	def hash_file(self, file):
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

	def hash_dir(self, dir):
		print('hash_dir()')
		hashes = []
		for path, dirs, files in os.walk(dir):
			for file in sorted(files): # we sort to guarantee that files will always go in the same order
				hashes.append(sha1OfFile(os.path.join(path, file)))
			for dir in sorted(dirs): # we sort to guarantee that dirs will always go in the same order
				hashes.append(hash_dir(os.path.join(path, dir)))
			break # we only need one iteration - to get files and dirs in current directory
		return print(str(hash(''.join(hashes))))

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
