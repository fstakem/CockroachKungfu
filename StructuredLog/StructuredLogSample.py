# ------------------------------------------------------
#
#   StructuredLogSample.py
#   By: Fred Stakem
#   Created: 4.20.13
#
# ------------------------------------------------------

# Libs
from StructuredLog import StructuredLog

class StructuredLogSample(object):
    """This class represents a structured log sample where structured data is held."""
    
    def __init__(self, name='Generic structured log sample', structured_log=StructuredLog(), event_samples=[]):
        self.name = name
        self.structured_log = structured_log
        self.event_samples = event_samples
        
    def __str__(self):
        output = 'Log sample name: %s\tLog: %s\tNumber of event found: %d' % \
                 (self.name, str(self.structured_log), len(self.event_samples))
        return output
    
    def __repr__(self):
        return str(self)