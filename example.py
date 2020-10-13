"""Example usage"""

import logging

from victron import Victron

logging.basicConfig(level=logging.INFO)

_LOGGER = logging.getLogger(__name__)

victron = Victron()

def on_connect(serial):
    _LOGGER.info(f"Connected with serial {serial}")
    victron.auto_discover()

def on_device(system, id):
    _LOGGER.info(f"Found {system} device with ID = {id}")
    victron.subscribe(system, id)

def on_state(system, id, key, value):
    _LOGGER.info(f"Received state update for {system} [{id}]: {key} = {value}")

victron.on_connect = on_connect
victron.on_device = on_device
victron.on_state = on_state

victron.connect()
