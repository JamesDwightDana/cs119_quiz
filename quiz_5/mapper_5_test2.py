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
    if re.findall('[0-9]*-[a-zA-Z]*(?=.txt)',filepath):
        return re.findall('[0-9]*-[a-zA-Z]*(?=.txt)',filepath)[0]
    else:
        return filepath
    
def main(argv):
    line = sys.stdin.readline()
    try:
        while line:
            # Get input file name.
            if 'mapreduce_map_input_file' in os.environ:
                filename = get_filename(os.environ['mapreduce_map_input_file'])
            elif 'map_input_file' in os.environ:
                filename = get_filename(os.environ['map_input_file'])
            else:
                filename = "placeholder"
            
            tokens = clean_text(str(line)).split()
            tokens_uq = list(set(tokens))

            # Print token + filename + count
            for tok in tokens_uq:
                print("mapper\t%s\t%s\t%s" % (tok, filename, str(tokens.count(tok))))
            
            line = sys.stdin.readline()
    except EOFError as error:
        return None

if __name__ == "__main__":
    main(sys.argv)

