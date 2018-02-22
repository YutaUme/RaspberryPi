# -*- coding:utf-8 -*-
import numpy as np
import cv2
from collections import Counter
import time
import RPi.GPIO as GPIO
import picamera


def capture():
  with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    #time.sleep(2) #カメラ初期化
    camera.capture('foo.jpg')



t = 0
while(1) :
	capture()
	print(t)
	time.sleep(1)
	t = t + 1

