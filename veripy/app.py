#!/usr/bin/python3
# File handler for our app that tests csv information.
#
# June 4, 2019
# Jordan Dysart
#
# Purpose: I just want to know how to do this shit maaan.
#

from veripy.common.logger import Logger
from veripy.common.state_constants import StateConstants
from veripy.data.filemanager import FileManager


import sys
import os

def run():

    logger = Logger(True)

    logger.debug("we are logging")
    logger.debug("We are up and running:")
    logger.debug("Filename: {}".format( sys.argv[0]))
    fileManager = FileManager("/veripy/resources/dummy.data")
    fileManager.verifyFile()
