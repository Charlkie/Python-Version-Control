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

class Commit(PVC):
	def __init__(self):
		PVC.__init__(self)
		self.log = self.repo+'/'+'logs'
		if not os.path.exists(self.log):
			os.makedirs(self.log+'/refs')
			open(self.log+'/HEAD','w+')
		if self.argv[2] != "-m":
			print("Insert error here")

	def commit(self):
		print("you just committed some stuff")
		print(self.argv)
		#writes commit to COMMIT_EDITMSG file
		commit_msg = open(self.repo+'/COMMIT_EDITMSG', 'w+')
		commit_msg.write(self.argv[3])
		print(self.argv[3])
		#
		
#loop through
if __name__ == "__main__":
	commit = Commit()
	commit.commit()
# for subdir, dirs, files in os.walk(self.repo+'/objects'):
# 	for file in files:
# 		print(subdir[-2:]+file)
