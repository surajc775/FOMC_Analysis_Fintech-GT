# categorize each file based on doc type

import os
import glob
from dotenv import load_dotenv
load_dotenv(".env")
import pickle
from pathlib import Path

from util import folder_check

# get mappings
doc_types = pickle.load(open("doc_types.pkl", "rb+"))
kw_to_doctype = doc_types["kw_to_type"]
kw_doc_items = kw_to_doctype.items()

data_dir = os.environ.get("data_dir", "data")

def folder_split(folder_path):
    for folder in glob.glob(os.path.join(folder_path, "*", "")):
        for path, folders, files in os.walk(folder):
            min_file_threshold = 2  # to account for files like .DS_Store
            if (len(files) < min_file_threshold):
                continue
            # basically I want to stop splitting when we hit the doctype folders
            # but this isn't a good way to do it :()
            if (path.split(os.sep)[-1] in doc_types["doctypes"] or path.split(os.sep)[-2] in doc_types["doctypes"]):
                continue
            for fn in files:
                fn_lower = fn.lower()
                for kw, doctype in kw_doc_items:
                    if kw.lower() in fn_lower:
                        doctype_folder = os.path.join(path, doctype)
                        folder_check(doctype_folder)
                        os.rename(os.path.join(path, fn), os.path.join(doctype_folder, fn))
                        break

def folder_merge(folder_path):
    for folder in glob.glob(os.path.join(folder_path, "*", "")):
        for path, folders, files in os.walk(folder):
            min_file_threshold = 2  # to account for files like .DS_Store
            if not files or (len(files) < min_file_threshold) and files[0] == ".DS_Store":
                continue
            for fn in files:
                fp = os.path.join(path, fn)
                p = Path(fp).absolute()
                parent_dir = p.parents[1]
                p.rename(parent_dir / p.name)
            # # we don't want to do this because it'll destroy the bigrams as well
            # os.rmdir(path)

if __name__ == "__main__":
    data_dir = os.environ.get("data_dir", "data")
    folder_merge(data_dir)
    folder_split(data_dir)