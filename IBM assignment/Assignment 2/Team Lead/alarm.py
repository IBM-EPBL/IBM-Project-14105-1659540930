import time
from playsound import playsound

for i in range(0,100):
    try:
        temperature = int(input("enter temperature in celcius "))
        humidity = int(input("enter humidity between 100 "))
        if(temperature > 40 and humidity > 40):
            playsound("alarm.wav")
            time.sleep(10)
    except:
        print("sound played")
