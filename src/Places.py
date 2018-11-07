#!/usr/bin/env python3

import os

filename = os.path.realpath(__file__)
src_folder = os.path.dirname(filename)
MAIN_FOLDER = os.path.dirname(src_folder)
DATA_FOLDER = os.path.join(MAIN_FOLDER, 'data')
MODEL_FOLDER = os.path.join(MAIN_FOLDER, 'model')
