import re
from collections import Counter

import os
import urllib.request
def download_txt(link, filename):
    if not os.path.exists(filename):
        with urllib.request.urlopen(link) as f:
            html = f.read().decode('utf-8')
            with open(filename, 'w+') as big:
                big.writelines(html)
data_dir = os.path.join("data")
word_corpus_fn = os.path.join(data_dir, 'big.txt')
download_txt('http://norvig.com/big.txt', word_corpus_fn)

# sauce: https://stackoverflow.com/questions/195010/how-can-i-split-multiple-joined-words/481773#481773
# this method segments text into words
def viterbi_segment(text):
    probs, lasts = [1.0], [0]
    for i in range(1, len(text) + 1):
        prob_k, k = max((probs[j] * word_prob(text[j:i]), j)
                        for j in range(max(0, i - max_word_length), i))
        probs.append(prob_k)
        lasts.append(k)
    words = []
    i = len(text)
    while 0 < i:
        words.append(text[lasts[i]:i])
        i = lasts[i]
    words.reverse()
    return words, probs[-1]

def word_prob(word): return dictionary[word] / total
def words(text): return re.findall('[a-z]+', text.lower())
dictionary = Counter(words(open(word_corpus_fn).read()))
max_word_length = max(map(len, dictionary))
total = float(sum(dictionary.values()))