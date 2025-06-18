# THIS CAN ACTUALLY BAN YOU FROM SERVERS OR EVEN FROM DISCORD
# USE AT YOUR OWN RISK.

import pyautogui as keyboardController
import time as actionController
from InquirerPy import prompt
from datetime import datetime

prefix = "$"
action = "work"
cooldown = 2
deposit = True # Set False if you don't want to deposit items after working
commandLimit = 2 # You can limit it by putting another number, 0 will be infinite.

actionController.sleep(2)

i = 0
def trigger():
    global i
    keyboardController.typewrite(f"{prefix}{action}")
    keyboardController.press("enter")
    current_time = datetime.now().strftime("[%H:%M:%S]")
    print(f"{current_time} Triggered {action} command!")
    actionController.sleep(0.7)
    if deposit:
        keyboardController.typewrite(f"{prefix}deposit all")
        keyboardController.press("enter")
        current_time = datetime.now().strftime("[%H:%M:%S]")
        print(f"{current_time} Triggered deposit all command!")
    i += 1
    if commandLimit > 0 and i == commandLimit:
        print(f"{current_time} Command limit reached, stopping.")
        questions = [
            {
                "type": "list",
                "message": "Press Enter to leave",
                "choices": ["Leave"],
                "name": "userInput1"
            }
        ]   
        result = prompt(questions)
        exit()


while True:
    trigger()
    actionController.sleep(cooldown)
