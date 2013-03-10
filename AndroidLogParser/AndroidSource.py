# ------------------------------------------------------
#
#   AndroidSource.py
#   By: Fred Stakem
#   Created: 3.9.13
#
# ------------------------------------------------------


# Libraries
import logging
from LogParser import LogSource
from LogParser import Symbol

# Classes
import Utilities

class AndroidSource(LogSource):
    """This class represents an android source for giving symbols to the scanner."""
       
    # Setup logging
    logger = Utilities.getLogger('AndroidSource')
    
    def __init__(self, name='Android Source', symbols=''):
        super(AndroidSource, self).__init__(name, symbols)
    
    def getNextSymbol(self):
        self.current_position += 1
        
        try:
            next_symbol = self.symbols[self.current_position]
            self.last_symbol = next_symbol
            
            return (next_symbol, self.current_position)
        except IndexError:
            return Symbol.EOL

        
        
    
            