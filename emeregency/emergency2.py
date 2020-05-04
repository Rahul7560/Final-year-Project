import soundmeter
import subprocess
import sys
import os

sys.path.append(os.path.abspath("/home/vaisakh/Desktop/density/led/"))
from led_one import *


bashcommand= "soundmeter --trigger +20000 3 --action stop"
output = subprocess.check_output(['bash','-c', bashcommand])
print(" emergency vehicle detected ")
green2on()
