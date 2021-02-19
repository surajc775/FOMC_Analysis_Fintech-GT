import pandas
from collections import Counter
import pickle
import os

from viterbi import viterbi_segment

def word_freq_pdf(page_list):
    # the input for this method is a list of list, each sublist containing all keywords from a page
    # returns Counter object
    parsed_words = [viterbi_segment(keyword)[0] for page in page_list for keyword in page]
    flattened_list = [word for arr in parsed_words for word in arr]  # run viterbi algo on the list and flatten again
    flattened_list = [w for w in flattened_list if len(w) >= 3]
    c = Counter(flattened_list)
    return c

def n_most_common(page_list, n):
    counts = word_freq_pdf(page_list)
    return counts.most_common(n)

# on second thought maybe loading this with numpy would be faster, buuuuuuut
if __name__ == "__main__":
    pkl_dir = os.path.join("data", "pkl")
    big_word_bank = []
    year_data = {}
    for file_tuple in os.walk(pkl_dir):
        if not file_tuple[2] or file_tuple[0] == pkl_dir:
            continue
        year = int(file_tuple[0].rsplit("/", 1)[-1])
        all_docs = [pickle.load(open(os.path.join(file_tuple[0], fn), 'rb+')) for fn in file_tuple[2]]
        # flatten the array
        all_docs = [arr for array2d in 
        all_docs for arr in array2d]
        big_word_bank.extend(all_docs)
        year_data[year] = word_freq_pdf(all_docs)
    overall_freq = word_freq_pdf(big_word_bank)

    # Store data
    results_dir = "results"
    pickle.dump(year_data, open(os.path.join(results_dir, 'year_freq.pkl'), 'wb+'))
    pickle.dump(overall_freq, open(os.path.join(results_dir, 'overall_freq.pkl'), 'wb+'))
