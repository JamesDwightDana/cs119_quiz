#!/usr/bin/env python
import os, sys, re, string

def load_afinn_word_list (afinn_path):
    afinn_word_list = {}
    with open(afinn_path, 'r') as file:
        for line in file:
            parts = str(line).strip().split('\t')
            if len(parts) == 2:
                word, score = parts
                afinn_word_list[word] = int(score)
    return afinn_word_list

afinn_path = './AFINN-en-165.txt'
afinn_word_list = load_afinn_word_list(afinn_path)

def main(argv):
    line = sys.stdin.readline()
    pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
    try:
        while line:
            for word in pattern.findall(line):
                print ("LongValueSum:" + word.lower() + "\t" + "1")
            line = sys.stdin.readline()
    except EOFError as error:
        return None

if __name__ == "__main__":
    main(sys.argv)