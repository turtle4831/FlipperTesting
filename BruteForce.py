import pyautogui
import time
pyautogui.hotkey("win","R")
pyautogui.hotkey("enter")
i = 0 
while True:
  pyautogui.typewrite(str(i), interval=0.02)
  pyautogui.hotkey("enter")
  i += 0 
  if i > 9999:
    break
  
