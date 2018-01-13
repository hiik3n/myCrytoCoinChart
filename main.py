import time
import logging
from src.remitano_scraper import RemitanoScraper
from src.my_sqlite_connector import RemitanoDBConnector

logging.basicConfig(
    # filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )

print("Hello World")

remitanoScraper = RemitanoScraper()
dbConnector = RemitanoDBConnector()

while 1:
    vnValue = remitanoScraper.get_vn_value()
    if vnValue is not None:
        logging.info("ETH_ASK=%s" % vnValue['eth_ask'])
        dbConnector.insert_data(vnValue)
    time.sleep(30)
