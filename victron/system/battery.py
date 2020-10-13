from victron.system.abstract import AbstractSystem


class BatterySystem(AbstractSystem):
    @classmethod
    def get_subscription_keys(cls):
        return {
            "ConsumedAmphours",
            "Serial",
            "Soc",
            "Devices/0/+",
            "Dc/0/+",
        }

    @classmethod
    def translate(cls, key, value):
        if key == "Dc/0/Current":
            return "current", {"value": value, "unit": "A"}

        elif key == "Dc/0/Voltage":
            return "voltage", {"value": value, "unit": "V"}

        elif key == "Dc/0/MidVoltage":
            return "mid_voltage", {"value": value, "unit": "V"}

        elif key == "Dc/0/Temperature":
            return "temperature", {"value": value, "unit": "°C"}

        elif key == "Dc/0/Power":
            return "power", {"value": value, "unit": "W"}

        elif key == "ConsumedAmphours":
            return "consumed_energy", {"value": value, "unit": "Ah"}

        elif key == "Devices/0/CustomName":
            return "custom_name", cls._value(value)

        elif key == "Devices/0/FirmwareVersion":
            return "firmware_version", cls._value(value)

        elif key == "Devices/0/ProductId":
            return "product_id", cls._value(value)

        elif key == "Devices/0/ProductId":
            return "product_id", cls._value(value)

        elif key == "Devices/0/ProductName":
            return "product_name", cls._value(value)

        return AbstractSystem.translate(key, value)
