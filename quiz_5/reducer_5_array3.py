#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys
import numpy as np

def get_TFIDF(dict_n):

    def get_terms_uq(dict):
        termset = {}
        for file in dict:
            termset.update(dict[file])
            return list(termset.keys())
    terms_K = get_terms_uq(dict_n)

    # Define a N (documents) by K (terms) array
    N = len(dict_n)
    nn_index = dict_n.keys()
    K = len(terms_K)
    kk_index = terms_K
    score_array = np.zeros((N,K))

    # Assign dict values to array.
    for nn, file in enumerate(nn_index):
        for kk, term in enumerate(kk_index):
            try:
                score_array[nn][kk] = dict_n[file][term]
            except:
                pass
    
    # Now, rely on matrix/array functionality to calculate efficiently.
    # Iterating on the array row (file name), get score/total score. Result is still N by K
    tf_array = np.array(
        list(
            map(lambda x: x/sum(x), score_array)
        )
    )

    # sum(score_array!=0) gets the unique count of each term (column).
    # then apply functions to that (1,K) array.
    idf_array = np.array(
        np.log(
            (1 + N) / (1 + sum(score_array!=0))
        ) + 1
    )

    # Multiplying (N,K) by (1,K) lets us broadcast the values.
    tfidf_array = tf_array*idf_array

    # Finally, get ranking and print to stdout by that ranking.
    for nn, file in enumerate(nn_index):
        # Get list of indices, and reverse them.
        sorted_index = list(np.argsort(tfidf_array[nn]))
        sorted_index.reverse()

        # print file, score, and term to stdout
        for ii in sorted_index:
            print(file,tfidf_array[nn][ii],terms_K[ii],sep="\t")

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
get_TFIDF(metadict)
