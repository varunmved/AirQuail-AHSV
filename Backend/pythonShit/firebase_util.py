# Util class for Firebase
import requests
import json
import urllib3
import urllib
from firebase import firebase

requests.packages.urllib3.disable_warnings()

firebase = firebase.FirebaseApplication('https://airquail.firebaseio.com/', None)



# put into car methods
def putIntoFirebaseSensor_Temp(Temperature):
    firebase.put('/Sensor', "Temperature", Temperature)

def putIntoFirebaseSensor_Humidity(Humidity):
    firebase.put('/Sensor', Humidity, "Humidity")

def putIntoFirebaseSensor_CO(CO):
    firebase.put('/Sensor', CO, "CO")

def putIntoFirebaseSensor_CO2(CO2):
    firebase.put('/Sensor', C02, "C02")
'''
def putIntoFirebaseSensor_Dust(Dust):
    firebase.put('/Sensor', Dust, "Dust")
'''
