#!/usr/bin/python3

import requests
import json
import sys

# Provided by Slack 
slack_webhook_url = 'WEBHOOK HERE'
# Data being passed as argument
data = sys.argv[1]
# Data To Send To Slack
slack_data = {'payload': "{\"channel\": \"#channel\", \"username\": \"Log-Bot\", \"text\": \"" + data + "\"}"}

# POST data into channel
response = requests.post(
    slack_webhook_url, data=slack_data
)

# Raise Error if not successful
if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )
