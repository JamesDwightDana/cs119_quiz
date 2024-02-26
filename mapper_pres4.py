#!/usr/bin/env python
import os, sys, re, string

def main(argv):
    try:
        while line:
            input_file = os.environ['mapreduce_map_input_file']
            cleaned = re.sub("[^a-zA-Z]+",'',input_file)
            print(cleaned+"\t"+"1")
            line = sys.stdin.readline()
    except EOFError as error:
        return None

if __name__ == "__main__":
    main(sys.argv)