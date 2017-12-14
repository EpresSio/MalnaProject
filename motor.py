import sys
import time
import RPi.GPIO as GPIO

mode = GPIO.getmode()

GPIO.cleanup()

R_1 = 26
R_2 = 20
L_1 = 19
L_2 = 16
sleeptime = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(R_1, GPIO.OUT)
GPIO.setup(R_2, GPIO.OUT)
GPIO.setup(L_1, GPIO.OUT)
GPIO.setup(L_2, GPIO.OUT)


def forward(x):
    GPIO.output(R_1, GPIO.HIGH)
    GPIO.output(L_1, GPIO.HIGH)
    print("Moving Forward")
    time.sleep(x)
    GPIO.output(R_1, GPIO.LOW)
    GPIO.output(L_1, GPIO.LOW)


def reverse(x):
    GPIO.output(R_2, GPIO.HIGH)
    GPIO.output(L_2, GPIO.HIGH)
    print("Moving Backward")
    time.sleep(x)
    GPIO.output(R_2, GPIO.LOW)
    GPIO.output(L_2, GPIO.LOW)

forward(1)

reverse(1)
GPIO.cleanup()