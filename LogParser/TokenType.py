# ------------------------------------------------------
#
#   TokenType.py
#   By: Fred Stakem
#   Created: 3.9.13
#
# ------------------------------------------------------


# Libraries
import logging

# Classes
import Utilities

class TokenType(object):
    """This class represents a token type that is found in a scanned file."""
       
    # Setup logging
    logger = Utilities.getLogger('TokenType')
    
    # Class constants
    NONE = 0
    OBJECT = 1
    
    readable_name = {
                     TokenType.NONE:                'None',
                     TokenType.OBJECT:              'Object',
                    }
     
    @classmethod
    def pprint(cls, type):
        return cls.readable_name[type]
    
    
    
    