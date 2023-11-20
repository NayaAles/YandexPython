import requests

class Token:
    def get_new_token(client_id: str, client_secret: str) -> str:

        url = 'https://oauth.yandex.ru/token'

        code = input(
            f'Перейдите по ссылке https://oauth.yandex.ru/authorize?response_type=code&client_id={client_id} и '
            'скопируйте code [(E)xit для выхода]: ')
        if code in ('E', 'Exit'):
            return ''

        res = requests.post(url,
                            data={'grant_type': 'authorization_code',
                                  'code': int(code),
                                  'client_id': client_id,
                                  'client_secret': client_secret},
                            headers={'Content-type': 'application/x-www-form-urlencoded'})
        token = res.json()['access_token']
        return token