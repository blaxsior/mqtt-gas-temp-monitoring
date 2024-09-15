from gpiozero import MCP3208

class GasMonitor:
  def __init__(self):
    self.gas = MCP3208(channel=0)

  def readGas(self) -> float:
    return self.gas.value * 100