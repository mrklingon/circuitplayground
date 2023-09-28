from adafruit_circuitplayground import cp
import time
import random

#Define colors
pink = (20,5,5)
gold = (25, 20, 5)
blue = (0,0,8)
orange = (25, 10, 0)
blank = (0,0,0)
grn = (0,20,0)
green  = (0,20,0)
red = (20,0,0)
white = (20,20,20)
violet = (20,0,20)

colors = [red,orange,pink,blank,green,blue,violet]

Psym = ["@","o","."," ","'",":","#"]
cosmos = []
c1 = []
c2 = []

for i in range(101):
    cosmos.append(0)
    c1.append(0)
    c2.append(0)
    
def create():
    global cosmos
    for x in range(100):
        cosmos[x] = random.randrange(-3,3)

def stable1():
    global cosmos
    for x in range(101):
        if x%2 >0:
            cosmos[x]=1
        else:
            cosmos[x]=-1
            



def display():
    for i in range(10):
        cell = i + 40
        cp.pixels[i] = colors[cosmos[cell]+3]
        
def pcosmos():
    global cosmos
    pic = ""
    
    for i in range(10,70):
        pic = pic + Psym[3+cosmos[i]]
        
    print (pic)
    
    
def checkWorld():
    global cosmos
    
    for i in (cosmos):
        if i != 0:
            return True
            
    return False

def doGen():
    global cosmos, c1, c2
    
    for i in range(100):
        c1[i]=0
        c2[i]=0
        
    for i in range(100):
        v = cosmos[i]
        if (v+i)>=0 and (v+i)<= 100:
            c1[v+i] = v
            n=v+i
            if cosmos[n] != 0:
                if (n+v) >=0 and (n+v)<=100:
                    c2[n+v] = cosmos[n]
    for i in range(100):
        cosmos[i]=0
    for i in range(100):
        if (c1[i]!=0):
            cosmos[i]= c1[i]
        
    for   i in range(100):
        if (c2[i]!=0):
            cosmos[i]= c2[i]

create()
pcosmos()
while True:
    display()
    if cp.button_a:
        doGen()
#       print(cosmos)
        pcosmos()
        
    if cp.touch_A1:
        stable1()
        display
 #       print(cosmos)
        pcosmos()
        
    if cp.button_b:
        create()
        #print(cosmos)
        pcosmos()
    if cp.switch:
        doGen()
        #print(cosmos)
        pcosmos()
        time.sleep(.1)
        
    if checkWorld() == False:
        cp.pixels.fill(white)
        time.sleep(2)
        create()

    time.sleep(.2)
