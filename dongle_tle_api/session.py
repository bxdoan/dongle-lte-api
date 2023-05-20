import json
import requests

from dongle_tle_api.enums import FidType, DEFAULT_URL, DEFAULT_USERNAME, DEFAULT_PASSWORD, HEADERS


class Session(object):

    def __init__(self, url=None, username=None, password=None, **kwargs):
        self.url      = url or DEFAULT_URL
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
            res = requests.post(self.url, data=json.dumps(login_params), headers=HEADERS)
            if res.status_code == 200:
                res_json = res.json()
                if res_json.get('session'):
                    return res_json['session']
            raise Exception("Login failed!!!")
        except Exception as e:
            raise Exception("Login failed!!!")
