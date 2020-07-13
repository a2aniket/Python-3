import cv2
import numpy as np

face_classifer=cv2.CascadeClassifier("Haarcascades/haarcascade_frontalface_default.xml")

def face_extractore(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

