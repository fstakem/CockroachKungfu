# ------------------------------------------------------
#
#   TestStructuredLog.py
#   By: Fred Stakem
#   Created: 4.20.13
#
# ------------------------------------------------------

# Libs
import unittest
from Utilities import *
from Globals import *
from StructuredData import StructuredLog
from StructuredData import StructuredLogSample

class StructuredLogTest(unittest.TestCase):
    
    # Setup logging
    logger = Utilities.getLogger('StructuredLogTest')
    
    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
     
    @log_test(logger, globals.log_separator)
    def testFindEventsInLog(self):
        expected_event_samples = []
        log = None
        events = []
        structured_log = StructuredLog('Test structured log', events)
        sample = structured_log.findEventsInLog('Test structured log sample', log)
        
        if len(sample.event_samples) == 0:
            StructuredLogTest.logger.error('No returned samples')
            
            
            
          
            
            
            
        