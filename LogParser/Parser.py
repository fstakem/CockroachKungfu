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
    
    def __init__(self, scanner, source):
        self.scanner = scanner
        self.source = source
        self.current_token = None
    
    def parseLog(self, log_lines):
        pass
    
    def parseLogLine(self, log_line):
        pass