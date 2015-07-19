import threading
import time, urllib, json, urllib3, requests
import datetime
#import firebase_util as fire
from firebase import firebase
import pymongo
from pymongo import MongoClient
import redis

#import human_curl as requests

requests.packages.urllib3.disable_warnings()

#f = open("lol.txt", 'w')
firebase = firebase.FirebaseApplication('https://airquail.firebaseio.com/', None)
#r = redis.StrictRedis(host='localhost', port=6379, db=0)
'''
def pushToFireBaseBulk(sensorData):
    fire.putIntoFirebaseSensor_Temp(sensorData['result'])
    fire.putIntoFirebaseSensor_Humidity()
'''
'''
def __init__(interval=1):
    """ Constructor
    :type interval: int
    :param interval: Check interval, in seconds
    """
    self.interval = interval
    f.write("ayy")

    thread = threading.Thread(target=self.run, args=())
    thread.daemon = True                            # Daemonize thread
    thread.start()                                  # Start the execution
'''


''''
def run():
    """ Method that runs forever """
    while True:

        # Do something
        #url = "http://172.31.99.4/vehicle"
        #f.write(r)
        url = "https://api.particle.io/v1/devices/55ff6d066678505541381667/temp?access_token=bb3dc001dbd1e097caf31f118ab706f977085740"
        # = hurl.get(url,auth=('test_username', 'test_password'))
        #f.write("lmao")
        response = urllib.urlopen(url);
        tempData = json.loads(response.read())
        #f.write(tempData)
        with open('data.txt', 'w') as outfile:
            json.dump(tempData, outfile)
        arghh = tempData['result']
        print('Doing something imporant in the background')
        pushToFireBaseBulk(arghh)
        print "reporting finished"
        time.sleep(1)
'''
def putIntoFirebaseSensor_Temp(Temperature):
    firebase.put('/Sensor', "Temperature", Temperature)

def putIntoFirebaseSensor_Humidity(Humidity):
    firebase.put('/Sensor', "Humidity", Humidity)

def putIntoFirebaseSensor_CO(CO):
    firebase.put('/Sensor',  "CO", CO)

def putIntoFirebaseSensor_CO2(CO2):
    firebase.put('/Sensor', "C02", C02)

def runFirebase():
    while True:
        url = "https://api.particle.io/v1/devices/53ff6f065067544833490587/temp?access_token=bb3dc001dbd1e097caf31f118ab706f977085740"
        url2 ="https://api.particle.io/v1/devices/53ff6f065067544833490587/rh?access_token=bb3dc001dbd1e097caf31f118ab706f977085740"
        url3= "https://api.particle.io/v1/devices/55ff6d066678505541381667/mq4?access_token=bb3dc001dbd1e097caf31f118ab706f977085740"
        #mq7 is carbonmonoxide
        url5= "https://api.particle.io/v1/devices/55ff6d066678505541381667/mq7?access_token=bb3dc001dbd1e097caf31f118ab706f977085740"

        results = requests.get(url)
        results2 = requests.get(url2)
        results3 = requests.get(url3)
        results5 = requests.get(url5)

        tempData = results.json()
        rhData = results2.json()
        #mq4Data = results3.json()
        #mq7Data = results5.json()

        print("1")
        baseTemp = tempData['result']
        if (baseTemp < 27):
            j = requests.get("https://messagingapi.sinch.com/v1/sms/14242535865", auth=('a2d52e58-fb8a-45b5-93a8-9575ea4ea749', 'YxZSH0WFjUi2r26iGsQoig=='))

        print("2")
        baseRH = rhData['result']
        #carbon monoxide
        print("3")
        #baseMQ7 = mq7Data['result']
        #MQ4
        print("4")


        #print(arghh)
        print('Doing something imporant in the background')
        #arghh = "a"
        #pushToFireBaseBulk(bulkData)
        putIntoFirebaseSensor_Temp(baseTemp)
        #putIntoFirebaseSensor_CO(baseMQ7)
        #putIntoFirebaseSensor_CO2(baseMQ4)
        putIntoFirebaseSensor_Humidity(baseRH)
        print "reporting finished"
        time.sleep(5)

def runMongoDB():
    while True:
        print('adding to mongo')
        client = MongoClient('localhost', 27017)
        client = MongoClient('mongodb://localhost:27017/')
        #db = client.test_database
        db = client['test-database']
        url = "https://api.particle.io/v1/devices/53ff6f065067544833490587/temp?access_token=bb3dc001dbd1e097caf31f118ab706f977085740"
        url2 ="https://api.particle.io/v1/devices/53ff6f065067544833490587/rh?access_token=bb3dc001dbd1e097caf31f118ab706f977085740"
        url3= "https://api.particle.io/v1/devices/55ff6d066678505541381667/mq4?access_token=bb3dc001dbd1e097caf31f118ab706f977085740"
        #mq7 is carbonmonoxide
        url5= "https://api.particle.io/v1/devices/55ff6d066678505541381667/mq7?access_token=bb3dc001dbd1e097caf31f118ab706f977085740"

        results = requests.get(url)
        results2 = requests.get(url2)
        results3 = requests.get(url3)
        results5 = requests.get(url5)

        tempData = results.json()
        rhData = results2.json()
        #mq4Data = results3.json()
        #mq7Data = results5.json()

        print("1")
        baseTemp = tempData['result']

        print("2")
        baseRH = rhData['result']
        #carbon monoxide
        print("3")
        #baseMQ7 = mq7Data['result']
        #MQ4
        print("4")

        #baseMQ4 = mq4Data['result']
        #methane
        #baseMethane = methaneData['result']
        post = {"temperature":baseTemp, "humidity":baseRH, "local_time": datetime.datetime.now()}
        posts = db.posts
        post_id = posts.insert(post)
        print("done")
        time.sleep(30)
'''
def runRedis():
    while True:
        r.set('foo', 'bar')
'''


'''
        r = requests.get(url);
        print(r.json())
        #print(r)
        #print(str(response))

        temperatureDataPull = json.loads(r.read())
        print('Doing something imporant in the background')
        pushToFireBaseBulk(temperatureDataPull)
        print "reporting finished"
        time.sleep(self.interval)

    while True:
            # Do something
            url = "http://172.31.99.4/vehicle"
            response = urllib.urlopen(url);
            carData = json.loads(response.read())
            print('Doing something imporant in the background')
            pushToFireBaseBulk(carData)
            print "reporting finished"
            time.sleep(self.interval)
'''
runFirebase()
#runMongoDB()
#runred()
'''
class background_daemon(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval
        f.write("ayy")

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            f.write(r)
            url = "https://api.particle.io/v1/devices/55ff6d066678505541381667/temp?access_token=bb3dc001dbd1e097caf31f118ab706f977085740"
            # = hurl.get(url,auth=('test_username', 'test_password'))
            f.write("lmao")

            r = requests.get(url);
            print(r.json())
            #print(r)
            #print(str(response))

            temperatureDataPull = json.loads(response.read())
            print('Doing something imporant in the background')
            pushToFireBaseBulk(temperatureDataPull)
            print "reporting finished"
            time.sleep(self.interval)

'''
