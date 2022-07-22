from os import listdir
from os.path import isdir
import re

FILES_AND_FOLDERS = r'/^[^\/]+\/statistics\/?(?:[^\/]+\/?)*$/gm'

#specify list of accepted files
def is_file(exp, file_name):
    return re.match(exp, file_name, flags = 0)

#return the list of all files in directory
def get_all_files(path):
    return listdir(path) if isdir(path) else []



