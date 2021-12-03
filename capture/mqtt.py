import paho.mqtt.client as mqtt


def connect():
    # MQTT variables, set the host IP
    host = "X.X.X.X"
    port = 1883

    client = mqtt.Client("DMM")
    client.connect(host, port)
    return client


def write(client, value):
    topic = "dmm/value"
    ret = client.publish(topic, value)
    return ret
