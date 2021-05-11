import os

def folder_check(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

split_dir = lambda mydir: os.path.normpath(mydir).split(os.sep)