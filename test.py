import urllib.request
import time


# Define a function that will post on server every 15 Seconds

def thingspeak_post():
    time.sleep(3)
    val=90
    URl='https://api.thingspeak.com/update?api_key='
    KEY='UKK7TET9TMHXYZZT'
    HEADER='&field1={}'.format(val)
    NEW_URL=URl+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)


if __name__ == '__main__':
    thingspeak_post()
