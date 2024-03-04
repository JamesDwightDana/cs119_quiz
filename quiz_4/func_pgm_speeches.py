#!/usr/bin/env python
import sys, re, string

def load_afinn_word_list (afinn_path):
    afinn_word_list = {}
    with open(afinn_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                word, score = parts
                afinn_word_list[word] = int(score)
    return afinn_word_list

afinn_path = "../afinn/afinn/data/AFINN-en-165.txt"
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

def func_pgm_speeches(argv):
    valence_sum_count = (0+0j)
    valence_sum_count += valence("In the presence of this vast assemblage of my countrymen I am about to supplement and seal by the oath which I shall take the manifestation of the will of a great and free people. In the exercise of their power and right of self-government they have committed to one of their fellow-citizens a supreme and sacred trust, and he here consecrates himself to their service.")
    print ("long line 1 valence", valence_sum_count.real/valence_sum_count.imag)

    valence_sum_count += valence("This impressive ceremony adds little to the solemn sense of responsibility with which I contemplate the duty I owe to all the people of the land. Nothing can relieve me from anxiety lest by any act of mine their interests may suffer, and nothing is needed to strengthen my resolution to engage every faculty and effort in the promotion of their welfare.")
    print ("long line 1&2 valence", valence_sum_count.real/valence_sum_count.imag)

    valence_sum_count += valence("Amid the din of party strife the people’s choice was made, but its attendant circumstances have demonstrated anew the strength and safety of a government by the people. In each succeeding year it more clearly appears that our democratic principle needs no apology, and that in its fearless and faithful application is to be found the surest guaranty of good government.")
    print ("long line 1&2&3 valence", valence_sum_count.real/valence_sum_count.imag)

    valence_sum_count = (0+0j)
    #with open("./cleveland/cleveland_speeches_000.txt", 'r', encoding='utf-8') as file:
    #    for line in file:
    #        valence_sum_count += valence(line)
    #        print ("./cleveland/cleveland_speeches_000.txt", line, valence_sum_count)
    #    print ("./cleveland/cleveland_speeches_000.txt", valence_sum_count.real/valence_sum_count.imag)

if __name__ == "__main__":
    func_pgm_speeches(sys.argv)

