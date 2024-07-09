from adafruit_circuitplayground import cp
import time
import random
import board

state=0

temp = 0
light = 1
gees = 2

sound = ["digits/temp.wav", "digits/light.wav", "digits/gees.wav"]

state = temp
cp.play_file(sound[state])

blue = (0,0,8)
blank = (0,0,0)
green  = (0,20,0)
red = (20,0,0)
white = (20,20,20)
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
def saytemp():
    temp = cp.temperature
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

saytemp()

while True:
    d = getdir()
    if cp.button_a:
        state = state + 1
        if state > gees:
            state = temp
        cp.play_file(sound[state])

    if cp.button_b:
        if state == temp:
            saytemp()
        if state == light:
            saylight()
        if state == gees:
            saygees()

    if d != "":
        print (d)
    time.sleep(.2)
