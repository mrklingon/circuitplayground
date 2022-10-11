
from adafruit_circuitplayground import cp
import time
import random

blank = (0,0,0)

USize = 10

Rule = [0,0,0,1,0,1,1,0]

SRule = [0,0,0,1,0,1,1,0]

Rule30 = [0,0,0,1,1,1,1,0]

Rule110 = [00,1,1,0,1,1,1,0]


Rpower = [7,6,5,4,3,2,1,0]

cells = [0, 0, 0, 0, 1, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0]

ncells = [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0]

colors = [(25,0,0), (25,25,0), (0,25,0), (0,25, 25), (0,0,25), (25,0,25)]

def showCells(colour):
    txtshow   = ""
    for i in range(10):
        if cells[i] ==1:
            cp.pixels[i] = colour
        else:
            cp.pixels[i] = blank
    
    for i in range(USize):
        if cells[i] ==1:
            txtshow = txtshow + "*"
        else:
            txtshow = txtshow + " "
        
    
    print (txtshow)

def blankCells():
    for i in range(10):
        cp.pixels[i] = (0,0,0)

def nRight(x):
    if x == USize-1:
        x=0
    return cells[x+1]
        
def nLeft(x):
    if x == 0:
        x=USize-1
    return cells[x-1]*4

def showUni(x):
    #number of gens, to show the whole Universe
    blankCells()
    for g in range(x):
        nGen()
        txtshow = ""
        for i in range(USize):
            if cells[i] == 1:
                cp.pixels[i % 10] = (0,15,0)
                txtshow = txtshow + "*"
            else:
                cp.pixels[i % 10] = (0,0,0)
                txtshow = txtshow + " "
            time.sleep(.05)
        print(txtshow)
        time.sleep(.5)
    Extinct()
    showCells((0,0,15))
              
def Extinct():
    tot = 0
    for i in range(USize):
        tot = tot + cells[i]
    
    if tot == 0: #extinct!
        for z in range(3):
            for i in range(10):
                cp.pixels[i] = (random.randrange(25),random.randrange(25),random.randrange(25))
                time.sleep(.05)
        blankCells()
            
        print ("Extinction reached!!")
        doRand() #regenerate!
        showCells(colors[0])
        
    

def nGen():
    for i in range(USize):
        tot = (2 * cells[i])+ nRight(i) + nLeft(i)
        ncells[i] = Rule[7-tot]
        
    for i in range(USize):
        cells[i] = ncells[i]
            
def showRule():
    blankCells()
    code = 0
    for i in range(8):
        if Rule[i] == 1:
            cp.pixels[i] = (0,0,10)
            code = code + (2 ** Rpower[i])
            
    print("rule:" + str(code))
            
    time.sleep(.5)
    showCells((10,0,10))
    

def doGen(x):
    showCells(colors[random.randrange(6)])
    for i in range(x):
        nGen()
        showCells(colors[random.randrange(6)])
        time.sleep(.35)
    
    Extinct() #check for extinction
            
def changeRule():
    for i in range(8):
        if random.randrange(10) >7:
            Rule[i] = 1
        else:
            Rule[i] = 0
    showRule()
              

def fixRule():
    for i in range(8):
        Rule[i] = SRule[i]
    showRule()


def setRule(newrule):
    for i in range(8):
        Rule[i] = newrule[i]
    showRule()
              


def doRand():
    for i in range(USize):
        if random.randrange(20) <  6:
            cells[i] = 1
        else:
            cells[i] = 0
            
while True:
    
    if cp.switch:
        USize = 10
    else:
        USize = 60
        
        
    if cp.button_a:
        doGen(10)
        
    if cp.button_b:
        showCells(colors[random.randrange(6)])
        doRand()
        time.sleep(.5)
        showCells(colors[random.randrange(6)])
        
    if cp.touch_A3:
        setRule(Rule110)

    if cp.touch_A1:
        fixRule()
        showCells(colors[random.randrange(6)])
        cells = [0, 0, 0, 0, 1, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0]
        time.sleep(.5)
        showCells(colors[random.randrange(6)])
        
    if cp.touch_A7:
        showRule()

    if cp.touch_A4:
        changeRule()

    if cp.touch_A2:
        setRule(Rule30)

    if cp.touch_A6:
        showUni(5)

        
