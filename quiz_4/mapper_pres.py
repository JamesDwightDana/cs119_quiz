#!/usr/bin/env python
import os, sys, re, string

def load_afinn_word_list (afinn_path):
    afinn_word_list = {}
    with open(afinn_path, 'r') as file:
        for line in file:
            parts = line.decode('utf-8').strip().split('\t')
            if len(parts) == 2:
                word, score = parts
                afinn_word_list[word] = int(score)
    return afinn_word_list

afinn_path = '/home/jamesdwightdana/AFINN-en-165.txt'
afinn_word_list = load_afinn_word_list(afinn_path)

def clean_text(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
    text = re.sub('[\d\n]', ' ', text)
    return text

def calc_valence(text, afinn):
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
    pattern = re.compile("[a-zA-Z]+(?=.tar.gz)")
    try:
        while line:
            input_file = os.environ['mapreduce_map_input_file']
            for prez in pattern.findall(input_file):
                try:
                    out_val = valence(line)
                    print(prez+"\t"+str(out_val.real)+"\t"+str(out_val.imag))
                except:
                    pass
            line = sys.stdin.readline()
    except EOFError as error:
        return None

if __name__ == "__main__":
    main(sys.argv)