from victron.system.abstract import AbstractSystem


class VebusSystem(AbstractSystem):
    @classmethod
    def get_subscription_keys(cls):
        return {
            "Ac/ActiveIn/+/+",
            "Ac/ActiveIn/+",
            "Ac/In/+/+",
            "Ac/Out/+/+",
            "Dc/0/+",
            "FirmwareVersion",
            "ProductId",
            "ProductName",
            "State",
            "Mode",
        }

    @classmethod
    def translate(cls, key, value):
        if key == "State":
            states = {
                0: "Off",
                1: "Low Power",
                2: "Fault",
                3: "Bulk",
                4: "Absorption",
                5: "Float",
                6: "Storage",
                7: "Equalize",
                8: "Passthru",
                9: "Inverting",
                10: "Power Assist",
                11: "Power Supply",
                252: "Bulk Protection",
            }
            return "state", cls._value(states[value] if value in states else "Unknown")

        if key == "Mode":
            modes = {1: "Charger Only", 2: "Inverter Only", 3: "On", 4: "Off"}
            return "state", cls._value(modes[value] if value in modes else "Unknown")

        elif key == "Ac/ActiveIn/L1/F":
            return "ac_in_l1_frequency", {"value": value, "unit": "Hz"}

        elif key == "Ac/ActiveIn/L1/P":
            return "ac_in_l1_power", {"value": value, "unit": "W"}

        elif key == "Ac/ActiveIn/L1/S":
            return "ac_in_l1_apparent_power", {"value": value, "unit": "W"}

        elif key == "Ac/ActiveIn/L1/I":
            return "ac_in_l1_current", {"value": value, "unit": "A"}

        elif key == "Ac/ActiveIn/L1/V":
            return "ac_in_l1_voltage", {"value": value, "unit": "V"}

        elif key == "Ac/ActiveIn/L2/F":
            return "ac_in_l2_frequency", {"value": value, "unit": "Hz"}

        elif key == "Ac/ActiveIn/L2/P":
            return "ac_in_l2_power", {"value": value, "unit": "W"}

        elif key == "Ac/ActiveIn/L2/S":
            return "ac_in_l2_apparent_power", {"value": value, "unit": "W"}

        elif key == "Ac/ActiveIn/L2/I":
            return "ac_in_l2_current", {"value": value, "unit": "A"}

        elif key == "Ac/ActiveIn/L2/V":
            return "ac_in_l2_voltage", {"value": value, "unit": "V"}

        elif key == "Ac/ActiveIn/P":
            return "ac_in_power", {"value": value, "unit": "W"}

        elif key == "Ac/ActiveIn/S":
            return "ac_in_apparent_power", {"value": value, "unit": "W"}

        elif key == "Ac/ActiveIn/ActiveInput":
            return "ac_in_active_input", cls._value(value)

        elif key == "Ac/ActiveIn/CurrentLimit":
            return "ac_in_current_limit", {"value": value, "unit": "A"}

        elif key == "Ac/In/1/CurrentLimit":
            return "ac_in_l1_current_limit", {"value": value, "unit": "A"}

        elif key == "Ac/In/2/CurrentLimit":
            return "ac_in_l2_current_limit", {"value": value, "unit": "A"}

        elif key == "Ac/Out/L1/F":
            return "ac_out_l1_frequency", {"value": value, "unit": "Hz"}

        elif key == "Ac/Out/L1/P":
            return "ac_out_l1_power", {"value": value, "unit": "W"}

        elif key == "Ac/Out/L1/S":
            return "ac_out_l1_apparent_power", {"value": value, "unit": "W"}

        elif key == "Ac/Out/L1/I":
            return "ac_out_l1_current", {"value": value, "unit": "A"}

        elif key == "Ac/Out/L1/V":
            return "ac_out_l1_voltage", {"value": value, "unit": "V"}

        elif key == "Ac/Out/L2/F":
            return "ac_out_l2_frequency", {"value": value, "unit": "Hz"}

        elif key == "Ac/Out/L2/P":
            return "ac_out_l2_power", {"value": value, "unit": "W"}

        elif key == "Ac/Out/L2/S":
            return "ac_out_l2_apparent_power", {"value": value, "unit": "W"}

        elif key == "Ac/Out/L2/I":
            return "ac_out_l2_current", {"value": value, "unit": "A"}

        elif key == "Ac/Out/L2/V":
            return "ac_out_l2_voltage", {"value": value, "unit": "V"}

        elif key == "Ac/Out/L3/F":
            return "ac_out_l3_frequency", {"value": value, "unit": "Hz"}

        elif key == "Ac/Out/L3/P":
            return "ac_out_l3_power", {"value": value, "unit": "W"}

        elif key == "Ac/Out/L3/S":
            return "ac_out_l3_apparent_power", {"value": value, "unit": "W"}

        elif key == "Ac/Out/L3/I":
            return "ac_out_l3_current", {"value": value, "unit": "A"}

        elif key == "Ac/Out/L3/V":
            return "ac_out_l3_voltage", {"value": value, "unit": "V"}

        elif key == "Dc/0/Current":
            return "dc_current", {"value": value, "unit": "A"}

        elif key == "Dc/0/MaxChargeCurrent":
            return "dc_max_charge_current", {"value": value, "unit": "A"}

        elif key == "Dc/0/Power":
            return "dc_power", {"value": value, "unit": "W"}

        elif key == "Dc/0/Voltage":
            return "dc_voltage", {"value": value, "unit": "V"}

        elif key == "Dc/0/Temperature":
            return "dc_temperature", {"value": value, "unit": "°C"}

        return AbstractSystem.translate(key, value)
