from rain.cam1  import *
from rain.cam2 import *
from rain.cam3 import *
from rain.cam4 import *
from rain.green import *
from rain.red import *
from rain.yellow import *
from rain.shot.control import *
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




