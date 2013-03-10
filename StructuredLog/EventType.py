# ------------------------------------------------------
#
#   EventType.py
#   By: Fred Stakem
#   Created: 3.10.13
#
# ------------------------------------------------------


# Libraries
import logging

# Classes
import Utilities

class EventType(object):
    """This class represents an event type that occurs in a log."""
       
    # Setup logging
    logger = Utilities.getLogger('EventType')
    
    # Class constants
    NONE = 0
    STANDARD = 1
    STATE_TRANSITION = 2
    STATE_ENTER = 3
    STATE_EXIT = 4
    
    readable_name = {
                     EventType.NONE:                'None',
                     EventType.STANDARD:            'Standard',
                     EventType.STATE_TRANSITION:    'State Transition',
                     EventType.STATE_ENTER:         'State Enter',
                     EventType.STATE_EXIT:          'State Exit'
                    }
    
    @classmethod
    def pprint(cls, type):
        return cls.readable_name[type]
    
    
    
    