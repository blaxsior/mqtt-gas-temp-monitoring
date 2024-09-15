from paho.mqtt.client import Client as MQTTClient
from datetime import datetime, timezone
from common.monitor_state import MonitoringState

class MQTTAlertNotifier:
  def __init__(self, client: MQTTClient):
    self.client = client

  def warn(self, device_name: str, message: str):
    message = f"[WARN] T: {datetime.now(timezone.utc)}, device: {device_name}, {message}"
    self.client.publish(f"log/warn", message)

  def urgent(self, defice_name: str, message: str):
    message = f"[URGENT] T: {datetime.now(timezone.utc)}, device: {defice_name}, {message}"
    self.client.publish(f"log/urgent", message)

  def notify(self, state: MonitoringState, device_name: str, message:str):
    match state:
      case MonitoringState.WARN:
        self.warn(device_name, message)
      case MonitoringState.URGENT:
        self.urgent(device_name, message)
      