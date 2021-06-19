import numpy as np
import pandas as pd
import os
from collections import Counter
from random import shuffle

os.chdir(r'H:/python/gtav/training data new')

files = []
w = []
wa = []
wd = []
#nok = []
total = 0

for file in os.listdir('.'):

    datas = np.load(file, allow_pickle=True)
    
    total += len(datas)
    for data in datas:
        img = data[0]
        control = data[1]

        if control == [0, 1, 0, 0, 0, 0, 0, 0, 0]:
            w.append([img, [0, 1, 0, 1]])   # A W D NoKey
        elif control == [0, 0, 0, 0, 1, 0, 0, 0, 0]:
            wa.append([img, [1, 0, 0, 0]])
        elif control == [0, 0, 0, 0, 0, 1, 0, 0, 0]:
            wd.append([img, [0, 0, 1, 0]])
##        elif control == [0, 0, 0, 0, 0, 0, 0, 0, 1]:
##            nok.append([img, [0, 0, 0, 1]])

w = w[:min(len(w), len(wd), len(wa))]
wa = wa[:len(w)]
wd = wd[:len(w)]

print(f'W: {len(w)}\nAW: {len(wa)}\nWD: {len(wd)}')#\nNokey: {len(nok)}')

print('Starting count: ',total)
final_data = w + wa + wd #+ nok
shuffle(final_data)
print('Balanced data: ', len(final_data))
np.save('balanced_data_for_trainingAWD.npy', final_data)
