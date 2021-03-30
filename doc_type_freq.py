import pandas
from collections import Counter
import pickle
import os
from dotenv import load_dotenv

from word_frequency import word_freq_pdf
from util import folder_check

data_dir = os.environ.get("data_dir", "data")
pkl_dir = os.environ.get("pkl_dir", "pkl")
doctype_map = pickle.load(open("doc_types.pkl", 'rb+'))
doctype_to_keyword, kw_to_doctype = doctype_map["type_to_kw"], doctype_map["kw_to_type"]

split_dir = lambda mydir: os.path.normpath(mydir).split(os.sep)

counter_obj = {}  # will initially hold pages, and then later be turned into the frequencies
counter_attr = {}  # same thing except one more layer (for example for bigrams, trigrams, each will have its own mapping)
for path, folders, files in os.walk(os.path.join(data_dir, pkl_dir)):
    # need to choose the folders with actual content in them
    if not files or path == pkl_dir or (len(files) == 1 and files[0] == ".DS_Store"):
        continue
    
    # get year and doc type
    path_parts = split_dir(path)
    len_dd, len_pd = len(split_dir(data_dir)), len(split_dir(pkl_dir))  # *insert len(pp) joke here*
    # also: I'm assuming the files are divided by year and then by doc type
    year, doctype = int(path_parts[len_dd + len_pd]), path_parts[len_dd + len_pd + 1]

    if (len(path_parts) > len_dd + len_pd + 2):  # meaning its in a subdirectory
        attribute = os.path.join(*path_parts[len_dd+len_pd+2:])
        if attribute not in counter_attr:
            counter_attr[attribute] = {}
        # get frequencies
        for fn in files:
            file_pages = pickle.load(open(os.path.join(path, fn), 'rb+'))
            if (year, doctype) not in counter_attr[attribute]:
                counter_attr[attribute][(year, doctype)] = file_pages
            else:
                counter_attr[attribute][(year, doctype)].extend(file_pages)
    else:
        # get frequencies
        for fn in files:
            file_pages = pickle.load(open(os.path.join(path, fn), 'rb+'))
            if (year, doctype) not in counter_obj:
                counter_obj[(year, doctype)] = file_pages
            else:
                counter_obj[(year, doctype)].extend(file_pages)

# count frequencies of each word
print("Parsing overall frequencies")
counter_obj = {k: word_freq_pdf(v, sticky_words=False) for k, v in counter_obj.items()}
for attr in counter_attr:
    print(f"Parsing {attr} frequencies")
    for year_doc in counter_attr[attr]:
        print(year_doc)
        # flattened_attr = [item for attr_list in counter_attr[attr][year_doc] for item in attr_list]
        counter_attr[attr][year_doc] = word_freq_pdf(counter_attr[attr][year_doc], sticky_words=True, filter_lengths=False)

# Store data
results_dir = os.environ.get("results_dir", "results")
folder_check(results_dir)
pickle.dump(counter_obj, open(os.path.join(results_dir, 'doctype_freq.pkl'), 'wb+'))
pickle.dump(counter_attr, open(os.path.join(results_dir, 'doctype_freq_attr.pkl'), 'wb+'))
print("Done!")
