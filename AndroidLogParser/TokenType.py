# ------------------------------------------------------
#
#   TokenType.py
#   By: Fred Stakem
#   Created: 3.9.13
#
# ------------------------------------------------------


# Libs
import Utilities

class TokenType(object):
    """This class represents a android token type that is found in a scanned file."""
       
    # Setup logging
    logger = Utilities.getLogger('AndroidLogParser::TokenType')
    
    # Class constants
    NONE = 0
    DATE = 1
    PID = 2
    TID = 3
    LEVEL = 4
    SOURCE = 5
    MSG = 6
    
    readable_name = {
                     TokenType.NONE:         'None',
                     TokenType.DATE:         'Date',
                     TokenType.PID:          'Pid',
                     TokenType.TID:          'Tid',
                     TokenType.LEVEL:        'Level',
                     TokenType.SOURCE:       'Source',
                     TokenType.MSG:          'Msg',
                    }
    
    def __init__(self):
        pass
    
    @classmethod
    def prettyPrint(cls, type):
        return cls.readable_name[type]
    
    
    
    