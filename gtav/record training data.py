#! python3

import numpy as np
import cv2
import time
from mss.windows import MSS as mss
import os
from controller_input import get_controller_input

sct = mss()
screen = {'left': 0,'top': 40, 'width': 1280, 'height': 700}
os.chdir(r'H:\python\gtav\training data new')

paused = True
print('Paused')

def main():
    global paused
    
    # Loading the training data
    fileNum = 1
    while True:
        fileName = f'training_data_{fileNum}.npy'
        if os.path.isfile(fileName):
            print(f'{fileName} File Exists.')
            fileNum += 1
        else:
            print(f'{fileName} does not exists, creating new training data')
            break
    
    training_data = []
    #last_time = time.time()
    
    while True:
        if not paused:
            frame = np.asarray(sct.grab(screen))
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            final_frame = cv2.resize(gray_frame, (128, 72))

            keys, pause = get_controller_input()    
            key_input = keys
            print(keys)
            training_data.append([final_frame, key_input])
            
            #print(f'Loop took {time.time() - last_time} seconds')
            #last_time = time.time()

            if len(training_data) % 500 == 0:
                print(len(training_data))
                np.save(fileName, training_data)
                print('Saving...')
            elif len(training_data) % 10001 == 0:
                print(len(training_data), 'New file creating...')
                np.save(fileName, training_data)
                print('Saving...')
                main()
                
        keys, pause = get_controller_input()
        if pause == 'Pressed':
            if not paused:
                print('Pause')
                paused = True
                time.sleep(1)
            else:
                print('Unpause')
                paused = False
                time.sleep(1)
                
if __name__ == '__main__':
    main()
