from adafruit_circuitplayground import cp
import time
import random

REPL = False
red = (20,0,0)
green = (0,20,0)
gold = (51,43,0)
blue = (0,0,20)
white = (20,20,20)
purple = (20,0,30)
blank = (0,0,0)
mcolors = [red, green, blue, gold]
colors = [red,green,gold,blue,white,purple,blank]

def compthink(cycles):
    if cp.switch:
        for i in range (10*cycles):
            freq = random.randrange(200,1200)
            dur = random.uniform(.02,.125)
            cp.play_tone(freq,dur)
        
def compthink2(cycles):
    for i in range (10*cycles):
        cp.pixels[random.randrange(10)] = random.choice(colors)
        cp.pixels.show()
        time.sleep(.1)
        
        
    cp.pixels.fill(blank)
    cp.pixels.show()
        

cpix = [1,0,9,8]
rpix = [3,4,5,6]



code=[]

guess = []

cp.pixels.fill((0,0,50))
cp.pixels.show()

def mkcode():
    for i in range(4):
        code.append(random.choice(mcolors))
        print(code)

def showcode(carray):
    cp.pixels.fill(blank)
    for i in range(4):
        cp.pixels[cpix[i]] = carray[i]
    cp.pixels.show()

def showscore(exact,off):
    cp.pixels.fill(blank)
    showcode(testarray)
    cp.pixels.show()
    if exact>0:
        for i in range(exact):
            cp.pixels[rpix[i]]=white
    if off>0:
        for i in range(off):
            cp.pixels[rpix[i+exact]] = purple
    cp.pixels.show()

def testit(carray,test):
    exact = 0 #number of correct cells
    off = 0 #number of correct colors
    sample = []
    csamp = []    

    for i in range(4):
        sample.append(test[i])
        csamp.append(carray[i])

    for i in range(4):
        if sample[i] == csamp[i]:
            exact = exact +1
            sample[i]=blank                
            csamp[i]=blank     

    for i in range(4):
        if sample[i] != blank:
            for j in range(4):
                if sample[i] == csamp[j]:
                    if sample[i] != blank:
                        sample[i]=blank                
                        csamp[j]=blank     
                        off = off + 1


    showcode(testarray)
    showscore(exact,off)
    time.sleep(3)
    if exact == 4:
        return(True)
    else:
        return(False)

compthink(1)
compthink2(10)
mkcode()

guess = 1 #creating code guess
testing = 2  #compare code to guess
test = 3  
ind = 0 #guess pixel index
clr = 0 #guess color

states = [guess, testing, test]
Done = False
state = guess

while not Done:
    val = 0
    if cp.touch_A1: #show code
        showcode(code)
        time.sleep(5)
        cp.pixels.fill(blank)
        cp.pixels.show()

    if cp.button_a:
        val = val + 1
    if cp.button_b:
        val = val + 2
   
    if state == guess:
        cp.pixels[cpix[ind]] = mcolors[clr]
        cp.pixels.show()

        if val == 1:
            clr = 3 & (clr+1)
        cp.pixels[cpix[ind]] = mcolors[clr]
        cp.pixels.show()
            
        if val == 2:
            ind = (ind + 1)
            if ind == 4:
                state = testing
                testarray = []
                for i in range(4):
                    testarray.append(cp.pixels[cpix[i]])
                showcode(testarray)
            
    if state == testing:
        Done = testit(code,testarray)
        if val == 1 or val ==2:
            state = guess
            showcode(testarray)
            time.sleep(1)
            ind = 0
            clr = 0
            
    time.sleep(.25)        
compthink(2)
compthink2(5)
