import pyautogui as keyboardController
import time as actionController
from datetime import datetime

prefix = "$"
action = "work"
cooldown = 30

actionController.sleep(2)

def trigger():
    keyboardController.typewrite(f"{prefix}{action}")
    keyboardController.press("enter")
    current_time = datetime.now().strftime("[%H:%M:%S]")
    print(f"{current_time} Triggered {action} command!")
    actionController.sleep(0.7)
    keyboardController.typewrite(f"{prefix}deposit all")
    keyboardController.press("enter")
    current_time = datetime.now().strftime("[%H:%M:%S]")
    print(f"{current_time} Triggered deposit all command!")
    

while True:
    trigger()
    actionController.sleep(cooldown)
