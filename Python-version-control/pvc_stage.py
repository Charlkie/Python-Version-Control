"""
Python-version-control-stage.

This file controls the staging function of PVC,
staging allows you to select which files you want
to commit to your repo. this can help when you don't
want some files in your repo

Use case:
use the command -
C:\path\to\your\repo> pvc stage [filename1, filename2]
- to selectively choose files or -
C:\path\to\your\repo> pvc stage *
- to stage all the files that have changed since last commit

optional methods:
-f :: force - ignores any errors and forces the code through
-m :: messege - adds a title to your repo, Defaults to "my_new_repo"
"""


class Stage(object, PVC):
	"""The main class for staging things in pvc."""
	def __init__(self, list_of_filenames):
		"""The initialiser for pvc stage."""
		self.dir = os.getcwd()
		self.repo = self.dir+".pvc"
		self.folders = ['objects','info','refs']
		PVC.__init__(self)
		self.files = list_of_filenames
