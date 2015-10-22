#!/usr/bin/env python

"""Example of TFIDF in Python
This script demonstrates TFIDF cosine similarity in python.
"""

import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer

stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)


def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''


def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')


def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0, 1]

print cosine_sim('a little bird', 'a little bird')
print cosine_sim('a little bird', 'a little bird chirps')
print cosine_sim('a little bird', 'a big dog barks')
