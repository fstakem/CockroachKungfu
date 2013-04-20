# ------------------------------------------------------
#
#   Event.py
#   By: Fred Stakem
#   Created: 3.10.13
#
# ------------------------------------------------------

# Libs
from EventType import EventType
from Metadata import Metadata
from EventSignature import Signature

class Event(object):
    """This class represents an event."""
    
    def __init__(self, name='Generic Event', event_type=EventType.NONE, signatures=[], metadata=Metadata()):
        self.name = name
        self.event_type = event_type
        self.signatures = signatures
        self.metadata = metadata
            
    def __str__(self):
        output = 'Event name: %s\tType: %s\tSignature: %s\tMetadata: %s' % \
                 (self.name, EventType.prettyPrint(self.event_type), str(self.signature), str(self.metadata))
        return output
    
    def __repr__(self):
        return str(self)
    
 
    
    
    
    