#!/usr/bin/python3
# File handler for our app that tests csv information.
#
# June 4, 2019
# Jordan Dysart
#
# Purpose: I just want to know how to do this shit maaan.
#

# Ditching some of the object oriented stuff to prove that this is going to work in the first place.

from veripy.common.logger import Logger
from veripy.common.state_constants import StateConstants
from veripy.data.filemanager import FileManager

import sys
import os
import csv
import urllib

BASE      = "https://maps.google.com/"
GEOCODE   = "maps/api/geocode/"

REQUEST   = "https://maps.google.com/maps/api/geocode/json?components=postal_code:75018&key=api_key"
GAPI      = "AIzaSyDxF6scdJ7TVSFWafqyo8bzMcT_r8cTobk"
FILE_PATH = 'python-verify-geo-csv-test-data.csv'


# List all of the values in the array
SETUP_PROMPT = "[{0}] {1}"


def run():

    logger = Logger(True)
    logger.debug("Filename: {}".format( sys.argv[0]))

    # Record the csv lines.
    setup = True
    # Find the right keys
    while (setup):
        # long, lat = setupCoordinateKeys()
        long, lat = "Longitude", "Latitude"

        print("Just to confirm, this is what you chose Lat: {0}, Long:{1}".format(lat, long))
        # answer = input("Is this right?")
        answer = 'yes'
        print("IS this right?")


        if 'yes' in answer:
            setup = False

        print("Moving on...")

    with open(FILE_PATH, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile)
        copycat = "copy_" + FILE_PATH

        with open('names.csv', 'w', newline='\n') as copyof_csvfile:
            for row in reader:
                fieldnames = [lat, long]
                writer = csv.DictWriter(copyof_csvfile, fieldnames=fieldnames)

                new_row = ', '.join(row)
                print("writing: {}".format(new_row))
                writer.writerow(new_row)
                print(row[lat], row[long])

    logger.debug("Done setting up")
    logger.debug("We are up and running:")

    # fileManager = FileManager("/veripy/resources/dummy.data")
    # fileManager.verifyFile()

    # Copy the csv (so we can alter this one)


    # Create the arrays
    # Evaluate our arrays

    # if non valid coordinates (i.e -180) build an api request

    # parse results

    # generate clickable link for debugging purposes

    # write to new csv




def setupCoordinateKeys():

    with open(FILE_PATH, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        # get header from first row this is what we will use to identify the part of the csv that we need.
        headers = next(reader)


    # Let's set this up manually for now.
    # break
    for head_value in headers:
        print(SETUP_PROMPT.format(headers.index(head_value), head_value))

    long = int(input("I'm a dumb computer, I don't know what longitude is. Do you: "))
    lat  = int(input("Where's that lattitude: "))

    return headers[lat], headers[long]
