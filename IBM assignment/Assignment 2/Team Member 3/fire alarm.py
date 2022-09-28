import winsound
import random
import time

print("Playing the file 'alarm.wav'")
while(True):
    try:
        temperature = random.randint(0,100)
        humidity = random.randint(0,100)
        if(temperature > 40 and humidity > 40):
            winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)
            time.sleep(3)
    except:
        print("alarm on")
