import json
import requests

from dongle_lte_api import utils
from dongle_lte_api.enums import DEFAULT_PASSWORD, DEFAULT_USERNAME


class DongleV2(object):
    def __init__(self, url=None, username=None, password=None, **kwargs):
        self.url = url
        self.username = username or DEFAULT_USERNAME
        self.password = password or DEFAULT_PASSWORD
        self.headers = {
            "Content-Type": "application/json;charset=UTF-8",
        }
        self.cookies = self._get_cookies()

    def _get_cookies(self):
        params = {
            "funcNo": "1000",
            "username": self.username,
            "password": self.password,
        }
        res = requests.post(self.url, data=json.dumps(params), headers=self.headers)
        if res.status_code == 200:
            res_json = res.json()
            cookies = res_json['results'][0]
            cookies = {k: str(v) for k, v in cookies.items()}
            return cookies
        else:
            raise Exception("Connect failed!!!")

    def get_data(self) -> dict:
        res1 = self._post_data({"funcNo": "1001"})
        res2 = self._post_data({"funcNo": "1002"})
        res3 = self._post_data({"funcNo": "1003"})
        data = {
            **res1['results'][0],
            **res2['results'][0],
            **res3['results'][0],
        }
        return data

    def reboot(self):
        res = self._post_data({"funcNo": "1013"})
        return res

    def change_ssid(self, ssid, max_connect=10):
        if not utils.validate_ssid(ssid):
            raise Exception("SSID invalid")
        params = {
            "funcNo": "1007",
            "ssid"  : ssid,
            "maxSta": str(max_connect)
        }
        self._post(params=params)
        self.reboot()

    def change_password(self, password : str = '', encrypt_type : str = '4') -> None:
        if not utils.validate_password(password):
            raise Exception("Password is valid for WiFi network!")
        params = {
            "funcNo"     : "1010",
            "pwd"        : password,
            "encryp_type": str(encrypt_type)
        }
        self._post(params=params)

    def _post_data(self, params):
        try:
            res = self._post(params=params)
            if res.status_code == 200:
                res_json = res.json()
                return res_json
            else:
                raise Exception("Connect failed!!!")
        except Exception as e:
            raise Exception("Connect failed!!!")

    def _post(self, params):
        res = requests.post(self.url, data=json.dumps(params), headers=self.headers, cookies=self.cookies)
        return res
