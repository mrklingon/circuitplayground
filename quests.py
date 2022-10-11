from adafruit_circuitplayground import cp
import time
import random

from blinknum import *
from qdata import *
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode


kbd = Keyboard(usb_hid.devices)
# we're americans :)
layout = KeyboardLayoutUS(kbd)


def prt(text):
    if cp.switch:
        print(text)
    else:
        layout.write(text + "\n")

def compthink(cycles):
    for i in range (10*cycles):
        freq = random.randrange(200,1200)
        dur = random.uniform(.02,.125)
        cp.play_tone(freq,dur)


def end(text):
    e = text[len(text)-1]
    return e

while True:
    node = 0
    prevnode = -1
    done = False
    while not done:
    
        if node != prevnode:
            blinknum(node,blue)
            compthink(1)
            remember = qs[node]
            prt(qs[node])
            prevnode = node
        
        if node == 0:
            node = 1
    
        val = 0
        if cp.button_a:
            val = val + 1
        if cp.button_b:
            val = val +2

        if val == 1: #"no"
            blinknum(node,red)
            prt ("no.")
            node = node * 2
            if end(remember)=="!":
                   prt("I give up!")            
        
        if val == 2: #"yes"
            blinknum(node,green)
            prt ("yes.")

            node = (node * 2)+1
            if end(remember)=="!":
                   prt("I win!!!")
                   done = True
            
        if node > 7:
            prt ("game over!!")
            done = True
           