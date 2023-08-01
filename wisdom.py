from adafruit_circuitplayground import cp
import time
import random
from blinknum import *


def file_len(filename):
    with open(filename) as f:
        for i, _ in enumerate(f):
            pass
    return i + 1

def wisdom(num,filename):
    qs = open(filename)
    for i in range(num+1):
        quote = qs.readline()
    print(quote)
    qs.close()
    return quote

lines = file_len("wisdom.txt")

while True:
    if cp.button_a:
        num = random.randrange(lines)
        quote = wisdom(num,"wisdom.txt")# Write your code here :-)
    time.sleep(.1)

