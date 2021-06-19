#! python3

import time
import cv2
import numpy as np
from numba import njit

SCALE = 1000
WIDTH, HEIGHT = 100, 100
PXSTEP = 1000 // WIDTH


def count(data, x, y):
    c = 0
    dirs = [-1, 0, 1]
    for i in dirs:
        for j in dirs:
            try:
                c += data[x + i][y + j]
            except IndexError:
                return 0
                
    return c


def dret(data):
    cell = data.copy()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            alive = count(data, x, y)
            if data[x][y]:
                alive -= 1
                if alive < 2 or alive > 3:
                    cell[x][y] = 0
            else:
                if alive == 3:
                    cell[x][y] = 1
    return cell


def draw_grid(img, line_color=(255, 255, 255), thickness=1, type_=cv2.LINE_AA, pxstep=PXSTEP):
    x = pxstep
    y = pxstep
    while x < img.shape[1]:
        cv2.line(img, (x, 0), (x, img.shape[0]), color=line_color, lineType=type_, thickness=thickness)
        x += pxstep

    while y < img.shape[0]:
        cv2.line(img, (0, y), (img.shape[1], y), color=line_color, lineType=type_, thickness=thickness)
        y += pxstep


def show_photo(data, tt):
    img1 = cv2.resize(data, (SCALE, SCALE), interpolation=cv2.INTER_NEAREST)
    time.sleep(tt)
    draw_grid(img1)
    cv2.imshow('conway', 1-img1)


def onMouse(event, x, y, flags, param):
    global img, lmbDown, rmbDown

    if event == cv2.EVENT_LBUTTONDOWN:
        lmbDown = True
    elif event == cv2.EVENT_LBUTTONUP:
        lmbDown = False

    if event == cv2.EVENT_RBUTTONDOWN:
        rmbDown = True
    elif event == cv2.EVENT_RBUTTONUP:
        rmbDown = False
        
    if event == cv2.EVENT_MOUSEMOVE:
        xs, ys = x//PXSTEP, y//PXSTEP
        try:
            if lmbDown:
                img[ys][xs] = 1
            elif rmbDown:
                img[ys][xs] = 0
        except IndexError:
            return
    
    grid = cv2.resize(img, (SCALE, SCALE), interpolation=cv2.INTER_NEAREST)
    cv2.imshow('conway', 1 - grid)

def draw_on(img):
    grid = cv2.resize(img, (SCALE, SCALE), interpolation=cv2.INTER_NEAREST)
##    cv2.namedWindow('conway')
    cv2.imshow('conway', 1 - grid)
    cv2.setMouseCallback('conway', onMouse)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':

##    img = np.random.randint(0, 2, size=(WIDTH, HEIGHT)).astype(float)
    lmbDown, rmbDown = False, False
    img = np.zeros(shape=(WIDTH, HEIGHT)).astype(float)
    draw_on(img)

    for i in range(1000):
        img = dret(img)
        show_photo(img, 1e-5)
        
        if cv2.waitKey(1) & 0xff in [27, ord('q')] or cv2.getWindowImageRect('conway')[0] == -1:
            cv2.destroyAllWindows()
            break
