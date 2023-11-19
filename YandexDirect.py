import requests
import json

class Direct:
    def __init__(self, token: str, login: str):
        self.token = token
        self.login = login
        self.headers = {
                        'Client-Login': self.login,
                        'Authorization': f'Bearer {self.token}',
                        'Accept-Language': 'en',
                        'processingMode': 'auto'}

    def get_retargeting_id_goals(self) -> dict[str:list]:

        url = 'https://api.direct.yandex.ru/live/v4/json/'
        body = {
            "method": "GetRetargetingGoals",
            "param": {
                "Logins": [
                    self.login
                ]
            },
            "locale": "ru",
            "token": self.token
        }
        res = requests.post(url, data=json.dumps(body))
        return res.json()

    def get_retargeting_lists(self, ids: list = None) -> dict[str:list]:

        url = 'https://api.direct.yandex.com/json/v5/retargetinglists'
        body = {
            "method": "get",
            "params": {
                "FieldNames": ["Type", "Id", "Name", "Description", "Rules", "IsAvailable"],
            }
        }
        if ids:
            body["params"]['SelectionCriteria'] = {'Ids': ids}

        res = requests.post(url,
                            data=json.dumps(body),
                            headers=self.headers)
        return res.json()

    def add_retargeting_lists(self, retargeting_lists: list) -> dict[str:list]:

        url = 'https://api.direct.yandex.com/json/v5/retargetinglists'
        body = {
            "method": "add",
            "params": {
                "RetargetingLists": retargeting_lists
            }
        }
        res = requests.post(url,
                            data=json.dumps(body),
                            headers=self.headers)
        return res.json()