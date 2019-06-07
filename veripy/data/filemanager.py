#!/usr/bin/python3
# File handler for our app that tests csv information.
#
#
#



from os import getcwd
from os.path import normpath, join
import logging


class FileManager(object):
    """docstring for FileManager
    Let's make sure we don't change any files that are brought into the program
    Maybe we can clone files and write new ones from here."""

    logger = logging.getLogger('general')

    def __init__(self, pathToFile):
        super(FileManager, self).__init__()

        self.localPathToFile = pathToFile
        self.logger.debug("is this going to cause issues")

    def getFilePath():
        return getcwd() + self.localPathToFile


# This should be a test!
    def verifyFile(self):
        self.logger.debug("")
        self.logger.debug(getcwd())
        self.logger.debug(self.localPathToFile)


        self.logger.debug(getFilePath)
        fo = open(file_path, 'rb')
        self.logger.debug("Name of the file: {}".format(fo.name))
        self.logger.debug("Closed or not : {}".format( fo.closed))
        self.logger.debug("Opening mode : {}".format( fo.mode))
        fo.close()

    def cloneFile(self):

        file_path = normpath(join(getcwd(), self.localPathToFile))
        fo = open(file_path, 'rb')

        path = "clone_{}".format(self.localPathToFile)
        file_path = normpath(join(getcwd(), path))
        newfo = open(file_path)
