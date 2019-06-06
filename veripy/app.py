#!/usr/bin/python3
# File handler for our app that tests csv information.
#
# June 4, 2019
# Jordan Dysart
#
# Purpose: I just want to know how to do this shit maaan.
#

from veripy.common.state_constants import StateConstants
from veripy.data.filemanager import FileManager

import sys



def run():




    print("we are running")
    log.debug("We are up and running:")
    log.debug("Filename: ", sys.argv[0])
    fileManager = FileManager(12)
    fileManager.promptLive()
