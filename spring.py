from adafruit_circuitplayground import cp
import time
import random
from blinknum import *


#Define colors
pink = (12,10,12)
gold = (50, 40, 5)
orange = (25, 10, 0)
blank = (0,0,0)
grn = (0,20,0)

red = (20,0,0)
orange = (25, 10, 0)
yellow = (24,24,2)
green  = (0,20,0)
blue = (0,0,8)
indigo = (18,0,26)
violet = (10,0,5)


white = (20,20,20)
palette = [pink,gold,blue,orange,blank,green,red,white]
rainbow = [red,orange,yellow,green,blue,indigo,violet]
rainbow2 = [orange,yellow,green,blue,indigo,violet,red]

def boom():
    for i in range(30):
        cp.pixels[loc(i)]=random.choice(palette)
        
    time.sleep(.25)
    for i in range(10):
        cp.pixels[i] = blank
        time.sleep(.1)
        

def loc(pos):
    pos = pos + 10
    return pos % 10

rocket = 0
star = 9
target = 5
cp.pixels[target]=random.choice(palette)
while True:
    
    time.sleep(.25)
    if random.randrange(10)>7:
        cp.pixels[target]=blank
        target = loc(target+(1-random.randrange(3)))
        cp.pixels[target]=random.choice(palette)
        time.sleep(.5)  

    spring = 0
    sspring = 0
    if cp.button_a:
        spring = spring + 1
        cp.pixels[rocket] = random.choice(rainbow)
        while cp.button_a:
            spring = spring + 1
            cp.pixels[rocket] = random.choice(rainbow)
            time.sleep(.1)
    cp.pixels[rocket] = blank
    if cp.button_b:
        sspring = sspring + 1
        cp.pixels[star] = random.choice(rainbow)
        while cp.button_b:
            sspring = sspring + 1
            cp.pixels[star] = random.choice(rainbow)
            time.sleep(.1)
    cp.pixels[star] = blank
    if spring > 0:
        delay = .01
        for x in range(spring%17):
            rocket = loc(rocket+1)
            if rocket == target:
                boom()
            cp.pixels[rocket] = random.choice(rainbow)
            time.sleep(delay)
            delay = delay*1.4
            cp.pixels[rocket]= blank
    if sspring > 0:
        delay = .01
        for x in range(sspring%17):
            star = loc(star-1)
            if star == target:
                boom()
            cp.pixels[star] = random.choice(rainbow)
            time.sleep(delay)
            delay = delay*1.4
            cp.pixels[star]= blank 
