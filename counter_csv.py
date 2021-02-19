import csv
import pickle
import os

results_dir = os.path.join("results")

# get overall freq first 
with open(os.path.join(results_dir, "overall_freq.csv"), 'w+') as f:
    writer = csv.writer(f, delimiter=",")
    headers = ['Word', 'Count']
    writer.writerow(headers)
    data_counter = pickle.load(open(os.path.join(results_dir, "overall_freq.pkl"), 'rb+'))
    for word in data_counter:
        writer.writerow([word, data_counter.get(word)])

# yearly frequencies
with open(os.path.join(results_dir, "yearly_freq.csv"), 'w+') as f:
    writer = csv.writer(f, delimiter=",")
    headers = ['Year', 'Word', 'Count']
    writer.writerow(headers)
    data_dict = pickle.load(open(os.path.join(results_dir, "year_freq.pkl"), 'rb+'))
    for year in data_dict:
        data_counter = data_dict[year]
        for word in data_counter:
            writer.writerow([year, word, data_counter.get(word)])