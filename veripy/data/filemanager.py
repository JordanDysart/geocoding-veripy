#!/usr/bin/python3
# File handler for our app that tests csv information.
#
#

import os
import sys
import webbrowser
from time import sleep as sleep_sheep


class FileManager(object):
    """docstring for FileManager."""

    def __init__(self, arg):
        super(FileManager, self).__init__()
        self.arg = arg

    def promptLive(self):

        print("running handlefile.py")
        print("That is all this project does so far. . .")
