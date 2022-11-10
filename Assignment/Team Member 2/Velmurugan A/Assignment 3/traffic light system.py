import time
import RPi.GPIO as GPIO

red_led = 18
yellow_led = 23
green_led = 24

red_led_two = 17
yellow_led_two = 27
green_led_two = 22

RUNNING = True


GPIO.setmode(GPIO.BCM)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(yellow_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(red_led_two, GPIO.OUT)
GPIO.setup(yellow_led_two, GPIO.OUT)
GPIO.setup(green_led_two, GPIO.OUT)


def trafficState(red, yellow, green):
	GPIO.output(red_led, red)
	GPIO.output(yellow_led, yellow)
	GPIO.output(green_led, green)

def trafficStateTwo(red, yellow, green):
	GPIO.output(red_led_two, red)
	GPIO.output(yellow_led_two, yellow)
	GPIO.output(green_led_two, green)

print ("Two Traffic Lights Simulation. Press CTRL + C to quit")

try:  
	while RUNNING:
      	# 1st Light Green for 10 seconds 2nd Light Red
      	trafficState(0,0,1)
		print("Go 10 seconds and stop")
      	trafficStateTwo(1,0,0)
		time.sleep(3)
       
		time.sleep(10)
      	# 1st Light Red for 10 seconds 2nd Light Green
      	trafficState(1,0,0)
      	print("Stop 10 seconds and Go")
      	trafficStateTwo(0,0,1)
		time.sleep(3)

      	time.sleep(10)
      	# 1st Light Red for 10 seconds 2nd Light Yellow
      	trafficState(1,0,0)
      	print("Stop 10 seconds and and ready")
      	trafficStateTwo(0,1,0)
      	time.sleep(3)

except KeyboardInterrupt:
	RUNNING = False
	print ("Quitting")
finally:
	GPIO.cleanup()
