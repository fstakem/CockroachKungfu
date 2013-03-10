# ------------------------------------------------------
#
#   Event.py
#   By: Fred Stakem
#   Created: 3.10.13
#
# ------------------------------------------------------

# Libs
from datetime import *
from EventType import EventType

class Event(object):
    """This class represents an event."""
    
    def __init__(self, type=EventType.NONE, raw_data='Fake data', time=datetime.now()):
        self.type = type
        self.raw_data = raw_data
        self.metadata = None
        self.signatures = []
        self.time_occured = time
        
    def isEvent(self, event_str):
        for sig in self.signatures:
            pass
            # Test for part of sig in event str
        
    def __str__(self):
        time_str = str(self.time_occured)
        return 'Type: %s Data: %s Timestamp: %s' % (EventType.pprint(self.type), self.data, time_str)
    
    def __repr__(self):
        return str(self)
    
 
    
    
    
    