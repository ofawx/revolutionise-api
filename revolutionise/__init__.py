from revolutionise.api import API

class Revolutionise(API):
    def __init__(self, base='https://client.revolutionise.com.au/', 
tenant=None, user=None, password=None):
        super().__init__(base, tenant, user, password)
