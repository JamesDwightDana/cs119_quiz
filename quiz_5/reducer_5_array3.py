#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys
import math
import itertools

metadict = {}
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    temp, file, word, count = line.split('\t', 3)

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
        continue

def get_terms_uq(metadict):
    termset = {}
    for file in metadict:
        termset.update(metadict[file])
    return list(termset.keys())

term_keys = get_terms_uq(metadict)

# Function to get Term Frequency per document/term.
def get_TF(wordkeys, dict_n):
    def get_TF_per_dict(wordkeys,dict_1):
        # {key: 0} for all keys
        tf = dict.fromkeys(wordkeys,float(0))
        # Get total count of document.
        total = float(sum(dict_1.values()))
        # Update with counts.
        for key in dict_1.keys():
            tf[key] = dict_1[key]/total
        return tf
    return {file:get_TF_per_dict(wordkeys,dict_n[file]) for file in dict_n}

# Term frequency is an N by K dictionary, where K is the total key count.
tf_dict = get_TF(term_keys, metadict)

# Function to get 
def get_IDF(wordkeys, dict_n):
    N = len(dict_n)
    # List of lists of unique words per document.
    dict_1n = [list(set(dict_n[file])) for file in dict_n.keys()]
    # Combine list of lists.
    list_of_words = list(itertools.chain.from_iterable(dict_1n))
    # Get dict based on keys
    idf_dict = {}
    for key in wordkeys:
        idf_count = list_of_words.count(key)
        idf_dict[key] = math.log((1+N)/(1+idf_count))+1
    return idf_dict

# IDF is a K sized dictionary.
idf_dict = get_IDF(term_keys, metadict)

# Combine elements of TF and IDF
tfidf_dict = {}
for file in metadict:
    tfidf_dict[file] = {}
    for key in term_keys:
        tfidf_dict[file][key] = format(tf_dict[file][key]*idf_dict[key],".5f")

for file in sorted(tfidf_dict):
    subdict = tfidf_dict[file]

    unsorted_keys = list(subdict.keys())
    unsorted_values = list(subdict.values())
    sorted_values, sorted_keys  = zip(*sorted(zip(unsorted_values,unsorted_keys),reverse=True))

    print("\n\n"+file)
    for ii, key in enumerate(sorted_keys):
        if float(sorted_values[ii])>0.0:
            print(key+"\t"+sorted_values[ii])