import soundmeter
import subprocess
import sys
import os
from led.led_one import*
import time

sys.path.append(os.path.abspath("/home/rahul/Desktop/tarffic/density/"))
from  green import  *


bashcommand= "soundmeter --trigger +1000 3 --action stop"


print(" emergency vehicle detected ")
output = subprocess.check_output(['bash','-c', bashcommand])
green1on()
yellow1off()
yellow2off()
yellow3off()
yellow4off()
red2on()
red3on()
red4on()
time.sleep(5)
