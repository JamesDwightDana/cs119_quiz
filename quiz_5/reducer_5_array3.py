#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_file = None
current_count = 0

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
        
print(metadict)