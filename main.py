from YandexDirect import Direct

with open(r'C:/Users/user/PycharmProjects/YandexAPI/token.txt') as f:
    token = f.readline()

with open(r'C:/Users/user/PycharmProjects/YandexAPI/login.txt') as f:
    login = f.readline()

direct = Direct(token, login)
segments = direct.get_retargeting_lists(None)