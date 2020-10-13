from victron.system.abstract import AbstractSystem


class SolarchargerSystem(AbstractSystem):
    @classmethod
    def get_subscription_keys(cls):
        return {
            "CustomName",
            "FirmwareVersion",
            "ProductId",
            "ProductName",
            "Serial",
            "State",
            "Yield/Power",
            "Dc/0/+",
            "Pv/+",
        }

    @classmethod
    def translate(cls, key, value):
        if key == "State":
            states = {
                0: "Off",
                2: "Fault",
                3: "Bulk",
                4: "Absorption",
                5: "Float",
                6: "Storage",
                7: "Equalize",
                11: "Other (Hub-1)",
                252: "External Control"
            }
            return "state", cls._value(states[value] if value in states else "Unknown")

        elif key == "Yield/Power":
            return "yield_power", {"value": value, "unit": "W"}

        elif key == "Dc/0/Current":
            return "output_current", {"value": value, "unit": "A"}

        elif key == "Dc/0/Voltage":
            return "output_voltage", {"value": value, "unit": "V"}

        elif key == "Pv/I":
            return "pv_current", {"value": value, "unit": "A"}

        elif key == "Pv/V":
            return "pv_voltage", {"value": value, "unit": "V"}

        return AbstractSystem.translate(key, value)
