"""Python API wrapper for Victron"""

from json import loads as decode
import logging
import re

from victron.gateway_mqtt import MQTTGateway
from victron.system import System

_LOGGER = logging.getLogger(__name__)


class Victron:
    """Victron client"""

    def __init__(self, broker="venus.local", port=1883, client_id=None):
        self.gateway = MQTTGateway(broker, port, client_id)
        self.gateway.recv = self.recv

        self.serial = None

        self.devices = {}

        for system in System.get_supported_systems():
            self.devices[system] = set()

    def connect(self):
        self.gateway.connect()

    def auto_discover(self):
        _LOGGER.debug("Beginning auto-discovery")
        for system in self.devices:
            self.gateway.subscribe(f"N/{self.serial}/{system}/+/DeviceInstance")

    def subscribe(self, system, id, keys=None):
        _LOGGER.debug(f"Subscribing to {system}")

        currentSystem = System.factory(system)

        if currentSystem is None:
            _LOGGER.warn(f"Trying to subscribe to an unsupported system: {system}")
            return

        for k in keys or currentSystem.get_subscription_keys():
            self.gateway.subscribe(f"N/{self.serial}/{system}/{id}/{k}")

    def on_connect(self, serial):
        pass

    def on_device(self, system, id):
        pass

    def on_state(self, system, id, key, value):
        pass

    def __on_serial(self, serial):
        if self.serial == serial:
            return

        self.serial = serial

        _LOGGER.debug(f"Received system serial: {serial}")

        self.on_connect(serial)

    def __on_device(self, system, id):
        if system not in self.devices:
            _LOGGER.debug(f"Unsupported device system: {system}")
            return

        if id in self.devices[system]:
            _LOGGER.debug(f"Device with ID [{id}] already exists in {system} system")
            return

        self.devices[system].add(id)
        self.on_device(system, id)

    def __on_state(self, system_name, id, key, value):
        if system_name not in self.devices:
            _LOGGER.debug(f"Unsupported device system: {system_name}")
            return

        if int(id) not in self.devices[system_name]:
            _LOGGER.debug(f"Unregistered device {id} in {system_name} system")
            return

        if value is None:
            # early return for empty values
            return

        system = System.factory(system_name)

        if system is None:
            _LOGGER.warn(f"Received state for an unsupported system: {system_name}")
            return

        k, v = system.translate(key, value)
        if k is not None:
            self.on_state(system_name, id, k, v)

    def recv(self, topic, payload, qos, retain):
        data = decode(payload)
        value = data["value"]

        _LOGGER.debug(f"Received message on topic: {topic} {data['value']}")

        # parse serial topic
        if re.search("^N/[0-9a-f]+/system/0/Serial$", topic):
            self.__on_serial(value)

        # parse auto discovery topics
        match = re.search(rf"^N/{self.serial}/(.+?)/[0-9]+/DeviceInstance$", topic)
        if match:
            self.__on_device(match.group(1), value)

        # parse state messages
        match = re.search(rf"^N/{self.serial}/(.+?)/([0-9]+)/(.+)$", topic)
        if match:
            self.__on_state(match.group(1), match.group(2), match.group(3), value)
