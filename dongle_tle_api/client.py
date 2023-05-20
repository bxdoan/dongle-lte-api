import json
import requests

from dongle_tle_api.enums import FidType, FIELDS_QUERY, FieldsQuery
from dongle_tle_api.session import Session


class Client(object):
    def __init__(self, url=None, username=None, password=None, **kwargs):

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
        res = self._post_data(params)
        return res['result']

    def _post_data(self, params):
        try:
            res = requests.post(self.session.url, data=json.dumps(params), headers=self.headers)
            if res.status_code == 200:
                res_json = res.json()
                return res_json
            else:
                raise Exception("Connect failed!!!")
        except Exception as e:
            raise Exception("Connect failed!!!")
