from revolutionise.api import API

class Revolutionise(API):
    def __init__(self, host='https://client.revolutionise.com.au', 
tenant=None, user=None, password=None):
        super().__init__(host, tenant, user, password)

    # Members
    from revolutionise.api.members import get_id_by_name
    from revolutionise.api.members import invoice_by_id
    from revolutionise.api.members import invoice_by_name
