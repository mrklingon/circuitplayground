from adafruit_circuitplayground import cp
import time
import random
import board

period = [24, 62, 100, 188]
planets = ["Mercury", "Venus", "Earth", "Mars"]
pix = [(255, 0, 0), (249,242,28), (0, 255, 0), (146, 0, 148)]
loc = [0, 0 ,0,0]
counter = [0,0,0,0]
def clearplanets(lcx):
    for i in range(10):
        cp.pixels[i] = (0,0,0)
def showplanets(lcx):

    for p in range(4):
        cp.pixels[loc[p]] = pix[p]
        
def mvplanet(planet):
    cp.pixels[loc[p]]=(0,0,0)
    loc[planet] = (loc[planet]+1)%10
    cp.pixels[loc[p]]=pix[p]

showplanets(loc)
while True:
    showplanets(loc)
    for p in range(4):
        counter[p] = counter[p]+1
        print (str(planets[p])+":"+str(counter[p])+":"+str(loc[p]))
        if counter[p]>period[p]:
            mvplanet(p)
            counter[p]=0
            
#    time.sleep(.01)
    
