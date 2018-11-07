#!/usr/bin/env python3

'''
Input file format
name1 name6
name2 name7
name3 name8
name4 name9
name5 name0
'''
import os
import sys

import gensim
import numpy as np

from src.Places import MODEL_FOLDER

model_path = os.path.join(MODEL_FOLDER, 'model.gensim')
if not os.path.exists(model_path):
    print("Missing model at %s" % model_path)
    sys.exit(1)

if len(sys.argv) < 1:
    print("Please specify an input file")
    sys.exit(2)
path = sys.argv[1]

if not os.path.exists(path):
    print("Cannot find input file %s" % path)
    sys.exit(3)

# Load the model
model = gensim.models.Word2Vec.load(model_path)

# Parse the file
sources = []
outputs = []
with open(path, 'r') as hand:
    for line in hand:
        line = line.strip()
        if len(line) == 0 or line.startswith("#"):
            continue
        source, out = line.split(" ")
        source = source.strip().lower()
        out = out.strip().lower()
        sources.append(source)
        outputs.append(out)

# Match
for source in sources:
    distances = model.wv.distances(source, outputs)
    best_index = np.argmin(distances)
    match = outputs[best_index]
    outputs.remove(match)
    print("%s --> %s" % (source, match))
