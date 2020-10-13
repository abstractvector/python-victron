import logging
from pathlib import Path

import paho.mqtt.client as mqtt


class MQTTGateway:
    """Victron MQTT client gateway"""

    def __init__(self, broker, port, client_id):
        """Set up MQTT gateway."""

        self.broker = broker
        self.port = port
        self.client_id = (
            client_id
            or "python-victron@"
            + (Path(__file__).parent / "../VERSION").read_text().strip()
        )

    def connect(self):
        self.client = mqtt.Client(client_id=self.client_id)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.client.connect(self.broker, self.port, 60)
        self.client.loop_forever()

    def subscribe(self, topic):
        self.client.subscribe(topic)

    def on_connect(self, client, userdata, flags, rc):
        client.subscribe("N/+/system/0/Serial")

    def on_message(self, client, userdata, msg):
        self.recv(msg.topic, msg.payload, msg.qos, msg.retain)

    def recv(self, topic, payload, qos, retain):
        pass
