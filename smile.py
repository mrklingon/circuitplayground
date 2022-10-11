from adafruit_circuitplayground import cp
import time
import random
import board

smile = [2,3,4,5,6,7]
sc = (50,50,50)
frown = [2,1,0,9,8,7]
fc = (0,0,50)
cc = (0,0,0)


def doSmile():
    for x in smile:
        cp.pixels[x] = sc
        
    time.sleep(1.5)
    for x in smile:
        cp.pixels[x] = cc
        
def doFrown():
    for x in frown:
        cp.pixels[x] = fc
        
    time.sleep(1.5)
    for x in frown:
        cp.pixels[x] = cc
        
while True:
    if cp.switch:
        if cp.button_a:
            doSmile()
        if cp.button_b:
            doFrown()

    else:
        if random.randrange(100) > 75:
            doSmile()
            time.sleep(10)