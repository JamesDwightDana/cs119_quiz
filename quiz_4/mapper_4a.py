#!/usr/bin/env python
import sys, re
import random

def main(argv):
    line = sys.stdin.readline()
    pattern1 = re.compile("[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+")
    try:
        while line:
            for address in pattern1.findall(line):
                if line.split(' ')[8]!="200":
                    print("AddressValue:" + address + "\t" + "1")
            line = sys.stdin.readline()
    except EOFError as error:
        return None

if __name__ == "__main__":
    main(sys.argv)
