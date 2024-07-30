# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
import random
from adafruit_circuitplayground import cp
from adafruit_motor import servo


import morse2

msgs = ["hi","bye","yes","no","what"]

red = (15,0,0)
blue =(0,0,15)
green = (0,15,0)
blank = (0,0,0)
eyes = [6,5,4,3,4,5,6,5,4,3]

def say():
    talk(msgs[random.randrange(len(msgs))])

def compthink(cycles):
    for i in range (10*cycles):
        freq = random.randrange(200,1200)
        dur = random.uniform(.02,.125)
        cp.play_tone(freq,dur)

def eye(cyc):
    cp.pixels.fill(blank)
    for x in range(len(eyes)):
        cp.pixels[eyes[x]] = red
        time.sleep(.25)
        cp.pixels.fill(blank)

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

def wave():
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    cp.pixels.fill(red)
    if cp.switch:
        compthink(1)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    cp.pixels.fill(blue)
    if cp.switch:
        compthink(1)
    else:
        time.sleep(.25)

def talk(msg):
    print(msg)
    morse2.blinkcode(morse2.encryption(msg))

talk("hello")
cp.pixels.fill(green)
time.sleep(.5)

if cp.switch:
    compthink(2)
time.sleep(.25)
cp.pixels.fill(blank)
while True:
    val = 0
    if cp.button_a:
        val = val + 1
    if cp.button_b:
        val = val +2
    if cp.touch_A4:
        eye(random.randrange(5,7))
    
    if cp.touch_A3:
        if cp.switch:
            compthink(1)
        say()
    
    if cp.touch_A7:
        for i in range(random.randrange(3,10)):
            wave()
            cp.pixels.fill(blank)
    
    AUTOMODE = False
    
    if cp.touch_A1:
        AUTOMODE = True
        compthink(1)
        time.sleep(.1)
        while AUTOMODE:
            if cp.touch_A3:
                AUTOMODE = False
                
                print("exit auto")
                morse2.flash()
                cp.pixels.fill(blank)
            
            if random.randrange(10) > 5:
                say()
            if random.randrange(10)>3:
                wave()
            if random.randrange(10)>2:
                eye(1+random.randrange(3))
            if cp.touch_A3:
                AUTOMODE = False
                print("exit auto")
                morse2.flash()
                cp.pixels.fill(blank)


    if val == 1:
        wave()
        cp.pixels.fill(blank)

    if val == 2:
        compthink(2)
        
 
