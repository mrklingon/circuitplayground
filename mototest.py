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

import morse

def compthink(cycles):
    for i in range (10*cycles):
        freq = random.randrange(200,1200)
        dur = random.uniform(.02,.125)
        cp.play_tone(freq,dur)
        
# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

def wave():
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    cp.pixels.fill((10,0,0))
    if cp.switch:
        compthink(1)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    cp.pixels.fill((0,0,20))
    if cp.switch:
        compthink(1)
    else:
        time.sleep(.25)
    
morse.blinkcode(morse.encryption("hello"))
cp.pixels.fill((0,20,0))
if cp.switch:
    compthink(2)
time.sleep(.25)
cp.pixels.fill((0,0,0))
while True:
    val = 0
    if cp.button_a:
        val = val + 1
    if cp.button_b:
        val = val +2
        
    if cp.touch_A7:
        for i in range(random.randrange(3,10)):
            wave()
            cp.pixels.fill((0,0,0))
    if val == 1:
        wave()
        cp.pixels.fill((0,0,0))

    if val == 2:
        compthink(2)
        