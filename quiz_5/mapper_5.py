#!/usr/bin/env python

import sys
import os
import re, string

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
# Load Stopwords
tokens_irrel = set(stopwords.words('english'))

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
        return "NA"
    
def main(argv):
    line = sys.stdin.readline()
    try:
        while line:
            # Get input file.
            filepath = os.environ['mapreduce_map_input_file']
            filename = get_filename(filepath)

            # Get cleaned words from line (duplicates exist)!
            tokens = nltk.word_tokenize(clean_text(line))

            # Get unique, relevant tokens
            #    In Python:   set A - set B  = {elements in A that aren't in B}
            tokens_uq = list(set(tokens)-tokens_irrel)

            # Print token + filename + count
            for tok in tokens_uq:
                print("mapper5\t%s\t%s\t%s" % (tok, filename, tokens.count(tok)))
            line = sys.stdin.readline()
    except EOFError as error:
        return None

if __name__ == "__main__":
    main(sys.argv)

