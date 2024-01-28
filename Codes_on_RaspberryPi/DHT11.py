"""
this is a test file to see if DHT11 is working okay or not.
in order to make it work, you should already have the required repo.
"""


#!/usr/bin/python
import sys
import Adafruit_DHT

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 25)

    print ('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))