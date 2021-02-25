import pyautogui

pyautogui.screenshot('.\\GUI\\example.png')


# print(pyautogui.locateOnScreen('.\\GUI\\calc7key.png'))
# This grab the center of the image aka 7 of the calculator
location = pyautogui.locateCenterOnScreen('.\\GUI\\calc7key.png')

pyautogui.moveTo(location, duration=1)
pyautogui.click(location)