# ------------------------------------------------------
#
#   Signature.py
#   By: Fred Stakem
#   Created: 4.20.13
#
# ------------------------------------------------------

# Libs

class Signature(object):
    """This base class represents a signature for an event."""
    
    def __init__(self, field_name='name', expected_value='generic component'):
        self.field_name = field_name
        self.expected_value = expected_value
    
    def __str__(self):
        return 'Field name: %s\tExpected value: %s' % (self.field_name, str(self.expected_value))
    
    def __repr__(self):
        return str(self)
    
    def isMatch(self, log_line):
        pass