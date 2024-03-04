#!/usr/bin/env python
import sys, re
import random

def main(argv):
    line = sys.stdin.readline()
    try:
        while line:
            linestring = line.strip()
            print(linestring.split('\t')[1]+"\t"+linestring.split('\t')[0])
            line = sys.stdin.readline()
    except EOFError as error:
        return None

if __name__ == "__main__":
    main(sys.argv)
