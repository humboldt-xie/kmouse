#!env python3
import pyautogui
import fcntl

import keyboard
switch=False
step=1
pyautogui.FAILSAFE=False


def on_down(e):
    global switch
    if e.scan_code==58 or e.scan_code==61:
        switch=True

def on_up(e):
    global switch
    if e.scan_code==58 or e.scan_code==61:
        switch=False

def on_press(e):
    global switch,step
    print("press:",e.event_type,e.scan_code," ",e.name,switch,step)
    if e.event_type=='up':
        on_up(e)
    if e.event_type=='down':
        on_down(e)
        return
    x,y=pyautogui.position()
    if not switch:
        return True
    if e.name>='1' and e.name<='9':
        s=ord(e.name)-ord('1')+1
        step=1<<s
    if e.name=='h':
        pyautogui.moveTo(x-step, y)
    if e.name=='l':
        pyautogui.moveTo(x+step, y)
    if e.name=='j':
        pyautogui.moveTo(x, y+step)
    if e.name=='k':
        pyautogui.moveTo(x, y-step)
    if e.name=='n':
        pyautogui.click(button='left')
    if e.name=='m':
        pyautogui.click(button='right')
    return False
    #pyautogui.moveTo(200, 150)
    #print("release:",e.scan_code)
#keyboard.on_release(on_release)

try:  
    fp = open('/tmp/kmouse','w')  
    fcntl.flock(fp.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)  
    keyboard.hook(on_press)
    print('start')
    keyboard.wait()
    fp.close()  
except IOError:  
    print("lock")

