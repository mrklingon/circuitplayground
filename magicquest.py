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

races = ["human","elf","dwarf","kender", "drow"]
classes = ["wizard", "thief","cleric","healer","warrior"]
names =  ["Krargrouk Honorgrog","Kargroun Shadowbrew","Vomdoick Emberminer",
    "Polo Littlefoot","Leutfrid Baggins","Fastolph Gardner","Alen Tormyar",
    "Ascal Perbanise","Felaern Tortoris","Crestiennet of the Night",
    "Thilrern Derorvo",
    "Bheksomu Dreinzul",
    "Khondui Bhugazel",
    "Averitt the Heroic","Heimeri of the South"]

destination = ["Alterwood Palace","Corftey Fortress","Clarn Castle","Wringcaster Citadel","The Eternal Haunt",
    "The Buried Burrows","The Ethereal Cells  ","Water Leopard Woods","Baxpool Covert","Kirkasing Woodland"]

weapons = ["Soulsliver",
    "Cryptic",
    "Blackout",
    "Doomguard",
    "Windsong Idol",
    "Thirsting Slicer",
    "Isolated Copper Sabre",
    "Pride's Steel Protector",
    "Aetherius, Quickblade of Eternal Bloodlust",
    "Treachery, Spine of Justice",
    "Stinger, Claymore of the Burning Sun",
    "Barbarian Iron Deflector",
    "Mournblade, Gift of Ancient Power"]

enemy = ["Phasething",
    "Chaosling",
    "Rottingstep",
    "Boulderfang",
    "Phantomman",
    "Dreadcrackle",
    "Soilserpent",
    "Mornlich",
    "The Lanky Statue",
    "The Feathered Bane Jackal",
    "The Black-Eyed Cinder Spider",
    "The Tusked Venom Drake"]



travel = [" travels to", " returns from", " explores within", " gets lost at"]
treasure = ["Fortune's Horn",
    "Worship Mirror",
    "Insanity Boots",
    "Sanctifying Ark",
    "Roaring Scepter",
    "Misty Satchel",
    "Hailstorm Charm"]

forest = ["Misty Bluff Wilds",
    "Pleasant Brook Grove",
    "Huge Wilds",
    "Majestic Wilds",
    "Short-Tailed Snail Woodland",
    "Speckled Squirrel Grove",
    "Faint Wood",
    "Jagged Covert",
    "Short-Tailed Treefrog Grove",
    "Imperial Spider Covert",
    "Mannear Wilds",
    "Shipsons Wood",
    "Alberboia Grove",
    "Bois de la Camris",
    "Fort du Bouluon",
    "Fort de la Carcaveil",
    "Fort de la Sarmont" ]

problem = [ "Suddenly out of {frst} appears a {monster}", "{name} is surprised when {monster} attacks from {frst}",
    "A battle begins. The deadly {monster} attacks {name} after leaping out of {frst}!",
    "Alarm! {monster} materializes from the edge of {frst}!"]

solution = [ "Stumbling badly, {name} somehow manages to find the {weapon} and dispatch them!",
             "Heroicly, {name} quickly banishes the creature to {forest} with the {weapon}.",
             "Even though {name} fails to find a weapon like {weapon}, the monster shuffles away to {forest}"]



purpose = ["seeking", "discovering", "losing","finding"]
cp.pixels.fill(blank)

# the keyboard object!
# sleep for a bit to avoid a race condition on some systems
time.sleep(1)
kbd = Keyboard(usb_hid.devices)
# we're americans :)
layout = KeyboardLayoutUS(kbd)

def player():
    nm = random.choice(names)
    rc = random.choice(races)
    cl = random.choice(classes)
    return [nm,rc,cl]

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
Player = player()

while not Done:
    val = 0

    if cp.button_a:
        val = val + 1

    if cp.button_b:
        val = val + 2# check each button

    if val == 1:
        cp.pixels.fill(blue)
        compthink(1)
        time.sleep(.25)
        cp.pixels.fill(blank)
        Player = player()
        prt ("name: "+ Player[0])
        prt ("race: "+ Player[1])
        prt ("class: "+ Player[2])

    if val == 2:
        cp.pixels.fill(green)

        compthink(2)
        prt("The " + Player[1]+ " " + Player[2] + " " + Player[0] )
        prt(random.choice(travel) )
        prt(random.choice(destination) )
        prt(random.choice(purpose) + " "+ random.choice(treasure))
        prt(random.choice(problem).format(name=Player[0],frst=random.choice(forest),monster=random.choice(enemy)))
        prt(random.choice(solution).format(name=Player[0],forest=random.choice(forest),monster=random.choice(enemy),weapon=random.choice(weapons)))


        time.sleep(.25)
        cp.pixels.fill(blank)


    if val == 3:
        prt ("Qapla'!")
        Done = True


