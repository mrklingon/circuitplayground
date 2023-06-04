import time
import microcontroller
import random
from adafruit_circuitplayground import cp

#Define colors
pink = (12,10,12)
gold = (50, 40, 5)
orange = (25, 10, 0)
blank = (0,0,0)
grn = (0,20,0)

red = (20,0,0)
orange = (25, 10, 0)
yellow = (24,24,2)
green  = (0,20,0)
blue = (0,0,8)
indigo = (18,0,26)
violet = (10,0,5)


white = (20,20,20)
palette = [pink,gold,blue,orange,blank,green,red,white]
rainbow = [red,orange,yellow,green,blue,indigo,violet]
rainbow2 = [orange,yellow,green,blue,indigo,violet,red]
   
def all():
    for cl in rainbow:
        cp.pixels.fill(cl)
        time.sleep(.5)
        
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

def rndGrad2():
    c1 = (random.randrange(100),random.randrange(100),random.randrange(100))
    c2 = (random.randrange(100),random.randrange(100),random.randrange(100))
    gradient(c1,c2)
    
while True:
    all()
    for i in range(7):
        gradient(rainbow[i],rainbow2[i])
    all()
    for i in range(7):
        gradient(rainbow[6-i],rainbow2[6-i])	
