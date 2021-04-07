import time
import sys
import ibmiotf.application
import ibmiotf.device
import urllib.request
import random
#IoT Device Credeentials
organization = "mc91ul"
deviceType = "NodeMCU"
deviceId = "Esp8266"
authMethod = "token"
authToken = "wastemanagement"

def myCommandCallback(cmd):
    print("Command Recieved: %s" % cmd.data)
try:
    deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "authmet": authMethod,"Tok":authToken}
    deviceCli = ibmiotf.device.Client(deviceOptions)

except Exception as e:
    print("Caught an Exception while connecting device: ")
    sys.exit()
deviceCli.connect()

while True:
    weight = random.radient(10 , 25)
    print(weight)
    percentage = (weight/25)*100
    data = {"Weight" : weight, "Percentage" : percentage}
    def myOnpublishCallback():
        print("The total weight of the garbage is" %weight , "Percentage filled is "% percentage)
    #success = deviceCli.publishEvent(data, qos=0, myOnPublishCallback())
    if percentage == 100:
        request_url=urllib.request.urlopen(' https://www.fast2sms.com/dev/bulkV2?authorization=5tGXMSnvP2r60kuNaQRl8eLfFmsUpJwWAyKC1zcbdO9jDHi4EqqelZ9Q1LST0nfGKPHFri25CX4oDa8k&route=q&message=Bin%20is%20full&language=english&flash=0&numbers=8838555452')
        print(request_url.read)
    success=0
    if not success:
        print("IoTF not Connected")
    time.sleep(5)
    #deviceCli.commandCallback = mycommandCallback()

deviceCli.disconnect()