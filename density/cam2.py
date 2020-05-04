import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from calculation2 import *

s2d=0
def detect2():

    im = cv2.imread('image/cam2.jpeg')
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    s2=int(label.count('car'))
    s2d=s2
    print("no of vehicles2",s2)
    calculation2(s2)
