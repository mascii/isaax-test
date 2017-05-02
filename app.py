#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(47, GPIO.OUT)

for i in range(1000):
    GPIO.output(47, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(47, GPIO.HIGH)
    time.sleep(0.2)

GPIO.cleanup()
