# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import cv2
from collections import Counter
import time
import RPi.GPIO as GPIO

def sound(hue,p):
	print(hue)
	if(hue == 1):
		print("C")
		p.ChangeFrequency(262)
		p.start(100)
		p.stop()
	elif(hue == 2):
		print("C#")
		p.ChangeFrequency(277)
		p.start(100)
		p.stop()
	elif(hue == 3):
		print("D")
		p.ChangeFrequency(294)
		p.start(100)
		p.stop()
	elif(hue == 4):
		print("D#")
		p.ChangeFrequency(311)
		p.start(100)
		p.stop()
	elif(hue == 5):
		print("E")
		p.ChangeFrequency(330)
		p.start(100)
		p.stop()
	elif(hue == 6):
		print("F")
		p.ChangeFrequency(349)
		p.start(100)
		p.stop()
	elif(hue == 7):
		print("F#")
		p.ChangeFrequency(370)
		p.start(100)
		p.stop()
	elif(hue == 8):
		print("G")
		p.ChangeFrequency(392)
		p.start(100)
		p.stop()
	elif(hue == 9):
		print("G#")
		p.ChangeFrequency(415)
		p.start(100)
		p.stop()
	elif(hue == 10):
		print("A")
		p.ChangeFrequency(440)
		p.start(100)
		p.stop()
	elif(hue == 11):
		print("A#")
		p.ChangeFrequency(466)
		p.start(100)
		p.stop()
	elif(hue == 12):
		print("B")
		p.ChangeFrequency(493)
		p.start(100)
		p.stop()


SOUNDER = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUNDER,GPIO.OUT,initial=GPIO.LOW)

p = GPIO.PWM(SOUNDER,1)

# 画像を読み込み
img_scr = cv2.imread("tomato.jpg")

# BGR->HSV に変換
img_hsv = cv2.cvtColor(img_scr, cv2.COLOR_BGR2HSV)

height = img_hsv.shape[0]
width = img_hsv.shape[1]

pixels = []

for y in range(height):
	for x in range(width):
		if (img_hsv[y, x, 1] > 45 and 32 < img_hsv[y, x, 2]):
			pixels.append(img_hsv[y, x, 0])

plt.xlim(0,180)
plt.xticks([0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180])
plt.hist(pixels, bins=12, range=(0,180), align="mid",rwidth=1.0,color="blue")

bins = np.linspace(0, 180, 13)
# print(bins)
index = np.digitize(pixels,bins)
c = Counter(index)
# print (c)
mode = c.most_common(1)



sound(mode[0][0],p)



