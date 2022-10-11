# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

from adafruit_circuitplayground import cp
import time
import random
import board

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


def bounce1():
    for x in [2, 1, 0, 9, 8, 7 ]:
            r = random.randrange(50)
            g = random.randrange(30)
            b = random.randrange(90)
            cp.pixels[x] = (r,g,b)
            time.sleep(0.1)
    for x in [2, 1, 0, 9, 8, 7 ]:
        time.sleep(0.1)
        cp.pixels[x] = (0, 0, 0)
        
def miss():
    for x in [3,4,5,6]:
        cp.pixels[x] = (50,0,0)
        time.sleep(0.2)

    for x in [3,4,5,6]:
        cp.pixels[x] = (0,0,0)
        

        
def miss2():
    for x in [6,5,4,3]:
        cp.pixels[x] = (50,0,0)
        time.sleep(0.2)

    for x in [6,5,4,3]:
        cp.pixels[x] = (0,0,0)
        
def score(scr,color):
    pix = [3,4,5,6]
    for x in range(scr):
        cp.pixels[pix[x]] = color
    time.sleep(0.2)
    for x in range(scr):
        cp.pixels[pix[x]] = (0,0,0)

def bounce2():
    for x in [7, 8, 9, 0, 1, 2]:
            r = random.randrange(50)
            g = random.randrange(30)
            b = random.randrange(90)
            cp.pixels[x] = (r,g,b)
            time.sleep(0.1)
    for x in [7, 8, 9, 0, 1, 2]:
        time.sleep(0.1)
        cp.pixels[x] = (0, 0, 0)
        
Tech = ["ST/Enterprise Doors.wav","ST/tng_tricorder9.wav  ","ST/Transporter Beam.wav"]
Talking = ["ST/1x14-beverlyshutupwesley-e.wav","ST/Communicator.wav ","ST/Console beeps 12.wav","ST/Console beeps 3.wav","ST/Console beeps.wav","ST/wouldyoumindidentifyingwhatyouare.wav","ST/raiseallshieldsphasersatready.wav", "ST/makeitso.wav","ST/acknowledge.wav", "ST/engage.wav"]

cp.play_file("ST/raiseallshieldsphasersatready.wav")
cp.play_file("ST/engage.wav")

ascore = 0
bscore = 0
a = (0,0,50)
b = (0,50,0)

while True:

    if cp.button_a or cp.touch_A6:
        bounce1()
        if cp.button_b or cp.touch_A1:
            bounce2()
        else:
            miss2()
            bscore += 1
            score(bscore,b)

    if cp.button_b or cp.touch_A1:
        bounce2()
        if cp.button_a or cp.touch_A6:
            bounce1()
        else:
            miss()
            ascore += 1
            score(ascore,a)
            
    if (bscore == 4 or ascore == 4):
        wave()
        wave()
        wave()
        ascore = 0
        bscore = 0
        cp.play_file("ST/engage.wav")

