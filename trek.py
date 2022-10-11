import time
import random
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull

from adafruit_circuitplayground import cp
kbd = Keyboard(usb_hid.devices)
# we're americans :)
layout = KeyboardLayoutUS(kbd)
red = (7,0,0)
green = (0,7,0)
blue = (0,0,7)
blank = (0,0,0)

def prt(text):
    if cp.switch:
        print(text)
    else:
        layout.write(text + "\n")
none = 0
mode = none
nav = 1
dock = 2
attack = 3
scan = 4
score = 0
allK = 0
modes = [0,nav,dock,attack,scan]
mnames= ["", "nav", "dock", "attack", "scan"]



def starmap(map):
    global allK
    enemies = int(map/10)
    stations = map - (enemies*10)
    prt("klingons: "+str(enemies))
    prt("stations: "+str(stations))
    ecount = 0
    statcount = 0
    ship = 0
    prt("score: "+str(score))
    left = allK - score
    prt("Klingons remaining: " + str(left))
    
    for i in range(10):
        line = ""
        for j in range(10):
            if random.randrange(10)>8:
                if ecount < enemies:
                    ecount = ecount + 1
                    line = line + "K"
                else:
                    if statcount<stations:
                        line = line + "S"
                        statcount = statcount + 1
    
                    else:
                        if ship == 0:
                            line = line + "E"
                            ship = 1
                        else:
                            line = line + "."
            else:
                line = line + "."
        prt(line)
        

def show(node):
    y = int(node/3)
    x = node - (3*y)
    prt("x: " + str(x) + " y: "+str(y))
    
def quad(x,y): #turn x,y into quad index to cosmos
    return (x%3)+(3*(3%y))

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

power = 100

def dodigit(digit,color):
    cp.pixels.fill(blank)
    if digit != 0:
        for i in range(digit):
            cp.pixels[i] = color
            cp.pixels.show()
            time.sleep(.14)
    else:
        for i in range(10):
            cp.pixels[i] = green
            cp.pixels.show()
            time.sleep(.14)
            
    time.sleep(.5)
    cp.pixels.fill(blank)
    
def mkquad():
    global allK
    stations = random.randrange(3)
    enemies = random.randrange(5)
    allK = allK + enemies
    quad = enemies * 10 + stations
    return quad
    
blinknum(3,green)

cosmos = [0,0,0,0,0,0,0,0,0]

#create 3x3cosmos
for i in range(9):
    cosmos[i]=mkquad()


blinknum(3,red)
node = 4
x=2
y=2

#for i in range(9):
#    starmap(cosmos[i])
    
Done = False


new = True

while not Done:
    val = 0
    if cp.button_a:
        val = val + 1
    if cp.button_b:
        val = val + 2
        
    if new:
        starmap(quad(x,y))
        new = False
        
    if val == 1:
        blinknum(1,blue)
        mode = (mode + 1)%5
        prt("mode: " + str(mode) + " " + mnames[mode])
        time.sleep(.25)
        
    if val == 2:
        blinknum(1,green)
        power =  power - 10
        time.sleep(.25)
        if mode == attack:
            prt("zap")
            blinknum(3,red)
            scn = cosmos[node]
            score = score + int(scn/10)
            scn = scn -  (int(scn/10)*10)
            cosmos[node] = scn #enemies gone
            mode = none
        
        if mode == scan:
            blinknum(2,green)
            prt("scan")
            starmap(cosmos[node])
            prt("power: " + str(power))
            mode = none
            
        if mode == dock:
            stations = cosmos[node]&3
            if stations > 0:
                blinknum(1,red)
                blinknum(1,blue)
                blinknum(1,green)
                power = 100
                prt("docked")
            else:
                prt("no stations here!")
            mode = none
        
        if mode == nav:
            blinknum(3,blue)
            node = random.randrange(9)
            prt("warp engaged!")
            show(cosmos[node])

        if power < 0:
            Done = True
    if val == 3 or allK == score:
        Done = True
        
prt("Game over! Score: "+str(score))
            