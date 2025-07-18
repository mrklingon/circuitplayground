# SPDX-FileCopyrightText: 2018 Anne Barela for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import audioio
import audiocore
import board
import neopixel
import random
from adafruit_crickit import crickit


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

color = [red,orange,gold,green,blue,white,pink]

def dodigit(digit,color):
    pixels.fill(blank)
    if digit != 0:
        for i in range(digit):
            pixels[i] = color
            pixels.show()
            time.sleep(.14)
    else:
        for i in range(10):
            pixels[i] = green
            pixels.show()
            time.sleep(.14)

    time.sleep(.5)
    pixels.fill(blank)

def blinknum(num,color):
    if num != 0:
        for i in range(num):
            pixels.fill(color)
            time.sleep(.25)
            pixels.fill(blank)
            time.sleep(.10)
    else:
        for i in range(10):
            pixels[i] = color
            pixels.show()
            time.sleep(.14)

        pixels.fill(blank)

def saydigit(digit,color):
    if (digit >= 0) and (digit <= 9):
        digit = int(digit)
        file = "digits/"+str(digit)+".wav"
        play_file(file)
        dodigit(digit,color)



def round(num):
    num = (int((num*100) +.5))/100
    return(num)

def showint(num):
    if num > 0:
        color = blue
    else:
        color = red
        play_file("digits/minus.wav")

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
        play_file("digits/minus.wav")


    nums = str(num)

    for i in range(len(nums)):
        if nums[i] != "-":
            if nums[i] != ".":
                saydigit(eval(nums[i]),color)
            else:
                play_file("digits/point.wav")
                blinknum(1,green)

advice = ["m8/asyes.wav","m8/count.wav","m8/hazy.wav","m8/sources.wav","m8/cannot.wav","m8/doubtful.wav","m8/outlook.wav","m8/yesdef.wav"]

texts = ["hello.wav","hello2.wav","niceday.wav"]
words = ["hello world", "hello", "have a nice day"]
# NeoPixels on the Circuit Playground Express Light Blue
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.3)
# Set audio out on speaker
speaker = audioio.AudioOut(board.A0)

# Start playing the file (in the background)
def play_file(wavfile):
    audio_file = open(wavfile, "rb")
    wav = audiocore.WaveFile(audio_file)
    speaker.play(wav)
    while speaker.playing:
        pass

def pick():  # create a random color
    return (random.randrange(200), random.randrange(200), random.randrange(200))

def wisdom():
    play_file(random.choice(advice))
    for i in range(10):
        pixels[i] = pick()
        time.sleep(.1)
        pixels.show()
    time.sleep(0.5)
    pixels.fill(pick())
    time.sleep(1)
    pixels.fill(0x0099FF)

def talk():
    p = random.randrange(3)
    print(words[p])
    play_file(texts[p])


# Fill them with our favorite color "#0099FF light blue" -> 0x0099FF
# (see http://www.color-hex.com/ for more colors and find your fav!)
pixels.fill(0x0099FF)

print("Hello world!")
play_file("hello.wav")       # play Hello World WAV file

while True:
    if crickit.touch_1.value:
        print("Touched Cap Touch Pad 1")
        talk()
        crickit.servo_1.angle = 75   # Set servo angle to 75 degrees
        time.sleep(1.0)              # do nothing for a 1 second
        crickit.servo_1.angle = 135  # Set servo angle to 135 degrees
        time.sleep(1.0+random.randrange(5))              # do nothing for a 1 second
    if crickit.touch_4.value:
        print("Touched Cap Touch Pad 4")
        wisdom()
        crickit.servo_1.angle = 75   # Set servo angle to 75 degrees
        time.sleep(1.0)              # do nothing for a 1 second
        crickit.servo_1.angle = 135  # Set servo angle to 135 degrees
        time.sleep(1.0+random.randrange(5))              # do nothing for a 1 second
    if crickit.touch_3.value:
        print("Touched Cap Touch Pad 3")
        shownum(22./7)
        crickit.servo_1.angle = 75   # Set servo angle to 75 degrees
        time.sleep(1.0)              # do nothing for a 1 second
        crickit.servo_1.angle = 135  # Set servo angle to 135 degrees
        time.sleep(1.0+random.randrange(5))              # do nothing for a 1 second
