# ------------------------------------------------------
#
#   AndroidScanner.py
#   By: Fred Stakem
#   Created: 3.5.13
#
# ------------------------------------------------------

# Libs
import Utilities
from LogParser import Symbol
from LogParser import Scanner
from LogParser import Token
from LogParser import ScanException
from AndroidTokenType import AndroidTokenType

AndroidScannerState = Utilities.enum('Start', 'ParsedDateTime', 'ParsedPid', \
                                     'ParsedTid', 'ParsedLevel', 'ParsedSource', \
                                     'ParsedMsg')


class AndroidScanner(Scanner):
    
    # Setup logging
    logger = Utilities.getLogger('AndroidScanner')
    
    def __init__(self, source):
        super(AndroidScanner, self).__init__(source)
        self.state = AndroidScannerState.Start
        
    def reset(self):
        self.state = AndroidScannerState.Start
        super(AndroidScanner, self).reset()

    def scan(self):
        self.current_symbol, self.current_position = self.source.getNextSymbol()
        self.start_position = self.current_position
        
        while True:
            if Symbol.isSeparator(self.current_symbol):
                self.scanSeperator(self.source)
            elif Symbol.isEol(self.current_symbol):
                return (None, self.current_symbol, self.state)
            else:
                return (self.scanToken(self.source), self.current_symbol, self.state)
            
    def scanSeperator(self):
        while Symbol.isSeparator(self.current_symbol):
            self.current_symbol, self.current_position = self.source.getNextSymbol()
            
    def scanToken(self):
        if self.state == AndroidScannerState.Start:
            return self.scanDateTime()
        elif self.state == AndroidScannerState.ParsedDateTime:
            return self.scanPid()
        elif self.state == AndroidScannerState.ParsedPid:
            return self.scanTid()
        elif self.state == AndroidScannerState.ParsedTid:
            return self.scanLevel()
        elif self.state == AndroidScannerState.ParsedLevel:
            return self.scanSource()
        elif self.state == AndroidScannerState.ParsedSource:
            return self.scanMsg()
        
        return None
            
    def scanDateTime(self):
        while Symbol.isDigit(self.current_symbol) or \
              Symbol.isDash(self.current_symbol):
            self.acceptSymbol(self.current_symbol)
            
        while Symbol.isSeparator(self.current_symbol):
            self.acceptSymbol(self.current_symbol)
            
        while Symbol.isDigit(self.current_symbol) or \
              Symbol.isColon(self.current_symbol) or \
              Symbol.isDot(self.current_symbol):
            self.acceptSymbol(self.current_symbol)
            
        tokens = self.symbol_buffer.split()
        if len(tokens) < 2:
            raise ScanException('Date time has incorrect number of subtokens.')
        elif len(tokens[0]) < 5:
            raise ScanException('First date time subtoken is incorrect length.')
        elif len(tokens[1]) < 12:
            raise ScanException('Second date time subtoken is incorrect length.')
        
        self.state = AndroidScannerState.ParsedDateTime
        
        return Token(AndroidTokenType.DATE, self.symbol_buffer, self.start_position, self.current_position-1)
    
    def scanPid(self):
        while Symbol.isDigit(self.current_symbol):
            self.acceptSymbol(self.current_symbol)
            
        if len(self.symbol_buffer) < 1:
            raise ScanException('No PID symbols found.')
        
        self.state = AndroidScannerState.ParsedPid
        
        return Token(AndroidTokenType.PID, self.symbol_buffer, self.start_position, self.current_position-1)

    def scanTid(self):
        while Symbol.isDigit(self.current_symbol):
            self.acceptSymbol(self.current_symbol)
            
        if len(self.symbol_buffer) < 1:
            raise ScanException('No TID symbols found.')
        
        self.state = AndroidScannerState.ParsedTid
        
        return Token(AndroidTokenType.TID, self.symbol_buffer, self.start_position, self.current_position-1)
    
    def scanLevel(self):
        while Symbol.isCharacter(self.current_symbol):
            self.acceptSymbol(self.current_symbol)
            
        if len(self.symbol_buffer) != 1:
            raise ScanException('Incorrect number of symbols for the log level.')
        
        self.state = AndroidScannerState.ParsedLevel
        
        return Token(AndroidTokenType.LEVEL, self.symbol_buffer, self.start_position, self.current_position-1)

    def scanSource(self):
        while Symbol.isCharacter(self.current_symbol) or \
              Symbol.isColon(self.current_symbol):
            self.acceptSymbol(self.current_symbol)
            
        if len(self.symbol_buffer) < 1:
            raise ScanException('No source symbols found.') 
        
        self.state = AndroidScannerState.ParsedSource
        
        return Token(AndroidTokenType.SOURCE, self.symbol_buffer, self.start_position, self.current_position-1)

    def scanMsg(self):
        while not Symbol.isEol(self.current_symbol):
            self.acceptSymbol(self.current_symbol)
            
        if len(self.symbol_buffer) < 1:
            raise ScanException('No msg symbols found.') 
        
        self.state = AndroidScannerState.ParsedMsg
        
        return Token(AndroidTokenType.MSG, self.symbol_buffer, self.start_position, self.current_position-1)

    
    
    
    
    
    
    
    