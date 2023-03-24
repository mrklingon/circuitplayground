from adafruit_circuitplayground import cp
import time
import random
import board
west = [1, 2, -1, 2, 3, 4, 5, 8, 9, 0]
east = [9, 0, 1, 4, 5, 6, 7, -1, 7, 8]
south = [-1, 0, 1, 2, 3, 6, 7, 8, 9, -1]
north = [1, 2, 3, 4, -1, -1, 5, 6, 7, 8]
next = [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]
def pick(): #create a random color
    return (random.randrange(200),random.randrange(200),random.randrange(200))
def clearnext(): #clear next matrix
    for i in range(10):
        next[i]=(0,0,0)
def dofill(): #fill all pixels with random colors
    for x in range(100):
        cp.pixels[random.randrange(10)]=pick()
def doclear(): #clear all pixels
    for x in range(10):
        cp.pixels[x]=(0,0,0)
 
def setnext(newpix): #"pour" pixels to direction using newpix matrix
    clearnext()
    for i in range(6):
        for i in range(10):
            if newpix[i]>=0:
                next[i] = cp.pixels[newpix[i]]
        for i in range(10):
            cp.pixels[i]=next[i]
        time.sleep(.1)
    doclear()
        
def getdir(): #get direction from tilt
    x, y, z = cp.acceleration
    dir = ""
    if (x>7):
        dir="left"
    if (x<-7):
        dir="right"
    if (y>7):
        dir="down"
    if (y<-7):
        dir="up"
    return dir

#switch to left:
#A button "fills" pixels with random colors
#B clears all pixels
#Shake "fills" pixels with random colors
#tilt left/right/up/down "pours"pixels in that direction

#switch to right refills pixels with random colors every second

dofill()
while True:
    if cp.switch:
        if cp.button_a:
            dofill()
        if cp.button_b:
            doclear()           
        if	cp.shake(shake_threshold=10):
            dofill()
        dir = getdir()
        if dir == "left":
            setnext(east)
        if dir == "right":
            setnext(west)
        if dir == "up":
            setnext(north)
        if dir == "down":
            setnext(south)
        time.sleep(.1)    
    else:
        dofill()
        time.sleep(1)
