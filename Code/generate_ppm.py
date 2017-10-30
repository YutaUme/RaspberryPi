
#-*- cording: utf-8 -*-
#encoding:UTF-8
import os
import feedparser
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
#encoding:UTF-8
import feedparser
import sys #モジュールargv
import time
argvs = sys.argv #コマンドライン引数を格納したリストの取得
argc = len(argvs) #引数の長さ min:1

#print argvs
#print argc



#############################################
#下のダブルクォーテーションの中に表示させたい文字を記入してください
#ここでは3つの文字列を順に出しています．
#色はRGBで(255,0,255)のように表現できます．
#############################################
Text1 = unicode("")
Text2 = unicode("")
Text3 = unicode("")

text = ((u"    " + news1,(255,0,255)),(u"    " + news2,(0,255,255)),(u"    " + news3,(0,255,0)))

font = ImageFont.truetype("/usr/share/fonts/truetype/takao-mincho/TakaoMincho.ttf", 16)
all_text = ""
for text_color_pair in text:
    t = text_color_pair[0]
    all_text = all_text + t

#print(all_text)
width, ignore = font.getsize(all_text)
#print(width)


im = Image.new("RGB", (width + 30, 16), "black")
draw = ImageDraw.Draw(im)

x = 0;
for text_color_pair in text:
    t = text_color_pair[0]
    c = text_color_pair[1]
    #print("t=" + t + " " + str(c) + " " + str(x))
    draw.text((x, 0), t, c, font=font)
    x = x + font.getsize(t)[0]

im.save("test.ppm")