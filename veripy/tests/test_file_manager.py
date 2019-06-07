from veripy.data.filemanger import fileManager
import unittest

class TestFileManager(unittest.TestCase):

    fm = FileManager("/veripy/resources/dummy.data" )
    #
    def test_verifyfile_success(self):



        self.assertTrue(fm.verifyFile, "")

        self.logger.debug(getcwd())
        self.logger.debug(self.pathToFile)
        file_path = getcwd() + self.pathToFile
        self.logger.debug(file_path)
        fo = open(file_path, 'rb')
        self.logger.debug("Name of the file: {}".format(fo.name))
        self.logger.debug("Closed or not : {}".format( fo.closed))
        self.logger.debug("Opening mode : {}".format( fo.mode))
        fo.close()


    def test_verifyfile_error(self):
