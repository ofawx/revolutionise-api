from revolutionise.utils import scrape_value

def get_id_by_name(self, name='', first=None, last=None):
    if name and not(first and last):
        first = name.split()[0]
        last = name.split()[1]
    path = '/members/list/'
    data = {
        'firstname': first,
        'surname': last,
    }
    resp = self.session.post(self.base + path, data=data)
    return scrape_value(resp.content, 'bulk_member[]')

def invoice_by_id(self, id, invoice_name='Invoice', items=[]):
    path = '/scripts/members/invoice/'
    data = {
        'chooseType': 'man',
        'issueViaEmail': 1,
        'notes': invoice_name,
        'freeinv_desc[]': [i['name'] for i in items],
        'freeinv_amt[]': [i['amount'] for i in items],
        'freeinv_qty[]': [1 for i in items],
        '_csrf': self.get_csrf(source_path=f'/members/invoice/{id}/'),
        'id': id,
    }
    self.session.post(self.base + path, data=data)

def invoice_by_name(self, name='', invoice_name='Invoice', items={}):
    id = self.get_id_by_name(name=name)
    invoice_by_id(
        id,
        invoice_name=invoice_by_name,
        items=items,
    )
