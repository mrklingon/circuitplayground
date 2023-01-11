# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

from adafruit_circuitplayground import cp
import time
import random
import board
import pwmio
from adafruit_motor import servo
saber = False
cp.detect_taps = 2

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

def wave():
    for x in range(10):
            r = random.randrange(50)
            g = random.randrange(30)
            b = random.randrange(90)
            cp.pixels[x] = (r,g,b)
            time.sleep(0.1)

        
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for x in range(10):
        time.sleep(0.1)
        cp.pixels[x] = (0, 0, 0)


Tech = ["ST/Enterprise Doors.wav","ST/tng_tricorder9.wav  ","ST/Transporter Beam.wav"]
Talking = ["ST/1x14-beverlyshutupwesley-e.wav","ST/Communicator.wav ","ST/Console beeps 12.wav","ST/Console beeps 3.wav","ST/Console beeps.wav","ST/wouldyoumindidentifyingwhatyouare.wav","ST/raiseallshieldsphasersatready.wav", "ST/makeitso.wav","ST/acknowledge.wav", "ST/engage.wav"]
while True:
    if cp.switch:
        if cp.touch_A3:
            cp.play_file("ST/tng_tricorder9.wav")
                
        if (cp.shake(shake_threshold=12) or (cp.button_a and cp.button_b)):
            if saber == False:
                saber = True
                r = random.randrange(50)
                g = random.randrange(30)
                b = random.randrange(90)

                cp.play_file("ST/Transporter Beam.wav")
                for x in range(10):
                    time.sleep(0.1)
                    cp.pixels[x] = (r,g,b)
                    
                saber = False
                for x in range(10):
                    time.sleep(0.1)
                    cp.pixels[x] = (0, 0, 0)
                
        if cp.button_a:
            a = random.randrange(3)
            cp.play_file(Tech[a])

        if cp.button_b:
            a = random.randrange(10)
            cp.play_file(Talking[a])
        
        if cp.light < 25:
            wave()
        
        if cp.touch_A1:        
            cp.play_file("ST/makeitso.wav")

        if cp.touch_A4:        
            cp.play_file("ST/Console beeps.wav")
            wave()
     
    else:
         r = random.randrange(6)
         
         if saber:
            saber = False
            for x in range(10):
                time.sleep(0.1)
                cp.pixels[x] = (0, 0, 0)
                
            
         if r == 0:
             wave()
             
         if r == 1:
             if saber == False:
                saber = True
                r = random.randrange(50)
                g = random.randrange(30)
                b = random.randrange(90)

                cp.play_file("ST/Transporter Beam.wav")
                for x in range(10):
                    time.sleep(0.1)
                    cp.pixels[x] = (r,g,b)
                                   
         if r == 2:
            a = random.randrange(2)   
            cp.play_file(Tech[a])             

         if r == 3:
            a = random.randrange(10)
            cp.play_file(Talking[a])
            if a >= 3 and a<=5 :
                wave()
              

         if r == 4:
             cp.play_file("ST/Enterprise Doors.wav")
              
              
         time.sleep(random.randrange(3)+1)
