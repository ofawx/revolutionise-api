# revolutionise-api

revolutioniseSPORT is an Australian sporting club management platform that has simplified many aspects of running community sporting clubs.

This repository implements a basic Python API for making some things even easier still, in the absence of an official API. It's very easy to use:

```python
from revolutionise import Revolutionise

client = Revolutionise(tenant='myclub',user='ofawx',password='nottelling')
client.invoice_by_name(name = "Bob Smith", invoice_name='Clothing', items=[
    {
        'name': 'T-Shirt',
        'amount': 9.99,
    },{
        'name': 'Bucket Hat',
        'amount': 4.99
    }
])
```

## Features
- Invoicing by member name

Expect this list to grow.

## Roadmap
- More member-management functionality
- Booking management functionality
- Tests
- PyPI (pip) library

### Disclaimer
This is completely unofficial and not endorsed in any way by revolutioniseSPORT. It is my hope that this repo becomes superceded by something official. Please use at your own risk/peril.