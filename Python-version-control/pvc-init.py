"""
Python-version-control-initialiser.

The code that gives you a fresh repo to put your code into.
Use the console command PVC init to generate a new repo at
the current location of your command line

Use case:
use the command -
C:\path\to\your\repo> pvc init
- to create a blank repo with the deafault name -
C:\path\to\your\repo> pvc init -m "My new repo"
- Creates a blank repo with a custom title

optional methods:
-f :: force - ignores any errors and forces the code through
-m :: messege - adds a title to your repo, Defaults to "my_new_repo"
"""


from __init__ import PVC


class init(object, PVC):
	"""The class for pvc-initialise"""
	def __init__():
		"""initialiser method for initialiser."""
		PVC.__init__(dir)
