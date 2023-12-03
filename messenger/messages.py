########################################################################
# COMPONENT:
#    MESSAGES
# Author:
#    Br. Helfrich, Kyle Mueller, Seth Bolander,
#    <your name here if you made a change>
# Summary: 
#    This class stores the notion of a collection of messages
########################################################################

import message
from control import get_control_from_string

##################################################
# MESSAGES
# The collection of high-tech messages
##################################################
class Messages:

    ##################################################
    # MESSAGES CONSTRUCTOR
    # Read a file to fill the messages
    ##################################################
    def __init__(self, filename):
        self._messages = []
        self._read_messages(filename)

    ##################################################
    # MESSAGES :: DISPLAY
    # Display the list of messages
    ################################################## 
    def display(self, user_control):
        for m in self._messages:
            m.display_properties(user_control)

    ##################################################
    # MESSAGES :: SHOW
    # Show a single message
    ################################################## 
    def show(self, id, user_control):
        for m in self._messages:
            if m.get_id() == id:
                m.display_text(user_control)
                return True
        return False

    ##################################################
    # MESSAGES :: UPDATE
    # Update a single message
    ################################################## 
    def update(self, id, text, user_control):
        for m in self._messages:
            if m.get_id() == id:
                m.update_text(text, user_control)

    ##################################################
    # MESSAGES :: REMOVE
    # Remove a single message
    ################################################## 
    def remove(self, id, user_control):
        for m in self._messages:
            if m.get_id() == id:
                m.clear(user_control)

    ##################################################
    # MESSAGES :: ADD
    # Add a new message
    ################################################## 
    def add(self, control, text, author, date):
        m = message.Message(control, text, author, date)
        self._messages.append(m)

    ##################################################
    # MESSAGES :: READ MESSAGES
    # Read messages from a file
    ################################################## 
    def _read_messages(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    text_control, author, date, text = line.split('|')
                    control_level = get_control_from_string(text_control)
                    self.add(control_level, text.rstrip('\r\n'), author, date)

        except FileNotFoundError:
            print(f"ERROR! Unable to open file \"{filename}\"")
            return
