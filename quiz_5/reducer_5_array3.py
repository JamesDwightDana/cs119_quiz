#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys
import numpy as np

metadict = {}
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    temp, file, word, count = line.split('\t', 3)

    try:
        count = int(count)
    except ValueError:
        continue

    if file in metadict:
        if word in metadict[file]:
            count += metadict[file][word]
        metadict[file].update({word:count})
    else:
        metadict[file] = {}
        metadict[file].update({word:count})

def get_TFIDF(dict_n):

    def get_terms_uq(dict):
        termset = {}
        for file in dict:
            termset.update(dict[file])
            return list(termset.keys())
    
    terms_K = get_terms_uq(dict_n)

    N = len(dict_n)
    nn_index = dict_n.keys()
    K = len(terms_K)
    kk_index = terms_K
    score_array = np.zeros((N,K))

    for nn, file in enumerate(nn_index):
        for kk, term in enumerate(kk_index):
            try:
                score_array[nn][kk] = dict_n[file][term]
            except:
                pass

    print(score_array)