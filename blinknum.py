## morse code module
from adafruit_circuitplayground import cp
import time
import microcontroller

red = (7,0,0)
green = (0,7,0)
blue = (0,0,7)
blank = (0,0,0)


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

def saydigit(digit,color):
    if (digit >= 0) and (digit <= 9):
        digit = int(digit)
        file = "digits/"+str(digit)+".wav"
        cp.play_file(file)
        dodigit(digit,color)



def round(num):
    num = (int((num*100) +.5))/100
    return(num)

def showint(num):
    if num > 0:
        color = blue
    else:
        color = red
        cp.play_file("digits/minus.wav")

    nums = str(num)
    
    for i in range(len(nums)):
        if nums[i] != "-":
            if nums[i] != ".":
                saydigit(eval(nums[i]),color)
            else:
                blinknum(1,green)

def shownum(num):
    num = round(num)
    if num > 0:
        color = blue
    else:
        color = red
        cp.play_file("digits/minus.wav")


    nums = str(num)
    
    for i in range(len(nums)):
        if nums[i] != "-":
            if nums[i] != ".":
                saydigit(eval(nums[i]),color)
            else:
                cp.play_file("digits/point.wav")
                blinknum(1,green)
                
def saytemp():
    temp = microcontroller.cpu.temperature
    if cp.switch:
        temp = 32 + (temp * 7)/5
    print (temp)
    shownum(temp)
    
def saylight():
    light = cp.light
    print (light)
    shownum(light)
    
def saygees():
    x,y,z = cp.acceleration
    print (str(x) + " x")
    shownum(x)
    print (str(y) + " y")
    shownum(y)
    print (str(z) + " z")
    shownum(z)
    