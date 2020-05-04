import soundmeter
import subprocess
import sys
import os
import signal
import  threading 
import time
a=0

def stop1():
    stop="xterm -hold -e pkill -f 'comparison.py'"
    #subprocess.call_in_new_window('python bb.py', shell=True)
    p = subprocess.check_output(['bash','-c', stop])

    


class traffic (threading.Thread):
    def run(self):
        bashcommand1= "gnome-terminal -e 'python3 comparison.py'"
        print("traffic running")
        p = subprocess.Popen(['bash','-c', bashcommand1])
        a=p.pid
        print(a)
        
        print("traffic running")
            


class emergency(threading.Thread):
    def run(self):
        print("emergency  start detected")
        bashcommand2= "python3 emergency.py"
        output = subprocess.check_output(['bash','-c', bashcommand2])    
        print("emergency detected")
        os.system("pkill -f comparison.py")
        time.sleep(10)
        
        if not t1.is_alive():
            bashcommand1= "gnome-terminal -e 'python3 comparison.py'"
            print("traffic running")
            p = subprocess.Popen(['bash','-c', bashcommand1])
        print("ended")
        
        
        

        
        
t1 = traffic()
t2 = emergency()

t1.start()
time.sleep(5)
t2.start()


