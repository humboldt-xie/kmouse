import pyautogui

import keyboard
i=0

def on_press(e):
    global i
    x,y=pyautogui.position()
    if e.name=='a':
        pyautogui.moveTo(x-10, y)
    if e.name=='d':
        pyautogui.moveTo(x+10, y)
    if e.name=='s':
        pyautogui.moveTo(x, y+10)
    if e.name=='w':
        pyautogui.moveTo(x, y-10)
    if e.event_type=='up' and e.scan_code==110:
        i=(i+1)%2
    #print("press:",e.event_type,e.scan_code," ",e.name,i)
def on_release(e):
    if e.scan_code==110:
        i=(i+1)%2
    print("status",i)
    #pyautogui.moveTo(200, 150)
    #print("release:",e.scan_code)
keyboard.hook(on_press)
#keyboard.on_release(on_release)

keyboard.wait()
