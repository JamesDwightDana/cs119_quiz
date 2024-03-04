#!/usr/bin/env python
"""reducer.py"""

# python mapper.py < input.txt | sort | python reducer.py
# hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input /user/inputs/inaugs.tar.gz -output /user/j_singh/inaugs

from operator import itemgetter
import sys
import numpy as np
import functools

def main(argv):
    metadict = {}
    for line in sys.stdin:
        # split input
        temp, word, file, count = line.strip().split('\t', 3)
        # convert count to int, store in metadict if blank, add to metadict if exists.
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
    get_TFIDF(metadict)

def get_TFIDF(dict_n):
    # Setup
    def get_wordkeys(metadict):
        wordset = {}
        for file in metadict:
            wordset.update(metadict[file])
        return list(wordset.keys())
    wordkeys = get_wordkeys(dict_n)

    # Function to get Term Frequency per document.
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
            idf_dict[key] = np.log((1+N)/(1+idf_count))+1
        return idf_dict
    
    # Term frequency is an N by K dictionary, where K is the total key count.
    tf_dict = get_TF(wordkeys, dict_n)
    # IDF is a K sized dictionary.
    idf_dict = get_IDF(wordkeys, dict_n)

    tfidf_dict = {}
    for file in dict_n:
        tfidf_dict[file] = {}
        for key in wordkeys:
            tfidf_dict[file][key] = tf_dict[file][key]*idf_dict[key]
    
    # Output the TF.IDF values
    for file in sorted(dict_n):
        print ('\n\nSPEECH:', file)
        sorted_tfidf_dict = dict(sorted(tfidf_dict[file].items(), key = lambda item: item[1], reverse = True))
        # Print tokens + scores.
        for token in sorted_tfidf_dict:
            print (token, sorted_tfidf_dict[token])

if __name__ == "__main__":
    main(sys.argv)
