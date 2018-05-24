"""
Python-version-control-stage.

This file controls the staging function of PVC,
staging allows you to select which files you want
to commit to your repo.

Goes through all system argument if files hashes the files contents and is it
doesnt already exist adds a zipped version of this content to a
directory in objects directory.

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
from sys import exit
import hashlib
import tarfile
import gzip
import zlib
import shutil
import re

class Stage(PVC):
	"""The main class for staging things in pvc."""
	def __init__(self, list_args):
		"""The initialiser for pvc stage."""
		if not os.path.exists(os.getcwd()+'/.pvc'):
			print("Repository has not been initialized, try -- pvc init")
			exit()
		PVC.__init__(self)
		if not os.path.exists(self.index):
			open(self.index, 'w+')

	def add(self):
		"""Main Function of pvc-stage."""
		not_found = []
		compress = False
		for obj in self.argv[2:]:
			path = self.dir+'/'+obj
			#cheks if file being staged exists
			if os.path.exists(path):
				if os.path.isfile(path):
					content_hash=PVC.hash_file(self, path)
					if not os.path.exists(self.obj+'/'+content_hash[:2]):
						Stage.add_blob(self, content_hash, obj)
						Stage.write_index(self, obj, content_hash)
						compress = True
				else:
					#this means the object is a directory
					for file in Stage.stage_dir(self, path):
						content_hash=PVC.hash_file(self, file)
						Stage.add_blob(self, content_hash, file[self.dirlen:])
						b = file[self.dirlen:]
						Stage.write_index(self, b, content_hash)
			else:
				not_found.append(obj)
		if len(not_found) > 0:
			print('pvc was unable to find these files:',
				  ', '.join([file for file in not_found]))
		if compress: PVC.compress(self.index, self.index)

	def stage_dir(self, dir):
		f = []
		for subdir, dirs, files in os.walk(dir):
			for file in files:
				path = subdir+'/'+file
				if file not in self.exclude: f.append(path)
		return f

	def add_blob(self, hash, obj):
		if not os.path.exists(self.obj+hash[0:2]):
			print('-added', obj)
			PVC.blob(self, hash, self.dir+'/'+obj)

	def write_index(self, path, hash):
		#checks if the files has a compressed file signature
		if r'x\xda' in str(open(self.index, 'rb').read()): #doesnt work with extre \ at end -- show Stephan
			PVC.decompress(self.index, self.index)
		f = open(self.index, 'a')
		line = '100644 '+hash+' 0 '+path+'\n'
		f.write(line); f.close()
		# PVC.compress(self.index, self.index)

if __name__ == '__main__':
	stage = Stage(['*'])
	stage.add()
