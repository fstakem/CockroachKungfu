# ------------------------------------------------------
#
#   TestScanner.py
#   By: Fred Stakem
#   Created: 3.30.13
#
# ------------------------------------------------------

# Libs
import unittest
from Globals import *
from Utilities import *
from LogParser import LogSource
from IosLogParser import TokenType
from IosLogParser import Token
from IosLogParser import Scanner
from IosLogParser import ScannerState

class ScannerTest(unittest.TestCase):
    
    # Setup logging
    logger = Utilities.getLogger('ScannerTest')
    data_file = '../data/iphone_log_1.txt'
    
    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        self.source = LogSource('iOS Test Source', None)
        self.scanner = Scanner('iOS Test Scanner', self.source)
    
    def tearDown(self):
        pass
    
    @log_test(logger, globals.log_separator)
    def testScannerTimestamp(self):
        timestamp_str = '2013-03-22 22:17:52.317'
        input_symbols = timestamp_str + ' MobileCalculator'
        input_token = Token(TokenType.TIMESTAMP, timestamp_str)
        self.scanner.reset(input_symbols)
        
        token, current_symbol, state, error = self.scanner.scan()    
        assert error == None, error[2]
            
        ScannerTest.logger.debug('Input data: %s' % (input_symbols))
        ScannerTest.logger.debug('Expected token: %s' % (str(input_token)))
        ScannerTest.logger.debug('Actual token: %s' % (str(token)))
        assert token == input_token, 'Timestamp string was incorrectly scanned.'
    
    @log_test(logger, globals.log_separator)
    def testScannerSource(self):
        pass
    
    @log_test(logger, globals.log_separator)
    def testScannerPid(self):
        pass
    
    @log_test(logger, globals.log_separator)
    def testScannerMachPort(self):
        pass
    
    @log_test(logger, globals.log_separator)
    def testScannerMsg(self):
        pass
    
    @log_test(logger, globals.log_separator)
    def testScannerLine(self):
        symbols = '2013-03-22 22:17:52.317 MobileCalculator[22262:c07] Digit pressed: 8\n'
        #self.scanner.reset(symbols)
        
        ScannerTest.logger.debug('Test line: ' + symbols[:-1])
    
        
    @log_test(logger, globals.log_separator)
    def testScannerRealData(self):
        ScannerTest.logger.debug('Testing data in the file: ' + ScannerTest.data_file)
        symbols = readStrFromFile(ScannerTest.data_file)
        self.scanner.reset(symbols)
        token = Token()
        
        #while token != None:
            #token, current_symbol, state, error = self.scanner()
            #if error != None:
                #pass
            #output = 'Scanned token: %s' % ( str(token) )
            #ScannerTest.logger.debug(output)
        
    
        
   
   
   
