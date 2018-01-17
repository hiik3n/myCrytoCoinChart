import os
import psycopg2
import logging
import time
from config import *


class RemitanoPostGresConnector(object):

    # tracked_cryptos = ['btc', 'eth', 'usdt']
    tracked_cryptos = ['eth']

    def __init__(self):
        self.logger = logging.getLogger()
        self.con = None
        self.cur = None

    def connect(self):
        try:
            self.con = psycopg2.connect("host='%s' dbname='%s' user='%s' password='%s'"
                                        % (DB_POSTGRES_HOST, DB_POSTGRES_NAME, DB_POSTGRES_USER, DB_POSTGRES_PWD))
            self.cur = self.con.cursor()
            self.logger.info("CONNECTED to POSTGRES DB")
            return self.con
        except Exception as e:
            self.logger.warning(repr(e))
            return None

    def close(self):
        if self.con:
            self.con.close()
            self.logger.info("DISCONNECTED to POSTGRES DB")

    def _insert_remitano_records(self, currency_type, crypto_type, ask_value, bid_value, timestamp):
        _records_insert_sql = """\
INSERT INTO "%s" ("currency_type", "crypto_type", "ask_value", "bid_value", "timestamp") \
VALUES ('%s', '%s', %s, %s, %s)"""
        self.cur.execute(_records_insert_sql %
                         (DB_POSTGRES_TABLE, currency_type, crypto_type, ask_value, bid_value, timestamp))

        self.logger.info("Insert to records (%s,%s,%s,%s,%s) (%s)"
                         % (currency_type, crypto_type, ask_value, bid_value, timestamp, self.cur.rowcount))

    def insert_data(self, record_dict):

        if record_dict is None:
            return None

        _timestamp = round(time.time())
        try:
            _currencyType = record_dict['currency']
        except KeyError:
            self.logger.warning("Cannot find currency in data %s" % repr(record_dict))
            return None

        for _crypto in self.tracked_cryptos:
            try:

                self._insert_remitano_records(_crypto, _currencyType,
                                              record_dict['%s_ask' % _crypto],
                                              record_dict['%s_bid' % _crypto],
                                              _timestamp)
                self.con.commit()
            except KeyError as e:
                self.logger.warning(repr(e))
                self.con.rollback()
                continue

    def check_table_exit(self):
        _sql = "SELECT * FROM pg_catalog.pg_tables"
        self.cur.execute(_sql)
        for _table in self.cur.fetchall():
            self.logger.info(_table)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")
    logging.info("Hi")
    dbConnector = RemitanoPostGresConnector()

    dbConnector.connect()
    # dbConnector.check_table_exit()
    testDict = eval('{"currency":"VND","btc_bid":373219510.752,"btc_ask":376186196.608,"eth_bid":34426616.4,"eth_ask":34845000.0,"usdt_bid":26769.6,"usdt_ask":27017.5}')
    dbConnector.insert_data(testDict)
    dbConnector.close()
