# -*- coding:utf-8 -*-
import numpy as np
import cv2
from collections import Counter
import time
import RPi.GPIO as GPIO
import picamera
import sys




SOUNDER = 18 # GPIO番号
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUNDER,GPIO.OUT)

p = GPIO.PWM(18,int(sys.argv[1]))

print(p)
p.start(100)

p.ChangeFrequency(290)

time.sleep(2)

print(p)
p.ChangeFrequency(440)

time.sleep(2)

print(p)
p.ChangeFrequency(330)

p.stop()
GPIO.cleanup()
