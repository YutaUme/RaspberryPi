# -*- coding:utf-8 -*-
import numpy as np
import cv2
from collections import Counter
import time
import RPi.GPIO as GPIO
import picamera



SOUNDER = 21 # GPIO番号
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUNDER,GPIO.OUT,initial=GPIO.LOW)

p = GPIO.PWM(SOUNDER,1)

p.start(100)

p.ChangeFrequency(262)

time.sleep(2)

p.ChangeFrequency(440)

time.sleep(2)

p.ChangeFrequency(330)

p.stop()
GPIO.cleanup()
