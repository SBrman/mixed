import os
os.environ["PYSDL2_DLL_PATH"] = r"C:\Users\Simanta\AppData\Local\Programs\Python\Python38\Lib\site-packages\sdl2"
import time
import ctypes
from sdl2 import *


class Joystick:
    def __init__(self):
        SDL_Init(SDL_INIT_JOYSTICK)
        self.axis = {0: 0, 4: -32000, 5: -32000, 9: 0}
        self.button = {5: ''}

    def update(self):
        event = SDL_Event()
        while SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == SDL_JOYDEVICEADDED:
                self.device = SDL_JoystickOpen(event.jdevice.which)
            elif event.type == SDL_JOYAXISMOTION:
                self.axis[event.jaxis.axis] = event.jaxis.value
            elif event.type == SDL_JOYBUTTONDOWN:
                self.button[event.jbutton.button] = True
            elif event.type == SDL_JOYBUTTONUP:
                self.button[event.jbutton.button] = False
                

joystick = Joystick()

def get_controller_input():
    joystick.update()
    keys = joystick.axis
    button = joystick.button      
    pause = 'Not Pressed'

    '''
    Convert keys to a ...multi-hot... array
     0  1  2  3  4   5   6   7    8
    [A, W, S, D, WA, WD, SA, SD, NOKEY] boolean values.
    '''
    output = [0,0,0,0,0,0,0,0,0]
    
    if button[5] == True:
        pause = 'Pressed'  
    elif keys[5] > -32000 and keys[0] < -1000:#WA
        output[4] = 1
    elif keys[5] > -32000 and keys[0] > 1000:#WD
        output[5] = 1
    elif keys[4] > -32000 and keys[0] < -1000:#SA
        output[6] = 1
    elif keys[4] > -32000 and keys[0] > 1000:#SD
        output[7] = 1
    elif keys[5] > -32000:#W
        output[1] = 1
    elif keys[4] > -32000:#S
        output[2] = 1
    elif keys[0] > 1000:#D
        output[3] = 1
    elif keys[0] < -1000:#A
        output[0] = 1
    else:
        output[8] = 1
    return output, pause
