# coding: utf-8
import RPi.GPIO as GPIO
import time

SOUNDER = 18

DO = 262
RE = 294
MI = 330
FA = 349
SO = 392
RA = 440

A_MELO = [ DO, DO , SO , SO , RA , RA , SO ]
B_MELO = [ FA, FA , MI , MI , RE , RE , DO ]
C_MELO = [ SO, SO , FA , FA , MI , MI , RE ]
MELODY = [ A_MELO , B_MELO , C_MELO , C_MELO , A_MELO , B_MELO ]

GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUNDER, GPIO.OUT, initial = GPIO.LOW)

p = GPIO.PWM(SOUNDER, 1)
p.start(50)

i = 0
j = 0

while i < len(MELODY) :

    while j < len(MELODY[i]) :
        p.ChangeFrequency(MELODY[i][j]*2)
        time.sleep(0.5)
        j = j + 1

    time.sleep(0.5)
    j = 0
    i = i + 1

p.stop()
GPIO.cleanup()