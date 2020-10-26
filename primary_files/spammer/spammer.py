import pyautogui, time

time.sleep(15)

f = open("spam.txt")

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

f.close()