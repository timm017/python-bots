import tkinter as tk
import time, pyautogui, sys

def handle_click(event):
    print("Mouse clicked at ({}, {})".format(event.x, event.y))

try:
    while True:
        time.sleep(2)
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr + "\n", end='')
except KeyboardInterrupt:
    print('\nDone.')