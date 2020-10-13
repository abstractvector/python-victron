class AbstractSystem:
    @classmethod
    def translate(cls, key, value):
        if key == "CustomName":
            return "custom_name", cls._value(value)

        if key == "FirmwareVersion":
            return "firmware_version", cls._value(value)

        elif key == "ProductId":
            return "product_id", cls._value(value)

        elif key == "ProductName":
            return "product_name", cls._value(value)

        elif key == "Serial":
            return "serial", cls._value(value)

        return None, None

    @classmethod
    def _value(cls, value):
        return {"value": value}

    @classmethod
    def get_subscription_keys(cls):
        return {"#"}
