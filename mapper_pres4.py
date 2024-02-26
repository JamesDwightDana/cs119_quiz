#!/usr/bin/env python
import os, sys, re, string

def main(argv):
    line = sys.stdin.readline()
    try:
        while line:
            input_file = os.environ['mapreduce_map_input_file']
            print(input_file)
            line = sys.stdin.readline()
    except EOFError as error:
        return None

if __name__ == "__main__":
    main(sys.argv)