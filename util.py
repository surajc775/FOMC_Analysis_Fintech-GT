import os

def folder_check(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)