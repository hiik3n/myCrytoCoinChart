import time
import sys
import logging
from src.remitano_scraper import RemitanoScraper
from src.my_postgres_connector import RemitanoPostGresConnector
from src.coinmarketcap_client import CoinMarketCapClient

logging.basicConfig(
    # filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )

print("Hello World")

remitanoScraper = RemitanoScraper()
dbConnector = RemitanoPostGresConnector()
coinMarketCapClient = CoinMarketCapClient()

if dbConnector.connect() is None:
    sys.exit(1)

while 1:
    vnValue = remitanoScraper.get_vn_value()
    if vnValue is not None:
        logging.info("ETH_ASK=%s" % vnValue['eth_ask'])
        dbConnector.insert_data(vnValue)

    cmcValue = coinMarketCapClient.get_eth_data()
    if cmcValue is not None:
        logging.info("ETH_ASK=%s" % cmcValue['eth_ask'])
        dbConnector.insert_data(cmcValue)

    time.sleep(60)