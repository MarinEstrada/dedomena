# from os import walk
import os
from os.path import join, normpath

def list_of_files(path_name):

	pathname_modified = path_name.replace('+', '/')


	list_of_files = []

	for dirpath, dirnames, filenames in os.walk(pathname_modified):
		list_of_files.extend(filenames)
		# print(list_of_files)
		# print(filenames)
		return list_of_files

	return list_of_files


# list_of_files("/drives/c/Users/adria/cmpt/bro_workfolder/dedomena/")