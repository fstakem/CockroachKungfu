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
    
    def __init__(self, scanner):
        self.scanner = scanner
        self.current_token = None
    
    def parseLog(self, name, log_lines):
        pass
    
    def parseLogLine(self, log_line):
        pass