# ------------------------------------------------------
#
#   AndroidTokenType.py
#   By: Fred Stakem
#   Created: 3.9.13
#
# ------------------------------------------------------


# Libraries
import logging

# Classes
import Utilities

class AndroidTokenType(object):
    """This class represents a android token type that is found in a scanned file."""
       
    # Setup logging
    logger = Utilities.getLogger('AndroidTokenType')
    
    # Class constants
    NONE = 0
    DATE = 1
    PID = 2
    TID = 3
    LEVEL = 4
    SOURCE = 5
    MSG = 6
    
    readable_name = {
                     AndroidTokenType.NONE:         'None',
                     AndroidTokenType.DATE:         'Date',
                     AndroidTokenType.PID:          'Pid',
                     AndroidTokenType.TID:          'Tid',
                     AndroidTokenType.LEVEL:        'Level',
                     AndroidTokenType.SOURCE:       'Source',
                     AndroidTokenType.MSG:          'Msg',
                    }
    
    def __init__(self):
        pass
    
    @classmethod
    def prettyPrint(cls, type):
        return cls.readable_name[type]
    
    
    
    