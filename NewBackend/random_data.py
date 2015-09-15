from datetime import datetime
import json
import random

def randomPM():
    pm = random.uniform(0.000,40.000)
    return pm

def randomTemp():
    temp = random.uniform(15.0,30.0)
    return temp

def randomHumidity():
    humidity = random.uniform(0.00,1.00)
    return humidity

def randomCO():
    co = random.uniform(0.00,75.00)
    return co
def randomTime():
    currentTime = random.randrange(143200,)

def createX():
    x = []
    return x

def createJSON():
    data = {}
    return data


def generateJSON(data):

    data = createJSON()

    ''' lets get the random values '''
    pm = randomPM()
    humidity = randomHumidity()
    temp = randomTemp()
    co = randomCO()
    coIsDangerous = False
    if(co > 70):
        coIsDangerous = True
    data['time'] = currentTime
    data['pm'] = pm
    data['co'] = co
    data['temp'] = temp
    data['humidity'] = humidity
    data['isDangerous'] = coIsDangerous
    json_data = json.dumps(data)
    return json_data

x = createX()
data = createJSON()
for i in range(0,100):
    res = generateJSON(data)
    x.append(res)

with open('data.json', 'w') as outfile:
    json.dump(x,outfile)
