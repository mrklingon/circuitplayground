
from adafruit_circuitplayground import cp
import time
import random
import board

DASH = [1,0,9,8]
DOT = [0,9]

dc = (0,0,40)
dtc= (0,40,0)
blank = (0,0,0)

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ',':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-'
}
def encryption(message):
   my_cipher = ''
   for myletter in message:
      if myletter != ' ':
         my_cipher += MORSE_CODE_DICT[myletter] + '  '
      else:
         my_cipher += ' '
         
   return my_cipher


#dot
def dot():
    for i in DOT:
        cp.pixels[i] = dtc
    time.sleep(.25)
    
    for i in DOT:
        cp.pixels[i] = blank
    time.sleep(.25)
    
#dash
def dash():
    for i in DASH:
        cp.pixels[i] = dc
    time.sleep(.75)
    
    for i in DASH:
        cp.pixels[i] = blank
    time.sleep(.25)  

def blinkcode(code):
    for chr in code:
        if (chr == "-"):
            dash()
        if (chr =="."):
            dot()
        else:
            time.sleep(.25)


while True:
        
    txt = input("?")
    print (encryption(txt.upper()))
    blinkcode(encryption(txt.upper()))

