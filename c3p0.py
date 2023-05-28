# SPDX-FileCopyrightText: 2017 Limor Fried for Adafruit Industries
#
# SPDX-License-Identifier: MIT


import time
import random
import board

from quotefile import *
from adafruit_circuitplayground import cp
from morse2 import *
def prt(text):
    print(text)
        
def compthink(cycles):
    for i in range (10*cycles):
        freq = random.randrange(200,1200)
        dur = random.uniform(.02,.125)
        cp.play_tone(freq,dur)
alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
colors = []

for x in range(55):
    clr = (20+random.randrange(100),20+random.randrange(100),20+random.randrange(100))
    colors.append(clr)
colors[0]=(0,0,0)


def doprint(msg):
    prt(msg)
    if cp.switch:
        for x in range(10):
            cp.pixels[x]=(0,0,0)
        for x in range(len(msg)):
            indx = 0
            if alphabet.find(msg[x])>-1:
                indx = alphabet.find(msg[x])
            cp.pixels[x%10] = colors[indx]
            time.sleep(.1)
        time.sleep(2)
    else:
        blinkcode(encryption(msg))
              
    for x in range(10):
        cp.pixels[x]=(0,0,0)
def doquote():
    compthink(1)
    doprint(random.choice(quotes))

compthink(1)
for x in range(10):
        cp.pixels[x]=(0,0,0)
Done = False
while not Done:
    val = 0
    
    if cp.button_a:
        val = val + 1
    if cp.button_b:
        val = val + 2
        
    if val == 1:
        compthink(1)
        doprint("We're Doomed!")
    if val == 2:
        doquote()	

    time.sleep(.2)

