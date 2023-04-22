from adafruit_circuitplayground import cp
import time
import random
import board
import math


#define walls
north = [1, 0, 9, 8]
south = [3, 4, 5, 6]
west = [1, 2, 3]
east = [6, 7, 8]

#define colors
blank = (0,0,0)
blue = (0,0,40)
red = (40,0,0)
green = (0,40,0)
purp = (20,0,20)

#how far is the traveler from the (10,10) goal
def dist():
    global x
    global y
    dist = 1
    print ("x:" + str(x) + " y:" + str(y))
    try:
        dist = math.sqrt(((10-x)**2)+((10-y)*2))
        print(dist)
    except:
        time.sleep(.1)
    return dist

#change in x,y with movement N/E/S/W 
deltas = [[0,-1],[1,0],[0,1],[-1,0]]

#briefly set all pixels to color
def flash(color):
    for i in range(10):
        cp.pixels[i] = color
    time.sleep(.25)
    for i in range(10):
        cp.pixels[i] = blank

# set pixels to color2 on "wall" side
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

#generate a new room - no more than 3 walls
def doNewRoom (): 
    global roomx
    roomx = [0,0,0,0]
    for i in range(3):
        roomx[random.randrange(4)] = 1

#flash red on the wall that is blocking the user
def bounce(dir):
    makeWall(dir,red)
    time.sleep(.25)
    makeWall(dir,blue)

#call generation of new room, and display it
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

#main loop
while True:
    #for tracking movement as approaching 10,10 goal
    x = 0
    y = 0
    curDist = 0 
    oldDist = 0
    roomx = [0,0,0,0]
    dofill()
    Done = False
    newRoom() #create first room
    while not Done:
        dir = getdir()
        if dir != 0: # a direction was tilted
            dir = dir - 1

            if roomx[dir] == 1:
                bounce(dir) #wall is blocked
            else: #move to new room
                oldDist = dist() #save current distance
                x = x + deltas[dir][0]
                y = y + deltas[dir][1]
                #move and calculate new distance
                curDist = dist()
                
                #flash green for "closer", purple for "farther"
                if curDist > oldDist:
                    flash(purp)
                if curDist < oldDist:
                    flash(green)
                #create new room
                newRoom()
                
                #check to see if we've arried
                if ((x ==10) and (y == 10)):
                    Done = True
                time.sleep(.25)

        time.sleep(.1)
    #celebrate, then restart.
    dofill()
    time.sleep(10)
