# ------------------------------------------------------
#
#   LogSource.py
#   By: Fred Stakem
#   Created: 3.9.13
#
# ------------------------------------------------------


# Libs
import Utilities
from LogParser import LogSource as BaseLogSource
from LogParser import Symbol

class LogSource(BaseLogSource):
    """This class represents an android source for giving symbols to the scanner."""
       
    # Setup logging
    logger = Utilities.getLogger('AndroidLogParser::LogSource')
    
    def __init__(self, name='Android Source', symbols=''):
        super(LogSource, self).__init__(name, symbols)
    
    def getNextSymbol(self):
        self.current_position += 1
        
        try:
            next_symbol = self.symbols[self.current_position]
            self.last_symbol = next_symbol
            
            return (next_symbol, self.current_position)
        except IndexError:
            return Symbol.EOL

        
        
    
            