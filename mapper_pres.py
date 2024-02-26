#!/usr/bin/env python
import os, sys, re, string
import requests

def load_afinn_word_list (afinn_path):
    afin_data = requests.get(afinn_path)
    afin_lines = afin_data.content.decode("utf-8").splitlines()

    afinn_word_list = {}
    for line in afin_lines:
        parts = str(line).strip().split('\t')
        if len(parts) == 2:
            word, score = parts
            afinn_word_list[word] = int(score)
    return afinn_word_list

afinn_path = 'https://raw.githubusercontent.com/fnielsen/afinn/master/afinn/data/AFINN-en-165.txt'
afinn_word_list = load_afinn_word_list(afinn_path)

def clean_text(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
    text = re.sub('[\d\n]', ' ', text)
    return text

def calc_valence(text, afinn):
    #
    # Write your program here
    #
    words = text.split()
    val = (0+0j)
    for word in words:
        try:
            val += complex(afinn[word], 1)
        except:
            pass
    return val 

def valence(text):
    return calc_valence(clean_text(text), afinn_word_list)

def main(argv):
    line = sys.stdin.readline()
    pattern = re.compile("[a-z]+(?=_speech)")
    try:
        while line:
            current_file = os.environ['mapreduce_map_input_file']
            print("Test\t1")
            line = sys.stdin.readline()
    except EOFError as error:
        return None

if __name__ == "__main__":
    main(sys.argv)