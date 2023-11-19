from adafruit_circuitplayground import cp
import time
import random
from blinknum import *


def loc(pos):
    pos = pos + 10
    return pos % 10

test = 50
ship = 0
dir = 1
while test > 0:
    cmd = 0
    cp.pixels[ship] = blue
    time.sleep(.3)
    cp.pixels[ship]=(0,0,0)
    ship = loc(ship + dir)
    if cp.button_a:
        cmd = cmd + 1
    if cp.button_b:
        cmd = cmd + 2
    if cmd == 1:
        dir = 1
    if cmd == 2:
        dir = -1

    test = test - 1

cp.pixels.fill((0,0,0))

if cp.switch:
    cp.play_file("trek/proximityalert_ep.wav")
while True:
    ship = 0
    dir = 1
    klingon = 5
    life = 5
    duration = 0
    pause = 0.51
    while life > 0:
        pause = pause - 0.01
        if pause < 0:
            pause = 0
        duration = duration + 0.1
        cp.pixels[ship] = blue
        cp.pixels[klingon] = green
        if ship == klingon:
            blinknum(life, red)
            life = life - 1
            if cp.switch:
                cp.play_file("trek/smallexplosion1.wav")
                klingon = loc(klingon + 1)
                ship = loc(ship - 1)
        time.sleep(0.2 + pause)
        cp.pixels[ship] = blank
        cp.pixels[klingon] = blank

        ship = loc(ship + dir)
        cmd = 0
        if cp.button_a:
            cmd = cmd + 1
        if cp.button_b:
            cmd = cmd + 2
        if cmd == 1:
            dir = 1
        if cmd == 2:
            dir = -1
        if random.randrange(100) > 49:
            klingon = loc(klingon + (2 - random.randrange(3)))
    if cp.switch:
        cp.play_file("trek/largeexplosion1.wav")
    shownum(duration)
    time.sleep(1)

    wait = True
    while wait:
        blinknum(1, red)
        blinknum(2, blue)
        blinknum(3, green)
        if cp.button_a or cp.button_b:
            wait = False
    if cp.switch:
        cp.play_file("trek/proximityalert_ep.wav")
