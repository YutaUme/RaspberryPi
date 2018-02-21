# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import cv2
from collections import Counter
import winsound

def sound(hue):
	print(hue)
	if(hue == 1):
		print("C")
		winsound.Beep(262,1000)
	elif(hue == 2):
		print("C#")
		winsound.Beep(277,1000)
	elif(hue == 3):
		print("D")
		winsound.Beep(294,1000)
	elif(hue == 4):
		print("D#")
		winsound.Beep(311,1000)
	elif(hue == 5):
		print("E")
		winsound.Beep(330,1000)
	elif(hue == 6):
		print("F")
		winsound.Beep(349,1000)
	elif(hue == 7):
		print("F#")
		winsound.Beep(370,1000)
	elif(hue == 8):
		print("G")
		winsound.Beep(392,1000)
	elif(hue == 9):
		print("G#")
		winsound.Beep(415,1000)
	elif(hue == 10):
		print("A")
		winsound.Beep(440,1000)
	elif(hue == 11):
		print("A#")
		winsound.Beep(466,1000)
	elif(hue == 12):
		print("B")
		winsound.Beep(494,1000)


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

sound(mode[0][0])



