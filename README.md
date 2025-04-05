# polish-py-payments
[![Downloads](https://static.pepy.tech/personalized-badge/polish-py-payments?period=total&units=international_system&left_color=black&right_color=blue&left_text=Downloads)](https://pepy.tech/project/polish-py-payments)
Dokumentacja nie jest skończona.

### Instalacja
```pip install polish-py-payments```

### Operator HotPay
#### Przelewy
```python
from polish_py_payments import HotpayTransfer

hotpay = HotpayTransfer("secret", "password")
payment_url = hotpay.generate(5.00, "Nazwa produktu", "https://successpage.com", "wlasne id zamowienia")
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