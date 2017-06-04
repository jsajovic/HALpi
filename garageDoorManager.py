#---------
#Author: Jason E Sajovic
#Twitter: @JasonSajovic LinkedIn: https://www.linkedin.com/in/jasonsajovic email: jason@sajovic.net 
#Project: HALpi
#Garage door controller - Can be used stand alone or part of the HAP-Nodejs Apple Home Kit suite
#Date: 06.02.2017
#dovVer: 1.0

#Python Version: 2.7.9
#Hardware Requires: A 5V relay hardwired to the gargage motor. These can be added in parallel with a hardwired activator normally loaced by the $
#In my prototyle by garage motor in a ready state was 25VDC so my realy had to suppor this voltage. An OMR-C-105H from Radio Shack. A standard 5$

#----------

import RPi.GPIO as GPIO #import the GPIO library and allow Python to load the library whcih will give it access to the pins
from time import sleep #from the time module import the sleep function

#this is the pin variable, change it if your relay is on a different pin.
relay=36;

#In the follwoing code we will have the relay line defined above to set to low as our trigger. Once this happens it will open the relay itself a$
# to ground opening/closing the garage door.

GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay, GPIO.OUT) #This is the pin we are going to setup as a data out pin
GPIO.output(relay, GPIO.HIGH) #this is going to set the pin to high menaing it will cary a voltage in its ready state
GPIO.output(relay, GPIO.LOW) #once the pin is set to low it will close the circuit on the attached relay and tell the garage door to close/open
sleep(1) #hold the low position for 1 second
GPIO.output(relay, GPIO.HIGH) #rest the pin to its ready state
GPIO.cleanup() #cleanup all variables and running code.