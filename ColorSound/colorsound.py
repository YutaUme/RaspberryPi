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
	print("Hue:",hue)
	if(hue == 1):
		print("sound: C")
		p.ChangeFrequency(262)
		
	elif(hue == 2):
		print("sound: C#")
		p.ChangeFrequency(277)
		
	elif(hue == 3):
		print("sound: D")
		p.ChangeFrequency(294)
		
	elif(hue == 4):
		print("sound: D#")
		p.ChangeFrequency(311)
		
	elif(hue == 5):
		print("sound: E")
		p.ChangeFrequency(330)
		
	elif(hue == 6):
		print("sound: F")
		p.ChangeFrequency(349)
		
	elif(hue == 7):
		print("sound: F#")
		p.ChangeFrequency(370)
		
	elif(hue == 8):
		print("sound: G")
		p.ChangeFrequency(392)
		
	elif(hue == 9):
		print("sound: G#")
		p.ChangeFrequency(415)
		
	elif(hue == 10):
		print("sound: A")
		p.ChangeFrequency(440)
		
	elif(hue == 11):
		print("sound: A#")
		p.ChangeFrequency(466)
	
	elif(hue == 12):
		print("sound: B")
		p.ChangeFrequency(493)


## Main

t = 0


SOUNDER = 21 # GPIO番号
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUNDER,GPIO.OUT,initial=GPIO.LOW)

p = GPIO.PWM(SOUNDER,1)

p.start(100)

try:
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

		# ある閾値を見たすピクセルと抽出(中心付近のみ)
		for y in range(height):
			if((1/3)*height < y < (2/3)*height):
				for x in range(width):
					if((1/3)*width < x < (2/3)*width):
						if (img_hsv[y, x, 1] > 45 and 32 < img_hsv[y, x, 2]):
							pixels.append(img_hsv[y, x, 0])

		# Hue判定用に180を15ずつの区画に区切る
		bins = np.linspace(0, 180, 13)

		print(pixels)
		print(bins)

		if(pixels != []):
			index = np.digitize(pixels,bins)
			
			c = Counter(index)

			# 最頻値
			mode = c.most_common(1)

			sound(mode[0][0],p)

			print("times:",t)
			time.sleep(1)
			t = t + 1

finally:
	p.stop()
	GPIO.cleanup()



