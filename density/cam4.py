import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from calculation4 import *

s4d=0
def detect4():

    im = cv2.imread('image/cam4.jpeg')
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    s4=int(label.count('car'))
    s4d=s4
    print("no of vehicles",s4)
    calculation4(s4d)
