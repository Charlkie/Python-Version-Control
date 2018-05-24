"""The Python Version control software."""
import os
import zlib
import hashlib
import sys

class PVC(object):
	"""The main class for PVC."""
	def __init__(self):
		"""The initialiser for The main PVC object"""
		self.dir = os.getcwd()
		self.dirlen = len(self.dir)+1
		self.argv = sys.argv
		self.exclude = ['.DS_Store']
		#self.files = {'info':[{'exclude':'#exclude'}], 'hooks':[]}
		self.dirs = ['objects', 'info', 'objects/info', 'objects/packs',
						'refs','refs/heads','refs/tags', 'hooks']
		self.repo = self.dir+'/.pvc'
		self.obj = self.repo+'/objects/'
		self.index = self.repo+'/index'
		self.heads = self.repo+'/refs/heads'
		self.exclude_dir = self.repo+"/info/exclude"
		self.blocksize = 65536 # 64 bytes
		self.staged = False

	def force(command):
		"""Base command for forcing git commands."""
		pass

	def messege(commnad):
		"""Base command for adding messeges to git commands."""
		pass

	def compress(dir, name):
		str_object1 = open(dir, 'rb').read()
		str_object2 = zlib.compress(str_object1, 9)
		f = open(name, 'wb')
		f.write(str_object2)
		f.close()

	def decompress(dir, name):
		file = open(dir, 'rb').read()
		content = zlib.decompress(file)
		f = open(name, 'wb')
		f.write(content)
		f.close()

	def read_zip(self, dir, file):
		PVC.decompress(dir, file)
		f = open(file, 'r')
		# print("something")
		# print("read",f.readlines())
		print("".join(f.readlines()),end="")
		PVC.compress(dir, file)

	def hash_file(self, filepath):
		hash = hashlib.sha1()
		with open(filepath, 'rb') as f:
			while True:
				block = f.read(self.blocksize)
				if not block:break
				hash.update(block)
			return hash.hexdigest()

	def blob(self, hash, file):
		"""Hash file container creation function."""
		path = os.path.join(self.repo+'/objects/', hash[0:2])
		os.makedirs(path)
		# Compresing the files
		# print("file", file)
		if not os.path.isdir(file):
			PVC.compress(file, path+'/'+hash[2:])
