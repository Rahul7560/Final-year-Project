
import time
from cam1  import *
from cam2 import *
from cam3 import *
from cam4 import *
import os
import sys
from led.led_one import *
def calculation4(x):
    i = 0
    red4off()

    if x >= 30:
        green4on()
        for i in range(0, 120):

            time.sleep(1)
            if i == 110:
                green4off()
                yellow4on()
        yellow4off()
        red4on()
        detect()


    elif 20 <= x <= 30:
        green4on()
        for i in range(0, 80):
            time.sleep(1)
            if i == 70:
                green4off()
                yellow4on()
        yellow4off()
        red4on()
        detect()
    elif 10 <= x <= 20:
        green4on()
        for i in range(0, 50):
            time.sleep(1)
            if i == 40:
                green4off()
                yellow4on()
        yellow4off()
        red4on()
        exit()
        detect()
    elif 5 <= x >= 10:
        green4on()
        for i in range(0, 30):
            time.sleep(1)
            if i == 20:
                green4off()
                yellow4on()
        yellow4off()
        red4on()
        detect()
    elif 0 < x <= 5:
        green4on()
        for i in range(0, 15):
            time.sleep(1)
            if i == 8:
                green4off()
                yellow4on()
        yellow4off()
        red4on()
        detect()
    elif 0 == x:
        red4on()
        detect()

