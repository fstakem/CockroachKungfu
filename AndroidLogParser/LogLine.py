# ------------------------------------------------------
#
#   LogLine.py
#   By: Fred Stakem
#   Created: 3.3.13
#
# ------------------------------------------------------

# Libs
import datetime
import Utilities
from LogParser import LogLine as BaseLogLine

LogLevel = Utilities.enum('Verbose', 'Info', 'Debug', 'Warn', 'Error', 'Assert')

class LogLine(BaseLogLine):
    
    def __init__(self, timestamp=datetime.datetime.now(), pid=-1, 
                 tid=-1, level=LogLevel.Verbose, source='Main', 
                 msg='Android log msg.'):
        self.timestamp = timestamp
        self.pid = pid
        self.tid = tid
        self.level = level
        self.source = source
        self.msg = msg
    
    def __str__(self):
        return str(self.timestamp) + ' ' + str(self.pid) + ' ' + \
               str(self.tid) + ' ' + str(self.level) + ' ' + \
               str(self.source) + ' '  + self.msg
                  
    def __repr__(self):
        return str(self)
    
    
    
    