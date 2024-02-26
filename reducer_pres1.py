#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_key = None
current_value = 0
key = None

# input comes from STDIN
for line in sys.stdin:
    print(line)