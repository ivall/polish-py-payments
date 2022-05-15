import re

from exceptions import *

pattern = re.compile("^[A-Za-z0-9]{8}$")


def validate_code(code: str):
    if not pattern.match(code):
        raise WrongCodeFormat("The code does not match with regex.")


def check_payment_status(payment_status: dict) -> bool:
    try:
        message = payment_status['message']
    except:
        message = ''
    if message == 'Connection error':
        raise IncorrectInitialData("Incorrect initial data")
    elif message == 'Code does not exist':
        return False
    elif message == 'User or service does not exist':
        raise NoPartnerOrService("Partner or service not found.")
    elif message == 'Number does not exist':
        raise WrongSmsNumber("Sms number is not valid.")
    elif payment_status['status'] == 1:
        return True
    else:
        return False
