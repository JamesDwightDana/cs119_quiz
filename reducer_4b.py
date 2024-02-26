#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    try:
        # parse the input we got from mapper.py
        count, word = line.split('\t', 1)
        print ('%s\t%s' % (count, word))
    except:
        pass