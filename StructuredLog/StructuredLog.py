# ------------------------------------------------------
#
#   StructuredLog.py
#   By: Fred Stakem
#   Created: 3.9.13
#
# ------------------------------------------------------

# Libs
from Metadata import Metadata

class StructuredLog(object):
    """This class represents a structured log where structured data is held."""
    
    def __init__(self, name='Generic structured log', events=[], metadata=Metadata()):
        self.name = name
        self.events = events
        self.metadata = metadata
        
    def __str__(self):
        output = 'Log name: %s\tNumber of events: %d\tMetadata: %s' % \
                 (self.name, len(self.events), str(self.metadata))
        return output
    
    def __repr__(self):
        return str(self)
    
    def findEventsInLog(self, log):
        pass