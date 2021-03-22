#!/usr/bin/python3

# Automation Login Script that will login in to url site provided.
# Url name and File must be provided
# Include the email address/username on 1st line, and password on 2nd line
# If site requires username instead of email address. Replace with username
# ChromeDriver must be running == bash /usr/lib/chromium-browser/chromedriver
import time
import sys
import os
from selenium import webdriver
import linecache
import requests
from requests.auth import HTTPDigestAuth
from selenium.webdriver.chrome.service import Service

# Engine
service = Service('/usr/lib/chromium-browser/chromedriver')

# Start Engine
service.start()

# Browser
driver = webdriver.Remote(service.service_url)

# Requirement is a url login page
# Pass as first argument
url = sys.argv[1]

# User can create a file with Credentials
# Requirements are the email_address is on line 1 and password on line 2
# Pass as second argument
filename = 'DIRECTORY TO CREDENTIALS'


# These function encompasses functionality to autologin using Selenium
# Can be ran from Command Line using [ autoLogin url ]
def facebook_login(url):
    # Open Browser and go to url provided
    driver.get(url)

    # email address is on line 1 in file provided
    email_address = linecache.getline(filename, 1)

    # find email address field and enter email address into url login page
    driver.find_element_by_xpath('//input[contains(@id, "email")]').send_keys(email_address)

    # password is on line 2 in file
    password = linecache.getline(filename, 2)

    try:
        # wait
        time.sleep(5)

        # find password field and enter password onto url login page
        driver.find_element_by_xpath('//input[contains(@id, "pass")]').send_keys(password)

        # wait
        time.sleep(5)
    except:
        pass

    # stay open 10 seconds
    time.sleep(10)

    # close browser
    driver.quit()

    # Stops engine
    os.system('pkill chromedriver')
    email = sys.argv[1]


# Run file, allow url and file to pass for function to work appropriately
if __name__ == '__main__':
    if url == 'http://facebook.com':
        facebook_login(url)
