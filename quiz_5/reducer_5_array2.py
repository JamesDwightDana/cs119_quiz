#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys
import numpy as np

def main(argv):
    # Get dictionary of scores.
    for line in sys.stdin:
        try:
            line = line.strip()
            print(line)
        except:
            continue

if __name__ == "__main__":
    main(sys.argv)