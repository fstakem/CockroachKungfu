# ------------------------------------------------------
#
#   TestIosParser.py
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

class IosParserTest(unittest.TestCase):
    
    # Setup logging
    logger = Utilities.getLogger('IosParserTest')
    
    def setUp(self):
        source = LogSource('iOS Test Source', None)
        scanner = Scanner(source)
        self.parser = Parser(scanner)
    
    def tearDown(self):
        pass
    
    @log_test(logger, globals.log_separator)
    def testX(self):
        name = ''
        log_lines = ''
        log, errors = self.parser.parseLog(name, log_lines)
    
        
    # TODO
    # various tests
