# ------------------------------------------------------
#
#   AndroidParser.py
#   By: Fred Stakem
#   Created: 3.5.13
#
# ------------------------------------------------------

# Libs
from datetime import *
import Utilities
from LogParser import Symbol
from LogParser import Parser
from LogParser import ParseException
from AndroidLogLine import AndroidLogLine
from AndroidLog import AndroidLog
from AndroidScanner import AndroidScannerState
from AndroidTokenType import AndroidTokenType
from AndroidLogLine import AndroidLogLevel

class AndroidParser(Parser):
    
    # Setup logging
    logger = Utilities.getLogger('AndroidParser')
    
    def __init__(self, scanner, source):
        super(AndroidParser, self).__init__(scanner, source)
    
    def parseLog(self, name, log_lines):
        log_lines = []
        errors = []
        for i, line in enumerate(log_lines):
            try:
                log_lines.append( self.parseLogLine(line) )
            except ParseException, e:
                errors.append( (i, e.msg()) )
            
        android_log = AndroidLog()
        android_log.name = name
        android_log.lines = log_lines
        
        return (android_log, errors) 
    
    def parseLogLine(self, log_line):
        android_log_line = AndroidLogLine()
        
        while True:
            token, symbol, state = self.scanner.scan()
        
            if token == None and Symbol.isEol(symbol) and state == AndroidScannerState.ParsedMsg:
                return android_log_line
            elif token.type == AndroidTokenType.DATE:
                android_log_line.timestamp = self.parseDateTime(token)
            elif token.type == AndroidTokenType.PID:
                android_log_line.pid = self.parsePid(token)
            elif token.type == AndroidTokenType.TID:
                android_log_line.tid = self.parseTid(token)
            elif token.type == AndroidTokenType.LEVEL:
                android_log_line.level = self.parseLevel(token)
            elif token.type == AndroidTokenType.SOURCE:
                android_log_line.source = self.parseSource(token)
            elif token.type == AndroidTokenType.MSG:
                android_log_line.msg = self.parseMsg(token)
            else:
                raise ParseException('Unknown token returned by the scanner.')
        
        raise ParseException('End of line not found.')
    
    def parseDateTime(self, token):
        dt = datetime.now()
        subtokens = token.split()
        
        date_subtokens = subtokens[0].split('-')
        if len(date_subtokens) < 2:
            raise ParseException('Error parsing date subtoken: %s' % (date_subtokens))
        dt.month = int(date_subtokens[0])
        dt.day = int(date_subtokens[1])
        
        time_subtokens = subtokens[1].split(':')
        if len(time_subtokens) < 3:
            raise ParseException('Error parsing time subtoken: %s' % (time_subtokens))
        dt.hour = int(time_subtokens[0])
        dt.minute = int(time_subtokens[1])
        
        seconds_subtokens = time_subtokens[2].split('.')
        if len(seconds_subtokens) < 2:
            raise ParseException('Error parsing seconds subtoken: %s' % (seconds_subtokens))
        dt.second = int(seconds_subtokens[0])
        dt.miccrosecond = int(seconds_subtokens[1])
        
        return dt
    
    def parsePid(self, token):
        try:
            pid = int(token.data)
            return pid
        except ValueError:
            raise ParseException('Error parsing pid token: %s' % str(token))
            
    def parseTid(self, token):
        try:
            tid = int(token.data)
            return tid
        except ValueError:
            raise ParseException('Error parsing tid token: %s' % str(token))
    
    def parseLevel(self, token):
        if token.data == 'V':
            return AndroidLogLevel.Verbose
        elif token.data == 'I':
            return AndroidLogLevel.Info
        elif token.data == 'D':
            return AndroidLogLevel.Debug
        elif token.data == 'W':
            return AndroidLogLevel.Warn
        elif token.data == 'E':
            return AndroidLogLevel.Error
        elif token.data == 'A':
            return AndroidLogLevel.Assert
        else:
            raise ParseException('Error parsing level token: %s' % str(token))
    
    def parseSource(self, token):
        return token.data[:-1]
    
    def parseMsg(self, token):
        return token.data
    
    
    
    