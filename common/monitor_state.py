from enum import IntEnum

class MonitoringState(IntEnum):
  URGENT=1
  WARN=2
  SAFE=3

def gasState(gas: float) -> MonitoringState:
  if gas <= 10:
    return MonitoringState.SAFE
  elif gas <= 25:
    return MonitoringState.WARN
  else:
    return MonitoringState.URGENT

def tempState(temp: float) -> MonitoringState:
  if temp <= 40:
    return MonitoringState.SAFE
  elif temp <= 65:
    return MonitoringState.WARN
  else:
    return MonitoringState.URGENT

# 
def getHighestPriorityState(*states: MonitoringState):
  state = MonitoringState.SAFE

  for s in states:
    if state > s:
      state = s

  return s