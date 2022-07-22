from os import listdir
from os.path import isdir
import re

#return the list of all files in directory
def get_all_files(path, files_only = True, exp = r'[a-zA-Z0-9_ ]*[.]'):
    all_files = listdir(path) if isdir(path) else []

    if files_only and len(all_files) > 0:
        all_files = list(filter(lambda file_name: re.match(exp, file_name), all_files))
        # all_files = [file_name for file_name in all_files if re.match(exp, file_name)]
    return all_files





