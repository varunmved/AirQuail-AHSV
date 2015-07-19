import threading
import time, urllib, json, urllib3, requests
#import firebase_util as fire
from firebase import firebase

#import human_curl as requests

#requests.packages.urllib3.disable_warnings()

#f = open("lol.txt", 'w')
firebase = firebase.FirebaseApplication('https://airquail.firebaseio.com/', None)
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
def run2():
    while True:
        url = "https://api.particle.io/v1/devices/55ff6d066678505541381667/temp?access_token=bb3dc001dbd1e097caf31f118ab706f977085740"
        url2 = "https://api.particle.io/v1/devices/55ff6d066678505541381667/rh?access_token=bb3dc001dbd1e097caf31f118ab706f977085740"
        url3= "https://api.particle.io/v1/devices/55ff6d066678505541381667/mq4?access_token=bb3dc001dbd1e097caf31f118ab706f977085740"
        #url4= "https://api.particle.io/v1/devices/55ff6d066678505541381667/methane?access_token=bb3dc001dbd1e097caf31f118ab706f977085740"
        #mq7 is carbonmonoxide
        url5= "https://api.particle.io/v1/devices/55ff6d066678505541381667/mq7?access_token=bb3dc001dbd1e097caf31f118ab706f977085740"
        #url6= "https://api.particle.io/v1/devices/55ff6d066678505541381667/carbonmonoxide?access_token=bb3dc001dbd1e097caf31f118ab706f977085740"

        results = requests.get(url)
        results2 = requests.get(url2)
        results3 = requests.get(url3)
        #results4 = requests.get(url4)
        results5 = requests.get(url5)
        #results6 = requests.get(url6)

        tempData = results.json()
        rhData = results2.json()
        mq4Data = results3.json()
        #methaneData = results4.json()
        mq7Data = results5.json()
        #carbonmonoxideData = results6.json()


        baseTemp = tempData['result']
        baseRH = rhData['results']
        #carbon monoxide
        baseMQ7 = mq7Data['result']
        #MQ4
        baseMQ4 = mq4Data['result']
        #methane
        baseMethane = methaneData['result']

        #print(arghh)
        print('Doing something imporant in the background')
        #arghh = "a"
        #pushToFireBaseBulk(bulkData)
        putIntoFirebaseSensor_Temp(baseTemp)
        putIntoFirebaseSensor_CO(baseMQ7)
        putIntoFirebaseSensor_CO2(baseMQ4)
        putIntoFirebaseSensor_Humidity(baseRH)
        print "reporting finished"
        time.sleep(5)

def putIntoFirebaseSensor_Temp(Temperature):
    firebase.put('/Sensor', "Temperature", Temperature)

def putIntoFirebaseSensor_Humidity(Humidity):
    firebase.put('/Sensor', "Humidity", Humidity)

def putIntoFirebaseSensor_CO(CO):
    firebase.put('/Sensor',  "CO", CO)

def putIntoFirebaseSensor_CO2(CO2):
    firebase.put('/Sensor', "C02", C02)

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
run2()
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
            #url = "http://172.31.99.4/vehicle"
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
