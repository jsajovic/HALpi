#---------
#Author: Jason E Sajovic
#Twitter: @JasonSajovic LinkedIn: https://www.linkedin.com/in/jasonsajovic email: jason@sajovic.net 
#Project: HALpi
#File: smsOutbound.py - SMS Outbound API trigger using Aspect/Voxeo SMS staging API
#Date: 06.02.2017
#dovVer: 1.0
#Python Version: 2.7.9

#Notes: You need an Aspect Evolution account with outbound SMS anabled in order to use this API. Once you ahve an account then create an SMS enabled application and the start document contents can be
#empty, but one muct be selected to save the application. Once the application is made in Evolution a botKey will be generated. This botKey is required to use the API along with an Evolution user name an$
#Aspect SMS API documentation --> http://help.voxeo.com/go/help/evolution.apis.sms.api.postapi
#----------

#Import the requests module to enable the get against the API
import requests
import sys

#------ Static Parameters ----------
#These parameters will not change as long as you are using the same evolution account. the SMSapiURL is pointing to the staging SMS gateway. If this were a production application then you woudl point it $

evoUserName='jsajovic'
evoPassword=sys.argv[2]
SMSapiURL='http://api.messaging.staging.voxeo.net/1.0/messaging'

#------ Dynamic Parameters ---------
#The following array are the API parameters that are required for outbound SMS. The following is a breakdown of each one. A description of each parameter is found here http://help.voxeo.com/go/help/evolu$

#To use this from the Python command line the sys.srgv array is used to pull vars from the comand line. Here is an exmaple: sudo python smsOutbound.py 'This is a successful test'
#The sys module argv builds an array where the name of the python file is arg[0] and the string following is arg [1]. Using this you can pass multiple arguements into the script like your evolution passw$
#An example of this on the command line is: sudo python smsOutbound.py 'this is a great example of how to use arguements' 'password
#make sure you include the ticks because you are passing strings into your script'

data = ({'botkey':'538449', 'apimethod':'send', 'msg':sys.argv[1], 'user':'14074886978','network':'SMS','from':'14073863891'})

#------ Execute Outbound SMS to Aspect SMS Gateway --------
SMSout = requests.get(SMSapiURL, params=(data), auth=(evoUserName, evoPassword))

#------ Display Results -------
print (SMSout.status_code)
print (SMSout.headers)
print (SMSout.url)