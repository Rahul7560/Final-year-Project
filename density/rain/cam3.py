import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from calculation3 import *

s3d=0
def detect3():

    im = cv2.imread('image/cam31.jpeg')
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    s=int(label.count('car'))
    im = cv2.imread('image/cam32.jpeg')
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    s=s+int(label.count('car'))
    im = cv2.imread('image/cam33.jpeg')
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    s=s+int(label.count('car'))
    im = cv2.imread('image/cam34.jpeg')
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    s=s+int(label.count('car'))
    m=(s/4)
    print("no of vehicles1 ",m)
    calculation3(m)
