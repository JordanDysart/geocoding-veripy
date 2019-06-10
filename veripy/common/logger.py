# module used for creating log files

import logging
from os import getcwd

# Just for the record this line runs if we import.
# print("Well that is interesting")

# I might need to change this in the future. Let's see if we can create decorators outside of this class.

STARS = "*" * 20

#The background is set with 40 plus the number of the color, and the foreground with 30
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

#These are the sequences need to get colored ouput
RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"
BOLD_SEQ = "\033[1m"

def formatter_message(message, use_color = True):
    if use_color:
        message = message.replace("$RESET", RESET_SEQ).replace("$BOLD", BOLD_SEQ)
    else:
        message = message.replace("$RESET", "").replace("$BOLD", "")
    return message

COLORS = {
    'WARNING': YELLOW,
    'INFO': WHITE,
    'DEBUG': BLUE,
    'CRITICAL': YELLOW,
    'ERROR': RED
}

class ColoredFormatter(logging.Formatter):
    def __init__(self, msg, use_color = True):
        logging.Formatter.__init__(self, msg)
        self.use_color = use_color

    def format(self, record):
        levelname = record.levelname
        if self.use_color and levelname in COLORS:
            levelname_color = COLOR_SEQ % (30 + COLORS[levelname]) + levelname + RESET_SEQ
            record.levelname = levelname_color
        return logging.Formatter.format(self, record)


class Logger(object):
    """docstring for Logger."""



    def __init__(self, arg):
        super(Logger, self).__init__()
        self.arg = arg

        #formatting for loggers
        logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
        # logFormatter = ColoredFormatter(self.COLOR_FORMAT)

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
        # self.rootLogger.addHandler(fileHandler)
        self.rootLogger.addHandler(consoleHandler)



        # do we still need this?
        FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'

    def setLogging(self):
        DEBUG_TO_CONSOLE = True
        DEBUG_TO_FILE    = True
        PATH_TO_LOG      = "veripy/logs/"
        LOG_NAME         = "debug.log"

    def debug(self, message):
        self.rootLogger.debug(message)

    def warning(self, message):
        self.rootLogger.warning(message)

    def newrow(self, message=''):
        self.rootLogger.debug(f"{STARS} NEW {message} {STARS}")


    def loggingToFile(self, isEnabled):

        d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
        logging.warning('Protocol problem: %s', 'connection reset', extra=d)
