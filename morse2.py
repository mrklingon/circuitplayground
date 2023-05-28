## morse code module
from adafruit_circuitplayground import cp
import time

DASH = [1,0,9,8]
DOT = [0,9]
FLASH = [1,8]

fc = (6,8,1)
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
   for myletter in message.upper():
      try:
          if myletter != ' ':
             my_cipher += MORSE_CODE_DICT[myletter] + '  '
          else:
             my_cipher += ' '
      except:
          my_cipher += ' '
          
   return my_cipher


#dot
def dot():
    for i in DOT:
        cp.pixels[i] = dtc
    time.sleep(.1)
    
    for i in DOT:
        cp.pixels[i] = blank
    time.sleep(.1)

#flash - at end of letter
def flash():
    for i in FLASH:
        cp.pixels[i] = fc
    time.sleep(.1)
    
    for i in FLASH:
        cp.pixels[i] = blank
    time.sleep(.1)

    
#dash
def dash():
    for i in DASH:
        cp.pixels[i] = dc
    time.sleep(.2)
    
    for i in DASH:
        cp.pixels[i] = blank
    time.sleep(.1)  

def blinkcode(code):
    for chr in code:
        if (chr == "-"):
            dash()
        if (chr =="."):
            dot()
        if (chr == " "):
            flash()
