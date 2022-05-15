import requests
import json

from typing import Union
from hashlib import sha256

from .exceptions import SmsException, IncorrectSmsCode, TransferException


strOrNone = Union[str, None]


class HotpayTransfer:
    def __init__(self, secret: str, password: str):
        self._secret = secret
        self._password = password

    def generate(
            self,
            price: float,
            service_name: str,
            redirect_url: str,
            order_id: str,
            email: strOrNone = None,
            personal_data: strOrNone = None,
            psc: bool = False
    ) -> str:

        price = ('%f' % price).rstrip('0').rstrip('.')

        params = {
            'KWOTA': price,
            'NAZWA_USLUGI': service_name,
            'ADRES_WWW': redirect_url,
            'ID_ZAMOWIENIA': order_id,
            'SEKRET': self._secret
        }

        params['HASH'] = self.generate_hash(params)

        params['EMAIL'] = email
        params['DANE_OSOBOWE'] = personal_data
        params['TYP'] = 'INIT'

        if psc:
            url = 'https://psc.hotpay.pl/'
        else:
            url = 'https://platnosc.hotpay.pl/'

        r = requests.post(url, data=params)
        try:
            data = json.loads(r.text)
        except json.JSONDecodeError:
            raise TransferException(f'HotPay returned HTML instead of JSON. Probably wrong secret or password.')
        if not data.get('STATUS'):
            raise TransferException(f'HotPay error: {r.json()["WIADOMOSC"]}')

        self._payment_url = r.json()['URL']

        return self._payment_url

    def generate_hash(self, params: dict):
        pass_to_hash = self._password + ';'
        pass_to_hash = pass_to_hash + ';'.join(map(str, list(params.values())))
        hash = sha256(pass_to_hash.encode('utf-8')).hexdigest()
        return hash


class HotpaySms:
    def __init__(self, secret: str):
        self._secret = secret

    def check(self, code: str) -> bool:
        data = {
            'sekret': self._secret,
            'kod_sms': code
        }
        r = requests.get('https://apiv2.hotpay.pl/v1/sms/sprawdz', params=data).json()
        if r.get('status') == 'ERROR' and r.get('tresc') != 'BLEDNA TRESC SMS':
            raise SmsException(f'HotPay error: {r.get("tresc")}')
        elif r.get('status') == 'SUKCESS':
            if int(r.get('aktywacja')) == 1:
                return True
            else:
                raise IncorrectSmsCode(f'Incorrect sms code')
        raise IncorrectSmsCode(f'Incorrect sms code')
