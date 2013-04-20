# ------------------------------------------------------
#
#   Sample.py
#   By: Fred Stakem
#   Created: 4.20.13
#
# ------------------------------------------------------

# Libs
from datetime import datetime
from Event import Event
from Match import Match

class Sample(object):
    """This class represents a sample of an event."""
    
    def __init__(self, name='Generic sample', event=Event(), timestamp=datetime(), match=Match()):
        self.name = name
        self.event = event
        self.timestamp = timestamp
        self.match = match
        
    def __str__(self):
        output = 'Sample name: %s\tEvent: %s\tTimestamp: %s\tMatch: %s' % \
                 (self.name, str(self.event), str(self.timestamp), str(self.match))
        return output
    
    def __repr__(self):
        return str(self)