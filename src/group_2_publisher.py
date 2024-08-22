import json
import paho.mqtt.client as mqtt
import time
from group_2_util import create_data


def publish():
    topic = "auto_data"
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv5)
    client.connect("mqtt.eclipseprojects.io", 1883, 60)

    for _ in range(5):
        data = create_data()
        data_str = json.dumps(data)
        client.publish(topic, data_str)
        print("Published data:", data_str)
        time.sleep(1)

    print("Data published:", data_str)
    client.disconnect()


if __name__ == "__main__":
    publish()
