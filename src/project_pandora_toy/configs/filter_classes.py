import logging

class IgnoreRepeatedMessages(logging.Filter):
    """
     Filter class that ignores repeated log messages
     """
    def __init__(self):
        super(IgnoreRepeatedMessages, self).__init__()
        self.logged_messages = set()
    
    def filter(self, record):
        # Check if the message is already logged
        if record.msg in self.logged_messages:
            return 0
        else:
            self.logged_messages.add(record.msg)
            return 1
        
class ShowBelowErrorOnly(logging.Filter):
    """
     Filter class that shows messages BELOW Critical
     """
    def __init__(self):
        super(ShowBelowErrorOnly, self).__init__()
        self.logged_messages = set()
    
    def filter(self, record):
        return record.levelno <= logging.ERROR 