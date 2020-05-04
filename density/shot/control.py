#resource = urllib.urlretrieve("http://192.168.43.1:8080/photo.jpg")
import urllib.request
import os

def cam1():

    cam1 = "http://192.168.43.1:8080/photo.jpg" #Your url goes here
    urllib.request.urlretrieve(cam1,'/home/rahul/Desktop/final/density/image/cam1.jpeg')
    
def cam2():
    cam2="http://192.168.43.1:8080/photo.jpg"
    urllib.request.urlretrieve(cam2,'/home/rahul/Desktop/final/density/image/cam2.jpeg')
    
def cam3():
    cam3="http://192.168.43.1:8080/photo.jpg"
    urllib.request.urlretrieve(cam3,'/home/rahul/Desktop/final/density/image/cam3.jpeg')
    
def cam4():
    cam4="http://192.168.43.1:8080/photo.jpg"
    urllib.request.urlretrieve(cam4,'/home/rahul/Desktop/final/density/image/cam4.jpeg')
    
