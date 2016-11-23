#!/usr/bin/env python
# -*- coding: utf-8 -*-



import os
import argparse
import time
import sys
import getpass

class FileTreeMaker(object):

	# FileTreeMaker code extracted from legendmohe Stack Overflow user. 
	# Link to post: http://stackoverflow.com/questions/16953842/using-os-walk-to-recursively-traverse-directories-in-python
	# Link to autor profile: http://stackoverflow.com/users/1349479/legendmohe

	__author__  = "legendmohe"

	def _recurse(self, parent_path, file_list, prefix, output_buf, level):
		if len(file_list) == 0 \
			or (self.max_level != -1 and self.max_level <= level):
			return
		else:
			file_list.sort(key=lambda f: os.path.isfile(os.path.join(parent_path, f)))
			for idx, sub_path in enumerate(file_list):
				if any(exclude_name in sub_path for exclude_name in self.exn):
					continue

				full_path = os.path.join(parent_path, sub_path)
				idc = "┣━"
				if idx == len(file_list) - 1:
					idc = "┗━"

				if os.path.isdir(full_path) and sub_path not in self.exf:
					output_buf.append("%s%s[%s]" % (prefix, idc, sub_path))
					if len(file_list) > 1 and idx != len(file_list) - 1:
						tmp_prefix = prefix + "┃  "
					else:
						tmp_prefix = prefix + "    "
					self._recurse(full_path, os.listdir(full_path), tmp_prefix, output_buf, level + 1)
				elif os.path.isfile(full_path):
					output_buf.append("%s%s%s" % (prefix, idc, sub_path))

	def make(self, args):
		self.root = args.root
		self.exf = args.exclude_folder
		self.exn = args.exclude_name
		self.max_level = args.max_level

		print("root: %s" % self.root)

		buf = []
		path_parts = self.root.rsplit(os.path.sep, 1)
		buf.append("[%s]" % (path_parts[-1],))
		self._recurse(self.root, os.listdir(self.root), "", buf, 0)

		output_str = "\n".join(buf)
		if len(args.output) != 0:
			with open(args.output, 'w') as of:
				of.write(output_str)
		return output_str




class fileExtractor(object):

	# This Class stores the information extracted into a folder whose name is the PC's name.
	# Into the folder there will be a txt file with the file and folders tree hierarchy of the computer
	# and also a collection of valuable system files as well as valuable data.

	__author__ = "EnriqueMoran"

	def createDir(self):
		nameOfComputer = os.environ['COMPUTERNAME']
		newpath = r'.\\' + nameOfComputer 
		if not os.path.exists(newpath):
			os.makedirs(newpath)
		return newpath

	def treeToFile(self, dirPath): 							### Hay que quitar la ultima linea, que pone siempre "None"
		nameOfComputer = os.environ['COMPUTERNAME']
		filename = nameOfComputer + "-Tree.txt"
		path = dirPath + "\\" + filename
		with open(path, 'w', encoding='utf-8') as f:
			sys.stdout = f
			print (print(FileTreeMaker().make(args)))
		f.close()

	def run(self):
		path = self.createDir()
		self.treeToFile(path)



if __name__ == "__main__":
	user = getpass.getuser()
	parser = argparse.ArgumentParser()
	parser.add_argument("-r", "--root", help="root of file tree", default="C:\\Users\\" + user + "\\Downloads")          # Root directory  
	parser.add_argument("-o", "--output", help="output file name", default="")
	parser.add_argument("-xf", "--exclude_folder", nargs='*', help="exclude folder", default=[])
	parser.add_argument("-xn", "--exclude_name", nargs='*', help="exclude name", default=[])
	parser.add_argument("-m", "--max_level", help="max level",
						type=int, default=-1)
	args = parser.parse_args()
	fileExtractor().run()


#### EJEMPLOS ####

'''
user = getpass.getuser()
parser.add_argument("-r", "--root", help="root of file tree", default="C:\\Users\\" + user + "\\Downloads")  # Get files tree hierarchy from Donwloads
parser.add_argument("-r", "--root", help="root of file tree", default="C:\\Users\\" + user + "\\Documents")  # Get files tree hierarchy from Documents
parser.add_argument("-r", "--root", help="root of file tree", default="C:\\Users\\" + user + "\\Desktop")  # Get files tree hierarchy from Desktop
parser.add_argument("-r", "--root", help="root of file tree", default="C:\\Program Files (x86)") # Get files tree hierarchy from Program Files (x86)
'''


''' TO DO

EN MUCHOS DIRECTORIOS NO TIENE PERMISO PARA METERSE, HAY QUE HACER QUE NO SE META
FALTA HACER QUE PASE LOS ARCHIVOS AL PENDRIVE
CREAR UNA CARPETA QUE SE LLAME 	nameOfComputer + "-DATA" DONDE SE METAN LOS PROGRAMAS Y DOCUMENTOS DEL PC

'''