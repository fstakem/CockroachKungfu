# ------------------------------------------------------
#
#   AndroidTokenizer.py
#   By: Fred Stakem
#   Created: 3.5.13
#
# ------------------------------------------------------

# Libs
import Utilities

class AndroidTokenizer(object):
    
    # Setup logging
    logger = Utilities.getLogger('AndroidParser')
    
    @classmethod
    def createTokens(cls, log_line):
        tokens = log_line.split(':')
        msg_token = ':'.join(tokens[3:]).strip()
        start_line = ':'.join(tokens[0:3])
        tokens = start_line.split()
        date_token = ' '.join(tokens[0:2])
        
        return [date_token, tokens[2], tokens[3], tokens[4], tokens[5], msg_token]