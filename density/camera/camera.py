import subprocess
import sys
import os

camera1="fswebcam  -r 640x480 -F20 --set Sharpness100 -d  v4l2:/dev/video0 image/cam1.jpeg  -S10"
camera2="fswebcam -r 640x480 -F20 --set sharpness100 -d  v4l2:/dev/video1 image/cam2.jpeg -S10"
camera3="fswebcam -r 640x480 -F5  -d  v4l2:/dev/video5 image/cam3.jpeg -S10"
camera4="fswebcam -r 640x480 -F5 -d  v4l2:/dev/video3 image/cam4.jpeg -S10"

def camera1short():
    output = subprocess.check_output(['bash','-c', camera1])
    print("cam1 captured")
def camera2short():
    output = subprocess.check_output(['bash','-c', camera2])
    print("cam2 captured")
def camera3short():
    output = subprocess.check_output(['bash','-c', camera3])
    print("cam3 captured")
def camera4short():
    output = subprocess.check_output(['bash','-c', camera4])
    print("cam4 captured")
