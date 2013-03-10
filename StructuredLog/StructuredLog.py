# ------------------------------------------------------
#
#   StructuredLog.py
#   By: Fred Stakem
#   Created: 3.9.13
#
# ------------------------------------------------------

# Libs
from LogParser import Log
from LogMetaData import LogMetaData

class StructuredLog(object):
    """This class represents a structured log where structured data is held."""
    
    def __init__(self, unstructured_log=Log(), metadata=LogMetaData(), \
                 line_metadata={}):
        self.unstructured_log = unstructured_log
        self.metadata = metadata
        self.line_metadata = line_metadata