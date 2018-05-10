"""The Python Version control software."""

import os

class PVC(object):
	"""The main class for PVC."""
	def __init__(self):
		"""The initialiser for The main PVC object"""
		self.dir = os.getcwd()
		self.repo = self.dir+'/.pvc'
		self.folders = ['objects','info','refs','hooks']

	def force(command):
		"""Base command for forcing git commands."""
		pass

	def messege(commnad):
		"""Base command for adding messeges to git commands."""
		pass
