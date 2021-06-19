import numpy as np
import pandas as pd
import cv2
from collections import Counter
from random import shuffle
import os

os.chdir(r'H:\python\gtav\training data new - Copy')

files = []

for file in os.listdir('.'):
    files.append(np.load(file, allow_pickle=True))

counter_dict = {'A': 0, 'W': 0, 'S': 0, 'D': 0, 'WA': 0, 'WD': 0, 'SA': 0, 'SD': 0, 'None': 0}

for np_file in files:
    # for data in np_file:
    df = pd.DataFrame(np_file)
    count = dict(Counter(df[1].apply(str)))
    for inpt in count:
        if inpt == '[1, 0, 0, 0, 0, 0, 0, 0, 0]':
            counter_dict['A'] += count[inpt]
        elif inpt == '[0, 1, 0, 0, 0, 0, 0, 0, 0]':
            counter_dict['W'] += count[inpt]
        elif inpt == '[0, 0, 1, 0, 0, 0, 0, 0, 0]':
            counter_dict['S'] += count[inpt]
        elif inpt == '[0, 0, 0, 1, 0, 0, 0, 0, 0]':
            counter_dict['D'] += count[inpt]
        elif inpt == '[0, 0, 0, 0, 1, 0, 0, 0, 0]':
            counter_dict['WA'] += count[inpt]
        elif inpt == '[0, 0, 0, 0, 0, 1, 0, 0, 0]':
            counter_dict['WD'] += count[inpt]
        elif inpt == '[0, 0, 0, 0, 0, 0, 1, 0, 0]':
            counter_dict['SA'] += count[inpt]
        elif inpt == '[0, 0, 0, 0, 0, 0, 0, 1, 0]':
            counter_dict['SD'] += count[inpt]
        elif inpt == '[0, 0, 0, 0, 0, 0, 0, 0, 1]':
            counter_dict['None'] += count[inpt]

print(counter_dict)
#[[ [[1 2 3 5 4 2 ...], [0 1 0 1 0 1]] ]]