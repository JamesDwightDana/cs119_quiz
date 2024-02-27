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
    key, value, count = line.split('\t', 2)

    # convert count (currently a string) to int
    try:
        value = float(value)
    except ValueError:
        continue

    try:
        count = float(count)
    except ValueError:
        continue
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_key == key:
        current_value += value
        current_count += count
    else:
        if current_key:
            # write result to STDOUT
            try:
                average_value = round(current_value/current_count,4)
                print ('%s\t%s' % (current_key, average_value))
            except:
                pass
        current_value = value
        current_key = key
        current_count = count

# do not forget to output the last word if needed!
if current_key == key:
    # write result to STDOUT
    try:
        average_value = round(current_value/current_count,4)
        print ('%s\t%s' % (current_key, average_value))
    except:
        pass