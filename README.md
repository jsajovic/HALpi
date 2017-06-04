# HALpi
This repo has several automation sensor packages built on the Raspberry Pi 3. All dependencies are included with the exception of Wiring Pi that need to be added seperately if you want to use LCD/displays with your project http://wiringpi.com/download-and-install/. Also, if you want to use Apple Home Kit as the desired unified framework the HAP-nodejs community can enable the bridge between sensors and automation. A good channel to bootstrap you project is https://www.youtube.com/channel/UC3AGxC2YOkov8pIchTHRqQw/featured

File Breakdown:
  
  garbagePi.py:
  
      #Author: Jason E Sajovic
      #Twitter: @JasonSajovic LinkedIn: https://www.linkedin.com/in/jasonsajovic email: jason@sajovic.net 
      #Project: HALpi
      #File: garbage.py - This script runs as part of a polling job of your choice, or triggered as a single action to read back the 
      current state of the garbage can. i.e. It is in its proper place or not.
      #Date: 06.02.2017
      #dovVer: 1.0
      #Python Version: 2.7.9

      #Notes: This project uses an ultra sonic sensor to measure the distance between the wall and the garbage cans. In my case my garbage 
      cans have a specific place in my garage, and therefore if they are not in that place I woudl assume that they are
      #at the curb to be taken out. I chose this method as RFID tagging would be more expensive, but more accurate as long as the garbage 
      cans are withing range of the RFID sensor.

      #Hardware Requirements: Ultrasonic sensor HC-SR04 was the one I used. It was very inexpensive for a pack of 10. You will also need 
      two resistors for the voltage devider on the ECHO pin. This is required
      #so a 5V burst is not sent to the RaspberryPi GPIO pin, and you dont need that much voltage to read the pin set.

      #Resources: All credit goes to Gaven MacDonald for his great video explaination --> https://youtu.be/xACy8l3LsXI
 
 recyclePi.py:
  
      #Author: Jason E Sajovic
      #Twitter: @JasonSajovic LinkedIn: https://www.linkedin.com/in/jasonsajovic email: jason@sajovic.net 
      #Project: HALpi
      #File: recycle.py - This script runs as part of a polling job of your choice, or triggered as a single action to read back the 
      current state of the recycle can. i.e. It is in its proper place or not.
      #Date: 06.02.2017
      #dovVer: 1.0
      #Python Version: 2.7.9

      #Notes: This project uses an ultra sonic sensor to measure the distance between the wall and the recycle can. In my case my recycle 
      can have a specific place in my garage, and therefore if they are not in that place I woudl assume that they are
      #at the curb to be taken out. I chose this method as RFID tagging would be more expensive, but more accurate as long as the recycle 
      can is within range of the RFID sensor.

      #Hardware Requirements: Ultrasonic sensor HC-SR04 was the one I used. It was very inexpensive for a pack of 10. You will also need  
      two resistors for the voltage devider on the ECHO pin. This is required
      #so a 5V burst is not sent to the RaspberryPi GPIO pin, and you dont need that much voltage to read the pin set.

      #Resources: All credit goes to Gaven MacDonald for his great video explaination --> https://youtu.be/xACy8l3LsXI
  
  smsModule.py:
  
      #Author: Jason E Sajovic
      #Twitter: @JasonSajovic LinkedIn: https://www.linkedin.com/in/jasonsajovic email: jason@sajovic.net 
      #Project: HALpi
      #File: smsModule.py - SMS Outbound API trigger using Aspect/Voxeo SMS staging API. This module was built to be used from within 
      other Python scripts to deliver context based messages.
      #Date: 06.02.2017
      #dovVer: 1.0
      #Python Version: 2.7.9

      #Notes: The defined module receives a single text input. There for an example of this input from another python script would look 
      like:
      #smsModule.smsMessage ("Take out the Garbage"). Make sure that you are including the module which looks like the following: import 
      smsModule
      #The function can be directly imported if desired by using something similar to import smsMessage from smsModule 
 
 garageDoorManager.py:
      #Author: Jason E Sajovic
      #Twitter: @JasonSajovic LinkedIn: https://www.linkedin.com/in/jasonsajovic email: jason@sajovic.net 
      #Project: HALpi
      #Garage door controller - Can be used stand alone or part of the HAP-Nodejs Apple Home Kit suite
      #Date: 06.02.2017
      #dovVer: 1.0

      #Python Version: 2.7.9
      #Hardware Requires: A 5V relay hardwired to the gargage motor. These can be added in parallel with a hardwired activator normally 
      loaced by the $
      #In my prototyle by garage motor in a ready state was 25VDC so my realy had to suppor this voltage. An OMR-C-105H from Radio Shack.
      A standard 5$

smsOutbound.py

      #Author: Jason E Sajovic
      #Twitter: @JasonSajovic LinkedIn: https://www.linkedin.com/in/jasonsajovic email: jason@sajovic.net 
      #Project: HALpi
      #File: smsOutbound.py - SMS Outbound API trigger using Aspect/Voxeo SMS staging API
      #Date: 06.02.2017
      #dovVer: 1.0
      #Python Version: 2.7.9

      #Notes: You need an Aspect Evolution account with outbound SMS anabled in order to use this API. Once you ahve an account then 
      create an SMS enabled application and the start document contents can be
      #empty, but one muct be selected to save the application. Once the application is made in Evolution a botKey will be generated. This 
      botKey is required to use the API along with an Evolution user name an$
      #Aspect SMS API documentation --> http://help.voxeo.com/go/help/evolution.apis.sms.api.postapi
 
 tempHumidPi.py
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
  
  dht11.py
  
      #Adding module author information 
      #Personal thanks goes out to szazo for his dht11 python module https://github.com/szazo/DHT11_Python.git

