# ------------------------------------------------------
#
#   TestParser.py
#   By: Fred Stakem
#   Created: 3.23.13
#
# ------------------------------------------------------

# Libs
import unittest
from Globals import *
from Utilities import *
from LogParser import LogSource
from IosLogParser import Scanner
from IosLogParser import Parser

class ParserTest(unittest.TestCase):
    
    # Setup logging
    logger = Utilities.getLogger('ParserTest')
    
    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        source = LogSource('iOS Test Source', None)
        scanner = Scanner(source)
        self.parser = Parser(scanner)
    
    def tearDown(self):
        pass
    
    @log_test(logger, globals.log_separator)
    def testParserMockData(self):
        name = ''
        log_lines = ''
        log, errors = self.parser(name, log_lines)
        
    @log_test(logger, globals.log_separator)
    def testParserRealData(self):
        pass
    
        
   
