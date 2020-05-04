from cam1  import *
from cam2 import *
from cam3 import *
from cam4 import *
from green import *
from red import *
from yellow import *
from shot.control import *
import time

from led.led_one import *

import serial
import time

cam1()
arduinodata=serial.Serial('/dev/ttyACM0',9600)
time.sleep(2)
red1on()
red2on()
red3on()
red4on()


detect()




