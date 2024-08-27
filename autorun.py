import pyautogui
from time import sleep
pyautogui.hotkey('win','r')
pyautogui.write('cmd')
pyautogui.press('enter')
sleep(2)
pyautogui.write('You are being hacked!')
sleep(2)
pyautogui.press('win')
sleep(2)
pyautogui.write('settings')
pyautogui.press('enter')