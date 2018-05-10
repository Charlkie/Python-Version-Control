from pvc_main import PVC
import subprocess as sb
import os


class Add(PVC):
	"""The class for pvc-initialise"""
	def __init__(self):
		"""initialiser method for initialiser."""
		PVC.__init__(self)

	def init_repo(self):
		if os.path.exists(self.repo) == False:
			os.makedirs(self.repo)
			for folder in self.folders:
				os.makedirs(self.repo+'/'+folder)
			print("Initialized empty repository in"+self.repo)
		else:
			print("PCV already exists")


	def test(self):
		"""The testing method for pvc-init."""
		hash = hash.Hash_Obj()
		#keep these
		hash.hash_obj_dir(".pyvcs/objects", folders)
		added_files=['test.txt']
		folders= [(hash.hash_file(file)[0:2],hash.hash_file(file)[2:-1]) for file in added_files]
		print(folders[0][0])
		hash.create_blob(folders, added_files)
		#keep these
		#print(input("file to decode: "))

"""Testing for initialiser"""
if __name__ == "__main__":
	init = Init()
	#init.init_repo()
