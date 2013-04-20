# ------------------------------------------------------
#
#   Event.py
#   By: Fred Stakem
#   Created: 3.10.13
#
# ------------------------------------------------------

# Libs
from Type import Type
from Metadata import Metadata
from Signature import Signature

class Event(object):
    """This class represents an event."""
    
    def __init__(self, name='Generic Event', type=Type.NONE, signature=Signature(), metadata=Metadata()):
        self.name = name
        self.type = type
        self.signature = signature
        self.metadata = metadata
            
    def __str__(self):
        
        return 'Type: %s Data: %s Timestamp: %s' % (EventType.pprint(self.type), self.data, time_str)
    
    def __repr__(self):
        return str(self)
    
 
    
    
    
    