import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from calculation3 import *

s3d=0
def detect3():

    im = cv2.imread('image/cam3.jpeg')
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    s3=int(label.count('car'))
    s3d=s3
    print("number of vehicles",s3)
    calculation3(s3)
