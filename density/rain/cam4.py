import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from calculation4 import *

s4d=0
def detect4():

   im = cv2.imread('image/cam41.jpeg')
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    s=int(label.count('car'))
    im = cv2.imread('image/cam42.jpeg')
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    s=s+int(label.count('car'))
    im = cv2.imread('image/cam43.jpeg')
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    s=s+int(label.count('car'))
    im = cv2.imread('image/cam44.jpeg')
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    s=s+int(label.count('car'))
    m=(s/4)
    print("no of vehicles1 ",m)
    calculation4(m)
