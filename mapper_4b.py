#!/usr/bin/env python
import sys, re
import random

def main(argv):
    line = sys.stdin.readline()
    try:
        while line:
            word, count = line.split('\t', 1)
            print(count+"\t"+word)
            line = sys.stdin.readline()
    except EOFError as error:
        return None

if __name__ == "__main__":
    main(sys.argv)
