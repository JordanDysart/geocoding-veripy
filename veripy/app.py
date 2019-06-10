#!/usr/bin/python3
# File handler for our app that tests csv information.
#
# June 4, 2019
# Jordan Dysart
#
# Purpose: I just want to know how to do this shit maaan.
#

# Ditching some of the object oriented stuff to prove that this is going
# to work in the first place.

from veripy.common.logger import Logger
from veripy.common.state_constants import StateConstants
from veripy.data.filemanager import FileManager
from veripy.common.api import GAPI
from veripy.data.netcallsqueue import NetCallsQueue

import sys
import os
import csv
import requests
from time import sleep as sleep

REQUEST   = "https://maps.google.com/maps/api/geocode/json?components=postal_code:75018&key=api_key"
BASE      = "https://maps.google.com/"
GEOCODE   = "maps/api/geocode/"
JSON      = "json?components="
GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json' # use this one

FILE_PATH = 'python-verify-geo-csv-test-data.csv'

# List all of the values in the array
SETUP_PROMPT = "[{0}] {1}"

# i don't think this is being used at the moment
def setupCoordinateKeys():
    ''' find the keys for long and lat based on our csv'''

    with open(FILE_PATH, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        # get header from first row this is what we will use to identify the part of the csv that we need.
        headers = next(reader)
        csv.close


    # Let's set this up manually for now.
    # break
    for head_value in headers:
        print(SETUP_PROMPT.format(headers.index(head_value), head_value))

    long = int(input("I'm just a computer, I don't know what longitude is. Do you: "))
    lat  = int(input("Where's that lattitude: "))

    return headers[lat], headers[long]

def makeCallWith(params):
    ''' make the request with the api
        TODO create param builder '''
    sleep(.025)
    req = requests.get(GOOGLE_MAPS_API_URL, params=params)

    # Example params from the internet
    params = {
        'address':'221B Baker Street, London, United Kingdom',
        'sensor':'false',
        'region':'US',
        'key':GAPI
        }


    res = req.json()

    geodata = dict()
    if len(res['results']) > 0:
        result = res['results'][0]
        geodata['lat'] = result['geometry']['location']['lat']
        geodata['lng'] = result['geometry']['location']['lng']
        geodata['address'] = result['formatted_address']
        print('{address}.(lat,lng) = ({lat}, {lng})'.format(**geodata))
    else:
        print('There are no results: {}'.format(res))

    # use this for evaluating the new
    return geodata['lat'], geodata['lng']


def run():

    # ignore the logger lines please.
    logger = Logger(True)
    logger.debug("Filename: {}".format( sys.argv[0]))

    # Record the csv lines.
    setup = True

    copycat = "copy_" + FILE_PATH
    callqueue = NetCallsQueue()
    csvlist = [] # for now let's put our dictionaries here.

    with open(FILE_PATH, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        # get header from first row this is what we will use to identify the part of the csv that we need.
        headers = next(reader)


    # Find the right keys
    while (setup):
        long, lat = setupCoordinateKeys()
        # long, lat = "Longitude", "Latitude"

        logger.debug("Just to confirm, this is what you chose Lat: {0}, Long:{1}".format(lat, long))
        # answer = input("Is this right?")
        answer = 'yes'
        logger.debug("Is this right?")

        if 'yes' in answer:
            setup = False

    # open our csv to copy into the new csv.
    with open(FILE_PATH, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

         # Let's not write until we have final values?
        fieldnames = [lat, long]
        # Evaluate our arrays (Do )
        for row in reader:

            logger.newrow(message="line")
            logger.debug("This is the type: {}".format(type(row)))
            logger.debug("Here are your co: {} {}".format(row[lat], row[long]))

            # Copying the csv file into a new file
            dict = {}
            # if they are empty or -181 we will have to build a request
            if row.get(lat) == row.get(long):
                logger.warning(f"These might be evaluating {lat} + {long}".format(**row))
                logger.debug("Coordinate evaluating was true, let's build a call")
                callqueue.enqueue(row)

            else:
                csvlist.append(row)

            # the request can be built after this for loop

            # TODO build a queue and time the requests for now.
            # ...just trying to separate tasks...
            # params have to get built.
            # this is doing nothing at the moment.
            # params = {}
            # makeCallWith(params)

    logger.debug("csv length          : {}".format(len(csvlist)))
    logger.debug("Is our queue empty  : {}".format(callqueue.isEmpty()))

    # if non valid coordinates (i.e -180) build an api request
    while ( not callqueue.isEmpty()):
        current_location = callqueue.dequeue()
        # logger.debug(current_location) # this is printing out the whole ordered dictionary. Don't.
        logger.debug(current_location.get('City'))
        logger.debug(current_location['City'])
        params = {}
        params['address'] = current_location.get('Address') + ', '
        params['address'] += current_location.get('City') + ', '
        params['address'] += current_location.get('Postal/Zip Code')
        params['region']  = current_location.get('Country')
        params['key']     = GAPI
        params['sensor']  = 'false'

        current_location[lat], current_location[long]  = makeCallWith(params)
        csvlist.append(current_location)


    # parse results

    # generate clickable link for debugging purposes


    # Copy the csv (so we can alter this one)


    with open(copycat, 'a', newline='\n') as copyof_csvfile:
        writer = csv.DictWriter(copyof_csvfile, fieldnames=headers)
        writer.writeheader()
        for row in csvlist:
            logger.debug("this is our row from csvlist: {}".format(row.values()))

            writer.writerow(row)





    # Create the arrays/ just use the dictionary ¯\_(ツ)_/¯
    with open(copycat, 'r') as csvfile:
        reader = csv.DictReader(csvfile)







    # write to new csv
