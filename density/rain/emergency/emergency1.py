import soundmeter
import subprocess
import sys
import os
sys.path.append(os.path.abspath("/home/rahul/Desktop/final/density/"))


bashcommand= "soundmeter --trigger +20000 3 --action stop"
print("started")
output = subprocess.check_output(['bash','-c', bashcommand])
print(" emergency vehicle detected ")
green()


