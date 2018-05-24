from pvc_main import PVC
import os

"""
Python-version-control-commit.

Creates a tree file of all

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

"""
from pvc_main import PVC
from pvc_stage import Stage
import hashlib
import zlib

class Commit(PVC):
	def __init__(self):
		PVC.__init__(self)
		# Stage._init__(self)
		self.log = self.repo+'/'+'logs'
		if not os.path.exists(self.log):
			os.makedirs(self.log+'/refs')
		if self.argv[2] != "-m":
			print("Insert error here")
		self.exclude = [line for line in open(self.exclude_dir, 'r')
						if line[0] != '#']

	def commit(self):
		print("you just committed some stuff")
		print(self.argv)
		#writes commit to COMMIT_EDITMSG file
		commit_msg = open(self.repo+'/COMMIT_EDITMSG', 'w+')
		commit_msg.write(self.argv[3])
		print(self.argv[3])
	#make tree dir

	#make commit object
	def commit_obj(self):
		master = self.heads+'/master'
		a = "somehash"
		b = "Chaasarl"
		c = "aaradl"
		content = "tree {}\nauthor {}\ncommiter {}".format(a, b, c)
		hash = hashlib.sha1(bytes(content, 'utf-8'))
		hex = hash.hexdigest()
		path = self.obj+hex[:2]
		file_name = path+'/'+hex[2:]
		os.makedirs(path)
		file = open(path+'/'+hex[2:], 'w')
		file.write(content)
		file.close()
		PVC.compress(file_name, file_name)

		#saves current commit to master file
		open(master, 'w+').write(hex)
		prev_hex = open(master, 'r').readlines()
		head = open(self.log+'/HEAD','w+')
		if os.path.getsize(self.log+'/HEAD') == 0:
			prev_hex = '0'*40
			initial = True
		head_content = prev_hex+' '+hex+' %s'%('(initial)\n' if initial==True else '\n')
		head.write(head_content)
		head.close()

	""" this creates a snapshot of the current working directory
		by creating a commit object and trees pointing to blobs """
	def snapshot(self):
		tree = [{dir:os.path.isfile(dir)} for dir in os.listdir(self.dir) if dir not in self.exclude]
		print(tree)

#loop through
if __name__ == "__main__":
	commit = Commit()
	commit.snapshot()
# for subdir, dirs, files in os.walk(self.repo+'/objects'):
# 	for file in files:
# 		print(subdir[-2:]+file)
