########################################################################
# COMPONENT:
#    MESSAGE
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of a message
########################################################################

from control import Control, control_read, control_write

##################################################
# MESSAGE
# One message to be displayed to the user or not
##################################################
class Message:

  # Static variable for the next id
  _id_next = 100

  ##################################################
  # MESSAGE DEFAULT CONSTRUCTOR
  # Set a message to empty
  ##################################################
  def __init__(self):
    self._empty = True
    self._control = Control.Public
    self._text = "Empty"
    self._author = ""
    self._date = ""
    self._id = Message._id_next
    Message._id_next += 1

  ##################################################
  # MESSAGE NON-DEFAULT CONSTRUCTOR
  # Create a message and fill it
  ##################################################  
  def __init__(self, control, text, author, date):
    self._control = control or Control.Public
    self._text = text
    self._author = author
    self._date = date
    self._id = Message._id_next
    Message._id_next += 1
    self._empty = False

  ##################################################
  # MESSAGE :: GET ID
  # Determine the unique ID of this message
  ##################################################   
  def get_id(self):
    return self._id

  ##################################################
  # MESSAGE :: DISPLAY PROPERTIES
  # Display the attributes/properties but not the
  # content of this message
  ##################################################  
  def display_properties(self, user_control):
    if self._empty:
        return
    if control_read(self._control, user_control):
      print(f"\t[{self._id}] Message from {self._author} at {self._date}")
    else:
      print(f"\t[{self._id}] UNAUTHORIZED ACCESS")

  ##################################################
  # MESSAGE :: DISPLAY TEXT
  # Display the contents or the text of the message
  ################################################## 
  def display_text(self, user_control):
    if control_read(self._control, user_control):
      print(f"\tMessage: {self._text}")
    else:
      print("UNAUTHORIZED ACCESS")

  ##################################################
  # MESSAGE :: UPDATE TEXT
  # Update the contents or text of the message
  ################################################## 
  def update_text(self, new_text, user_control):
    if control_write(self._control, user_control):
      self._text = new_text
    else:
      print("RESTRICTED WRITE ACCESS")

  ##################################################
  # MESSAGE :: CLEAR
  # Delete the contents of a message and mark it as empty
  ################################################## 
  def clear(self, user_control):
    if control_write(self._control, user_control):
      self._text = "Empty"
      self._author = ""
      self._date = ""
      self._empty = True
    else:
      print("RESTRICTED DELETE ACCESS")
