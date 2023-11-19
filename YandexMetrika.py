import requests
import json

class Metrika:
    def __init__(self, token: str, counter: int):
        self.token = token
        self.counter = counter
        self.headers = {
                        'Authorization': f'Bearer {self.token}',
                        'Accept-Language': 'en',
                        'processingMode': 'auto'}

    def get_segments(self) -> dict[str:list]:

        url = f'https://api-metrika.yandex.net/management/v1/counter/{self.counter}/apisegment/segments'
        res = requests.get(url, headers=self.headers)
        return res.json()

    def add_segment(self, segment_name, segment_condition_name, segment_condition_value) -> dict[str:list]:

        url = f'https://api-metrika.yandex.net/management/v1/counter/{self.counter}/apisegment/segments'
        body = {
            "segment": {
                "name": segment_name,
                "expression": f"(EXISTS ((cdp:o:{segment_condition_name}=='{segment_condition_value}')))",
                'retargeting': True,
            }
        }

        res = requests.post(url,
                            data=json.dumps(body),
                            headers=self.headers)
        return res.json()