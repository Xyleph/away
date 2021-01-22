import pyautogui
import time

while(1):
	pyautogui.moveRel(0, 100, duration=1)
	time.sleep(5)
	pyautogui.moveRel(0, -100, duration=1)
