#!/usr/bin/env python3

import os
import re
from smart_open import smart_open

from src.Places import DATA_FOLDER
from src.Static import STOPWORDS

NONALPHABETIC = re.compile('[^-a-zA-Z]+')

def encode(charcode):
    def decorator(f):
        def wrapper(self, word):
            decoded = word.decode(charcode)
            res = f(self, decoded)
            if res is None or len(res) == 0:
                return None
            return res
        return wrapper
    return decorator

class DataCleaner:

    def __init__(self, dirname):
        self.dirname = dirname

    @encode("UTF-8")
    def cleanup(self, word):
        word = word.lower()
        if word in STOPWORDS:
            return ''
        word = word.replace("’s", "").replace("'s", "")
        # Remove non alphabetical chars
        word = NONALPHABETIC.sub('', word)
        # Ignore words shorter than 3 chars
        if len(word) < 3:
            return ''
        return word

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in smart_open(os.path.join(self.dirname, fname), 'rb'):
                words = line.split()
                cleaned = []
                for word in words:
                    word = self.cleanup(word)
                    if word is not None and len(word) > 0:
                        cleaned.append(word)
                # Cleanup
                yield cleaned

def load():
    cleaner = DataCleaner(DATA_FOLDER)
    return cleaner
