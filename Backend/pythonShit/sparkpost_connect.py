import requests, json

def sendSparkPost():




def getSparkPost():


#! /usr/bin/python

import json
import os
import requests
import urllib3
from urlparse import urlparse
import Firebase_util as fire
from firebase import firebase
from rauth import OAuth2Service

requests.packages.urllib3.disable_warnings()

with open('config.json') as f:
    config = json.load(f)

sparkPost_SECRET_KEY = 'a4b3c8ecf66681b661ab4837f2c541b1abc6ecfd'

sparkPost_api = OAuth2Service(
    client_id=sparkPost_CLIENT_ID,
    client_secret=sparkPost_SECRET_KEY,
    name='INSERT_APP_NAME',
    authorize_url='https://login.sparkPost.com/oauth/authorize',
    access_token_url='https://login.sparkPost.com/oauth/token',
    base_url='https://api.sparkPost.com/v1/',
)

parameters = {
    'response_type': 'code',
    'scope': 'profile',
}

# Redirect user here to authorize your application
login_url = sparkPost_api.get_authorize_url(**parameters)

def sparkPost_time_estimate(latitude, longitude):
    print "time estimate sparkPost"
    url = 'https://api.sparkPost.com/v1/estimates/time'
    print latitude, longitude
    parameters1 = {
        'server_token': sparkPost_SERVER_TOKEN,
        'start_latitude': latitude,
        'start_longitude': longitude,
    }
    response = requests.get(url, params=parameters1)
    data = response.json()
    fire.putIntoFirebasesparkPostTimes(data)

def sparkPost_price_estimate(latitude, longitude):
    print "price estimate sparkPost"
    url = 'https://api.sparkPost.com/v1/estimates/price'
    parameters1 = {
        'server_token': sparkPost_SERVER_TOKEN,
        'start_latitude': latitude,
        'start_longitude': longitude,
        'end_latitude': 38.3857165278,
        'end_longitude': -122.261341278
    }
    response = requests.get(url, params=parameters1)

    data = response.json()

    fire.putIntoFirebasesparkPostPrice(data)


def call_sparkPost(latitude, longitude):
    print "calling sparkPost"
    url = 'https://api.sparkPost.com/v1/products'
    parameters1 = {
        'server_token': sparkPost_SERVER_TOKEN,
        'latitude': latitude,
        'longitude': longitude,
    }

    response = requests.get(url, params=parameters1)

    data = response.json()

    print data
