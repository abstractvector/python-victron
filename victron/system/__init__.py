from victron.system.battery import BatterySystem
from victron.system.gps import GpsSystem
from victron.system.solarcharger import SolarchargerSystem
from victron.system.vebus import VebusSystem


class System:
    @classmethod
    def get_supported_systems(cls, name_only=True):
        systems = {
            "battery": BatterySystem,
            "gps": GpsSystem,
            "solarcharger": SolarchargerSystem,
            "vebus": VebusSystem
        }

        if name_only:
            return set(systems.keys())

        return systems

    @classmethod
    def factory(cls, system):
        systems = cls.get_supported_systems(False)

        if system in systems:
            return systems[system]
