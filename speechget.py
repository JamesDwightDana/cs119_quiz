#!/usr/bin/env python
import sys, re, string
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

if __name__ == "__main__":
    print(afinn_word_list)