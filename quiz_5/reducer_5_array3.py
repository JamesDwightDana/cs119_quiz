#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys
import functools
import math

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
        tf = dict.fromkeys(wordkeys,0)
        # Get total count of document.
        total = sum(dict_1.values())
        # Update with counts.
        for key in dict_1.keys():
            tf[key] = dict_1[key]/total
        return tf
    return {file:get_TF_per_dict(wordkeys,dict_n[file]) for file in dict_n.keys()}

# Function to get 
def get_IDF(wordkeys, dict_n):
    N = len(dict_n)
    # List of lists of unique words per document.
    dict_1n = [list(set(dict_n[file])) for file in dict_n.keys()]
    # Combine list of lists.
    list_of_words = list(functools.reduce(lambda x,y: x+y, dict_1n))
    # Get dict based on keys
    idf_dict = {}
    for key in wordkeys:
        idf_count = list_of_words.count(key)
        idf_dict[key] = math.log((1+N)/(1+idf_count))+1
    return idf_dict

# Term frequency is an N by K dictionary, where K is the total key count.
tf_dict = get_TF(term_keys, metadict)
# IDF is a K sized dictionary.
idf_dict = get_IDF(term_keys, metadict)

for term in term_keys:
    print(term)