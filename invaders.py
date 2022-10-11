from adafruit_circuitplayground import cp
import time
import random
from bach import *
from blinknum import *

red = (7,0,0)
green = (0,7,0)
blue = (0,0,7)
blank = (0,0,0)
klingons = [1,0,9,8]
feds = [3,4,5,6]

fed = 0

cp.pixels.fill(blank)
def setk():
    for i in range(4):
        cp.pixels[klingons[i]] = green

def chkK():
    for i in range(4):
        if cp.pixels[klingons[i]] != red:
            return(False)
    return(True)   
        
setk()
torps = 10

if cp.switch:
    sttune(1)
cp.pixels[feds[fed]] = blue

done = False
score = 0 
while not done:
    if chkK():
        blinknum(3,green)
        score = score + 1000
        
    val = 0
    
    if random.randrange(1000) >900:
        setk()
    if cp.touch_A7: #restart game
        cp.pixels.fill(blank)
        if cp.switch:
            sttune(1)
        setk()
        score = 0
        torps = 10
    if cp.touch_A2:
        saytemp()
    if cp.touch_A3:
        compthink(2)
        
    if cp.touch_A1: #show score
        cp.pixels.fill(blank)
        showint(score)
        cp.pixels.fill(blank)
        setk()
        
    if cp.button_a:
        val = val + 1
    if cp.button_b:
        val = val + 2
        
    if val ==3 :
        print ("zap")
        if cp.pixels[klingons[fed]] == green:
            if torps > 0 :
                cp.pixels[klingons[fed]] = red
                cp.play_tone(allnotes[23],.25)
                score = score + random.randrange(20)
                torps = torps - 1
        else:
            if torps > 0:
                cp.pixels[klingons[fed]] = (10,10,10)
                cp.play_tone(allnotes[5],.25)
                score = score - random.randrange(20)
                torps = torps - 1
    if val == 1:
        cp.pixels[feds[fed]]=blank
        fed = fed - 1
        if fed < 0:
            fed = 0
    
    if val == 2:
        cp.pixels[feds[fed]]=blank
        fed = fed + 1
        if fed > 3:
            fed = 3
        
    cp.pixels[feds[fed]] = blue

    time.sleep(.25)      

