import soundmeter
import subprocess
import sys
import os

sys.path.append(os.path.abspath("/home/rahul/Desktop/tarffic/density/"))
from green import *


bashcommand= "soundmeter --trigger +20000 3 --action stop"
pribt("software ready for vehicle detection")
print ("sound monitoring started")
output = subprocess.check_output(['bash','-c', bashcommand])
stop()

print(" emergency vehicle detected ")

green()


