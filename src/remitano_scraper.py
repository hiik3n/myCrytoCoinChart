from lxml import html
import requests


class RemitanoScraper(object):

    def __init__(self):
        self.url = "https://eth.remitano.com/vn"
        self.page = None
        pass

    def _get_page(self):
        _page = requests.get(self.url)
        if _page.status_code == 200:
            print("Response %d" % _page.status_code)
            self.page = html.fromstring(_page.content)
            return _page.content
        else:
            print("Response %d" % _page.status_code)
            return None

    def _find_react_rails_env_text(self):
        _pattern1 = "window.REACT_RAILS_ENV ="
        _pattern2 = "window.COIN_CURRENCY_CONFIG ="
        scripts = self.page.xpath('//body/script[@type="text/javascript"]/text()')
        for script in scripts:
            if script.find(_pattern1) != -1 and script.find(_pattern2) != -1:
                return script[script.find(_pattern1) + len(_pattern1):script.find(_pattern2)].strip()
        return ""

    def _get_bid(self):
        print((self._find_react_rails_env_text()))

    def __repr__(self):
        self._get_page()
        self._get_bid()
        print("Hi")
        return ""


if __name__ == "__main__":
    remitanoScraper = RemitanoScraper()
    print(remitanoScraper)
    pass