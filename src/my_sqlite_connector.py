import os
import sqlite3
import logging
import time


class RemitanoDBConnector(object):

    tracked_cryptos = ['btc', 'eth', 'usdt']

    def __init__(self, db_path=os.path.join(os.path.dirname(__file__), 'RemitanoDB.db')):
        self.logger = logging.getLogger()
        self.defaultPath = db_path

        self.connection = self.connect()

        if not self._check_table_exist("records"):
            self._create_remitano_record_table()
            if self._check_table_exist('records'):
                self.logger.info("Created table: records")

    def connect(self):
        try:
            con = sqlite3.connect(self.defaultPath)
            logging.info("Connected to %s" % self.defaultPath)
            return con
        except Exception as e:
            logging.warning(repr(e))
            return None

    def close(self):
        self.connection.close()

    def _create_remitano_record_table(self):
        remitano_record_create_sql = """\
CREATE TABLE records (\
id integer PRIMARY KEY,\
currency_type text NOT NULL,\
crypto_type text NOT NULL,\
ask_value real NOT NULL,\
bid_value real NOT NULL,\
timestamp integer NOT NULL)"""

        if self.connection is None:
            return None

        self.connection.execute(remitano_record_create_sql)

    def _check_table_exist(self, table_name):
        if self.connection is None:
            return None

        _res = self.connection.execute("""SELECT sql FROM sqlite_master WHERE type='table' AND name='%s'"""
                                       % table_name)
        if len(_res.fetchall()) != 0:
            return True
        else:
            return False

    def _insert_remitano_records(self, currency_type, crypto_type, ask_value, bid_value, timestamp):
        records_insert_sql = """\
INSERT INTO records (currency_type, crypto_type, ask_value, bid_value, timestamp) VALUES (?, ?, ?, ?, ?)"""
        _res = self.connection.execute(records_insert_sql,
                                       (currency_type, crypto_type, ask_value, bid_value, timestamp))

        self.logger.info("Insert to records (%s,%s,%s,%s,%s) (%s)"
                         % (currency_type, crypto_type, ask_value, bid_value, timestamp, _res.rowcount))

    def insert_data(self, record_dict):
        if record_dict is None:
            return None

        _timestamp = round(time.time())
        try:
            _currencyType = record_dict['currency']
        except KeyError as e:
            self.logger.warning("Cannot find currency in data %s" % repr(record_dict))
            return None

        for _crypto in self.tracked_cryptos:
            try:
                self._insert_remitano_records(_crypto, _currencyType,
                                              record_dict['%s_ask' % _crypto],
                                              record_dict['%s_bid' % _crypto],
                                              _timestamp)
            except KeyError as e:
                self.logger.warning(repr(e))
                continue
        self.connection.commit()

    def select_all_record_data(self):
        record_select_all_sql = """SELECT * FROM records"""
        print(self.connection.execute(record_select_all_sql).fetchall())

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")

    dbConnector = RemitanoDBConnector()

    testDict = eval('{"currency":"VND","btc_bid":373219510.752,"btc_ask":376186196.608,"eth_bid":34426616.4,"eth_ask":34845000.0,"usdt_bid":26769.6,"usdt_ask":27017.5}')
    dbConnector.insert_data(testDict)
    dbConnector.select_all_record_data()
    dbConnector.close()