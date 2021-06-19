import numpy as np
import cv2
import os

data = np.load(r'H:/python/gtav/balanced_training_data/balanced_data_for_training.npy', allow_pickle=True)

for d in data:    
    frame = d[0]
    key_input = d[1]
    print(key_input)
    cv2.imshow('Window', cv2.resize(frame, (1280,720)))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
