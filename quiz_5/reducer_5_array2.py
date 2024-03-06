#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys
import numpy as np

for line in sys.stdin:
    line = line.strip()
    temp, file, term, count = line.split("\t",3)
    print(file)