########################################################################
# COMPONENT:
#    INTERACT
# Author:
#    Br. Helfrich, Kyle Mueller, Seth Bolander,
#    <your name here if you made a change>
# Summary:
#    This class allows one user to interact with the system
########################################################################

import messages
import control


###############################################################
# USER
# User has a name and a password
###############################################################
class User:

  def __init__(self, name, password, control):
    self.name = name
    self.password = password
    self.control = control


userlist = [["AdmiralAbe", "password", control.Control.Secret],
            ["CaptainCharlie", "password", control.Control.Priviliged],
            ["SeamanSam", "password", control.Control.Confidential],
            ["SeamanSue", "password", control.Control.Confidential],
            ["SeamanSly", "password", control.Control.Confidential]]

###############################################################
# USERS
# All the users currently in the system
###############################################################
users = [User(*u) for u in userlist]

ID_INVALID = -1


######################################################
# INTERACT
# One user interacting with the system
######################################################
class Interact:

  ##################################################
  # INTERACT CONSTRUCTOR
  # Authenticate the user and get him/her all set up
  ##################################################
  def __init__(self, username, password, p_messages):
    control_level = self._authenticate(username, password)
    if not control_level:
      raise Exception("User and password does not match!")
      return
    self._username = username
    self._control_level = control_level
    self._p_messages = p_messages
  
  ##################################################
  # INTERACT :: SHOW
  # Show a single message
  ##################################################
  def show(self):
    id_ = self._prompt_for_id("display")
    if not self._p_messages.show(id_, self._control_level):
      print(f"ERROR! Message ID \'{id_}\' does not exist")
    print()

  ##################################################
  # INTERACT :: DISPLAY
  # Display the set of messages
  ##################################################
  def display(self):
    print("Messages:")
    self._p_messages.display(self._control_level)
    print()

  ##################################################
  # INTERACT :: ADD
  # Add a single message
  ##################################################
  def add(self):
    self._p_messages.add(self._prompt_for_control(),
                         self._prompt_for_line("message"),
                         self._username,
                         self._prompt_for_line("date"))

  ##################################################
  # INTERACT :: UPDATE
  # Update a single message
  ##################################################
  def update(self):
    id_ = self._prompt_for_id("update")
    if not self._p_messages.show(id_, self._control_level):
      print(f"ERROR! Message ID \'{id_}\' does not exist\n")
      return
    self._p_messages.update(id_, self._prompt_for_line("message"),
                            self._control_level)
    print()

  ##################################################
  # INTERACT :: REMOVE
  # Remove one message from the list
  ##################################################
  def remove(self):
    self._p_messages.remove(self._prompt_for_id("delete"),
                            self._control_level)

  ##################################################
  # INTERACT :: PROMPT FOR LINE
  # Prompt for a line of input
  ##################################################
  def _prompt_for_line(self, verb):
    return input(f"Please provide a {verb}: ")

  ##################################################
  # INTERACT :: PROMPT FOR CONTROL
  # Prompt for a message's control level
  ##################################################
  def _prompt_for_control(self):
    control_level = int(input("Please provide a control level (1 = Public, 2 = Confidential, 3 = Secret, 4 = Top Secret): "))
    if self._control_level.value >= control_level:
      print("Control level input too low, upgrading to higher sensitivity.")
      return self._control_level
    elif 1 <= control_level <= 4:
      return int(control_level)
    else:
      print("Invalid input, upgrading to current user's sensitivity.")
      return self._control_level

  ##################################################
  # INTERACT :: PROMPT FOR ID
  # Prompt for a message ID
  ##################################################
  def _prompt_for_id(self, verb):
    return int(input(f"Select the message ID to {verb}: "))

  ##################################################
  # INTERACT :: AUTHENTICATE
  # Authenticate the user: find their control level
  ##################################################
  def _authenticate(self, username, password):
    id_ = self._id_from_user(username)
    if ID_INVALID == id_:
      return control.Control.Public
    elif password == users[id_].password:
      # returns control level of user  
      return users[id_].control
    else:
      # if user exists but password is incorrect, throw
      raise Exception("User and password does not match!")
      return
  
  ##################################################
  # INTERACT :: ID FROM USER
  # Find the ID of a given user
  ##################################################
  def _id_from_user(self, username):
    for id_user in range(len(users)):
      if username == users[id_user].name:
        return id_user
    return ID_INVALID


#####################################################
# INTERACT :: DISPLAY USERS
# Display the set of users in the system
#####################################################
def display_users():
  for user in users:
    print(f"\t{user.name}")
