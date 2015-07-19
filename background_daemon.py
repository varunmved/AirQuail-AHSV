import threading
import time, urllib, json, urllib3, requests
import Firebase_util as fire
import human_curl as requests

requests.packages.urllib3.disable_warnings()


def pushToFireBaseBulk(sensorData):
    fire.putIntoFirebaseSensor_Temp(['Sensor'])

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

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            #url = "http://172.31.99.4/vehicle"
            url2  = "https://api.particle.io/v1/devices/55ff6d066678505541381667/temp?access_token=bb3dc001dbd1e097caf31f118ab706f977085740""
            response = urllib.urlopen(url);
            temperatureDataPull = json.loads(response.read())
            print('Doing something imporant in the background')
            pushToFireBaseBulk(temperatureDataPull)
            print "reporting finished"
            time.sleep(self.interval)
