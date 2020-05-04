import time
from cam1 import *
from cam2 import *
from cam3 import *
from cam4 import *
import os
import sys
from led.led_one import *
from shot.control import *


def calculation3(x):
    i = 0
    red3off()

    if x >= 30:
        green3on()
        for i in range(0, 120):

            time.sleep(1)
            if i == 110:
                green3off()
                yellow3on()
                cam4()
        yellow3off()
        red3on()
        detect4()


    elif 20 <= x <= 30:
        green3on()
        for i in range(0, 80):
            time.sleep(1)
            if i == 70:
                green3off()
                yellow3on()
                cam4()
        yellow3off()
        red3on()
        detect4()
    elif 10 <= x <= 20:
        green2on()
        for i in range(0, 50):
            time.sleep(1)
            if i == 40:
                green3off()
                yellow3on()
                cam4()
        yellow3off()
        red3on()
        detect4()
    elif 5 <= x >= 10:
        green3on()
        for i in range(0, 30):
            time.sleep(1)
            if i == 20:
                green3off()
                yellow3on()
                cam4()
        yellow3off()
        red3on()
        detect4()
    elif 0 < x <= 5:
        green3on()
        for i in range(0, 15):
            time.sleep(1)
            if i == 8:
                green3off()
                yellow3on()
                cam4()
        yellow3off()
        red3on()
        detect4()

    elif 0 == x:
        cam4()
        red3on()
        detect4()
