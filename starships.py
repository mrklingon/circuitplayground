# SPDX-FileCopyrightText: 2017 Limor Fried for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Circuit Playground HID Keyboard

import time
import random
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull

from adafruit_circuitplayground import cp

red = (7,0,0)
green = (0,7,0)
blue = (0,0,7)
blank = (0,0,0)
        
Systems = ["Proxima Centauri#", "4.2465", "Wolf 359#", "7.856", "Lalande 21185", "8.304", "Epsilon Eridani", "10.489", "Lacaille 9352#", "10.724", "Ross 128", "11.007", "Struve 2398 B#", "11.491", "Groombridge 34 A#", "11.619", "Epsilon Indi A", "11.867", "Tau Ceti#", "11.912"]
ships = ["Churchill", "Karma", "Ace of Spades", "Dream", "The Trident",
         "ISS Crack", "SSE Alice", "CS Conscience", "STS Reliant",
         "HWSS Halo","Warrior", "Kyozist",
         "Invincible", "Amazon", "The Leviathan", "SSE Stalker", "CS Ark Royal", "HWSS Providence", "USS Herminia", "ISSMarduk","The Enterprise", "The Millenium Falcon", "Solar Sail Rembrandt"]
travel = ["travels to", "returns from"]
purpose = ["with supplies", "carrying passengers", "with ancient artifacts", "escaping a battle", "pursuing an enemy"]
problem = ["and is damaged in an explosion", "and loses power", "and runs out of fuel"]
solution =  ["is repaired by automated systems.", " and tumbles out of control till emergency crews reach them", "and just barely reaches destination stardock."]
twist = ["And then a mysterious message arrives from {alien} {place}.",
         "Suddenly a ship appears from {place} warning of imminent {alien} attack.",
         "An urgent emergency message from {place} arrives. The {alien} planet is experiencing an epidemic.",
         "Word comes that the {alien} ambassador has just died on {place}."]

aliens = ["Stezets",
    "Scuns",
    "Cuds",
    "Vrucuins",
    "Bhisih",
    "Ahleath",
    "Dandaeds",
    "Qat'iet",
    "Gad",
    "Nahrins"]

planets = ["Mageinope",
    "Thotreatune",
    "Zolinda",
    "Nilreron",
    "Uclite",
    "Notania",
    "Guapra",
    "Brozalea",
    "Gerth NYV",
    "Strilia Q5OV"]


cp.pixels.fill(blank)

# the keyboard object!
# sleep for a bit to avoid a race condition on some systems
time.sleep(1)
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

# make all pin objects, make them inputs with pulldowns
Done = False
while not Done:
    val = 0
    
    if cp.button_a:
        val = val + 1
        system = random.randrange(10)
        star = Systems[system*2]
        dist = Systems[1+(system*2)]
        location = "Star: " + star + " at distance " + dist + " light years"

    if cp.button_b:
        val = val + 2# check each button
    
    if val == 1:
        cp.pixels.fill(blue)
        compthink(1)
        system = random.randrange(10)
        star = Systems[system*2]
        dist = Systems[1+(system*2)]
        location = "Star: " + star + " at distance " + dist + " light years"
        prt (location)
        time.sleep(.25)
        cp.pixels.fill(blank)

    if val == 2:
        cp.pixels.fill(green)

        compthink(2)
        story = random.choice(ships) + "\n"
        story = story + random.choice(travel) + "\n"
        story = story + star + "\n"
        story = story + random.choice(purpose) + "\n"
        story = story + random.choice(problem) + "\n"
        story = story + random.choice(solution) + "\n"
        story = story + random.choice(twist).format(place=random.choice(planets), alien = random.choice(aliens)) +"\n"

        prt (story)
        time.sleep(.25)
        cp.pixels.fill(blank)

    if val == 3:
        prt ("Qapla'!")
        Done = True

