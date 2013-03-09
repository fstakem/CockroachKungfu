# ------------------------------------------------------
#
#   ScanException.py
#   By: Fred Stakem
#   Created: 3.9.13
#
# ------------------------------------------------------


# Libraries
import sys

# Classes

class ScanException(Exception):
    """This class represents an exception caused when scanning."""
    
    def __init__(self, *args):
        Exception.__init__(self, *args)
        self.wrapped_exc = sys.exc_info( )
       