#!/usr/bin/env python
"""reducer.py"""

import sys
import numpy as np

def main(argv):
    # Get dictionary of scores.
    for line in sys.stdin:
        line = line.strip()
        print(line)
    
if __name__ == "__main__":
    main(sys.argv)