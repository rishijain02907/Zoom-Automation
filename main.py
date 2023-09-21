import subprocess
import pyautogui
import pandas as pd
import time
import datetime as datetime

def sign_in(meetingid,pswd):
    subprocess.call('C:\\zoom.exe')

    time.sleep(5)

    join = pyautogui.locateCenterOnScreen('join.png')
    pyautogui.moveTo(join)
    pyautogui.click()

    mid = pyautogui.locateCenterOnScreen('mid.png')
    pyautogui.moveTo(mid)
    pyautogui.click()
    pyautogui.write(meetingid)

    check = pyautogui.locateCenterOnScreen('check.png')
    for btn in check:
        pyautogui.moveTo(check)
        pyautogui.click()
        time.sleep(2)

    join2 = pyautogui.locateCenterOnScreen('join2.png')
    pyautogui.moveTo(join2)
    pyautogui.click()

    time.sleep(5)

    pswd = pyautogui.locateCenterOnScreen('pswd.png')
    pyautogui.moveTo(pswd)
    pyautogui.click()
    pyautogui.write(pswd)
    pyautogui.press('enter')

sign_in(87997565931,1234)