#!/usr/bin/env python
import sys, re
import random

def main(argv):
    line = sys.stdin.readline()
    pattern1 = re.compile("[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+")
    try:
        while line:
            # Typical Line?
            if pattern1.findall(line):
                # Print COMMAND + 1
                print(line.split(' ')[5][1:]+"\t"+"1")
            line = sys.stdin.readline()
    except EOFError as error:
        return None

if __name__ == "__main__":
    main(sys.argv)
