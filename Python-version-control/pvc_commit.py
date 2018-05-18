from pvc_main import PVC
import os

class Commit(PVC):
	def __init__(self):
		PVC.__init__(self)
		self.log = self.repo+'/'+'logs'
		if not os.path.exists(self.log):
			os.makedirs(self.log+'/refs')
			open(self.log+'/HEAD','w+')
		if not os.path.exists(self.repo+'/index'):
			open(self.repo+'/index','w+')

	def commit(self):
		print("yes")
		for subdir, dirs, files in os.walk(self.repo+'/objects'):
			for file in files:
				print(subdir[-2:]+file)


if __name__ == "__main__":
	commit = Commit()
	commit.commit()
