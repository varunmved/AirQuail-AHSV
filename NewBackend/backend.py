import urllib3
import requests
import json
import os
import psycopg2
import django
import boto.rds
from datetime import datetime
import random_data as rd
from firebase import firebase
PASSWORD = "Ilovestephdu!69"


# conn = boto.rds.connect_to_region(
#     "us-west-2",
#     aws_access_key_id ='AKIAIKDVNEOKND4I6VVQ',
#     aws_secret_access_key='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')
#
# db = conn.create_dbinstance("db-master-1", 10, 'db.m1.small', 'root', 'hunter2')
#
# if 'aa1b1x4r6opzze' in os.environ:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': os.environ['ebdb'],
#             'USER': os.environ['quailmaster'],
#             'PASSWORD': os.environ[PASSWORD],
#             'HOST': os.environ['aa1b1x4r6opzze.cpjyzndy4ytb.us-west-2.rds.amazonaws.com'],
#             'PORT': os.environ['5432'],
#         }
#     }
#
# TEMPERATURE_URL = "https://api.particle.io/v1/devices/53ff6f065067544833490587/temp?access_token=bb3dc001dbd1e097caf31f118ab706f977085740"
#
#
#
# def getFromSparkCloud():
#     results = requests.get(TEMPERATURE_URL)
#     tempData = results.json()
#     baseTemp = tempData['result']

def makeData():
    rds

def parseSparkCloud():



def putToAWS():


def init_main():
'''
