#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys
import numpy

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

kk_index = get_terms_uq(metadict)
K = len(kk_index)

for key in kk_index:
    print(key)