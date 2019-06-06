



class StateConstants(object):
    """docstring for StateConstants."""

    def __init__(self):
        super(StateConstants, self).__init__()

    DEBUG_TO_CONSOLE = True
    DEBUG_TO_FILE    = True
    PATH_TO_LOG      = "veripy/logs/"
    LOG_NAME         = "debug.log"

    def loggingToFile(isEnabled):
        FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
        logging.basicConfig(format=FORMAT)
        d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
        logging.warning('Protocol problem: %s', 'connection reset', extra=d)
