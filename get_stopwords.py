#!/usr/bin/env python

import nltk
import nltk.corpus
from nltk.corpus import stopwords
nltk.download('stopwords')

stopwords = stopwords.words('english')

with open('inaug_stopwords', 'w') as writer:
    for word in stopwords:
        writer.writelines(word+"\n")