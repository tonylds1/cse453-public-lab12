#    <your name here if you made a change>########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, Seth Bolander,
#    <your name here if you made a change>
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

# you may need to put something here...
from enum import Enum

class Control(Enum):
  """
  This class stores the notion of Bell-LaPadula
  """
  # Control Modes
  Public = 1
  Confidential = 2
  Priviliged = 3
  Secret = 4
  
def get_control_from_string(text_control):
  """
  This function takes a string and returns a Control object
  """
  if text_control == "Public":
    return Control.Public
  elif text_control == "Confidential":
    return Control.Confidential
  elif text_control == "Privileged":
    return Control.Priviliged
  elif text_control == "Secret":
    return Control.Secret
  else:
    return None

def control_read(assetControl, subjectControl): 
  return subjectControl.value >= assetControl.value

def control_write(assetControl, subjectControl): 
  return subjectControl.value <= assetControl.value