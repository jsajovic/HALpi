#---------
#Author: Jason E Sajovic
#Twitter: @JasonSajovic LinkedIn: https://www.linkedin.com/in/jasonsajovic email: jason@sajovic.net 
#Project: HALpi
#File: smsModule.py - SMS Outbound API trigger using Aspect/Voxeo SMS staging API. This module was built to be used from within other Python scripts to deliver context based messages.
#Date: 06.02.2017
#dovVer: 1.0
#Python Version: 2.7.9

#Notes: The defined module receives a single text input. There for an example of this input from another python script would look like:
#smsModule.smsMessage ("Take out the Garbage"). Make sure that you are including the module which looks like the following: import smsModule
#The function can be directly imported if desired by using something similar to import smsMessage from smsModule 
#----------

import requests

def smsMessage(text):
	#------ Static Parameters ----------
	#These parameters will not change as long as you are using the same evolution account. the SMSapiURL is pointing to the staging SMS gateway. If this were a production application then you woudl point it $

	evoUserName='' #Insert Aspect Evolution Username between ticks
	evoPassword='' #Insert Aspect Evolution Password between ticks
	SMSapiURL='http://api.messaging.staging.voxeo.net/1.0/messaging'

	#------ Dynamic Parameters ---------
	#The following array are the API parameters that are required for outbound SMS. The following is a breakdown of each one. A description of each parameter is found here http://help.voxeo.com/go/help/evolu$
	
	#Insert Evolution botkey between ticks 
	#insert user or destination mobile between user ticks
	#Insert from or Evolution SMS enabled DID that is assigned to your evolution application between the ticks 
	data = ({'botkey':'', 'apimethod':'send', 'msg':text, 'user':'','network':'SMS','from':''})

	#------ Execute Outbound SMS to Aspect SMS Gateway --------
	SMSout = requests.get(SMSapiURL, params=(data), auth=(evoUserName, evoPassword))

	#------ Display Results -------
	print (SMSout.status_code)
	print (SMSout.headers)
	print (SMSout.url)