#!/usr/bin/env python3

import os
import sys
import gensim
from src.Places import MODEL_FOLDER

model_path = os.path.join(MODEL_FOLDER, 'model.gensim')
if not os.path.exists(model_path):
    print("Missing model at %s" % model_path)
    sys.exit(1)

if len(sys.argv) < 3:
    print("Please specify at least 3 words")
    sys.exit(2)
word_a = sys.argv[1].lower()
word_b = sys.argv[2].lower()
word_c = sys.argv[3].lower()

model = gensim.models.Word2Vec.load(model_path)
target_vector = model.wv.get_vector(word_b) -  model.wv.get_vector(word_a) +  model.wv.get_vector(word_c)
targets = model.similar_by_vector(target_vector, topn=4)
for target in targets:
    name, _ = target
    if name not in [word_a, word_b, word_c]:
        result = name
        break
print("%s is to %s like %s is to %s" % (word_a, word_b, word_c, result))
