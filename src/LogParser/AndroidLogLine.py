# ------------------------------------------------------
#
#   AndroidLogLine.py
#   By: Fred Stakem
#   Created: 3.3.13
#
# ------------------------------------------------------

# Libs
from LogLine import LogLine

class AndroidLogLine(LogLine):
    
    def __init__(self, timestamp=-1, pid=-1, tid=-1, level=-1, source=-1, msg=''):
        self.timestamp = timestamp
        self.pid = pid
        self.tid = tid
        self.level = level
        self.source = source
        self.msg = msg
    
    def __str__(self):
        return ''
    
    def __repr__(self):
        return str(self)