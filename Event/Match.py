# ------------------------------------------------------
#
#   Match.py
#   By: Fred Stakem
#   Created: 4.20.13
#
# ------------------------------------------------------

# Libs
from EventSignature import Signature
from LogParser import LogLine
from MatchType import MatchType

class Match(object):
    """This class represents a match of an event."""
    
    def __init__(self, name='Generic event match', match_type=MatchType.NONE,
                 signature=Signature(), log_line=LogLine(), line_number=0):
        self.name = name
        self.match_type = match_type
        self.signature = signature
        self.log_line = log_line
        self.line_number = line_number
        
    def __str__(self):
        output = 'Match name: %s\tSignature: %s\tLog line:%s\tLine number:%s' % \
                 (self.name, str(self.signature), str(self.log_line), str(self.line_number))
        return output
    
    def __repr__(self):
        return str(self)