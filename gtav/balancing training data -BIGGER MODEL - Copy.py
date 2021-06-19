import numpy as np
import pandas as pd
import os
from collections import Counter
from random import shuffle

os.chdir(r'H:/python/gtav/training data new')

files = []

a = []
w = []
s = []
d = []
wa = []
wd = []
sa = []
sd = []
nok = []

total = 0
#{'A': 10141, 'W': 139798, 'S': 2102, 'D': 10155,
#'WA': 91927, 'WD': 90380, 'SA': 1826, 'SD': 2904, 'None': 11253}
for file in os.listdir('.'):

    datas = np.load(file, allow_pickle=True)
    
    total += len(datas)
    for data in datas:
        img = data[0]
        control = data[1]

        if control == [1, 0, 0, 0, 0, 0, 0, 0, 0]:
            for i in range(5): a.append([img, control])
        elif control == [0, 1, 0, 0, 0, 0, 0, 0, 0]:
            w.append([img, control])
        elif control == [0, 0, 1, 0, 0, 0, 0, 0, 0]:
            for i in range(25): s.append([img, control])
        elif control == [0, 0, 0, 1, 0, 0, 0, 0, 0]:
            for i in range(6): d.append([img, control])
        elif control == [0, 0, 0, 0, 1, 0, 0, 0, 0]:
            wa.append([img, control])
        elif control == [0, 0, 0, 0, 0, 1, 0, 0, 0]:
            wd.append([img, control])
        elif control == [0, 0, 0, 0, 0, 0, 1, 0, 0]:
            for i in range(25): sa.append([img, control])
        elif control == [0, 0, 0, 0, 0, 0, 0, 1, 0]:
            for i in range(25): sd.append([img, control])
        elif control == [0, 0, 0, 0, 0, 0, 0, 0, 1]:
            for i in range(6): nok.append([img, control])        

minLen = len(w)
for i in [a, w, s, d, wa, wd, sa, sd, nok]:
    shuffle(i)
    if minLen > len(i):
        minLen = len(i)
        
a = a[:minLen]
w = w[:minLen]
s = s[:minLen]
d = d[:minLen]
wa = wa[:minLen]
wd = wd[:minLen]
sa = sa[:minLen]
sd = sd[:minLen]
nok = nok[:minLen]

print(f'A: {len(a)}\nW: {len(w)}\nS: {len(s)}\nD: {len(d)}\nWA: {len(wa)}\nWD: {len(wd)}\nSA: {len(sa)}\nSD: {len(sd)}\nNoKey: {len(nok)}')

print('Starting count: ',total)
final_data = a + w + s + d + wa + wd + sa + sd + nok
shuffle(final_data)
print('Balanced data: ', len(final_data))

c = 'ALL'
np.save(f'balanced_data_for_training_{c}.npy', final_data)
