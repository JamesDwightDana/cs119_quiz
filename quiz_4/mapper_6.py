#!/usr/bin/env python
import sys, re
import random

def main(argv):
    line = sys.stdin.readline()
    pattern1 = re.compile("[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+")
    try:
        while line:
            if pattern1.findall(line):
                # Get Status Field, store first character (200 => 2, 299 => 2, etc)
                print("StatusCode:"+line.split(' ')[8][0] + "\t" + "1")
            line = sys.stdin.readline()
    except EOFError as error:
        return None

if __name__ == "__main__":
    main(sys.argv)
