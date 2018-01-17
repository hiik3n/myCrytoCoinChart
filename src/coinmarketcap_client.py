import requests
import logging
import json


class CoinMarketCapClient(object):

    coinIds = ['ethereum']

    def __init__(self):
        self.logger = logging.getLogger()

    def _get_recent_coin_data(self, crypto_type):
        _api = "https://api.coinmarketcap.com/v1/ticker/%s/"
        try:
            _page = requests.get(_api % crypto_type)
            if _page.status_code == 200:
                logging.info("Response %d" % _page.status_code)
                _str = _page.content.decode('utf-8')
                return json.loads(_str)[0]
            else:
                logging.warning("Response %d" % _page.status_code)
                return None
        except Exception as e:
            logging.warning(repr(e))
            return None

    def get_eth_data(self):
        _coinDict = self._get_recent_coin_data("ethereum")

        try:
            _coinVal = float(_coinDict['price_usd'])
        except Exception as e:
            logging.warning(repr(e))
            return None

        # work arround
        if _coinDict is None:
            return None
        else:
            return {'crypto_type': 'eth',
                    'currency': 'USD',
                    'eth_bid': _coinVal,
                    'eth_ask': _coinVal
                    }

if __name__ == "__main__":
    logging.basicConfig(
        # filename="test.log",
        level=logging.DEBUG,
        format="%(asctime)s:%(levelname)s:%(message)s"
    )
    print("hi")
    coinMarketCapClient = CoinMarketCapClient()
    print(coinMarketCapClient.get_eth_data())