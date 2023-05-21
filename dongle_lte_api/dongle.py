import json
from pydoc import locate
import requests

from dongle_lte_api import utils
from dongle_lte_api.config import get_logger
from dongle_lte_api.enums import APIVersions, DongleVersions

logger = get_logger(__name__)


class BaseDongle(object):
    def __init__(self, url=None, username=None, password=None, **kwargs):
        self.session = None
        self.url = self._get_url(url)
        self.username = username
        self.password = password
        self.headers = {
            "Content-Type": "application/json;charset=UTF-8",
        }

    def _get_url(self, url=None):
        if url:
            res = requests.post(url, data=json.dumps({}))
            if res.status_code != 200:
                raise Exception("Dongle version is not support!!!")
            return url
        else:
            for v in APIVersions.all():
                res = requests.post(v, data=json.dumps({}))
                if res.status_code == 200:
                    return v

            raise Exception("Dongle version is not support!!!")


class Dongle(BaseDongle):
    def __init__(self, url=None, username=None, password=None, **kwargs):
        super().__init__(url=url, username=username, password=password, **kwargs)
        self.instance = self._get_instance()

    def _get_instance(self):
        key = utils.get_key_obj(self.url, APIVersions)
        class_path = getattr(DongleVersions, key)
        processor_class = locate(class_path)
        define_value = {
            'url': self.url,
            'username': self.username,
            'password': self.password,
        }
        instance = processor_class(**define_value)
        return instance

    def get_data(self, **kwargs) -> dict:
        return self.instance.get_data(**kwargs)

    def change_ssid(self, **kwargs) -> dict:
        return self.instance.change_ssid(**kwargs)

    def change_password(self, **kwargs) -> dict:
        return self.instance.change_password(**kwargs)

    def reboot(self, **kwargs) -> dict:
        return self.instance.reboot(**kwargs)

    def ip(self):
        utils.ip()
