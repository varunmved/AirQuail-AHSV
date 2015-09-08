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
        url = "https://api.particle.io/v1/devices/53ff6f065067544833490587/temp?access_token=bb3dc001dbd1e097caf31f118ab706f977085740"
        url2 ="https://api.particle.io/v1/devices/53ff6f065067544833490587/rh?access_token=bb3dc001dbd1e097caf31f118ab706f977085740"
        url3= "https://api.particle.io/v1/devices/53ff6f065067544833490587/mq4?access_token=bb3dc001dbd1e097caf31f118ab706f977085740"
       
       #mq7 is carbonmonoxide
        url5= "https://api.particle.io/v1/devices/53ff6f065067544833490587/mq7?access_token=bb3dc001dbd1e097caf31f118ab706f977085740"


        results = requests.get(url)
        print("1a")
        results2 = requests.get(url2)
        print("1")
        results3 = requests.get(url3)
        results5 = requests.get(url5)
    
        tempData = results.json()
        rhData = results2.json()
        mq4Data = results3.json()
        mq7Data = results5.json()

        print("1")
        baseTemp = tempData['result']
        if (baseTemp < 27):
            j = requests.get("https://messagingapi.sinch.com/v1/sms/14242535865", auth=('a2d52e58-fb8a-45b5-93a8-9575ea4ea749', 'YxZSH0WFjUi2r26iGsQoig=='))

        print("2")
        baseRH = rhData['result']
        #carbon monoxide
        print("3")
        baseMQ7 = mq7Data['result']
        #MQ4
        print("4")
        baseMQ4 = mq4Data['result']

        print('Doing something imporant in the background')
        nowTime = datetime.datetime.now().strftime('%s')
        putIntoFirebaseSensor_Temp(baseTemp,nowTime)
        putIntoFirebaseSensor_CO(baseMQ7,nowTime)
        putIntoFirebaseSensor_CO2(baseMQ4,nowTime)
        putIntoFirebaseSensor_Humidity(baseRH,nowTime)
        print "reporting finished"

        time.sleep(10)

runFirebase()

