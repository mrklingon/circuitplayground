# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

from adafruit_circuitplayground import cp
import time
import random
import board
from blinknum import *
from dirship import *

picard = ["ST/makeitso.wav","ST/acknowledge.wav","ST/engage.wav","ST/Status report.wav"]
def saydeck(deck):
    cp.play_file("ST/deck.wav")
    showint(deck)
def showroom(deck,room):
    rm = entdir[deck][1][room]
    if rm.find("olod") >= 0:
        cp.play_file("ST/holodeck.wav")
    if rm.find("argo") >= 0:
        cp.play_file("ST/cargo.wav")
    if rm.find("bridge") >= 0:
        cp.play_file("ST/bridge.wav")
        cp.play_file(random.choice(picard))
    if rm.find("anspor") >= 0:
        cp.play_file("ST/transporter.wav")
        cp.play_file("ST/Transporter Beam.wav")
    if rm.find("uarter") >= 0:
        cp.play_file("ST/quarters.wav")
    if rm.find("ick") >= 0:
        cp.play_file("ST/tng_tricorder9.wav")
        cp.play_file("ST/sickbay.wav")
    if rm.find("orward") >= 0:
        cp.play_file("ST/tenforward.wav")
    if rm.find("lab") >= 0:
        cp.play_file("ST/lab.wav")
        cp.play_file("ST/tng_tricorder9.wav")

    if rm.find("uttle") >= 0:
        cp.play_file("ST/shuttlebay.wav")
    print(rm)

def curfloor(deck):
    return entdir[deck][0]

def enterfloor(deck):
#    cp.play_file("ST/Enterprise Doors.wav")
    saydeck(curfloor(deck))
#    print (entdir[deck][1])
    return(entdir[deck][1])
#cp.play_file("ST/Status report.wav")

deck = 0
room = 0

while not cp.switch:
    blinknum(1,blue)
    
cp.play_file("ST/Status report.wav")
rooms = enterfloor(deck)

turbo = False

while True:
    if cp.switch == False and turbo == False:
        turbo = True
        cp.play_file("ST/Enterprise Doors.wav")
        saydeck(curfloor(deck))
    
    if cp.switch == True and turbo == True:
        turbo = False
        cp.play_file("ST/Enterprise Doors.wav")
        rooms = enterfloor(deck)
        
    if not cp.switch and turbo == True:        
        if cp.button_a:
            deck = deck - 1
            if deck < 0:
                deck = 0
            else:
                enterfloor(deck)
                
        if cp.button_b:
            deck = deck + 1
            if deck == len(entdir):
                deck = deck - 1
            else:
                enterfloor(deck)
                
    if cp.switch and turbo == False:
        
        if cp.button_a:
            room = room - 1
            if room < 0:
                room = 0
            showroom(deck,room)
                
        if cp.button_b:
            room = room + 1
            if room == len(rooms):
                room = len(rooms) - 1
            showroom(deck,room)
    if cp.touch_A4:        
         cp.play_file("ST/tng_tricorder9.wav")
         cp.play_file("ST/temp.wav")
         saytemp()
         
    if cp.touch_A5:        
         cp.play_file("ST/tng_tricorder9.wav")
         cp.play_file("ST/light.wav")
         saylight()     
         
    time.sleep(.1)
                
    

        
