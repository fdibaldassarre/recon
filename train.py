#!/usr/bin/env python3

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

import gensim
from tempfile import mkstemp

from src import DataCleaner
from src.Places import MODEL_FOLDER

# Training settings
MIN_WORD_COUNT = 10

# Machine-dependant optimization settings
WORKERS = 4

sentences = DataCleaner.load()
model = gensim.models.Word2Vec(sentences, min_count=MIN_WORD_COUNT, workers=WORKERS)
fs, temp_path = mkstemp(suffix=".gensim", prefix="model-", dir=MODEL_FOLDER)
model.save(temp_path)
