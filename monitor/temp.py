from os import system

class ThermMonitor:
  __filename: str

  def __init__(self, filename: str) -> None:
    self.__filename=filename
    system('modprobe w1-gpio')
    system('modprobe w1-therm')

  def readTemp(self) -> float:
    data = ""
    with open(self.__filename, "r") as f:
      data = f.readline()
    # data는 마이크로 단위의 온도
    return float(data) / 1000