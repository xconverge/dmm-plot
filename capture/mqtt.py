import paho.mqtt.client as mqtt
import socket
import time

def on_connect(client, userdata, flags, rc):
    print("MQTT Connected with result code "+str(rc))

def on_disconnect(client, userdata, flags, rc):
    print("MQTT disconnected with result code "+str(rc))

def connect():
    # Set timeout for connection and reconnection
    socket.setdefaulttimeout(2)

    # MQTT variables, set the host IP
    host = "X.X.X.X"
    port = 1883

    client = mqtt.Client("DMM")
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.connect(host, port)

    # MQTT Threaded loop starting
    client.loop_start()

    while not client.is_connected():
        print("Waiting to be connected")
        time.sleep(1)

    print("Connected")

    return client


def write(client : mqtt.Client, value):
    try:
        topic = "dmm/value"
        ret = client.publish(topic, value)
        return ret
    except:
        print("Exception in MQTT write")
        return
