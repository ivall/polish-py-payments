import requests


class Lvlup:
    def __init__(self, api_key: str, debug: bool):
        if debug:
            self.url = "https://api.sandbox.lvlup.pro/v4/"
        else:
            self.url = "https://api.lvlup.pro/v4/"
        self.headers = {
            "accept": "application/json",
            "Authorization": "Bearer " + api_key,
        }

    def create_payment(self, amount: float, redirect_url: str = "", webhook_url: str = ""):
        amount = format(float(amount), '.2f')
        data = '{ "amount": "%s", "redirectUrl": "%s", "webhookUrl": "%s"}' % (amount ,redirect_url, webhook_url)
        response = requests.post(self.url + "wallet/up", headers=self.headers, data=data)
        return response.json()

    def is_paid(self, id: str):
        response = requests.get(self.url + "wallet/up/" + id, headers=self.headers)

        info = response.json()
        try:
            payed = info["payed"]
        except:
            return False
        return payed

    def balance(self):
        response = requests.get(self.url + "wallet", headers=self.headers)
        return response.json()

    def payments(self, limit: int):
        params = (("limit", str(limit)),)
        response = requests.get(self.url + "payments", headers=self.headers, params=params)
        return response.json()
