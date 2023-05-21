import json
import requests

from dongle_tle_api.enums import FidType, DEFAULT_USERNAME, DEFAULT_PASSWORD, HEADERS, FieldsQuery, FIELDS_QUERY
from dongle_tle_api import utils


class Session(object):

    def __init__(self, url=None, username=None, password=None, **kwargs):
        self.url      = url
        self.username = username or DEFAULT_USERNAME
        self.password = password or DEFAULT_PASSWORD

        self.sessionID = self._get_session()

    def _get_session(self):
        login_params = {
            "fid": FidType.Login,
            "username": '',
            "password": self.password,
            "sessionID": None,
        }
        try:
            res = self._post(params=login_params)
            if res.status_code == 200:
                res_json = res.json()
                if res_json.get('session'):
                    return res_json['session']
            raise Exception("Login failed!!!")
        except Exception as e:
            raise Exception("Login failed!!!")

    def _post(self, params):
        res = requests.post(self.url, data=json.dumps(params), headers=HEADERS)
        return res


class DongleV1(object):
    def __init__(self, url=None, username=None, password=None, **kwargs):
        self.url = url
        self.session = Session(url=url, username=username, password=password)
        self.headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": f"{self.session.sessionID}",
        }

    def get_data(self, fields = None) -> dict:
        if fields is None:
            fields = FieldsQuery.Data
        params = {
            "fid": FidType.Query,
            "fields": FIELDS_QUERY.get(fields),
            "sessionId": f"{self.session.sessionID}"
        }
        res = self._post_data(params)
        return res['fields']

    def reboot(self):
        params = {
            "fid": FidType.Reboot,
            "sessionId": f"{self.session.sessionID}"
        }
        res = self._post(params)
        return res

    def change_ssid(self, ssid):
        if not utils.validate_ssid(ssid):
            raise Exception("SSID invalid")
        fields_params = self.get_data(fields=FieldsQuery.WifiInfo)
        fields_params.update({
            "ssidName": ssid,
        })
        self._change_wifi_settings(fields_params=fields_params)

    def change_password(self, password : str = '') -> None:
        if not utils.validate_password(password):
            raise Exception("Password is valid for WiFi network!")
        fields_params = self.get_data(fields=FieldsQuery.WifiInfo)
        fields_params.update({
            "ssidPassword": password,
        })
        self._change_wifi_settings(fields_params=fields_params)

    def _change_wifi_settings(self, fields_params=None):
        params = {
            "fid": FidType.SetWifi,
            "fields": fields_params,
            "sessionId": f"{self.session.sessionID}"
        }
        res = self._post(params)
        return res

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
        res = requests.post(self.session.url, data=json.dumps(params), headers=self.headers)
        return res
