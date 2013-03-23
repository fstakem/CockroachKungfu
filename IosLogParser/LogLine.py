# ------------------------------------------------------
#
#   LogLine.py
#   By: Fred Stakem
#   Created: 3.23.13
#
# ------------------------------------------------------

# Libs
import datetime
from LogParser import LogLine as BaseLogLine

class LogLine(BaseLogLine):
    
    def __init__(self, timestamp=datetime.datetime.now(), pid=-1, 
                 mach_port=-1, source='Main', msg='iOS log msg.'):
        self.timestamp = timestamp
        self.source = source
        self.pid = pid
        self.mach_port = mach_port
        self.msg = msg
    
    def __str__(self):
        return str(self.timestamp) + ' ' + str(self.pid) + ' ' + \
               str(self.mach_port) +  ' ' + str(self.source) + ' ' + \
               self.msg
                  
    def __repr__(self):
        return str(self)
    
    
    
    