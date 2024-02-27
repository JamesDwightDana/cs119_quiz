#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_key = None
current_value = 0
current_count = 0
key = None


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    key, value = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        value = float(value)
    except ValueError:
        # ignore/discard this line
        continue
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_key == key:
        current_value += value
        current_count += 1
    else:
        if current_key:
            # write result to STDOUT
            print ('%s\t%s\t%s' % (current_key, current_value, current_count))
        current_value = value
        current_key = key
        current_count = 0

# do not forget to output the last word if needed!
if current_key == key:
    print ('%s\t%s\t%s' % (current_key, current_value, current_count))
