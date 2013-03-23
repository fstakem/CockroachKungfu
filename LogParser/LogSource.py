# ------------------------------------------------------
#
#   LogSource.py
#   By: Fred Stakem
#   Created: 3.9.13
#
# ------------------------------------------------------


# Libs
import Utilities
from Symbol import Symbol

class LogSource(object):
    """This class represents a log source for giving symbols to the scanner."""
       
    # Setup logging
    logger = Utilities.getLogger('LogParser::LogSource')
    
    def __init__(self, name='Generic Source', symbols=''):
        self.name = name
        self.symbols = symbols
        self.last_symbol = None
        self.current_position = -1
    
    def getNextSymbol(self):
        self.current_position += 1
        
        try:
            next_symbol = self.symbols[self.current_position]
            self.last_symbol = next_symbol
            
            return (next_symbol, self.current_position)
        except IndexError:
            return Symbol.EOL
        
        
    
            