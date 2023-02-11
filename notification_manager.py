class NotificationManager:
    def __init__(self):
        self.name = 'name'

    def getsalut(self, dictik):
        import requests
        parameters3 = {
            'api_id': 'AF84CB21-3868-D9B3-FCF4-23192654C9A0',
            'to': '79534165743',
            'msg': f"Тип: {dictik['Тип']}, {dictik['Имя']}, {dictik['Номер']}, {dictik['Описание']}",
            'json': 1
        }
        res3 = requests.get(url='https://sms.ru/sms/send', params=parameters3)
        pass