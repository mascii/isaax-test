#!/usr/bin/env python3
import time
import wiringpi as w 
w.wiringPiSetup()
w.pinMode(0,1)
w.digitalWrite(0,1)
time.sleep(1)
w.digitalWrite(0,0)
