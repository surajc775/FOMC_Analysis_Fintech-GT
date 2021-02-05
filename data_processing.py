import pdfplumber
import pickle
import os
import re

from util import folder_check

def pdfToList(filename):
    with pdfplumber.open(filename) as pdf:
        data = [page.extract_text() for page in pdf.pages]
        return data

def text_cleaner(filename, text_list):
    lc_filename = filename.lower()
    return [page for page in text_list if len(re.split('\W+', page)) >= 50 and not "TABLE OF CONTENTS" in page]  # gotta make sure there's like actual words on it

if __name__ == "__main__":
    source_dir = os.path.join("data")
    pdfs_dirname = "pdfs"
    pkl_dirname = "pkl"
    data_dir = os.path.join(source_dir, pdfs_dirname)
    pickle_dir = os.path.join(source_dir, pkl_dirname)
    folder_check(pickle_dir)
    for file_tuple in os.walk(data_dir):
        if not file_tuple[2]:
            continue
        curr_dir = file_tuple[0]
        dir_parts = file_tuple[0].rsplit("/", 2)
        pkl_file_base = os.path.join(dir_parts[0], pkl_dirname, dir_parts[2])
        folder_check(pkl_file_base)
        for filename in file_tuple[2]:
            print(f"Parsing {filename}")
            text = pdfToList(os.path.join(curr_dir, filename))
            pkl_name = os.path.join(pkl_file_base, filename.rsplit(".", 1)[0] + ".pkl")
            pickle.dump(text, open(pkl_name, "wb+"))