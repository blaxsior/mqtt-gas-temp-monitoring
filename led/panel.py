from gpiozero import LED
from common.monitor_state import MonitoringState

class LEDNotificationPanel:
  __resent_state: MonitoringState

  def __init__(self, pin_urgent_no: int, pin_warn_no: int, pin_safe_no: int):
    self.led_urgent = LED(pin_urgent_no)
    self.led_warn = LED(pin_warn_no)
    self.led_safe = LED(pin_safe_no)
    # 초기 상태 safe로
    self.__resent_state = MonitoringState.SAFE
    self.led_safe.on()

  def show(self, state: MonitoringState):
    # 상태 같으면 갱신 안함
    if self.__resent_state == state:
      return
    
    self.__resent_state = state
    self.led_urgent.off()
    self.led_warn.off()
    self.led_safe.off()
    
    match state:
      case MonitoringState.URGENT:
        self.led_urgent.on()
      case MonitoringState.WARN:
        self.led_warn.on()
      case MonitoringState.SAFE:
        self.led_safe.on()
