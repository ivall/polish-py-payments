import requests
import hashlib

from utils import check_payment_status, validate_code


class Microsms:
    def __init__(self):
        self.base_url = 'https://microsms.pl/api/v2/index.php'
        self.transfer_base_url = 'https://microsms.pl/api/'

    def sms(self, user_id: int, service_id: int, code: str, number: int) -> bool:
        validate_code(code)

        url = self.base_url + f'?userid={user_id}&code={code}&serviceid={service_id}&number={number}'

        r = requests.get(url).json()
        paid = check_payment_status(r['data'])
        return paid

    def bank_tansfer(
            self,
            shop_id: int,
            hash: str,
            amount: float,
            control: str = None,
            return_urlc: str = None,
            return_url: str = None,
            description: str = None) -> str:
        amount = format(float(amount), '.2f')
        signature = hashlib.md5(f'{shop_id}{hash}{amount}'.encode('utf-8')).hexdigest()

        payload = {
            'shopid': shop_id,
            'signature': signature,
            'amount': amount,
            'control': control,
            'return_urlc': return_urlc,
            'return_url': return_url,
            'description': description
        }

        r = requests.get(self.transfer_base_url+'bankTransfer', params=payload)
        if 'D:ERROR-108' in r.text:
            signature = hashlib.sha256(f'{shop_id}{hash}{amount}'.encode('utf-8')).hexdigest()
            payload['signature'] = signature
            r = requests.get(self.transfer_base_url + 'bankTransfer', params=payload)
        return r.url

    def validate_ip(self, ip: str) -> bool:
        ips = requests.get('https://microsms.pl/psc/ips/').text
        ips = ips.split(',')
        return ip in ips
