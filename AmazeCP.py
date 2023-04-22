from adafruit_circuitplayground import cp
import time
import random
import board
import math

#for tracking movement as approaching 10,10 goal
x = 0
y = 0
curDist = 0 
oldDist = 0

north = [1, 0, 9, 8]
south = [3, 4, 5, 6]
west = [1, 2, 3]
east = [6, 7, 8]
blank = (0,0,0)
blue = (0,0,40)
red = (40,0,0)
green = (0,40,0)
purp = (20,0,20)

roomx = [0,0,0,0]

def dist():
    global x
    global y
    
    dist = math.sqrt(((10-x)**2)+((10-y)*2))
    print(dist)
    return dist

deltas = [[0,-1],[1,0],[0,1],[-1,0]]

def flash(color):
    for i in range(10):
        cp.pixels[i] = color
    time.sleep(.25)
    for i in range(10):
        cp.pixels[i] = blank


def makeWall (dir,color2):
    if (dir == 0) :
        for i in (north):
            cp.pixels[i] = color2
    if (dir == 1) :
        for i in (east):
            cp.pixels[i] = color2

    if (dir == 2) :
        for i in (south):
            cp.pixels[i] = color2
    if (dir == 3) :
        for i in (west):
            cp.pixels[i] = color2
def pick(): #create a random color
    return (random.randrange(200),random.randrange(200),random.randrange(200))
def dofill(): #fill all pixels with random colors
    for x in range(100):
        cp.pixels[random.randrange(10)]=pick()
def doNewRoom (): 
    global roomx
    roomx = [0,0,0,0]
    for i in range(3):
        roomx[random.randrange(4)] = 1
def bounce(dir):
    makeWall(dir,red)
    time.sleep(.25)
    makeWall(dir,blue)
    
def newRoom ():
    doNewRoom()
    flash(blank)
    for room in range(4):
        if (roomx[room] == 1):
            makeWall(room, blue)
        else:
            makeWall(room, blank)
def getdir(): #get direction from tilt
    x, y, z = cp.acceleration
    dir = 0
    if (x>7):
        dir=4
    if (x<-7):
        dir=2
    if (y>7):
        dir=3
    if (y<-7):
        dir=1
    return dir
dofill()
Done = False
newRoom()
while not Done:
    dir = getdir()
    if dir != 0:
        dir = dir - 1

        if roomx[dir] == 1:
            bounce(dir)
        else:
            oldDist = dist()
            x = x + deltas[dir][0]
            y = y + deltas[dir][1]
            curDist = dist()
            if curDist > oldDist:
                flash(purp)
            if curDist < oldDist:
                flash(green)
            newRoom()
            if curDist <1:
                Done = True
            time.sleep(.25)

    time.sleep(.1)    
dofill()
