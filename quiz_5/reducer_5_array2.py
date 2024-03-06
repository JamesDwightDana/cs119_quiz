#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys
import numpy as np

for line in sys.stdin:
    try:
        line = line.strip()
        print(line)
    except:
        continue