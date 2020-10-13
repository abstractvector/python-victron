Victron
===

Python API for talking to a local Victron gateway.

This is a very early `0.0.1` version and should be considered highly unstable.

## Background

This library interfaces with a product from the [Victron GX](https://www.victronenergy.com/live/venus-os:start) family such as the Victron CCGX by using its built-in MQTT broker.

Please see the `example.py` file for usage. If you have a local Victron GX device on your network with MQTT enabled and mDNS configured (it is by default), then you should just be able to run:

```bash
python example.py
```

and messages will be output to the terminal.

The library was created primarily to enable creation of a custom Victron integration with [Home Assistant](https://www.home-assistant.io/).
