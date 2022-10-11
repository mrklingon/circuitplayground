# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

from adafruit_circuitplayground import cp
import time
import random
import board
from bach import *

moves = [1,2,2,1,2,2,1,1,2,1]

def wave():
    for x in range(10):
            r = random.randrange(50)
            g = random.randrange(30)
            b = random.randrange(90)
            cp.pixels[x] = (r,g,b)
            time.sleep(0.1)
    for x in range(10):
        time.sleep(0.1)
        cp.pixels[x] = (0, 0, 0)


def thinking():
    if cp.switch:
        compthink(1)
    for x in range(10):
            r = random.randrange(50)
            g = random.randrange(30)
            b = random.randrange(90)
            cp.pixels[x] = (r,g,b)
            time.sleep(0.1)
    for x in range(10):
        time.sleep(0.1)
        cp.pixels[x] = (0, 0, 0)

def compmove(total):
    thinking()
    return moves[total]
    
comp = (0,25,0)  #computer color green
humn = (0,0,25)  #human color blue
score = (25,0,25) # score purple


def shownum(number,color):
        for x in range(10):
            time.sleep(0.1)
            cp.pixels[x] = (0, 0, 0)
#clear screen
        
        for x in range(number):
            time.sleep(0.1)
            cp.pixels[x] = color

TOTAL = 0
saber = False
wave()
while True:

    if cp.touch_A1: #computer turn
        cmove = compmove(TOTAL)
        shownum(cmove,comp)
        time.sleep(0.5)
        TOTAL += cmove
        shownum(TOTAL,score)
        if TOTAL == 10:
            if cp.switch:
                cp.play_file("ST/compwin.wav")
            shownum(TOTAL,comp)

    if cp.touch_A3: #reset game
        TOTAL = 0
        wave()
                
        
    if cp.button_a:  #human adds 1
        shownum(1,humn)
        time.sleep(0.25)
        TOTAL +=1
        shownum(TOTAL,score)
        if TOTAL == 10:
            if cp.switch:
                cp.play_file("ST/humanwin.wav")
            wave()
            wave()
            shownum(TOTAL,humn)



    if cp.button_b:  #human adds 1
        shownum(2,humn)
        time.sleep(0.25)
        TOTAL +=2
        shownum(TOTAL,score)
        if TOTAL == 10:
            if cp.switch:
                cp.play_file("ST/humanwin.wav")
            wave()
            wave()
            shownum(TOTAL,humn)

