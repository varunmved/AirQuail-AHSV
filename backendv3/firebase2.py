import threading
import time, urllib, json, requests
import datetime
#import firebase_util as fire
from firebase import firebase
import datetime


requests.packages.urllib3.disable_warnings()


firebase = firebase.FirebaseApplication('https://airquail.firebaseio.com/', None)

def putIntoFirebaseSensor_Temp(Temperature, time):
    firebase.put('/Sensor', "Temperature", Temperature)

def putIntoFirebaseSensor_Humidity(Humidity, time):
    firebase.put('/Sensor', "Humidity", Humidity)

def putIntoFirebaseSensor_CO(CO,time):
    firebase.put('/Sensor',  "CO", CO)

def putIntoFirebaseSensor_CO2(CO2,time):
    firebase.put('/Sensor', "CO2", CO2)

def runFirebase():
    while True:
        url3 = "https://api.particle.io/v1/devices/1e002a001447343338333633/mq4?access_token=bb3dc001dbd1e097caf31f118ab706f977085740" 
       #mq7 is carbonmonoxide
        url5 = "https://api.particle.io/v1/devices/1e002a001447343338333633/mq7?access_token=bb3dc001dbd1e097caf31f118ab706f977085740"

        results3 = requests.get(url3)
        results5 = requests.get(url5)
    
        mq4Data = results3.json()
        mq7Data = results5.json()

        baseMQ7 = mq7Data['result']
        #MQ4
        print("4")
        baseMQ4 = mq4Data['result']

        print('Doing something imporant in the background')
        nowTime = datetime.datetime.now().strftime('%s')
        putIntoFirebaseSensor_CO(baseMQ7,nowTime)
        putIntoFirebaseSensor_CO2(baseMQ4,nowTime)
        print "reporting finished"

        time.sleep(10)

runFirebase()

