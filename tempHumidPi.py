#---------
#Author: Jason E Sajovic
#Twitter: @JasonSajovic LinkedIn: https://www.linkedin.com/in/jasonsajovic email: jason@sajovic.net 
#Project: HALpi
#File: tempHumidity.py - The DHT11 sensor is used to measure the current temprature and humidity.
#Dependencies: dht11.py - Author: szazo --> dht11 python module https://github.com/szazo/DHT11_Python.git.
#Date: 06.02.2017
#dovVer: 1.0
#Python Version: 2.7.9

#Resources: Personal thanks goes out to szazo for his dht11 python module https://github.com/szazo/DHT11_Python.git
#Hardware Requirement: dht11 which is an inexpensive temp/humidity sensor that can be picked up from many online vendors.
#The DHT11 is not as accurate as a other sensors, but will do the job as long as you are not using it for mission critial decisions.
#----------

import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO. I prefer to use the GPIO.BOARD option as the BCM option can change more with newer verions of the Pi.
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

# read data using BOARD pin 7
instance = dht11.DHT11(pin=7)

#read temp and humidity data
count = 1
while (count == 1):
    result = instance.read()
    if result.is_valid():
        print "Temperature: %d F" % (result.temperature*1.8+32), ', %d C' % result.temperature
        print("Humidity: %d %%" % result.humidity)
	count = count - 1