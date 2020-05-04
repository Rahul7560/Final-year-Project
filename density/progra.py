#rahul
from camera.camera import *
import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

s1d=0


def detect():

        im = cv2.imread('image/cam2.jpeg')
        bbox, label, conf = cv.detect_common_objects(im)
        output_image = draw_bbox(im, bbox, label, conf)
        plt.imshow(output_image)
        plt.show()
        s=int(label.count('car'))
        s1d=s
        print("no of vehicles1 ",s)


    

camera1short()

camera2short()

camera3short()

camera4short()

detect()


