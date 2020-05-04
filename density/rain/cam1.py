import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from calculation import *
from shot.control import *
s1d=0
cam1()
s=0

def detect():

    im = cv2.imread('image/cam11.jpeg')
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    s=int(label.count('car'))
    im = cv2.imread('image/cam12.jpeg')
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    s=s+int(label.count('car'))
    im = cv2.imread('image/cam13.jpeg')
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    s=s+int(label.count('car'))
    im = cv2.imread('image/cam14.jpeg')
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    s=s+int(label.count('car'))
   
    m=(s/4)
    print("no of vehicles1 ",m)
    calculation1(m)


