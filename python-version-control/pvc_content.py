from pvc_main import PVC
import os
import ntpath
import zlib
from sys import exit

class Content(PVC):
	def __init__(self):
		PVC.__init__(self)
		if not len(self.argv) == 3:
			print("need three arguments")
			exit()
		self.file = self.argv[2]

	def content(self):
		path = self.obj+self.file[:2]+'/'
		if not os.path.exists(path):
			print("File doesnt exist")
			exit()
		file = open(path+os.listdir(path)[0], 'rb').read()
		content = zlib.decompress(file)
		print(content.decode('utf-8'))

if __name__ == "__main__":
	content = Content()
	content.content()
