import usb_hid
from adafruit_circuitplayground import cp
import random
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from mwords import *
from kwords import *
import time

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)


red = (7,0,0)
green = (0,7,0)
blue = (0,0,7)
blank = (0,0,0)

def blinknum(num,color):
    if num != 0:
        for i in range(num):
            cp.pixels.fill(color)
            time.sleep(.25)
            cp.pixels.fill(blank)
            time.sleep(.10)
    else:
        for i in range(10):
            cp.pixels[i] = color
            cp.pixels.show()
            time.sleep(.14)
            
        cp.pixels.fill(blank)
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


def trans(galactic):
    file_one = open("trans", "r")

    for word in file_one:
        try:
            (gal,eng) = word.split(":")
            eng = eng.strip("\n")
            gal = gal.strip(" ")
            if (gal == galactic):
                return(eng)
            if (word.find(galactic+":") == 0 ):
                return(eng+"*")
                
            #print ("Gal: "+gal+" English: " + eng)
        except:
            galactic = galactic
            
def kcode():
    code = ""
    tword = ""
    for i in range(6):
        kword =  kwords[random.randrange(len(kwords))]
        code = code + " " +kword
#        print(kword)
        trns = trans(kword)
        tword = tword + " " + trns
#        print(tword)
    return (code+"\n"+tword)


def mcode():
    codew = ""
    tword = ""

    for i in range(6):
        mword = mwords[random.randrange(len(mwords))]
        codew = codew + " " + mword
        trns = trans(mword)
        tword = tword + " " + trns
    return (codew+"\n"+tword)



done = False

blinknum(1,blue)
blinknum(2,red)
blinknum(3,green)

while not done:
    Val = 0
    if cp.button_a:
        Val = Val + 1
    if cp.button_b:
        Val = Val + 2

    if Val == 1:
        compthink(2)
        blinknum(1,blue)
        code = mcode()
        prt (code)
        time.sleep(.25)
    
    if Val == 2:
        compthink(3)
        blinknum(2,green)
        code = kcode()
        prt (code)
        time.sleep(.25)

        