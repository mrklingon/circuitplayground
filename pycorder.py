from adafruit_circuitplayground import cp
import time
import random
from bach import *

from blinknum import *

temp = 0
light = 1
gees = 2

sound = ["digits/temp.wav", "digits/light.wav", "digits/gees.wav"]

blinknum(1,red)
docage()
blinknum(2,green)
blinknum(3,blue)

state = temp
cp.play_file(sound[state])

while True:
    
    if cp.button_a:
        state = state + 1
        if state > gees:
            state = temp
        cp.play_file(sound[state])
        
    if cp.button_b:
        if state == temp:
            saytemp()
        if state == light:
            saylight()
        if state == gees:
            saygees()
    
    if cp.touch_A7:
        docage()

    if cp.touch_A1:
        swtune(1)
        
    if cp.touch_A2:
       compthink(3)
