#!/usr/bin/env python

import sys
import os
import re, string

def clean_text(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
    text = re.sub('[\d\n]', ' ', text)
    return text

def get_filename(filepath):
    if re.findall('[a-z]*_[a-z]*_[0-9]*(?=.txt)',filepath):
        return re.findall('[a-z]*_[a-z]*_[0-9]*(?=.txt)',filepath)[0]
    else:
        return "placeholder"
    
def main(argv):
    line = sys.stdin.readline()
    try:
        while line:
            # Get input file.
            if 'map_input_file' in os.environ:
                filename = os.environ['mapreduce_map_input_file']
            else:
                filename = "placeholder"
            
            tokens = clean_text(str(line)).split()

            for tok in tokens:
                print(filename,tok)
            line = sys.stdin.readline()
    except EOFError as error:
        return None

if __name__ == "__main__":
    main(sys.argv)

