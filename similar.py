#!/usr/bin/env python3

import os
import sys
import gensim
from src.Places import MODEL_FOLDER

model_path = os.path.join(MODEL_FOLDER, 'model.gensim')
if not os.path.exists(model_path):
    print("Missing model at %s" % model_path)
    sys.exit(1)

if len(sys.argv) < 1:
    print("Please specify a word")
    sys.exit(2)
word = sys.argv[1].lower()

model = gensim.models.Word2Vec.load(model_path)
print(model.most_similar(word))
