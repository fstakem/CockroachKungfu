# ------------------------------------------------------
#
#   Scanner.py
#   By: Fred Stakem
#   Created: 3.9.13
#
# ------------------------------------------------------

# Libraries
import logging

# Classes
import Utilities
from Symbol import Symbol

class Scanner(object):
    """This class represents a scanner that scans a log line outputting tokens."""
       
    # Setup logging
    logger = Utilities.getLogger('LogParser::Scanner')
    
    def __init__(self, source):
        self.source = source
        self.reset()
        
    def reset(self):
        self.current_symbol = None
        self.start_position = None
        self.current_position = None
        self.symbol_buffer = ''
        
    def scan(self):
        pass
    
    def getFirstSymbol(self, advance=False):
        if advance:
            self.current_symbol, self.current_position = self.source.getNextSymbol()
        self.start_position = self.current_position
    
    def acceptSymbol(self):
        self.symbol_buffer += self.current_symbol
        self.current_symbol, self.current_position = self.source.getNextSymbol()
        
    def rejectSymbol(self):
        self.current_symbol, self.current_position = self.source.getNextSymbol()
            
 