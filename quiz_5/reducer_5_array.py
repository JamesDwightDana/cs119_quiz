#!/usr/bin/env python
"""reducer.py"""

import sys
import numpy as np

def main(argv):
    # Get dictionary of scores.
    metadict = {}
    for line in sys.stdin:
        # split input
        temp, word, file, count = line.strip().split('\t', 3)
        # convert count to int, store in metadict if blank, add to metadict if exists.
        print(word,file,count)
        
        try:
            count = int(count)
            if file in metadict:
                if word in metadict[file]:
                    count += metadict[file][word]
                metadict[file].update({word:count})
            else:
                metadict[file] = {}
                metadict[file].update({word:count})
        except ValueError:
            pass

    #print(metadict)
    #get_TFIDF(metadict)

def get_TFIDF(dict_n):

    # get unique terms.
    def get_terms_uq(metadict):
        termset = {}
        for file in metadict:
            termset.update(metadict[file])
        return list(termset.keys())
    terms_K = get_terms_uq(dict_n)

    # Define a N (documents) by K (terms) array
    N = len(dict_n)
    nn_index = dict_n.keys()
    K = len(terms_K)
    kk_index = terms_K
    score_array = np.zeros((N,K))

    # Assign values to the array if possible.
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

if __name__ == "__main__":
    main(sys.argv)
