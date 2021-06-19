import numpy as np

file = r'H:/python/gtav/New folder/balanced_data_for_training9.npy'
data = np.load(file, allow_pickle=True)

print(len(data))

count = {'A': 0, 'W': 0, 'S': 0, 'D': 0, 'WA': 0, 'WD': 0, 'SA': 0, 'SD': 0, 'None': 0}
for d in data:
    if d[1] == [1, 0, 0, 0, 0, 0, 0, 0, 0]:
        count['A'] += 1
    elif d[1] == [0, 1, 0, 0, 0, 0, 0, 0, 0]:
        count['W'] += 1
    elif d[1] == [0, 0, 1, 0, 0, 0, 0, 0, 0]:
        count['S'] += 1
    elif d[1] == [0, 0, 0, 1, 0, 0, 0, 0, 0]:
        count['D'] += 1
    elif d[1] == [0, 0, 0, 0, 1, 0, 0, 0, 0]:
        count['WA'] += 1
    elif d[1] == [0, 0, 0, 0, 0, 1, 0, 0, 0]:
        count['WD'] += 1
    elif d[1] == [0, 0, 0, 0, 0, 0, 1, 0, 0]:
        count['SA'] += 1
    elif d[1] == [0, 0, 0, 0, 0, 0, 0, 1, 0]:
        count['SD'] += 1
    elif d[1] == [0, 0, 0, 0, 0, 0, 0, 0, 1]:
        count['None'] += 1

print(count)
