from serial import Serial
import urllib.request
import time
import os
print("================================================================================")
print ("                            Air quality sensor(Ver.2.0)      By CK")
print("================================================================================")
time.sleep(5)
print("\n")
print("Getting info....")
print("\n\n")
time.sleep(1)
print("Board            :Arduino Uno(Genuino)")
time.sleep(1)
print("Gas sensor       :mq135")
time.sleep(1)
print("Port             :com4")
print("\n")
time.sleep(1)
print("Heating up the sensor......")
time.sleep(5)
ser = serial.Serial('com4', 9600, timeout=1)


while True:
    os.system('cls')
    print("================================================================================")
    print ("                            Air quality sensor")
    print("================================================================================")
    print("the PPM in Air:")
    reading = ser.readline()
    data=reading.decode('utf-8')
    print(data)
    URl='https://api.thingspeak.com/update?api_key='
    KEY='UKK7TET9TMHXYZZT'
    HEADER='&field1={}'.format(data)
    NEW_URL=URl+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)
    time.sleep(2)
