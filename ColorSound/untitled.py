# -*- coding:utf-8 -*-
import numpy as np
import cv2
from collections import Counter
import time
import RPi.GPIO as GPIO
import picamera
import sys

import pigpio


SOUNDER = 18 # GPIO番号
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(SOUNDER,GPIO.OUT)

pin = pigpio.pi()
pin.set_mode(SOUNDER, pigpio.OUTPUT)
pin.hardware_PWM(SOUNDER, 0, 0)

# p = GPIO.PWM(18,int(sys.argv[1]))


pin.hardware_PWM(SOUNDER, 4000, 500000)

time.sleep(2)

pin.hardware_PWM(SOUNDER, 2000, 500000)

time.sleep(2)

pin.hardware_PWM(SOUNDER, 4000, 500000)


pin.hardware_PWM(SOUNDER, 0, 0)
pin.set_mode(SOUNDER, pigpio.INPUT)
pin.stop()
GPIO.cleanup()
