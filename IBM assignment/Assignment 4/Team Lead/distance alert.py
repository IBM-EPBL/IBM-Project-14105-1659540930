import RPi.GPIO as GPIO
import time
import time
import sys
import ibmiotf.application
import ibmiotf.device


#Provide your IBM Watson Device Credentials
organization = "br1jua"
deviceType = "distance_measure"
deviceId = "distance"
authMethod = "token"
authToken = "nkoOigiknlFCNVhbkb3"
GPIO.setmode(GPIO.BCM)
 
GPIO_TRIGGER = 18
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    GPIO.output(GPIO_TRIGGER, True)

    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def myCommandCallback(cmd):
   print("Command received: %s" % cmd.data['command'])
   print(cmd)
        


try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

deviceCli.connect()

while True:
    try:
        dist = distance()
        if (dist < 100):
		data = {"d":{ 'distance':'dist'}}
        	def myOnPublishCallback():
            		print ("Published Distance = %s cm, %dist, "to IBM Watson")

        	success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
        	if not success:
           		print("Not connected to IoTF")
        	time.sleep(1)
        
        	deviceCli.commandCallback = myCommandCallback

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

deviceCli.disconnect()