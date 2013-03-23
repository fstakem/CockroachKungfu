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
    """This class represents a iOS token type that is found in a scanned file."""
       
    # Setup logging
    logger = Utilities.getLogger('IosLogParser::TokenType')
    
    # Class constants
    NONE = 0
    TIMESTAMP = 1
    SOURCE = 2
    PID = 3
    MACH_PORT = 4
    MSG = 5
    
    readable_name = {
                     TokenType.NONE:         'None',
                     TokenType.TIMESTAMP:    'Timestamp',
                     TokenType.SOURCE:       'Source',
                     TokenType.PID:          'Pid',
                     TokenType.MACH_PORT:    'Mach Port',
                     TokenType.MSG:          'Msg',
                    }
    
    def __init__(self):
        pass
    
    @classmethod
    def prettyPrint(cls, type):
        return cls.readable_name[type]
    
    
    
    