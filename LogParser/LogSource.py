# ------------------------------------------------------
#
#   LogSource.py
#   By: Fred Stakem
#   Created: 3.9.13
#
# ------------------------------------------------------


# Libraries
import logging

# Classes
import Utilities

class LogSource(object):
    """This class represents a log source for giving symbols to the scanner."""
       
    # Setup logging
    logger = Utilities.getLogger('LogSource')
    
    def __init__(self, name='Generic Source', symbols=''):
        self.name = name
        self.symbols = symbols
        self.last_symbol = None
        self.current_position = -1
    
    def getNextSymbol(self):
        pass
        
        
    
            