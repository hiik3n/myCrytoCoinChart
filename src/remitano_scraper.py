import requests
import re
import logging


class RemitanoScraper(object):

    def __init__(self):
        self.url = "https://eth.remitano.com/vn"
        self.logger = logging.getLogger()

    def _get_html(self):
        try:
            _page = requests.get(self.url)
            if _page.status_code == 200:
                logging.info("Response %d" % _page.status_code)
                return _page.content.decode('utf-8')
            else:
                logging.warning("Response %d" % _page.status_code)
                return None
        except Exception as e:
            logging.warning(repr(e))
            return None

    @staticmethod
    def _find_vn_ask_bid(text_str):
        if text_str is None:
            return None

        _re_pattern = '''"vn"\s*:\s*(\{\s*"currency"\s*:\s*"VND"\s*,\
\s*"btc_bid"\s*:([0-9]*[.])?[0-9]+\s*,\s*"btc_ask"\s*:([0-9]*[.])?[0-9]+\s*,\
\s*"eth_bid"\s*:([0-9]*[.])?[0-9]+\s*,\s*"eth_ask"\s*:([0-9]*[.])?[0-9]+\s*,\
\s*"usdt_bid"\s*:([0-9]*[.])?[0-9]+\s*,\s*"usdt_ask"\s*:([0-9]*[.])?[0-9]+\s*\})'''

        _res = re.search(_re_pattern, text_str)
        if _res:
            try:
                return eval(_res.group(1))
            except Exception as e:
                print(repr(e))
                return None

        return None

    def get_vn_value(self):
        return self._find_vn_ask_bid(self._get_html())


if __name__ == "__main__":
    logging.basicConfig(
        # filename="test.log",
        level=logging.DEBUG,
        format="%(asctime)s:%(levelname)s:%(message)s"
    )
    print(RemitanoScraper().get_vn_value())