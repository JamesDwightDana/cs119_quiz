#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_file = None
current_count = 0

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    temp, file, word, count = line.split('\t', 3)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_file == file:
        current_count += count
    else:
        if current_file:
            print ('%s\t%s' % (current_file, current_count))
        current_file = file
        current_count = count

if current_file == file:
    print('%s\t%s' % (current_file, current_count))