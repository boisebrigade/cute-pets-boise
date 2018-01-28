# Cute Pets Boise
A python twitter bot origionally developed to be ran on a raspberry pi that grabs information from PetFinder API and posts tweets to [Cute Pets Boise](www.twitter.com/cutepetsboise)
This script is designed to run and be done. Below is information on setting up a cron job to run this multiple times at set intervals.

## Initial Setup
### Python setup
In order to utilize any code contained in this repository one needs to follow the proper guide for installing python on their operating system.  
[Installing Python on Windows](http://docs.python-guide.org/en/latest/starting/install3/win/)  
[Installing Python on Linux With apt](http://docs.python-guide.org/en/latest/starting/install3/linux/)  
[Installing Python on Mac](http://docs.python-guide.org/en/latest/starting/install3/osx/)

### Get-pip Setup
We utilize the python package manager get-pip to keep all our external code needs up to date, to install please follow this guide after installing python.  
[Installing get-pip](https://pip.pypa.io/en/stable/installing/)

## Using This Code
### Installing the necessary packages
This project requires 1 package from the package manager  
`pip install python-twitter`  

## Setting up Petfinder API Access
You need to login or create an account at petfinder [Petfinder](https://www.petfinder.com/developers/api-key).  
Follow the on screen steps to get an API key and place it in the quotes for `petfinder_api_key` in `apikeys.py`.

## Setting up Twitter API access
[How to setup Twitter API Access](https://themepacific.com/how-to-generate-api-key-consumer-token-access-key-for-twitter-oauth/994/) is a great guide for setting this up.

## Setting up a CRON Job
[Setting up a basic cron job in linux](https://www.taniarascia.com/setting-up-a-basic-cron-job-in-linux/)

#Running the Script
After setup has been completed you can run the script by issuing `python cutepets.py`