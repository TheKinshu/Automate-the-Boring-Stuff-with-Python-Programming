# pip install pyautogui

import pyautogui

print(pyautogui.size())

width, height = pyautogui.size()

print(pyautogui.position())

pyautogui.moveTo(10, 10, duration=1.5)

pyautogui.moveRel(200,0, duration=1.5)

pyautogui.moveRel(0, 100, duration=1)

# Somethings you can do with click is changed what you do with the mouse
# rightClick, middleClick, or run click without the position
# dragTo, dragRel drags the mouse to the location
pyautogui.click(pyautogui.position())

# This tracks the position of the mouse
# import pyautogui
# pyatogui.displayMousePosition()