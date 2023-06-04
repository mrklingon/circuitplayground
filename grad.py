import time
import microcontroller
import random

from adafruit_circuitplayground import cp

#Define colors
pink = (12,10,12)
gold = (50, 40, 5)
blue = (0,0,8) 
orange = (25, 10, 0)
blank = (0,0,0)
grn = (0,20,0)
green  = (0,20,0)
red = (20,0,0)
white = (20,20,20)
palette = [pink,gold,blue,orange,blank,green,red,white]

    
def gradient(start,end):
    (sr,sg,sb) = start
    (er,eg,eb) = end
    
    rg = (er-sr)/9 #red gradient
    gg = (eg-sg)/9 #green gradient
    bg = (eb-sb)/9 #blue gradient
    
    cp.pixels.fill(blank)
    clr = start
    for i in range (10):
        cp.pixels[i] = clr
        (r,g,b) = clr
        clr = (r+rg,g+gg,b+bg)
        time.sleep(.2)
        
        
def rndGrad():
    c1 = random.choice(palette)
    c2 = random.choice(palette)
    gradient(c1,c2)


while True:
    rndGrad()