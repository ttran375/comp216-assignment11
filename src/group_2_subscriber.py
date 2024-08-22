import json
import paho.mqtt.client as mqtt
from group_2_util import print_data


def on_message(client, userdata, message):
    msg_str = message.payload.decode("utf-8")
    data = json.loads(msg_str)
    print_data(data)


def subscribe():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv5)
    client.on_message = on_message
    client.connect("mqtt.eclipseprojects.io", 1883, 60)
    client.subscribe("auto_data")
    print("Subscribed to topic: test/topic")

    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("\nDisconnecting from broker")
        client.disconnect()


if __name__ == "__main__":
    subscribe()
