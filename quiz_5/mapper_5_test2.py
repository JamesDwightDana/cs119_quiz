#!/usr/bin/env python

import sys
import os
import re, string

#import requests
#stopwords_list = requests.get("https://gist.githubusercontent.com/rg089/35e00abf8941d72d419224cfd5b5925d/raw/12d899b70156fd0041fa9778d657330b024b959c/stopwords.txt").content
#tokens_irrel = set(stopwords_list.decode().splitlines()) 

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
            if 'mapreduce_map_input_file' in os.environ:
                filename = get_filename(os.environ['mapreduce_map_input_file'])
            else:
                filename = "placeholder"
            
            tokens = re.findall('[a-z]+',clean_text(str(line)))
            for tok in tokens:
                print(filename,tok)
            
            line = sys.stdin.readline()
    except EOFError as error:
        return None

if __name__ == "__main__":
    main(sys.argv)

