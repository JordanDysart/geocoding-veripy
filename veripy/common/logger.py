# module used for creating log files

import logging
from os import getcwd

# Just for the record this line runs if we import.
# print("Well that is interesting")

# I might need to change this in the future. Let's see if we can create decorators outside of this class.

class Logger(object):
    """docstring for Logger."""

    def __init__(self, arg):
        super(Logger, self).__init__()
        self.arg = arg

        #formatting for loggers
        logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")

        # create logger controller
        self.rootLogger = logging.getLogger('general')
        self.rootLogger.setLevel(logging.DEBUG)

        # log to file
        logPath = getcwd()
        logPath += "/veripy/logs/"
        fileName = "prim"
        # create second logger
        # set where the .log file will go and what is the name
        fileHandler = logging.FileHandler("{0}/{1}.log".format(logPath, fileName))
        # TODO it would probably be cool to have a logger that creates new files
        fileHandler.setLevel(logging.DEBUG)
        fileHandler.setFormatter(logFormatter)

        # log to stderr
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logFormatter)

        # add loggers
        self.rootLogger.addHandler(fileHandler)
        self.rootLogger.addHandler(consoleHandler)



        # do we still need this?
        FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'

    def setLogging(self):
        DEBUG_TO_CONSOLE = True
        DEBUG_TO_FILE    = True
        PATH_TO_LOG      = "veripy/logs/"
        LOG_NAME         = "debug.log"

    def debug(self, log):
        self.rootLogger.debug(log)


    def loggingToFile(self, isEnabled):

        d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
        logging.warning('Protocol problem: %s', 'connection reset', extra=d)
