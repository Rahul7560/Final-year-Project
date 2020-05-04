import soundmeter
import subprocess
import sys
import os
import  threading 
import time



class traffic (threading.Thread):
    def run(self):
        bashcommand= "python3 comparison.py"
        output = subprocess.check_output(['bash','-c', bashcommand])    
        print("traffic running")

class emergency(threading.Thread):
    def run(self):
        bashcommand= "python3 emergency.py"
        print("emergency detected")
        output = subprocess.check_output(['bash','-c', bashcommand])    
        print("emergency detected")
        t1.terminate()
t1 = traffic()
t2 = emergency()

t1.start()
time.sleep(50)
t2.start()

def stop():
    t1.stop()
