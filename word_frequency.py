import pandas
from collections import Counter

import pickle
import os

def word_freq_pdf(page_list):
    # the input for this method is a list of list, each sublist containing all keywords from a page
    # returns Counter object
    flattened_list = [keyword for page in page_list for keyword in page]
    c = Counter(flattened_list)
    return c

def n_most_common(page_list, n):
    counts = word_freq_pdf(page_list)
    return counts.most_common(n)

if __name__ == "__main__":
    pkl_dir = os.path.join("data", "pkl")
    year = 2013
    filename = "Beigebook_20130116.pkl"
    filepath = os.path.join(pkl_dir, str(year), filename)
    word_2darray = pickle.load(open(filepath, 'rb+'))
    print(n_most_common(word_2darray, 10))