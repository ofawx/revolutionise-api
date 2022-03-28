import requests

from revolutionise.utils import scrape_value

class API(object):
    def __init__(
        self,
        host,
        tenant,
        user,
        password,

    ):
        self.host = host
        self.tenant = tenant
        self.base = f"{host}/{tenant}"
        self.user = user
        self.password = password

        self.session = requests.Session()

        self._login()

    def _login(self):
        data = {
            'user': self.user,
            'password': self.password,
            '_csrf': self.get_csrf(),
        }
        auth = self.session.post(self.base + '/scripts/login/client/', data=data)
        
        # test auth success
        if (self.session.get(self.base + '/dashboard/overview/').status_code == 200):
            return
        else:
            raise Exception()

    def get_csrf(self, source_path='/') -> str:
        src = self.session.get(self.base + source_path)
        csrf = scrape_value(src.content, '_csrf')
        return csrf
