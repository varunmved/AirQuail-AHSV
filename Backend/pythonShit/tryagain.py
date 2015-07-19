from firebase import firebaseimport threading
import time, urllib, json, urllib3, requests
import firebase_util as fire
import human_curl as requests

firebase = firebase.FirebaseApplication('https://airquail.firebaseio.com/', None)
new_user = 'Ozgur Vatansever'

result = firebase.post('/ayy', new_user)
print result
{u'name': u'-Io26123nDHkfybDIGl7'}
