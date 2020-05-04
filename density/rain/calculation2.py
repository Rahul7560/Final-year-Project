import time
from cam1 import *
from cam2 import *
from cam3 import *
import os
import sys
from led.led_one import *
from shot.control import *


def calculation2(x):
    i = 0
    red2off()

    if x >= 30:
        green2on()
        for i in range(0, 120):

            time.sleep(1)
            if i == 110:
                green2off()
                yellow2on()
                cam3()
        yellow2off()
        red2on()
        detect3()


    elif 20 <= x <= 30:
        green2on()
        for i in range(0, 80):
            time.sleep(1)
            if i == 70:
                green2off()
                yellow2on()
                cam3()
        yellow2off()
        red2on()
        detect3()
    elif 10 <= x <= 20:
        green2on()
        for i in range(0, 50):
            time.sleep(1)
            if i == 40:
                green2off()
                yellow2on()
                cam3()
        yellow2off()
        red2on()
        detect3()

    elif 5 <= x <= 10:
        green2on()
        for i in range(0, 30):
            time.sleep(1)
            if i == 20:
                green2off()
                yellow2on()
                cam3()
        yellow2off()
        red2on()
        detect3()
    elif 0 < x <= 5:
        green2on()
        for i in range(0, 15):
            time.sleep(1)
            if i == 8:
                green2off()
                yellow2on()
                cam3()
        yellow2off()
        red2on()
        detect3()
    elif 0 == x:
        cam3()
        red2on()
        detect3()
