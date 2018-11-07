#!/usr/bin/env python3

import os
import sys

import numpy as np
from scipy import stats

ALPHA = 0.05

if len(sys.argv) < 2:
    print("Please specify tow data files")
    sys.exit(1)
path_a = sys.argv[1]
path_b = sys.argv[2]

for path in [path_a, path_b]:
    if not os.path.exists(path):
        print("Cannot find input file %s" % path)
        sys.exit(2)

# Retrieve the data
def retrieve_data(path):
    data = []
    with open(path, "r") as hand:
        for line in hand:
            line = line.strip()
            if len(line) == 0 or line.startswith("#"):
                continue
            data.append(float(line))
    return data

a = retrieve_data(path_a)
b = retrieve_data(path_b)

# Welch's t-test
t, p = stats.ttest_ind(a, b, equal_var=False)
print(p)
if p < ALPHA:
    print("Samples are from different populations")
else:
    print("Seems fine")
