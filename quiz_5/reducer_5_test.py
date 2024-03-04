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
    print(metadict)

if __name__ == "__main__":
    main(sys.argv)
