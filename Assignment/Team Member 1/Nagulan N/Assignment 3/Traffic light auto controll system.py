import time
import RPi.GPIO as GPIO

red_led = 18
yellow_led = 23
green_led = 24

RUNNING = True


GPIO.setmode(GPIO.BCM)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(yellow_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)


def trafficState(red, yellow, green):
    GPIO.output(red_led, red)
    GPIO.output(yellow_led, yellow)
    GPIO.output(green_led, green)


print ("Traffic Lights Simulation. Press CTRL + C to quit")

try:
    while RUNNING:
        
        trafficState(0,0,1)
        time.sleep(10)
        trafficState(0,1,0)
        trafficStateTwo(1,0,0)
        time.sleep(3)
        trafficState(1,0,0)
        time.sleep(10)
        trafficState(1,0,0)
        time.sleep(3)

except KeyboardInterrupt:
    RUNNING = False
    print ("Quitting")

finally:
    GPIO.cleanup()
