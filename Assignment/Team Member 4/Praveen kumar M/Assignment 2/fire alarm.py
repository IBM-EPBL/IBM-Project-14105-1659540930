import time
from playsound import playsound


while(True):
    try:
        temp = int(input("enter temperature in celcius"))
        hum = int(input("enter humidity between 100"))
        if(temp > 40 and hum > 40):
            playsound("alarm.wav")
            time.sleep(10)
    except:
        print("sound played")
