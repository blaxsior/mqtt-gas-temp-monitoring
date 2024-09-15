from time import sleep
from glob import glob
from dotenv import load_dotenv
import paho.mqtt.client as mqtt
from os import getenv

from monitor.temp import ThermMonitor
from monitor.gas import GasMonitor
from led.panel import LEDNotificationPanel
from common.notifier import MQTTAlertNotifier
from common.monitor_state import getHighestPriorityState, gasState, tempState, MonitoringState

# load .env settings
load_dotenv()
device_no = getenv('DEVICE_NO')
username = getenv('MQTT_USER')
password = getenv('MQTT_PASSWORD')
broker_url = getenv('MQTT_BROKER_URL')

# mqtt setting
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(username=username, password=password)
client.connect(broker_url)

# init objs
folderName = glob("/sys/bus/w1/devices/28*")[0]
filename = folderName + "/temperature"

thermMonitor = ThermMonitor(filename=filename)
gasMonitor = GasMonitor()
panel = LEDNotificationPanel(21, 20, 16)
notifier = MQTTAlertNotifier(client)

while True:
  gas = gasMonitor.readGas()
  gas_state = gasState(gas)
  client.publish("item/gas", gas)
  notifier.notify(gas_state, device_no, f"gas = {gas:.3f}%")

  temp = thermMonitor.readTemp()
  temp_state = tempState(temp)
  client.publish("item/temp", temp)
  notifier.notify(temp_state, device_no, f"temp = {temp:.3f}˚C")

  state = getHighestPriorityState(gas_state, temp_state)
  panel.show(state)

  sleep(1)