import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
#Provide your IBM Watson Device Credentials
organization = "mc91ul"
deviceType = "NodeMCU"
deviceId = "Esp8266"
authMethod = "token"
authToken = "smartwaste"

def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)
        

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
                
        w =random.randint(0, 25)
        #print(hum)
        p =(w/25)*100
        #Send Temperature & Humidity to IBM Watson
        data = { 'Weight' : w, 'Percentage': p }
        #print (data)
        print (data)
        def myOnPublishCallback():
            print ("Weight = %s C" %w, "percentage = %s %%" % p)

        success = deviceCli.publishEvent("Wastelevel", "json", data, qos=0, on_publish=myOnPublishCallback)
	if percentage == 100:
                request_url=urllib.request.urlopen(' https://www.fast2sms.com/dev/bulkV2?authorization=5tGXMSnvP2r60kuNaQRl8eLfFmsUpJwWAyKC1zcbdO9jDHi4EqqelZ9Q1LST0nfGKPHFri25CX4oDa8k&route=q&message=Bin%20is%20full&language=english&flash=0&numbers=8838555452')
                print(request_url.read)
        if not success:
            print("Not connected to IoTF")
        time.sleep(5)
        
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
