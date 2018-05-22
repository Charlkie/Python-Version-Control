from pvc_main import PVC
import tarfile
import gzip
import zlib

class LsFiles(PVC):
	def __init__(self):
		PVC.__init__(self)

	def decide(self):
		if self.argv[2] == '--stage':
			"""read content of zipped file"""
			PVC.decompress(self.index, self.index)
			f = open(self.index, 'r')
			print("".join(f.readlines()),end="")
			PVC.compress(self.index, self.index)

if __name__ == "__main__":
	ls = LsFiles()
	ls.decide()
