import RPi.GPIO as GPIO		
#import RPi.GPIO module

import time

LED = 40			        
#pin no. as per BOARD

GPIO.setwarnings(False) 	
#disable warnings

GPIO.setmode(GPIO.BOARD)	
#set pin numbering format

GPIO.setup(LED, GPIO.OUT)	
#set GPIO as output

while True:
   
        GPIO.output(LED,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED,GPIO.LOW)
        time.sleep(1)