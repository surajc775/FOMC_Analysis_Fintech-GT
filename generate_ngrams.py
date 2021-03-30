# Author: Alex Liu
# Purpose: Generate n-grams of all words in the original files

import nltk
from nltk import bigrams, trigrams, ngrams

import pickle
import os
from dotenv import load_dotenv
load_dotenv(".env")
data_dir = os.environ.get("data_dir", "data")
pkl_dir = os.environ.get("pkl_dir", "pkl")

from util import folder_check

if __name__ == "__main__":
    for path, folders, files in os.walk(os.path.join(data_dir, pkl_dir)):
        if not files or (len(files) < 2 and files[0][0] == "."):
            continue
        print(path)
        folder_check(os.path.join(path, "bigram"))
        folder_check(os.path.join(path, "trigram"))
        for file in files:
            fn = file.split(".")[0]
            pages = pickle.load(open(os.path.join(path, file), "rb+"))
            # bigrams
            fn_bigrams = [[g for g in bigrams(page)] for page in pages]
            bigrams_file = os.path.join(path, "bigram", f"{fn}_bigrams.pkl")
            pickle.dump(fn_bigrams, open(bigrams_file, "wb+"))
            # trigrams
            fn_trigrams = [[g for g in trigrams(page)] for page in pages]
            trigrams_file = os.path.join(path, "trigram", f"{fn}_trigrams.pkl")
            pickle.dump(fn_trigrams, open(trigrams_file, "wb+"))
        