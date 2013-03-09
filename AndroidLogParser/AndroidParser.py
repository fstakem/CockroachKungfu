# ------------------------------------------------------
#
#   AndroidParser.py
#   By: Fred Stakem
#   Created: 3.5.13
#
# ------------------------------------------------------

# Libs
import Utilities
from Parser import Parser
from AndroidTokenizer import AndroidTokenizer
from AndroidLogLine import AndroidLogLine
from AndroidLog import AndroidLog
from ParseException import ParseException

class AndroidParser(Parser):
    
    # Setup logging
    logger = Utilities.getLogger('AndroidParser')
    
    @classmethod
    def createLog(cls, log_lines):
        android_log_lines = []
        for line in log_lines:
            android_log_line = cls.createLogLine(line)
            
        # TODO
        android_log = AndroidLog()
        
        return android_log 
    
    @classmethod
    def createLogLine(cls, log_line):
        tokens = AndroidTokenizer.createTokens(log_line)
        
        # TODO
        # get tokens
        timestamp = cls.parseTimestamp(tokens[0])
        pid = cls.parsePid(tokens[1])
        tid = cls.parseTid(tokens[2])
        level = cls.parseLevel(tokens[3])
        source = cls.parseSource(tokens[4])
        msg = cls.parseMsg(tokens[5])
        android_log_line = AndroidLogLine(timestamp, pid, tid, level, source, msg)
        
        return android_log_line
    
    @classmethod
    def parseTimestamp(cls, token):
        pass
    
    @classmethod
    def parsePid(cls, token):
        try:
            pid = int(token)
            return pid
        except ValueError:
            raise ParseException('Error parsing pid token:' % (token) )
            
    @classmethod
    def parseTid(cls, token):
        pass
    
    @classmethod
    def parseLevel(cls, token):
        pass
    
    @classmethod
    def parseSource(cls, token):
        pass
    
    @classmethod
    def parseMsg(cls, token):
        pass
    
    
    
    