import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from calculation import *
from shot.control import *
s1d=0
cam1()

def detect():

    im = cv2.imread('image/cam1.jpeg')
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    s=int(label.count('car'))
    s1d=s
    print("no of vehicles1 ",s)
    calculation1(s)


