from bs4 import BeautifulSoup as bs

def scrape_value(html, name) -> str:
    try:
        return bs(
            html,
            features='html.parser'
        ).find(
            attrs={
                'name': name
            }
        )['value']
    except:
        return None
