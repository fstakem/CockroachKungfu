# ------------------------------------------------------
#
#   Scanner.py
#   By: Fred Stakem
#   Created: 3.5.13
#
# ------------------------------------------------------

# Libs
import Utilities
from LogParser import Symbol
from LogParser import Scanner as BaseScanner
from LogParser import Token
from LogParser import ScanException
from TokenType import TokenType

ScannerState = Utilities.enum('Start', 'ParsedDateTime', 'ParsedPid', \
                              'ParsedTid', 'ParsedLevel', 'ParsedSource', \
                              'ParsedMsg')


class Scanner(BaseScanner):
    
    # Setup logging
    logger = Utilities.getLogger('AndroidLogParser::Scanner')
    
    def __init__(self, source):
        super(Scanner, self).__init__(source)
        self.state = ScannerState.Start
        
    def reset(self):
        self.state = ScannerState.Start
        super(Scanner, self).reset()

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
        if self.state == ScannerState.Start:
            return self.scanDateTime()
        elif self.state == ScannerState.ParsedDateTime:
            return self.scanPid()
        elif self.state == ScannerState.ParsedPid:
            return self.scanTid()
        elif self.state == ScannerState.ParsedTid:
            return self.scanLevel()
        elif self.state == ScannerState.ParsedLevel:
            return self.scanSource()
        elif self.state == ScannerState.ParsedSource:
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
        
        self.state = ScannerState.ParsedDateTime
        
        return Token(TokenType.DATE, self.symbol_buffer, self.start_position, self.current_position-1)
    
    def scanPid(self):
        while Symbol.isDigit(self.current_symbol):
            self.acceptSymbol(self.current_symbol)
            
        if len(self.symbol_buffer) < 1:
            raise ScanException('No PID symbols found.')
        
        self.state = ScannerState.ParsedPid
        
        return Token(TokenType.PID, self.symbol_buffer, self.start_position, self.current_position-1)

    def scanTid(self):
        while Symbol.isDigit(self.current_symbol):
            self.acceptSymbol(self.current_symbol)
            
        if len(self.symbol_buffer) < 1:
            raise ScanException('No TID symbols found.')
        
        self.state = ScannerState.ParsedTid
        
        return Token(TokenType.TID, self.symbol_buffer, self.start_position, self.current_position-1)
    
    def scanLevel(self):
        while Symbol.isCharacter(self.current_symbol):
            self.acceptSymbol(self.current_symbol)
            
        if len(self.symbol_buffer) != 1:
            raise ScanException('Incorrect number of symbols for the log level.')
        
        self.state = ScannerState.ParsedLevel
        
        return Token(TokenType.LEVEL, self.symbol_buffer, self.start_position, self.current_position-1)

    def scanSource(self):
        while Symbol.isCharacter(self.current_symbol) or \
              Symbol.isColon(self.current_symbol):
            self.acceptSymbol(self.current_symbol)
            
        if len(self.symbol_buffer) < 1:
            raise ScanException('No source symbols found.') 
        
        self.state = ScannerState.ParsedSource
        
        return Token(TokenType.SOURCE, self.symbol_buffer, self.start_position, self.current_position-1)

    def scanMsg(self):
        while not Symbol.isEol(self.current_symbol):
            self.acceptSymbol(self.current_symbol)
            
        if len(self.symbol_buffer) < 1:
            raise ScanException('No msg symbols found.') 
        
        self.state = ScannerState.ParsedMsg
        
        return Token(TokenType.MSG, self.symbol_buffer, self.start_position, self.current_position-1)

    
    
    
    
    
    
    
    