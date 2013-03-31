# ------------------------------------------------------
#
#   Token.py
#   By: Fred Stakem
#   Created: 3.30.13
#
# ------------------------------------------------------


# Libraries
import logging

# Classes
import Utilities
from TokenType import TokenType
from LogParser import Token as BaseToken

class Token(BaseToken):
    """This class represents a token that is found in a scanned line."""
       
    # Setup logging
    logger = Utilities.getLogger('IosLogParser::Token')
    
    def __init__(self, type=TokenType.NONE, data=None, start_position=-1, end_position=-1):
        super(Token, self).__init__(type, data, start_position, end_position)
        
    def __str__(self):
        return 'Type: %s Data: %s Position: %s to %s' % (TokenType.prettyPrint(self.type), 
                                                         self.data, 
                                                         str(self.start_position),
                                                         str(self.end_position))
      
   
    
    
    
    
    
    