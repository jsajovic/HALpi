#---------
#Author: Jason E Sajovic
#Twitter: @JasonSajovic LinkedIn: https://www.linkedin.com/in/jasonsajovic email: jason@sajovic.net 
#Project: HALpi
#File: garbage.py - This script runs as part of a polling job of your choice, or triggered as a single action to read back the current state of the garbage can. i.e. It is in its proper place or not.
#Date: 06.02.2017
#dovVer: 1.0
#Python Version: 2.7.9

#Notes: This project uses an ultra sonic sensor to measure the distance between the wall and the garbage cans. In my case my garbage cans have a specific place in my garage, and therefore if they are not in that place I woudl assume that they are
#at the curb to be taken out. I chose this method as RFID tagging would be more expensive, but more accurate as long as the garbage cans are withing range of the RFID sensor.

#Hardware Requirements: Ultrasonic sensor HC-SR04 was the one I used. It was very inexpensive for a pack of 10. You will also need two resistors for the voltage devider on the ECHO pin. This is required
#so a 5V burst is not sent to the RaspberryPi GPIO pin, and you dont need that much voltage to read the pin set.

#Resources: All credit goes to Gaven MacDonald for his great video explaination --> https://youtu.be/xACy8l3LsXI
#----------


#This module that we build in the last lesson is added if you want to send a text message letting you know the state of your garbage cans so you can take action if needed.
import smsModule
#----- Import and Set the GPIO pins and import time as well will need to perform measurements.
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

#Set Pin out connection based on Pin number and not using GPIO numbering
TRIG=15
ECHO=18

#Setup our pins ready state
GPIO.setup(TRIG,GPIO.OUT)
GPIO.output(TRIG,0)
GPIO.setup(ECHO,GPIO.IN) #pull down resister is not required as it is connected to ground and will do the job of pulling it to ground when it is not in use
time.sleep(0.1) # This is in ms so this is 100ms which is more than enough for the 50ms cycle period

# The following will tell the sensor to poll by pulling up the TRIG for 10 microSeconds. After this the sensor will begin sending an 8 cycle burst
print "Starting Measurement..."
GPIO.output(TRIG,1) # Set trigger High
time.sleep(0.00001) # Wait 10 micro seconds
GPIO.output(TRIG,0) # Set Trigger Low

#Now we need to listen to the input pin. Because this will happen incredably fast we have to be as efficent as possible with the code
while GPIO.input(ECHO) == 0: # the while loop will continue until the input becomes high. When it does the start signal has arived and we start the timer
	pass #while in teh loop the pass command symply says to do nothing which means the program spends most of its time looking at the status of the pins
start = time.time() #expresses the current time in seconds

while GPIO.input(ECHO) == 1: #once the signal is low the signal has ended
	pass
stop = time.time()

#print (stop - start) * 17000 # now that we know the start and stop times we can determine the length of the pulse. We multiply by 17000 whics is the speed of sound divided by 2 because there is the first pulse and then the return pulse. So we will do this using the following equation
# Speed = distance divided by time
# 340 (This is the speed of sound in m/s) = 2d divided by time
# d= 170 * time if we want to print the distance in cm then we would multiply by 100

distance = (stop - start) * 17000
print (distance)

GPIO.cleanup() #this will reset all the GPIO pins to another polling

#Now determine if the garbage can is still in its spot or if it is out at the curb.
if (distance < 10):
	print ("Take out the Garbage")
else:
	print ("The garbage is out at the curb")

#If you want this script to text you  the garbage position to you then call the smsModule.py script and pass the text you want for your message

if (distance < 10):
        smsModule.smsMessage ("Take out the Garbage")
else:
        smsModule.smsMessage ("The garbage is out at the curb")
