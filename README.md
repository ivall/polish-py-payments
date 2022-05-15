# polish-py-payments

#### Dokumentacja nie jest skończona.

### Instalacja
```pip install polish-py-payments```

### Operator lvlup
```python
from polish_py_payments import Lvlup

lvlup = Lvlup("secret")
payment_url = lvlup.create_payment(5.00, "https://successpage.com", "https://webhook.com")
```

### Operator HotPay
#### Przelewy
```python
from polish_py_payments import HotpayTransfer
```
#### PSC
```python
from polish_py_payments import HotpayTransfer


```
#### SMS
```python
from polish_py_payments import HotpaySms
```

### Operator MicroSms
```python
from polish_py_payments import Microsms
```