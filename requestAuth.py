#!/usr/bin/python3

# import requests module
import requests
from requests.auth import HTTPDigestAuth
import linecache

filename = 'directory to file'
password = linecache.getline(filename, 5)
email_address = linecache.getline(filename, 4)
PARAMS = {'email_address': email_address, 'password': password}
# Making a post request
sendCredentials = requests.post('URL TO POST DATA', data=PARAMS)

print(sendCredentials)
