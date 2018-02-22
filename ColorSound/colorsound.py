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

def sound(hue,p):
	print(hue)
	if(hue == 1):
		print("sound: C")
		p.ChangeFrequency(262)
		p.start(100)
		p.stop()
	elif(hue == 2):
		print("sound: C#")
		p.ChangeFrequency(277)
		p.start(100)
		p.stop()
	elif(hue == 3):
		print("sound: D")
		p.ChangeFrequency(294)
		p.start(100)
		p.stop()
	elif(hue == 4):
		print("sound: D#")
		p.ChangeFrequency(311)
		p.start(100)
		p.stop()
	elif(hue == 5):
		print("sound: E")
		p.ChangeFrequency(330)
		p.start(100)
		p.stop()
	elif(hue == 6):
		print("sound: F")
		p.ChangeFrequency(349)
		p.start(100)
		p.stop()
	elif(hue == 7):
		print("sound: F#")
		p.ChangeFrequency(370)
		p.start(100)
		p.stop()
	elif(hue == 8):
		print("sound: G")
		p.ChangeFrequency(392)
		p.start(100)
		p.stop()
	elif(hue == 9):
		print("sound: G#")
		p.ChangeFrequency(415)
		p.start(100)
		p.stop()
	elif(hue == 10):
		print("sound: A")
		p.ChangeFrequency(440)
		p.start(100)
		p.stop()
	elif(hue == 11):
		print("sound: A#")
		p.ChangeFrequency(466)
		p.start(100)
		p.stop()
	elif(hue == 12):
		print("sound: B")
		p.ChangeFrequency(493)
		p.start(100)
		p.stop()





## Main

t = 0

SOUNDER = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUNDER,GPIO.OUT,initial=GPIO.LOW)

p = GPIO.PWM(SOUNDER,1)

while(1) :
	
	#撮影
	capture()

	# 画像を読み込み
	img_scr = cv2.imread("foo.jpg")

	# BGR->HSV に変換
	img_hsv = cv2.cvtColor(img_scr, cv2.COLOR_BGR2HSV)

	height = img_hsv.shape[0]
	width = img_hsv.shape[1]

	# ピクセル抽出用の配列
	pixels = []

	# ある閾値を見たすピクセルと抽出
	for y in range(height):
		for x in range(width):
			if (img_hsv[y, x, 1] > 45 and 32 < img_hsv[y, x, 2]):
				pixels.append(img_hsv[y, x, 0])

	# Hue判定用に180を15ずつの区画に区切る
	bins = np.linspace(0, 180, 13)

	index = np.digitize(pixels,bins)
	
	c = Counter(index)

	# 最頻値
	mode = c.most_common(1)

	sound(mode[0][0],p)

	print("times:",t)
	time.sleep(1)
	t = t + 1




