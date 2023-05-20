from enum import Enum, EnumMeta


class EnumDirectValueMeta(EnumMeta):
    def __getattribute__(cls, name):
        value = super().__getattribute__(name)
        if isinstance(value, cls):
            value = value.value
        return value


class BaseEnum(Enum, metaclass=EnumDirectValueMeta):
    @classmethod
    def all(cls, except_list=None):
        if except_list is None:
            except_list = []
        return [c.value for c in cls if c.value not in except_list]

    @classmethod
    def keys(cls):
        return [k.name for k in cls]

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    @classmethod
    def all_element_index(cls, index):
        # check element is list and len
        first_element = cls.all()[0]
        if type(first_element) in (list, tuple):
            if index > len(first_element) - 1:
                return []

        e = []
        for c in cls.all():
            e.append(c[index])

        return e


class FidType(BaseEnum):
    Query = 'queryFields'
    Reboot = 'rebootSystem'
    Login = 'login'


FIELDS_QUERY = {
    "data": {
       "simCardState": "invalid",
       "sn": "",
       "imei": "",
       "imsi": "",
       "mac": "",
       "iccId": "",
       "ssidName": "",
       "signalStrength": -200,
       "hardwareVersion": "",
       "systemVersion": "",
       "appVersion": "",
       "wanIpAddress": "",
       "basebandVersion": ""
    },
    "device_list": {"deviceList": []}
}


class FieldsQuery(BaseEnum):
    Data = 'data'
    DeviceList = 'device_list'


DEFAULT_URL = "http://192.168.100.1/api/json"
DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD = "admin"
HEADERS = {
    "Content-Type": "application/json",
}
