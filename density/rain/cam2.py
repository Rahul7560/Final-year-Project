import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from calculation2 import *

s2d=0
def detect2():

    im = cv2.imread('image/cam22.jpeg')
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    s=s+int(label.count('car'))
    im = cv2.imread('image/cam23.jpeg')
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    s=s+int(label.count('car'))
    im = cv2.imread('image/cam23.jpeg')
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    s=s+int(label.count('car'))
    im = cv2.imread('image/cam24.jpeg')
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    s=s+int(label.count('car'))
    m=(s/4)
    print("no of vehicles1 ",m)
    calculation2(m)
