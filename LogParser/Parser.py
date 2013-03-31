# ------------------------------------------------------
#
#   Parser.py
#   By: Fred Stakem
#   Created: 3.3.13
#
# ------------------------------------------------------

# Libs

class Parser(object):
    """This class represents a parser to parse log files."""
    
    def __init__(self, name, scanner):
        self.name = name
        self.scanner = scanner
        self.current_token = None
        
    def __call__(self):
        pass
    
    def reset(self):
        self.scanner.reset()
    
    def parseLogLine(self, log_line):
        pass