from victron.system.abstract import AbstractSystem


class GpsSystem(AbstractSystem):
    @classmethod
    def get_subscription_keys(cls):
        return {
            "Altitude",
            "Course",
            "Speed",
            "NrOfSatellites",
            "ProductId",
            "ProductName",
            "Position/+",
        }

    @classmethod
    def translate(cls, key, value):
        if key == "Altitude":
            return "altitude", {"value": value, "unit": "m"}

        elif key == "Course":
            return "course", {"value": value, "unit": "deg"}

        elif key == "Speed":
            return "speed", {"value": value, "unit": "m/s"}

        elif key == "NrOfSatellites":
            return "number_of_satellites", cls._value(value)

        elif key == "Position/Latitude":
            return "latitude", {"value": value, "unit": "deg"}

        elif key == "Position/Longitude":
            return "longitude", {"value": value, "unit": "deg"}

        return AbstractSystem.translate(key, value)
