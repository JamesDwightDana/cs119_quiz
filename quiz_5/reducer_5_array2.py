#!/usr/bin/env python
"""reducer.py"""

import sys
import numpy as np
from operator import itemgetter

def main(argv):
    # Get dictionary of scores.
    for line in sys.stdin:
        print(str(len(line)))
    print("0")

if __name__ == "__main__":
    main(sys.argv)