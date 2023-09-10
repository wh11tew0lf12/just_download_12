#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""






from urllib.parse import unquote


from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import requests
import random


webhooks = []
for line in open("/root/webhooks.txt","r+").readlines():
    line = line.split("\n")
    line = line[0]
    if line not in webhooks:
        webhooks.append(line)
open("/root/webhooks.txt","r+").close()

max_trade = 5
curr_num = 0
profit = 0.0
trade_number = 0


status_trade_COTIUSDT = 0



status_COTIUSDT = 0
last_status_COTIUSDT = 0
last_bar_COTIUSDT = 0
status_trade_LINKUSDT = 0
status_LINKUSDT = 0
last_status_LINKUSDT = 0
last_bar_LINKUSDT = 0
status_trade_LINKUSDT = 0
status_LINKUSDT = 0
last_status_LINKUSDT = 0
last_bar_LINKUSDT = 0
status_trade_QTUMUSDT = 0
status_QTUMUSDT = 0
last_status_QTUMUSDT = 0
last_bar_QTUMUSDT = 0
status_trade_XLMUSDT = 0
status_XLMUSDT = 0
last_status_XLMUSDT = 0
last_bar_XLMUSDT = 0
status_trade_LTCUSDT = 0
status_LTCUSDT = 0
last_status_LTCUSDT = 0
last_bar_LTCUSDT = 0
status_trade_LRCUSDT = 0
status_LRCUSDT = 0
last_status_LRCUSDT = 0
last_bar_LRCUSDT = 0
status_trade_MATICUSDT = 0
status_MATICUSDT = 0
last_status_MATICUSDT = 0
last_bar_MATICUSDT = 0
status_trade_XTZUSDT = 0
status_XTZUSDT = 0
last_status_XTZUSDT = 0
last_bar_XTZUSDT = 0
status_trade_DYDXUSDT = 0
status_DYDXUSDT = 0
last_status_DYDXUSDT = 0
last_bar_DYDXUSDT = 0
status_trade_SOLUSDT = 0
status_SOLUSDT = 0
last_status_SOLUSDT = 0
last_bar_SOLUSDT = 0
status_trade_DOTUSDT = 0
status_DOTUSDT = 0
last_status_DOTUSDT = 0
last_bar_DOTUSDT = 0
status_trade_ADAUSDT = 0
status_ADAUSDT = 0
last_status_ADAUSDT = 0
last_bar_ADAUSDT = 0
status_trade_XRPUSDT = 0
status_XRPUSDT = 0
last_status_XRPUSDT = 0
last_bar_XRPUSDT = 0
status_trade_FILUSDT = 0
status_FILUSDT = 0
last_status_FILUSDT = 0
last_bar_FILUSDT = 0
status_trade_FTMUSDT = 0
status_FTMUSDT = 0
last_status_FTMUSDT = 0
last_bar_FTMUSDT = 0
status_trade_TRXUSDT = 0
status_TRXUSDT = 0
last_status_TRXUSDT = 0
last_bar_TRXUSDT = 0
status_trade_ALICEUSDT = 0
status_ALICEUSDT = 0
last_status_ALICEUSDT = 0
last_bar_ALICEUSDT = 0
status_trade_C98USDT = 0
status_C98USDT = 0
last_status_C98USDT = 0
last_bar_C98USDT = 0
status_trade_AAVEUSDT = 0
status_AAVEUSDT = 0
last_status_AAVEUSDT = 0
last_bar_AAVEUSDT = 0
status_trade_THETAUSDT = 0
status_THETAUSDT = 0
last_status_THETAUSDT = 0
last_bar_THETAUSDT = 0
status_trade_DASHUSDT = 0
status_DASHUSDT = 0
last_status_DASHUSDT = 0
last_bar_DASHUSDT = 0
status_trade_BTSUSDT = 0
status_BTSUSDT = 0
last_status_BTSUSDT = 0
last_bar_BTSUSDT = 0
status_trade_AVAXUSDT = 0
status_AVAXUSDT = 0
last_status_AVAXUSDT = 0
last_bar_AVAXUSDT = 0
status_trade_BNBUSDT = 0
status_BNBUSDT = 0
last_status_BNBUSDT = 0
last_bar_BNBUSDT = 0
status_trade_COMPUSDT = 0
status_COMPUSDT = 0
last_status_COMPUSDT = 0
last_bar_COMPUSDT = 0
status_trade_BLZUSDT = 0
status_BLZUSDT = 0
last_status_BLZUSDT = 0
last_bar_BLZUSDT = 0
status_trade_SNXUSDT = 0
status_SNXUSDT = 0
last_status_SNXUSDT = 0
last_bar_SNXUSDT = 0
status_trade_KAVAUSDT = 0
status_KAVAUSDT = 0
last_status_KAVAUSDT = 0
last_bar_KAVAUSDT = 0
status_trade_TOMOUSDT = 0
status_TOMOUSDT = 0
last_status_TOMOUSDT = 0
last_bar_TOMOUSDT = 0
status_trade_IOTAUSDT = 0
status_IOTAUSDT = 0
last_status_IOTAUSDT = 0
last_bar_IOTAUSDT = 0
status_trade_RVNUSDT = 0
status_RVNUSDT = 0
last_status_RVNUSDT = 0
last_bar_RVNUSDT = 0
status_trade_UNIUSDT = 0
status_UNIUSDT = 0
last_status_UNIUSDT = 0
last_bar_UNIUSDT = 0
status_trade_IOTXUSDT = 0
status_IOTXUSDT = 0
last_status_IOTXUSDT = 0
last_bar_IOTXUSDT = 0
status_trade_ONEUSDT = 0
status_ONEUSDT = 0
last_status_ONEUSDT = 0
last_bar_ONEUSDT = 0
status_trade_RUNEUSDT = 0
status_RUNEUSDT = 0
last_status_RUNEUSDT = 0
last_bar_RUNEUSDT = 0
status_trade_RLCUSDT = 0
status_RLCUSDT = 0
last_status_RLCUSDT = 0
last_bar_RLCUSDT = 0
status_trade_EOSUSDT = 0
status_EOSUSDT = 0
last_status_EOSUSDT = 0
last_bar_EOSUSDT = 0
status_trade_SUSHIUSDT = 0
status_SUSHIUSDT = 0
last_status_SUSHIUSDT = 0
last_bar_SUSHIUSDT = 0
status_trade_WAVESUSDT = 0
status_WAVESUSDT = 0
last_status_WAVESUSDT = 0
last_bar_WAVESUSDT = 0
status_trade_VETUSDT = 0
status_VETUSDT = 0
last_status_VETUSDT = 0
last_bar_VETUSDT = 0
status_trade_ZECUSDT = 0
status_ZECUSDT = 0
last_status_ZECUSDT = 0
last_bar_ZECUSDT = 0
status_trade_XMRUSDT = 0
status_XMRUSDT = 0
last_status_XMRUSDT = 0
last_bar_XMRUSDT = 0
status_trade_MASKUSDT = 0
status_MASKUSDT = 0
last_status_MASKUSDT = 0
last_bar_MASKUSDT = 0
status_trade_STORJUSDT = 0
status_STORJUSDT = 0
last_status_STORJUSDT = 0
last_bar_STORJUSDT = 0
status_trade_XEMUSDT = 0
status_XEMUSDT = 0
last_status_XEMUSDT = 0
last_bar_XEMUSDT = 0
status_trade_KLAYUSDT = 0
status_KLAYUSDT = 0
last_status_KLAYUSDT = 0
last_bar_KLAYUSDT = 0
status_trade_DOGEUSDT = 0
status_DOGEUSDT = 0
last_status_DOGEUSDT = 0
last_bar_DOGEUSDT = 0
status_trade_AUDIOUSDT = 0
status_AUDIOUSDT = 0
last_status_AUDIOUSDT = 0
last_bar_AUDIOUSDT = 0
status_trade_1INCHUSDT = 0
status_1INCHUSDT = 0
last_status_1INCHUSDT = 0
last_bar_1INCHUSDT = 0
status_trade_OGNUSDT = 0
status_OGNUSDT = 0
last_status_OGNUSDT = 0
last_bar_OGNUSDT = 0
status_trade_KSMUSDT = 0
status_KSMUSDT = 0
last_status_KSMUSDT = 0
last_bar_KSMUSDT = 0
status_trade_MTLUSDT = 0
status_MTLUSDT = 0
last_status_MTLUSDT = 0
last_bar_MTLUSDT = 0
status_trade_BCHUSDT = 0
status_BCHUSDT = 0
last_status_BCHUSDT = 0
last_bar_BCHUSDT = 0
status_trade_ICPUSDT = 0
status_ICPUSDT = 0
last_status_ICPUSDT = 0
last_bar_ICPUSDT = 0
status_trade_TRBUSDT = 0
status_TRBUSDT = 0
last_status_TRBUSDT = 0
last_bar_TRBUSDT = 0
status_trade_ETHUSDT = 0
status_ETHUSDT = 0
last_status_ETHUSDT = 0
last_bar_ETHUSDT = 0
status_trade_ETCUSDT = 0
status_ETCUSDT = 0
last_status_ETCUSDT = 0
last_bar_ETCUSDT = 0
status_trade_ATOMUSDT = 0
status_ATOMUSDT = 0
last_status_ATOMUSDT = 0
last_bar_ATOMUSDT = 0
status_trade_ONTUSDT = 0
status_ONTUSDT = 0
last_status_ONTUSDT = 0
last_bar_ONTUSDT = 0
status_trade_BATUSDT = 0
status_BATUSDT = 0
last_status_BATUSDT = 0
last_bar_BATUSDT = 0
status_trade_NEOUSDT = 0
status_NEOUSDT = 0
last_status_NEOUSDT = 0
last_bar_NEOUSDT = 0
status_trade_IOSTUSDT = 0
status_IOSTUSDT = 0
last_status_IOSTUSDT = 0
last_bar_IOSTUSDT = 0
status_trade_KNCUSDT = 0
status_KNCUSDT = 0
last_status_KNCUSDT = 0
last_bar_KNCUSDT = 0
status_trade_SXPUSDT = 0
status_SXPUSDT = 0
last_status_SXPUSDT = 0
last_bar_SXPUSDT = 0
status_trade_ZILUSDT = 0
status_ZILUSDT = 0
last_status_ZILUSDT = 0
last_bar_ZILUSDT = 0
status_trade_BANDUSDT = 0
status_BANDUSDT = 0
last_status_BANDUSDT = 0
last_bar_BANDUSDT = 0
status_trade_MKRUSDT = 0
status_MKRUSDT = 0
last_status_MKRUSDT = 0
last_bar_MKRUSDT = 0
status_trade_DEFIUSDT = 0
status_DEFIUSDT = 0
last_status_DEFIUSDT = 0
last_bar_DEFIUSDT = 0
status_trade_BALUSDT = 0
status_BALUSDT = 0
last_status_BALUSDT = 0
last_bar_BALUSDT = 0
status_trade_CRVUSDT = 0
status_CRVUSDT = 0
last_status_CRVUSDT = 0
last_bar_CRVUSDT = 0
status_trade_EGLDUSDT = 0
status_EGLDUSDT = 0
last_status_EGLDUSDT = 0
last_bar_EGLDUSDT = 0
status_trade_ICXUSDT = 0
status_ICXUSDT = 0
last_status_ICXUSDT = 0
last_bar_ICXUSDT = 0
status_trade_HNTUSDT = 0
status_HNTUSDT = 0
last_status_HNTUSDT = 0
last_bar_HNTUSDT = 0
status_trade_FLMUSDT = 0
status_FLMUSDT = 0
last_status_FLMUSDT = 0
last_bar_FLMUSDT = 0
status_trade_NEARUSDT = 0
status_NEARUSDT = 0
last_status_NEARUSDT = 0
last_bar_NEARUSDT = 0
status_trade_RSRUSDT = 0
status_RSRUSDT = 0
last_status_RSRUSDT = 0
last_bar_RSRUSDT = 0
status_trade_OCEANUSDT = 0
status_OCEANUSDT = 0
last_status_OCEANUSDT = 0
last_bar_OCEANUSDT = 0
status_trade_CVCUSDT = 0
status_CVCUSDT = 0
last_status_CVCUSDT = 0
last_bar_CVCUSDT = 0
status_trade_AXSUSDT = 0
status_AXSUSDT = 0
last_status_AXSUSDT = 0
last_bar_AXSUSDT = 0
status_trade_ALPHAUSDT = 0
status_ALPHAUSDT = 0
last_status_ALPHAUSDT = 0
last_bar_ALPHAUSDT = 0
status_trade_SKLUSDT = 0
status_SKLUSDT = 0
last_status_SKLUSDT = 0
last_bar_SKLUSDT = 0
status_trade_GRTUSDT = 0
status_GRTUSDT = 0
last_status_GRTUSDT = 0
last_bar_GRTUSDT = 0
status_trade_CHZUSDT = 0
status_CHZUSDT = 0
last_status_CHZUSDT = 0
last_bar_CHZUSDT = 0
status_trade_LITUSDT = 0
status_LITUSDT = 0
last_status_LITUSDT = 0
last_bar_LITUSDT = 0
status_trade_REEFUSDT = 0
status_REEFUSDT = 0
last_status_REEFUSDT = 0
last_bar_REEFUSDT = 0
status_trade_ARPAUSDT = 0
status_ARPAUSDT = 0
last_status_ARPAUSDT = 0
last_bar_ARPAUSDT = 0
status_trade_CELOUSDT = 0
status_CELOUSDT = 0
last_status_CELOUSDT = 0
last_bar_CELOUSDT = 0
status_trade_CELRUSDT = 0
status_CELRUSDT = 0
last_status_CELRUSDT = 0
last_bar_CELRUSDT = 0
status_trade_GALAUSDT = 0
status_GALAUSDT = 0
last_status_GALAUSDT = 0
last_bar_GALAUSDT = 0
status_trade_RAYUSDT = 0
status_RAYUSDT = 0
last_status_RAYUSDT = 0
last_bar_RAYUSDT = 0
status_trade_TLMUSDT = 0
status_TLMUSDT = 0
last_status_TLMUSDT = 0
last_bar_TLMUSDT = 0
status_trade_BTCUSDT = 0
status_BTCUSDT = 0
last_status_BTCUSDT = 0
last_bar_BTCUSDT = 0
status_trade_SANDUSDT = 0
status_SANDUSDT = 0
last_status_SANDUSDT = 0
last_bar_SANDUSDT = 0
status_trade_GTCUSDT = 0
status_GTCUSDT = 0
last_status_GTCUSDT = 0
last_bar_GTCUSDT = 0
status_trade_STMXUSDT = 0
status_STMXUSDT = 0
last_status_STMXUSDT = 0
last_bar_STMXUSDT = 0
status_trade_ZENUSDT = 0
status_ZENUSDT = 0
last_status_ZENUSDT = 0
last_bar_ZENUSDT = 0
status_trade_HBARUSDT = 0
status_HBARUSDT = 0
last_status_HBARUSDT = 0
last_bar_HBARUSDT = 0
status_trade_MANAUSDT = 0
status_MANAUSDT = 0
last_status_MANAUSDT = 0
last_bar_MANAUSDT = 0
status_trade_LINAUSDT = 0
status_LINAUSDT = 0
last_status_LINAUSDT = 0
last_bar_LINAUSDT = 0
status_trade_BAKEUSDT = 0
status_BAKEUSDT = 0
last_status_BAKEUSDT = 0
last_bar_BAKEUSDT = 0
status_trade_NKNUSDT = 0
status_NKNUSDT = 0
last_status_NKNUSDT = 0
last_bar_NKNUSDT = 0
status_trade_SCUSDT = 0
status_SCUSDT = 0
last_status_SCUSDT = 0
last_bar_SCUSDT = 0
status_trade_DENTUSDT = 0
status_DENTUSDT = 0
last_status_DENTUSDT = 0
last_bar_DENTUSDT = 0
status_trade_ANKRUSDT = 0
status_ANKRUSDT = 0
last_status_ANKRUSDT = 0
last_bar_ANKRUSDT = 0
status_trade_FLOWUSDT = 0
status_FLOWUSDT = 0
last_status_FLOWUSDT = 0
last_bar_FLOWUSDT = 0
status_trade_PEOPLEUSDT = 0
status_PEOPLEUSDT = 0
last_status_PEOPLEUSDT = 0
last_bar_PEOPLEUSDT = 0
status_trade_BELUSDT = 0
status_BELUSDT = 0
last_status_BELUSDT = 0
last_bar_BELUSDT = 0
status_trade_BNXUSDT = 0
status_BNXUSDT = 0
last_status_BNXUSDT = 0
last_bar_BNXUSDT = 0
status_trade_BTCSTUSDT = 0
status_BTCSTUSDT = 0
last_status_BTCSTUSDT = 0
last_bar_BTCSTUSDT = 0
status_trade_CHRUSDT = 0
status_CHRUSDT = 0
last_status_CHRUSDT = 0
last_bar_CHRUSDT = 0
status_trade_CTKUSDT = 0
status_CTKUSDT = 0
last_status_CTKUSDT = 0
last_bar_CTKUSDT = 0
status_trade_CTSIUSDT = 0
status_CTSIUSDT = 0
last_status_CTSIUSDT = 0
last_bar_CTSIUSDT = 0
status_trade_DARUSDT = 0
status_DARUSDT = 0
last_status_DARUSDT = 0
last_bar_DARUSDT = 0
status_trade_DGBUSDT = 0
status_DGBUSDT = 0
last_status_DGBUSDT = 0
last_bar_DGBUSDT = 0
status_trade_DUSKUSDT = 0
status_DUSKUSDT = 0
last_status_DUSKUSDT = 0
last_bar_DUSKUSDT = 0
status_trade_ENJUSDT = 0
status_ENJUSDT = 0
last_status_ENJUSDT = 0
last_bar_ENJUSDT = 0
status_trade_ENSUSDT = 0
status_ENSUSDT = 0
last_status_ENSUSDT = 0
last_bar_ENSUSDT = 0
status_trade_FTTUSDT = 0
status_FTTUSDT = 0
last_status_FTTUSDT = 0
last_bar_FTTUSDT = 0
status_trade_GALAUSDT = 0
status_GALAUSDT = 0
last_status_GALAUSDT = 0
last_bar_GALAUSDT = 0
status_trade_GMTUSDT = 0
status_GMTUSDT = 0
last_status_GMTUSDT = 0
last_bar_GMTUSDT = 0
status_trade_HOTUSDT = 0
status_HOTUSDT = 0
last_status_HOTUSDT = 0
last_bar_HOTUSDT = 0
status_trade_IMXUSDT = 0
status_IMXUSDT = 0
last_status_IMXUSDT = 0
last_bar_IMXUSDT = 0
status_trade_JASMYUSDT = 0
status_JASMYUSDT = 0
last_status_JASMYUSDT = 0
last_bar_JASMYUSDT = 0
status_trade_LPTUSDT = 0
status_LPTUSDT = 0
last_status_LPTUSDT = 0
last_bar_LPTUSDT = 0
status_trade_OMGUSDT = 0
status_OMGUSDT = 0
last_status_OMGUSDT = 0
last_bar_OMGUSDT = 0
status_trade_OPUSDT = 0
status_OPUSDT = 0
last_status_OPUSDT = 0
last_bar_OPUSDT = 0
status_trade_RENUSDT = 0
status_RENUSDT = 0
last_status_RENUSDT = 0
last_bar_RENUSDT = 0
status_trade_ROSEUSDT = 0
status_ROSEUSDT = 0
last_status_ROSEUSDT = 0
last_bar_ROSEUSDT = 0
status_trade_WOOUSDT = 0
status_WOOUSDT = 0
last_status_WOOUSDT = 0
last_bar_WOOUSDT = 0






class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()



    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        global curr_num
        global max_trade
        global profit
        global trade_number

        global status_trade_COTIUSDT
        global status_COTIUSDT
        global last_status_COTIUSDT
        global last_bar_COTIUSDT
        global status_trade_LINKUSDT
        global status_LINKUSDT
        global last_status_LINKUSDT
        global last_bar_LINKUSDT
        global status_trade_LINKUSDT
        global status_LINKUSDT
        global last_status_LINKUSDT
        global last_bar_LINKUSDT
        global status_trade_QTUMUSDT
        global status_QTUMUSDT
        global last_status_QTUMUSDT
        global last_bar_QTUMUSDT
        global status_trade_XLMUSDT
        global status_XLMUSDT
        global last_status_XLMUSDT
        global last_bar_XLMUSDT
        global status_trade_LTCUSDT
        global status_LTCUSDT
        global last_status_LTCUSDT
        global last_bar_LTCUSDT
        global status_trade_LRCUSDT
        global status_LRCUSDT
        global last_status_LRCUSDT
        global last_bar_LRCUSDT
        global status_trade_MATICUSDT
        global status_MATICUSDT
        global last_status_MATICUSDT
        global last_bar_MATICUSDT
        global status_trade_XTZUSDT
        global status_XTZUSDT
        global last_status_XTZUSDT
        global last_bar_XTZUSDT
        global status_trade_DYDXUSDT
        global status_DYDXUSDT
        global last_status_DYDXUSDT
        global last_bar_DYDXUSDT
        global status_trade_SOLUSDT
        global status_SOLUSDT
        global last_status_SOLUSDT
        global last_bar_SOLUSDT
        global status_trade_DOTUSDT
        global status_DOTUSDT
        global last_status_DOTUSDT
        global last_bar_DOTUSDT
        global status_trade_ADAUSDT
        global status_ADAUSDT
        global last_status_ADAUSDT
        global last_bar_ADAUSDT
        global status_trade_XRPUSDT
        global status_XRPUSDT
        global last_status_XRPUSDT
        global last_bar_XRPUSDT
        global status_trade_FILUSDT
        global status_FILUSDT
        global last_status_FILUSDT
        global last_bar_FILUSDT
        global status_trade_FTMUSDT
        global status_FTMUSDT
        global last_status_FTMUSDT
        global last_bar_FTMUSDT
        global status_trade_TRXUSDT
        global status_TRXUSDT
        global last_status_TRXUSDT
        global last_bar_TRXUSDT
        global status_trade_ALICEUSDT
        global status_ALICEUSDT
        global last_status_ALICEUSDT
        global last_bar_ALICEUSDT
        global status_trade_C98USDT
        global status_C98USDT
        global last_status_C98USDT
        global last_bar_C98USDT
        global status_trade_AAVEUSDT
        global status_AAVEUSDT
        global last_status_AAVEUSDT
        global last_bar_AAVEUSDT
        global status_trade_THETAUSDT
        global status_THETAUSDT
        global last_status_THETAUSDT
        global last_bar_THETAUSDT
        global status_trade_DASHUSDT
        global status_DASHUSDT
        global last_status_DASHUSDT
        global last_bar_DASHUSDT
        global status_trade_BTSUSDT
        global status_BTSUSDT
        global last_status_BTSUSDT
        global last_bar_BTSUSDT
        global status_trade_AVAXUSDT
        global status_AVAXUSDT
        global last_status_AVAXUSDT
        global last_bar_AVAXUSDT
        global status_trade_BNBUSDT
        global status_BNBUSDT
        global last_status_BNBUSDT
        global last_bar_BNBUSDT
        global status_trade_COMPUSDT
        global status_COMPUSDT
        global last_status_COMPUSDT
        global last_bar_COMPUSDT
        global status_trade_BLZUSDT
        global status_BLZUSDT
        global last_status_BLZUSDT
        global last_bar_BLZUSDT
        global status_trade_SNXUSDT
        global status_SNXUSDT
        global last_status_SNXUSDT
        global last_bar_SNXUSDT
        global status_trade_KAVAUSDT
        global status_KAVAUSDT
        global last_status_KAVAUSDT
        global last_bar_KAVAUSDT
        global status_trade_TOMOUSDT
        global status_TOMOUSDT
        global last_status_TOMOUSDT
        global last_bar_TOMOUSDT
        global status_trade_IOTAUSDT
        global status_IOTAUSDT
        global last_status_IOTAUSDT
        global last_bar_IOTAUSDT
        global status_trade_RVNUSDT
        global status_RVNUSDT
        global last_status_RVNUSDT
        global last_bar_RVNUSDT
        global status_trade_UNIUSDT
        global status_UNIUSDT
        global last_status_UNIUSDT
        global last_bar_UNIUSDT
        global status_trade_IOTXUSDT
        global status_IOTXUSDT
        global last_status_IOTXUSDT
        global last_bar_IOTXUSDT
        global status_trade_ONEUSDT
        global status_ONEUSDT
        global last_status_ONEUSDT
        global last_bar_ONEUSDT
        global status_trade_RUNEUSDT
        global status_RUNEUSDT
        global last_status_RUNEUSDT
        global last_bar_RUNEUSDT
        global status_trade_RLCUSDT
        global status_RLCUSDT
        global last_status_RLCUSDT
        global last_bar_RLCUSDT
        global status_trade_EOSUSDT
        global status_EOSUSDT
        global last_status_EOSUSDT
        global last_bar_EOSUSDT
        global status_trade_SUSHIUSDT
        global status_SUSHIUSDT
        global last_status_SUSHIUSDT
        global last_bar_SUSHIUSDT
        global status_trade_WAVESUSDT
        global status_WAVESUSDT
        global last_status_WAVESUSDT
        global last_bar_WAVESUSDT
        global status_trade_VETUSDT
        global status_VETUSDT
        global last_status_VETUSDT
        global last_bar_VETUSDT
        global status_trade_ZECUSDT
        global status_ZECUSDT
        global last_status_ZECUSDT
        global last_bar_ZECUSDT
        global status_trade_XMRUSDT
        global status_XMRUSDT
        global last_status_XMRUSDT
        global last_bar_XMRUSDT
        global status_trade_MASKUSDT
        global status_MASKUSDT
        global last_status_MASKUSDT
        global last_bar_MASKUSDT
        global status_trade_STORJUSDT
        global status_STORJUSDT
        global last_status_STORJUSDT
        global last_bar_STORJUSDT
        global status_trade_XEMUSDT
        global status_XEMUSDT
        global last_status_XEMUSDT
        global last_bar_XEMUSDT
        global status_trade_KLAYUSDT
        global status_KLAYUSDT
        global last_status_KLAYUSDT
        global last_bar_KLAYUSDT
        global status_trade_DOGEUSDT
        global status_DOGEUSDT
        global last_status_DOGEUSDT
        global last_bar_DOGEUSDT
        global status_trade_AUDIOUSDT
        global status_AUDIOUSDT
        global last_status_AUDIOUSDT
        global last_bar_AUDIOUSDT
        global status_trade_1INCHUSDT
        global status_1INCHUSDT
        global last_status_1INCHUSDT
        global last_bar_1INCHUSDT
        global status_trade_OGNUSDT
        global status_OGNUSDT
        global last_status_OGNUSDT
        global last_bar_OGNUSDT
        global status_trade_KSMUSDT
        global status_KSMUSDT
        global last_status_KSMUSDT
        global last_bar_KSMUSDT
        global status_trade_MTLUSDT
        global status_MTLUSDT
        global last_status_MTLUSDT
        global last_bar_MTLUSDT
        global status_trade_BCHUSDT
        global status_BCHUSDT
        global last_status_BCHUSDT
        global last_bar_BCHUSDT
        global status_trade_ICPUSDT
        global status_ICPUSDT
        global last_status_ICPUSDT
        global last_bar_ICPUSDT
        global status_trade_TRBUSDT
        global status_TRBUSDT
        global last_status_TRBUSDT
        global last_bar_TRBUSDT
        global status_trade_ETHUSDT
        global status_ETHUSDT
        global last_status_ETHUSDT
        global last_bar_ETHUSDT
        global status_trade_ETCUSDT
        global status_ETCUSDT
        global last_status_ETCUSDT
        global last_bar_ETCUSDT
        global status_trade_ATOMUSDT
        global status_ATOMUSDT
        global last_status_ATOMUSDT
        global last_bar_ATOMUSDT
        global status_trade_ONTUSDT
        global status_ONTUSDT
        global last_status_ONTUSDT
        global last_bar_ONTUSDT
        global status_trade_BATUSDT
        global status_BATUSDT
        global last_status_BATUSDT
        global last_bar_BATUSDT
        global status_trade_NEOUSDT
        global status_NEOUSDT
        global last_status_NEOUSDT
        global last_bar_NEOUSDT
        global status_trade_IOSTUSDT
        global status_IOSTUSDT
        global last_status_IOSTUSDT
        global last_bar_IOSTUSDT
        global status_trade_KNCUSDT
        global status_KNCUSDT
        global last_status_KNCUSDT
        global last_bar_KNCUSDT
        global status_trade_SXPUSDT
        global status_SXPUSDT
        global last_status_SXPUSDT
        global last_bar_SXPUSDT
        global status_trade_ZILUSDT
        global status_ZILUSDT
        global last_status_ZILUSDT
        global last_bar_ZILUSDT
        global status_trade_BANDUSDT
        global status_BANDUSDT
        global last_status_BANDUSDT
        global last_bar_BANDUSDT
        global status_trade_MKRUSDT
        global status_MKRUSDT
        global last_status_MKRUSDT
        global last_bar_MKRUSDT
        global status_trade_DEFIUSDT
        global status_DEFIUSDT
        global last_status_DEFIUSDT
        global last_bar_DEFIUSDT
        global status_trade_BALUSDT
        global status_BALUSDT
        global last_status_BALUSDT
        global last_bar_BALUSDT
        global status_trade_CRVUSDT
        global status_CRVUSDT
        global last_status_CRVUSDT
        global last_bar_CRVUSDT
        global status_trade_EGLDUSDT
        global status_EGLDUSDT
        global last_status_EGLDUSDT
        global last_bar_EGLDUSDT
        global status_trade_ICXUSDT
        global status_ICXUSDT
        global last_status_ICXUSDT
        global last_bar_ICXUSDT
        global status_trade_HNTUSDT
        global status_HNTUSDT
        global last_status_HNTUSDT
        global last_bar_HNTUSDT
        global status_trade_FLMUSDT
        global status_FLMUSDT
        global last_status_FLMUSDT
        global last_bar_FLMUSDT
        global status_trade_NEARUSDT
        global status_NEARUSDT
        global last_status_NEARUSDT
        global last_bar_NEARUSDT
        global status_trade_RSRUSDT
        global status_RSRUSDT
        global last_status_RSRUSDT
        global last_bar_RSRUSDT
        global status_trade_OCEANUSDT
        global status_OCEANUSDT
        global last_status_OCEANUSDT
        global last_bar_OCEANUSDT
        global status_trade_CVCUSDT
        global status_CVCUSDT
        global last_status_CVCUSDT
        global last_bar_CVCUSDT
        global status_trade_AXSUSDT
        global status_AXSUSDT
        global last_status_AXSUSDT
        global last_bar_AXSUSDT
        global status_trade_ALPHAUSDT
        global status_ALPHAUSDT
        global last_status_ALPHAUSDT
        global last_bar_ALPHAUSDT
        global status_trade_SKLUSDT
        global status_SKLUSDT
        global last_status_SKLUSDT
        global last_bar_SKLUSDT
        global status_trade_GRTUSDT
        global status_GRTUSDT
        global last_status_GRTUSDT
        global last_bar_GRTUSDT
        global status_trade_CHZUSDT
        global status_CHZUSDT
        global last_status_CHZUSDT
        global last_bar_CHZUSDT
        global status_trade_LITUSDT
        global status_LITUSDT
        global last_status_LITUSDT
        global last_bar_LITUSDT
        global status_trade_REEFUSDT
        global status_REEFUSDT
        global last_status_REEFUSDT
        global last_bar_REEFUSDT
        global status_trade_ARPAUSDT
        global status_ARPAUSDT
        global last_status_ARPAUSDT
        global last_bar_ARPAUSDT
        global status_trade_CELOUSDT
        global status_CELOUSDT
        global last_status_CELOUSDT
        global last_bar_CELOUSDT
        global status_trade_CELRUSDT
        global status_CELRUSDT
        global last_status_CELRUSDT
        global last_bar_CELRUSDT
        global status_trade_GALAUSDT
        global status_GALAUSDT
        global last_status_GALAUSDT
        global last_bar_GALAUSDT
        global status_trade_RAYUSDT
        global status_RAYUSDT
        global last_status_RAYUSDT
        global last_bar_RAYUSDT
        global status_trade_TLMUSDT
        global status_TLMUSDT
        global last_status_TLMUSDT
        global last_bar_TLMUSDT
        global status_trade_BTCUSDT
        global status_BTCUSDT
        global last_status_BTCUSDT
        global last_bar_BTCUSDT
        global status_trade_SANDUSDT
        global status_SANDUSDT
        global last_status_SANDUSDT
        global last_bar_SANDUSDT
        global status_trade_GTCUSDT
        global status_GTCUSDT
        global last_status_GTCUSDT
        global last_bar_GTCUSDT
        global status_trade_STMXUSDT
        global status_STMXUSDT
        global last_status_STMXUSDT
        global last_bar_STMXUSDT
        global status_trade_ZENUSDT
        global status_ZENUSDT
        global last_status_ZENUSDT
        global last_bar_ZENUSDT
        global status_trade_HBARUSDT
        global status_HBARUSDT
        global last_status_HBARUSDT
        global last_bar_HBARUSDT
        global status_trade_MANAUSDT
        global status_MANAUSDT
        global last_status_MANAUSDT
        global last_bar_MANAUSDT
        global status_trade_LINAUSDT
        global status_LINAUSDT
        global last_status_LINAUSDT
        global last_bar_LINAUSDT
        global status_trade_BAKEUSDT
        global status_BAKEUSDT
        global last_status_BAKEUSDT
        global last_bar_BAKEUSDT
        global status_trade_NKNUSDT
        global status_NKNUSDT
        global last_status_NKNUSDT
        global last_bar_NKNUSDT
        global status_trade_SCUSDT
        global status_SCUSDT
        global last_status_SCUSDT
        global last_bar_SCUSDT
        global status_trade_DENTUSDT
        global status_DENTUSDT
        global last_status_DENTUSDT
        global last_bar_DENTUSDT
        global status_trade_ANKRUSDT
        global status_ANKRUSDT
        global last_status_ANKRUSDT
        global last_bar_ANKRUSDT
        global status_trade_FLOWUSDT
        global status_FLOWUSDT
        global last_status_FLOWUSDT
        global last_bar_FLOWUSDT
        global status_trade_PEOPLEUSDT
        global status_PEOPLEUSDT
        global last_status_PEOPLEUSDT
        global last_bar_PEOPLEUSDT
        global status_trade_BELUSDT
        global status_BELUSDT
        global last_status_BELUSDT
        global last_bar_BELUSDT
        global status_trade_BNXUSDT
        global status_BNXUSDT
        global last_status_BNXUSDT
        global last_bar_BNXUSDT
        global status_trade_BTCSTUSDT
        global status_BTCSTUSDT
        global last_status_BTCSTUSDT
        global last_bar_BTCSTUSDT
        global status_trade_CHRUSDT
        global status_CHRUSDT
        global last_status_CHRUSDT
        global last_bar_CHRUSDT
        global status_trade_CTKUSDT
        global status_CTKUSDT
        global last_status_CTKUSDT
        global last_bar_CTKUSDT
        global status_trade_CTSIUSDT
        global status_CTSIUSDT
        global last_status_CTSIUSDT
        global last_bar_CTSIUSDT
        global status_trade_DARUSDT
        global status_DARUSDT
        global last_status_DARUSDT
        global last_bar_DARUSDT
        global status_trade_DGBUSDT
        global status_DGBUSDT
        global last_status_DGBUSDT
        global last_bar_DGBUSDT
        global status_trade_DUSKUSDT
        global status_DUSKUSDT
        global last_status_DUSKUSDT
        global last_bar_DUSKUSDT
        global status_trade_ENJUSDT
        global status_ENJUSDT
        global last_status_ENJUSDT
        global last_bar_ENJUSDT
        global status_trade_ENSUSDT
        global status_ENSUSDT
        global last_status_ENSUSDT
        global last_bar_ENSUSDT
        global status_trade_FTTUSDT
        global status_FTTUSDT
        global last_status_FTTUSDT
        global last_bar_FTTUSDT
        global status_trade_GALAUSDT
        global status_GALAUSDT
        global last_status_GALAUSDT
        global last_bar_GALAUSDT
        global status_trade_GMTUSDT
        global status_GMTUSDT
        global last_status_GMTUSDT
        global last_bar_GMTUSDT
        global status_trade_HOTUSDT
        global status_HOTUSDT
        global last_status_HOTUSDT
        global last_bar_HOTUSDT
        global status_trade_IMXUSDT
        global status_IMXUSDT
        global last_status_IMXUSDT
        global last_bar_IMXUSDT
        global status_trade_JASMYUSDT
        global status_JASMYUSDT
        global last_status_JASMYUSDT
        global last_bar_JASMYUSDT
        global status_trade_LPTUSDT
        global status_LPTUSDT
        global last_status_LPTUSDT
        global last_bar_LPTUSDT
        global status_trade_OMGUSDT
        global status_OMGUSDT
        global last_status_OMGUSDT
        global last_bar_OMGUSDT
        global status_trade_OPUSDT
        global status_OPUSDT
        global last_status_OPUSDT
        global last_bar_OPUSDT
        global status_trade_RENUSDT
        global status_RENUSDT
        global last_status_RENUSDT
        global last_bar_RENUSDT
        global status_trade_ROSEUSDT
        global status_ROSEUSDT
        global last_status_ROSEUSDT
        global last_bar_ROSEUSDT
        global status_trade_WOOUSDT
        global status_WOOUSDT
        global last_status_WOOUSDT
        global last_bar_WOOUSDT






        def send_post(self, message, url):
            requests.post(url, data = message)
        if str(self.path) == "/webhook/waterflow_12_w0lf/LINKUSDT":
            content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
            post_data = self.rfile.read(content_length) # <--- Gets the data itself'''
            dt = post_data.decode('utf-8').replace("+"," ")
            dt = unquote(dt)




            def open_trade(pair,direction,dt,webhook2):
                if direction == "LONG":
                    entry = dt.split(" - ")
                    entry = entry[1]
                    entry = entry.split(" Bar_Index:")
                    entry = entry[0]
                    entry = float(entry)
                    target1 = entry + (entry/100*0.45)
                    target2 = entry + (entry/100*1)
                    target3 = entry + (entry/100*2)
                    sl_long = entry - (entry/100*0.5)
                    message = "Binance Futures\nPair: " + str(pair) + " " + str(direction) + "\nLeverage: Isolated 20x\nEntry: " + str(entry) + "\nTargets: " + str(target1) + "\nSL: " + str(sl_long)
                    send_post(self, message, webhook2)
                if direction == "SHORT":
                    entry = dt.split(" - ")
                    entry = entry[1]
                    entry = entry.split(" Bar_Index:")
                    entry = entry[0]
                    entry = float(entry)
                    target1 = entry - (entry/100*0.45)
                    target2 = entry - (entry/100*1)
                    target3 = entry - (entry/100*2)
                    sl_long = entry + (entry/100*0.5)
                    message = "Binance Futures\nPair: " + str(pair) + " " + str(direction) + "\nLeverage: Isolated 20x\nEntry: " + str(entry) + "\nTargets: " + str(target1) + "\nSL: " + str(sl_long)
                    send_post(self, message, webhook2)

            def close_trade(pair,dt,webhook1):
                entry = dt.split(" - ")
                entry = entry[1]
                entry = entry.split(" Bar_Index:")
                entry = entry[0]
                entry = float(entry)
                message = "close all " + pair + " - " + str(entry)
                send_post(self, message, webhook1)






            if "COTIUSDT LONG" in dt and status_trade_COTIUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_COTIUSDT = bar
                open_trade("COTIUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_COTIUSDT = 1
                curr_num = curr_num + 1
                    
            if "COTIUSDT SHORT" in dt and status_trade_COTIUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_COTIUSDT = bar
                open_trade("COTIUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_COTIUSDT = -1
                curr_num = curr_num + 1

            if ("COTIUSDT end of trade" in dt) and (status_trade_COTIUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_COTIUSDT:
                    close_trade("COTIUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_COTIUSDT = 0
                    curr_num = curr_num - 1

            if ("COTIUSDT end of trade" in dt) and (status_trade_COTIUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_COTIUSDT:
                    close_trade("COTIUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_COTIUSDT = 0
                    curr_num = curr_num - 1


            if "COTIUSDT LONG" in dt and (status_trade_COTIUSDT == -1 or status_trade_COTIUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_COTIUSDT:
                    close_trade("COTIUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_COTIUSDT = 0
                    curr_num = curr_num - 1

            if "COTIUSDT SHORT" in dt and (status_trade_COTIUSDT == -1 or status_trade_COTIUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_COTIUSDT:
                    close_trade("COTIUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_COTIUSDT = 0
                    curr_num = curr_num - 1  




            if "LINKUSDT LONG" in dt and status_trade_LINKUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_LINKUSDT = bar
                open_trade("LINKUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_LINKUSDT = 1
                curr_num = curr_num + 1
                    
            if "LINKUSDT SHORT" in dt and status_trade_LINKUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_LINKUSDT = bar
                open_trade("LINKUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_LINKUSDT = -1
                curr_num = curr_num + 1

            if ("LINKUSDT end of trade" in dt) and (status_trade_LINKUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LINKUSDT:
                    close_trade("LINKUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LINKUSDT = 0
                    curr_num = curr_num - 1

            if ("LINKUSDT end of trade" in dt) and (status_trade_LINKUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LINKUSDT:
                    close_trade("LINKUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LINKUSDT = 0
                    curr_num = curr_num - 1


            if "LINKUSDT LONG" in dt and (status_trade_LINKUSDT == -1 or status_trade_LINKUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LINKUSDT:
                    close_trade("LINKUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LINKUSDT = 0
                    curr_num = curr_num - 1

            if "LINKUSDT SHORT" in dt and (status_trade_LINKUSDT == -1 or status_trade_LINKUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LINKUSDT:
                    close_trade("LINKUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LINKUSDT = 0
                    curr_num = curr_num - 1  




            if "QTUMUSDT LONG" in dt and status_trade_QTUMUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_QTUMUSDT = bar
                open_trade("QTUMUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_QTUMUSDT = 1
                curr_num = curr_num + 1
                    
            if "QTUMUSDT SHORT" in dt and status_trade_QTUMUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_QTUMUSDT = bar
                open_trade("QTUMUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_QTUMUSDT = -1
                curr_num = curr_num + 1

            if ("QTUMUSDT end of trade" in dt) and (status_trade_QTUMUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_QTUMUSDT:
                    close_trade("QTUMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_QTUMUSDT = 0
                    curr_num = curr_num - 1

            if ("QTUMUSDT end of trade" in dt) and (status_trade_QTUMUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_QTUMUSDT:
                    close_trade("QTUMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_QTUMUSDT = 0
                    curr_num = curr_num - 1


            if "QTUMUSDT LONG" in dt and (status_trade_QTUMUSDT == -1 or status_trade_QTUMUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_QTUMUSDT:
                    close_trade("QTUMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_QTUMUSDT = 0
                    curr_num = curr_num - 1

            if "QTUMUSDT SHORT" in dt and (status_trade_QTUMUSDT == -1 or status_trade_QTUMUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_QTUMUSDT:
                    close_trade("QTUMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_QTUMUSDT = 0
                    curr_num = curr_num - 1  




            if "XLMUSDT LONG" in dt and status_trade_XLMUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_XLMUSDT = bar
                open_trade("XLMUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_XLMUSDT = 1
                curr_num = curr_num + 1
                    
            if "XLMUSDT SHORT" in dt and status_trade_XLMUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_XLMUSDT = bar
                open_trade("XLMUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_XLMUSDT = -1
                curr_num = curr_num + 1

            if ("XLMUSDT end of trade" in dt) and (status_trade_XLMUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_XLMUSDT:
                    close_trade("XLMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_XLMUSDT = 0
                    curr_num = curr_num - 1

            if ("XLMUSDT end of trade" in dt) and (status_trade_XLMUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_XLMUSDT:
                    close_trade("XLMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_XLMUSDT = 0
                    curr_num = curr_num - 1


            if "XLMUSDT LONG" in dt and (status_trade_XLMUSDT == -1 or status_trade_XLMUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_XLMUSDT:
                    close_trade("XLMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_XLMUSDT = 0
                    curr_num = curr_num - 1

            if "XLMUSDT SHORT" in dt and (status_trade_XLMUSDT == -1 or status_trade_XLMUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_XLMUSDT:
                    close_trade("XLMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_XLMUSDT = 0
                    curr_num = curr_num - 1  




            if "LTCUSDT LONG" in dt and status_trade_LTCUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_LTCUSDT = bar
                open_trade("LTCUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_LTCUSDT = 1
                curr_num = curr_num + 1
                    
            if "LTCUSDT SHORT" in dt and status_trade_LTCUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_LTCUSDT = bar
                open_trade("LTCUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_LTCUSDT = -1
                curr_num = curr_num + 1

            if ("LTCUSDT end of trade" in dt) and (status_trade_LTCUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LTCUSDT:
                    close_trade("LTCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LTCUSDT = 0
                    curr_num = curr_num - 1

            if ("LTCUSDT end of trade" in dt) and (status_trade_LTCUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LTCUSDT:
                    close_trade("LTCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LTCUSDT = 0
                    curr_num = curr_num - 1


            if "LTCUSDT LONG" in dt and (status_trade_LTCUSDT == -1 or status_trade_LTCUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LTCUSDT:
                    close_trade("LTCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LTCUSDT = 0
                    curr_num = curr_num - 1

            if "LTCUSDT SHORT" in dt and (status_trade_LTCUSDT == -1 or status_trade_LTCUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LTCUSDT:
                    close_trade("LTCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LTCUSDT = 0
                    curr_num = curr_num - 1  




            if "LRCUSDT LONG" in dt and status_trade_LRCUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_LRCUSDT = bar
                open_trade("LRCUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_LRCUSDT = 1
                curr_num = curr_num + 1
                    
            if "LRCUSDT SHORT" in dt and status_trade_LRCUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_LRCUSDT = bar
                open_trade("LRCUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_LRCUSDT = -1
                curr_num = curr_num + 1

            if ("LRCUSDT end of trade" in dt) and (status_trade_LRCUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LRCUSDT:
                    close_trade("LRCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LRCUSDT = 0
                    curr_num = curr_num - 1

            if ("LRCUSDT end of trade" in dt) and (status_trade_LRCUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LRCUSDT:
                    close_trade("LRCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LRCUSDT = 0
                    curr_num = curr_num - 1


            if "LRCUSDT LONG" in dt and (status_trade_LRCUSDT == -1 or status_trade_LRCUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LRCUSDT:
                    close_trade("LRCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LRCUSDT = 0
                    curr_num = curr_num - 1

            if "LRCUSDT SHORT" in dt and (status_trade_LRCUSDT == -1 or status_trade_LRCUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LRCUSDT:
                    close_trade("LRCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LRCUSDT = 0
                    curr_num = curr_num - 1  




            if "MATICUSDT LONG" in dt and status_trade_MATICUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_MATICUSDT = bar
                open_trade("MATICUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_MATICUSDT = 1
                curr_num = curr_num + 1
                    
            if "MATICUSDT SHORT" in dt and status_trade_MATICUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_MATICUSDT = bar
                open_trade("MATICUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_MATICUSDT = -1
                curr_num = curr_num + 1

            if ("MATICUSDT end of trade" in dt) and (status_trade_MATICUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_MATICUSDT:
                    close_trade("MATICUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_MATICUSDT = 0
                    curr_num = curr_num - 1

            if ("MATICUSDT end of trade" in dt) and (status_trade_MATICUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_MATICUSDT:
                    close_trade("MATICUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_MATICUSDT = 0
                    curr_num = curr_num - 1


            if "MATICUSDT LONG" in dt and (status_trade_MATICUSDT == -1 or status_trade_MATICUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_MATICUSDT:
                    close_trade("MATICUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_MATICUSDT = 0
                    curr_num = curr_num - 1

            if "MATICUSDT SHORT" in dt and (status_trade_MATICUSDT == -1 or status_trade_MATICUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_MATICUSDT:
                    close_trade("MATICUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_MATICUSDT = 0
                    curr_num = curr_num - 1  




            if "XTZUSDT LONG" in dt and status_trade_XTZUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_XTZUSDT = bar
                open_trade("XTZUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_XTZUSDT = 1
                curr_num = curr_num + 1
                    
            if "XTZUSDT SHORT" in dt and status_trade_XTZUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_XTZUSDT = bar
                open_trade("XTZUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_XTZUSDT = -1
                curr_num = curr_num + 1

            if ("XTZUSDT end of trade" in dt) and (status_trade_XTZUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_XTZUSDT:
                    close_trade("XTZUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_XTZUSDT = 0
                    curr_num = curr_num - 1

            if ("XTZUSDT end of trade" in dt) and (status_trade_XTZUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_XTZUSDT:
                    close_trade("XTZUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_XTZUSDT = 0
                    curr_num = curr_num - 1


            if "XTZUSDT LONG" in dt and (status_trade_XTZUSDT == -1 or status_trade_XTZUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_XTZUSDT:
                    close_trade("XTZUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_XTZUSDT = 0
                    curr_num = curr_num - 1

            if "XTZUSDT SHORT" in dt and (status_trade_XTZUSDT == -1 or status_trade_XTZUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_XTZUSDT:
                    close_trade("XTZUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_XTZUSDT = 0
                    curr_num = curr_num - 1  




            if "DYDXUSDT LONG" in dt and status_trade_DYDXUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_DYDXUSDT = bar
                open_trade("DYDXUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_DYDXUSDT = 1
                curr_num = curr_num + 1
                    
            if "DYDXUSDT SHORT" in dt and status_trade_DYDXUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_DYDXUSDT = bar
                open_trade("DYDXUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_DYDXUSDT = -1
                curr_num = curr_num + 1

            if ("DYDXUSDT end of trade" in dt) and (status_trade_DYDXUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DYDXUSDT:
                    close_trade("DYDXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DYDXUSDT = 0
                    curr_num = curr_num - 1

            if ("DYDXUSDT end of trade" in dt) and (status_trade_DYDXUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DYDXUSDT:
                    close_trade("DYDXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DYDXUSDT = 0
                    curr_num = curr_num - 1


            if "DYDXUSDT LONG" in dt and (status_trade_DYDXUSDT == -1 or status_trade_DYDXUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DYDXUSDT:
                    close_trade("DYDXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DYDXUSDT = 0
                    curr_num = curr_num - 1

            if "DYDXUSDT SHORT" in dt and (status_trade_DYDXUSDT == -1 or status_trade_DYDXUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DYDXUSDT:
                    close_trade("DYDXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DYDXUSDT = 0
                    curr_num = curr_num - 1  




            if "SOLUSDT LONG" in dt and status_trade_SOLUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_SOLUSDT = bar
                open_trade("SOLUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_SOLUSDT = 1
                curr_num = curr_num + 1
                    
            if "SOLUSDT SHORT" in dt and status_trade_SOLUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_SOLUSDT = bar
                open_trade("SOLUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_SOLUSDT = -1
                curr_num = curr_num + 1

            if ("SOLUSDT end of trade" in dt) and (status_trade_SOLUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SOLUSDT:
                    close_trade("SOLUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SOLUSDT = 0
                    curr_num = curr_num - 1

            if ("SOLUSDT end of trade" in dt) and (status_trade_SOLUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SOLUSDT:
                    close_trade("SOLUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SOLUSDT = 0
                    curr_num = curr_num - 1


            if "SOLUSDT LONG" in dt and (status_trade_SOLUSDT == -1 or status_trade_SOLUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SOLUSDT:
                    close_trade("SOLUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SOLUSDT = 0
                    curr_num = curr_num - 1

            if "SOLUSDT SHORT" in dt and (status_trade_SOLUSDT == -1 or status_trade_SOLUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SOLUSDT:
                    close_trade("SOLUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SOLUSDT = 0
                    curr_num = curr_num - 1  




            if "DOTUSDT LONG" in dt and status_trade_DOTUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_DOTUSDT = bar
                open_trade("DOTUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_DOTUSDT = 1
                curr_num = curr_num + 1
                    
            if "DOTUSDT SHORT" in dt and status_trade_DOTUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_DOTUSDT = bar
                open_trade("DOTUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_DOTUSDT = -1
                curr_num = curr_num + 1

            if ("DOTUSDT end of trade" in dt) and (status_trade_DOTUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DOTUSDT:
                    close_trade("DOTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DOTUSDT = 0
                    curr_num = curr_num - 1

            if ("DOTUSDT end of trade" in dt) and (status_trade_DOTUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DOTUSDT:
                    close_trade("DOTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DOTUSDT = 0
                    curr_num = curr_num - 1


            if "DOTUSDT LONG" in dt and (status_trade_DOTUSDT == -1 or status_trade_DOTUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DOTUSDT:
                    close_trade("DOTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DOTUSDT = 0
                    curr_num = curr_num - 1

            if "DOTUSDT SHORT" in dt and (status_trade_DOTUSDT == -1 or status_trade_DOTUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DOTUSDT:
                    close_trade("DOTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DOTUSDT = 0
                    curr_num = curr_num - 1  




            if "ADAUSDT LONG" in dt and status_trade_ADAUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ADAUSDT = bar
                open_trade("ADAUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ADAUSDT = 1
                curr_num = curr_num + 1
                    
            if "ADAUSDT SHORT" in dt and status_trade_ADAUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ADAUSDT = bar
                open_trade("ADAUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ADAUSDT = -1
                curr_num = curr_num + 1

            if ("ADAUSDT end of trade" in dt) and (status_trade_ADAUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ADAUSDT:
                    close_trade("ADAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ADAUSDT = 0
                    curr_num = curr_num - 1

            if ("ADAUSDT end of trade" in dt) and (status_trade_ADAUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ADAUSDT:
                    close_trade("ADAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ADAUSDT = 0
                    curr_num = curr_num - 1


            if "ADAUSDT LONG" in dt and (status_trade_ADAUSDT == -1 or status_trade_ADAUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ADAUSDT:
                    close_trade("ADAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ADAUSDT = 0
                    curr_num = curr_num - 1

            if "ADAUSDT SHORT" in dt and (status_trade_ADAUSDT == -1 or status_trade_ADAUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ADAUSDT:
                    close_trade("ADAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ADAUSDT = 0
                    curr_num = curr_num - 1  




            if "XRPUSDT LONG" in dt and status_trade_XRPUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_XRPUSDT = bar
                open_trade("XRPUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_XRPUSDT = 1
                curr_num = curr_num + 1
                    
            if "XRPUSDT SHORT" in dt and status_trade_XRPUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_XRPUSDT = bar
                open_trade("XRPUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_XRPUSDT = -1
                curr_num = curr_num + 1

            if ("XRPUSDT end of trade" in dt) and (status_trade_XRPUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_XRPUSDT:
                    close_trade("XRPUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_XRPUSDT = 0
                    curr_num = curr_num - 1

            if ("XRPUSDT end of trade" in dt) and (status_trade_XRPUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_XRPUSDT:
                    close_trade("XRPUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_XRPUSDT = 0
                    curr_num = curr_num - 1


            if "XRPUSDT LONG" in dt and (status_trade_XRPUSDT == -1 or status_trade_XRPUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_XRPUSDT:
                    close_trade("XRPUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_XRPUSDT = 0
                    curr_num = curr_num - 1

            if "XRPUSDT SHORT" in dt and (status_trade_XRPUSDT == -1 or status_trade_XRPUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_XRPUSDT:
                    close_trade("XRPUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_XRPUSDT = 0
                    curr_num = curr_num - 1  




            if "FILUSDT LONG" in dt and status_trade_FILUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_FILUSDT = bar
                open_trade("FILUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_FILUSDT = 1
                curr_num = curr_num + 1
                    
            if "FILUSDT SHORT" in dt and status_trade_FILUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_FILUSDT = bar
                open_trade("FILUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_FILUSDT = -1
                curr_num = curr_num + 1

            if ("FILUSDT end of trade" in dt) and (status_trade_FILUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_FILUSDT:
                    close_trade("FILUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_FILUSDT = 0
                    curr_num = curr_num - 1

            if ("FILUSDT end of trade" in dt) and (status_trade_FILUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_FILUSDT:
                    close_trade("FILUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_FILUSDT = 0
                    curr_num = curr_num - 1


            if "FILUSDT LONG" in dt and (status_trade_FILUSDT == -1 or status_trade_FILUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_FILUSDT:
                    close_trade("FILUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_FILUSDT = 0
                    curr_num = curr_num - 1

            if "FILUSDT SHORT" in dt and (status_trade_FILUSDT == -1 or status_trade_FILUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_FILUSDT:
                    close_trade("FILUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_FILUSDT = 0
                    curr_num = curr_num - 1  




            if "FTMUSDT LONG" in dt and status_trade_FTMUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_FTMUSDT = bar
                open_trade("FTMUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_FTMUSDT = 1
                curr_num = curr_num + 1
                    
            if "FTMUSDT SHORT" in dt and status_trade_FTMUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_FTMUSDT = bar
                open_trade("FTMUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_FTMUSDT = -1
                curr_num = curr_num + 1

            if ("FTMUSDT end of trade" in dt) and (status_trade_FTMUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_FTMUSDT:
                    close_trade("FTMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_FTMUSDT = 0
                    curr_num = curr_num - 1

            if ("FTMUSDT end of trade" in dt) and (status_trade_FTMUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_FTMUSDT:
                    close_trade("FTMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_FTMUSDT = 0
                    curr_num = curr_num - 1


            if "FTMUSDT LONG" in dt and (status_trade_FTMUSDT == -1 or status_trade_FTMUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_FTMUSDT:
                    close_trade("FTMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_FTMUSDT = 0
                    curr_num = curr_num - 1

            if "FTMUSDT SHORT" in dt and (status_trade_FTMUSDT == -1 or status_trade_FTMUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_FTMUSDT:
                    close_trade("FTMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_FTMUSDT = 0
                    curr_num = curr_num - 1  




            if "TRXUSDT LONG" in dt and status_trade_TRXUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_TRXUSDT = bar
                open_trade("TRXUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_TRXUSDT = 1
                curr_num = curr_num + 1
                    
            if "TRXUSDT SHORT" in dt and status_trade_TRXUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_TRXUSDT = bar
                open_trade("TRXUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_TRXUSDT = -1
                curr_num = curr_num + 1

            if ("TRXUSDT end of trade" in dt) and (status_trade_TRXUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_TRXUSDT:
                    close_trade("TRXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_TRXUSDT = 0
                    curr_num = curr_num - 1

            if ("TRXUSDT end of trade" in dt) and (status_trade_TRXUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_TRXUSDT:
                    close_trade("TRXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_TRXUSDT = 0
                    curr_num = curr_num - 1


            if "TRXUSDT LONG" in dt and (status_trade_TRXUSDT == -1 or status_trade_TRXUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_TRXUSDT:
                    close_trade("TRXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_TRXUSDT = 0
                    curr_num = curr_num - 1

            if "TRXUSDT SHORT" in dt and (status_trade_TRXUSDT == -1 or status_trade_TRXUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_TRXUSDT:
                    close_trade("TRXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_TRXUSDT = 0
                    curr_num = curr_num - 1  




            if "ALICEUSDT LONG" in dt and status_trade_ALICEUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ALICEUSDT = bar
                open_trade("ALICEUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ALICEUSDT = 1
                curr_num = curr_num + 1
                    
            if "ALICEUSDT SHORT" in dt and status_trade_ALICEUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ALICEUSDT = bar
                open_trade("ALICEUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ALICEUSDT = -1
                curr_num = curr_num + 1

            if ("ALICEUSDT end of trade" in dt) and (status_trade_ALICEUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ALICEUSDT:
                    close_trade("ALICEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ALICEUSDT = 0
                    curr_num = curr_num - 1

            if ("ALICEUSDT end of trade" in dt) and (status_trade_ALICEUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ALICEUSDT:
                    close_trade("ALICEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ALICEUSDT = 0
                    curr_num = curr_num - 1


            if "ALICEUSDT LONG" in dt and (status_trade_ALICEUSDT == -1 or status_trade_ALICEUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ALICEUSDT:
                    close_trade("ALICEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ALICEUSDT = 0
                    curr_num = curr_num - 1

            if "ALICEUSDT SHORT" in dt and (status_trade_ALICEUSDT == -1 or status_trade_ALICEUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ALICEUSDT:
                    close_trade("ALICEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ALICEUSDT = 0
                    curr_num = curr_num - 1  




            if "C98USDT LONG" in dt and status_trade_C98USDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_C98USDT = bar
                open_trade("C98USDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_C98USDT = 1
                curr_num = curr_num + 1
                    
            if "C98USDT SHORT" in dt and status_trade_C98USDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_C98USDT = bar
                open_trade("C98USDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_C98USDT = -1
                curr_num = curr_num + 1

            if ("C98USDT end of trade" in dt) and (status_trade_C98USDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_C98USDT:
                    close_trade("C98USDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_C98USDT = 0
                    curr_num = curr_num - 1

            if ("C98USDT end of trade" in dt) and (status_trade_C98USDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_C98USDT:
                    close_trade("C98USDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_C98USDT = 0
                    curr_num = curr_num - 1


            if "C98USDT LONG" in dt and status_trade_C98USDT == -1 and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_C98USDT:
                    close_trade("C98USDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_C98USDT = 0
                    curr_num = curr_num - 1

            if "C98USDT SHORT" in dt and status_trade_C98USDT == 1 and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_C98USDT:
                    close_trade("C98USDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_C98USDT = 0
                    curr_num = curr_num - 1  




            if "AAVEUSDT LONG" in dt and status_trade_AAVEUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_AAVEUSDT = bar
                open_trade("AAVEUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_AAVEUSDT = 1
                curr_num = curr_num + 1
                    
            if "AAVEUSDT SHORT" in dt and status_trade_AAVEUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_AAVEUSDT = bar
                open_trade("AAVEUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_AAVEUSDT = -1
                curr_num = curr_num + 1

            if ("AAVEUSDT end of trade" in dt) and (status_trade_AAVEUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_AAVEUSDT:
                    close_trade("AAVEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_AAVEUSDT = 0
                    curr_num = curr_num - 1

            if ("AAVEUSDT end of trade" in dt) and (status_trade_AAVEUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_AAVEUSDT:
                    close_trade("AAVEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_AAVEUSDT = 0
                    curr_num = curr_num - 1


            if "AAVEUSDT LONG" in dt and (status_trade_AAVEUSDT == -1 or status_trade_AAVEUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_AAVEUSDT:
                    close_trade("AAVEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_AAVEUSDT = 0
                    curr_num = curr_num - 1

            if "AAVEUSDT SHORT" in dt and (status_trade_AAVEUSDT == -1 or status_trade_AAVEUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_AAVEUSDT:
                    close_trade("AAVEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_AAVEUSDT = 0
                    curr_num = curr_num - 1  




            if "THETAUSDT LONG" in dt and status_trade_THETAUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_THETAUSDT = bar
                open_trade("THETAUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_THETAUSDT = 1
                curr_num = curr_num + 1
                    
            if "THETAUSDT SHORT" in dt and status_trade_THETAUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_THETAUSDT = bar
                open_trade("THETAUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_THETAUSDT = -1
                curr_num = curr_num + 1

            if ("THETAUSDT end of trade" in dt) and (status_trade_THETAUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_THETAUSDT:
                    close_trade("THETAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_THETAUSDT = 0
                    curr_num = curr_num - 1

            if ("THETAUSDT end of trade" in dt) and (status_trade_THETAUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_THETAUSDT:
                    close_trade("THETAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_THETAUSDT = 0
                    curr_num = curr_num - 1


            if "THETAUSDT LONG" in dt and (status_trade_THETAUSDT == -1 or status_trade_THETAUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_THETAUSDT:
                    close_trade("THETAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_THETAUSDT = 0
                    curr_num = curr_num - 1

            if "THETAUSDT SHORT" in dt and (status_trade_THETAUSDT == -1 or status_trade_THETAUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_THETAUSDT:
                    close_trade("THETAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_THETAUSDT = 0
                    curr_num = curr_num - 1  




            if "DASHUSDT LONG" in dt and status_trade_DASHUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_DASHUSDT = bar
                open_trade("DASHUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_DASHUSDT = 1
                curr_num = curr_num + 1
                    
            if "DASHUSDT SHORT" in dt and status_trade_DASHUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_DASHUSDT = bar
                open_trade("DASHUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_DASHUSDT = -1
                curr_num = curr_num + 1

            if ("DASHUSDT end of trade" in dt) and (status_trade_DASHUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DASHUSDT:
                    close_trade("DASHUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DASHUSDT = 0
                    curr_num = curr_num - 1

            if ("DASHUSDT end of trade" in dt) and (status_trade_DASHUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DASHUSDT:
                    close_trade("DASHUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DASHUSDT = 0
                    curr_num = curr_num - 1


            if "DASHUSDT LONG" in dt and (status_trade_DASHUSDT == -1 or status_trade_DASHUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DASHUSDT:
                    close_trade("DASHUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DASHUSDT = 0
                    curr_num = curr_num - 1

            if "DASHUSDT SHORT" in dt and (status_trade_DASHUSDT == -1 or status_trade_DASHUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DASHUSDT:
                    close_trade("DASHUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DASHUSDT = 0
                    curr_num = curr_num - 1  




            if "BTSUSDT LONG" in dt and status_trade_BTSUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BTSUSDT = bar
                open_trade("BTSUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BTSUSDT = 1
                curr_num = curr_num + 1
                    
            if "BTSUSDT SHORT" in dt and status_trade_BTSUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BTSUSDT = bar
                open_trade("BTSUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BTSUSDT = -1
                curr_num = curr_num + 1

            if ("BTSUSDT end of trade" in dt) and (status_trade_BTSUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BTSUSDT:
                    close_trade("BTSUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BTSUSDT = 0
                    curr_num = curr_num - 1

            if ("BTSUSDT end of trade" in dt) and (status_trade_BTSUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BTSUSDT:
                    close_trade("BTSUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BTSUSDT = 0
                    curr_num = curr_num - 1


            if "BTSUSDT LONG" in dt and (status_trade_BTSUSDT == -1 or status_trade_BTSUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BTSUSDT:
                    close_trade("BTSUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BTSUSDT = 0
                    curr_num = curr_num - 1

            if "BTSUSDT SHORT" in dt and (status_trade_BTSUSDT == -1 or status_trade_BTSUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BTSUSDT:
                    close_trade("BTSUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BTSUSDT = 0
                    curr_num = curr_num - 1  




            if "AVAXUSDT LONG" in dt and status_trade_AVAXUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_AVAXUSDT = bar
                open_trade("AVAXUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_AVAXUSDT = 1
                curr_num = curr_num + 1
                    
            if "AVAXUSDT SHORT" in dt and status_trade_AVAXUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_AVAXUSDT = bar
                open_trade("AVAXUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_AVAXUSDT = -1
                curr_num = curr_num + 1

            if ("AVAXUSDT end of trade" in dt) and (status_trade_AVAXUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_AVAXUSDT:
                    close_trade("AVAXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_AVAXUSDT = 0
                    curr_num = curr_num - 1

            if ("AVAXUSDT end of trade" in dt) and (status_trade_AVAXUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_AVAXUSDT:
                    close_trade("AVAXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_AVAXUSDT = 0
                    curr_num = curr_num - 1


            if "AVAXUSDT LONG" in dt and (status_trade_AVAXUSDT == -1 or status_trade_AVAXUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_AVAXUSDT:
                    close_trade("AVAXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_AVAXUSDT = 0
                    curr_num = curr_num - 1

            if "AVAXUSDT SHORT" in dt and (status_trade_AVAXUSDT == -1 or status_trade_AVAXUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_AVAXUSDT:
                    close_trade("AVAXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_AVAXUSDT = 0
                    curr_num = curr_num - 1  




            if "BNBUSDT LONG" in dt and status_trade_BNBUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BNBUSDT = bar
                open_trade("BNBUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BNBUSDT = 1
                curr_num = curr_num + 1
                    
            if "BNBUSDT SHORT" in dt and status_trade_BNBUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BNBUSDT = bar
                open_trade("BNBUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BNBUSDT = -1
                curr_num = curr_num + 1

            if ("BNBUSDT end of trade" in dt) and (status_trade_BNBUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BNBUSDT:
                    close_trade("BNBUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BNBUSDT = 0
                    curr_num = curr_num - 1

            if ("BNBUSDT end of trade" in dt) and (status_trade_BNBUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BNBUSDT:
                    close_trade("BNBUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BNBUSDT = 0
                    curr_num = curr_num - 1


            if "BNBUSDT LONG" in dt and (status_trade_BNBUSDT == -1 or status_trade_BNBUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BNBUSDT:
                    close_trade("BNBUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BNBUSDT = 0
                    curr_num = curr_num - 1

            if "BNBUSDT SHORT" in dt and (status_trade_BNBUSDT == -1 or status_trade_BNBUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BNBUSDT:
                    close_trade("BNBUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BNBUSDT = 0
                    curr_num = curr_num - 1  




            if "COMPUSDT LONG" in dt and status_trade_COMPUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_COMPUSDT = bar
                open_trade("COMPUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_COMPUSDT = 1
                curr_num = curr_num + 1
                    
            if "COMPUSDT SHORT" in dt and status_trade_COMPUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_COMPUSDT = bar
                open_trade("COMPUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_COMPUSDT = -1
                curr_num = curr_num + 1

            if ("COMPUSDT end of trade" in dt) and (status_trade_COMPUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_COMPUSDT:
                    close_trade("COMPUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_COMPUSDT = 0
                    curr_num = curr_num - 1

            if ("COMPUSDT end of trade" in dt) and (status_trade_COMPUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_COMPUSDT:
                    close_trade("COMPUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_COMPUSDT = 0
                    curr_num = curr_num - 1


            if "COMPUSDT LONG" in dt and (status_trade_COMPUSDT == -1 or status_trade_COMPUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_COMPUSDT:
                    close_trade("COMPUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_COMPUSDT = 0
                    curr_num = curr_num - 1

            if "COMPUSDT SHORT" in dt and (status_trade_COMPUSDT == -1 or status_trade_COMPUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_COMPUSDT:
                    close_trade("COMPUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_COMPUSDT = 0
                    curr_num = curr_num - 1  




            if "BLZUSDT LONG" in dt and status_trade_BLZUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BLZUSDT = bar
                open_trade("BLZUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BLZUSDT = 1
                curr_num = curr_num + 1
                    
            if "BLZUSDT SHORT" in dt and status_trade_BLZUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BLZUSDT = bar
                open_trade("BLZUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BLZUSDT = -1
                curr_num = curr_num + 1

            if ("BLZUSDT end of trade" in dt) and (status_trade_BLZUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BLZUSDT:
                    close_trade("BLZUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BLZUSDT = 0
                    curr_num = curr_num - 1

            if ("BLZUSDT end of trade" in dt) and (status_trade_BLZUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BLZUSDT:
                    close_trade("BLZUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BLZUSDT = 0
                    curr_num = curr_num - 1


            if "BLZUSDT LONG" in dt and (status_trade_BLZUSDT == -1 or status_trade_BLZUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BLZUSDT:
                    close_trade("BLZUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BLZUSDT = 0
                    curr_num = curr_num - 1

            if "BLZUSDT SHORT" in dt and (status_trade_BLZUSDT == -1 or status_trade_BLZUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BLZUSDT:
                    close_trade("BLZUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BLZUSDT = 0
                    curr_num = curr_num - 1  




            if "SNXUSDT LONG" in dt and status_trade_SNXUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_SNXUSDT = bar
                open_trade("SNXUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_SNXUSDT = 1
                curr_num = curr_num + 1
                    
            if "SNXUSDT SHORT" in dt and status_trade_SNXUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_SNXUSDT = bar
                open_trade("SNXUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_SNXUSDT = -1
                curr_num = curr_num + 1

            if ("SNXUSDT end of trade" in dt) and (status_trade_SNXUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SNXUSDT:
                    close_trade("SNXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SNXUSDT = 0
                    curr_num = curr_num - 1

            if ("SNXUSDT end of trade" in dt) and (status_trade_SNXUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SNXUSDT:
                    close_trade("SNXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SNXUSDT = 0
                    curr_num = curr_num - 1


            if "SNXUSDT LONG" in dt and (status_trade_SNXUSDT == -1 or status_trade_SNXUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SNXUSDT:
                    close_trade("SNXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SNXUSDT = 0
                    curr_num = curr_num - 1

            if "SNXUSDT SHORT" in dt and (status_trade_SNXUSDT == -1 or status_trade_SNXUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SNXUSDT:
                    close_trade("SNXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SNXUSDT = 0
                    curr_num = curr_num - 1  




            if "KAVAUSDT LONG" in dt and status_trade_KAVAUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_KAVAUSDT = bar
                open_trade("KAVAUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_KAVAUSDT = 1
                curr_num = curr_num + 1
                    
            if "KAVAUSDT SHORT" in dt and status_trade_KAVAUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_KAVAUSDT = bar
                open_trade("KAVAUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_KAVAUSDT = -1
                curr_num = curr_num + 1

            if ("KAVAUSDT end of trade" in dt) and (status_trade_KAVAUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_KAVAUSDT:
                    close_trade("KAVAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_KAVAUSDT = 0
                    curr_num = curr_num - 1

            if ("KAVAUSDT end of trade" in dt) and (status_trade_KAVAUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_KAVAUSDT:
                    close_trade("KAVAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_KAVAUSDT = 0
                    curr_num = curr_num - 1


            if "KAVAUSDT LONG" in dt and (status_trade_KAVAUSDT == -1 or status_trade_KAVAUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_KAVAUSDT:
                    close_trade("KAVAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_KAVAUSDT = 0
                    curr_num = curr_num - 1

            if "KAVAUSDT SHORT" in dt and (status_trade_KAVAUSDT == -1 or status_trade_KAVAUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_KAVAUSDT:
                    close_trade("KAVAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_KAVAUSDT = 0
                    curr_num = curr_num - 1  




            if "TOMOUSDT LONG" in dt and status_trade_TOMOUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_TOMOUSDT = bar
                open_trade("TOMOUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_TOMOUSDT = 1
                curr_num = curr_num + 1
                    
            if "TOMOUSDT SHORT" in dt and status_trade_TOMOUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_TOMOUSDT = bar
                open_trade("TOMOUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_TOMOUSDT = -1
                curr_num = curr_num + 1

            if ("TOMOUSDT end of trade" in dt) and (status_trade_TOMOUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_TOMOUSDT:
                    close_trade("TOMOUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_TOMOUSDT = 0
                    curr_num = curr_num - 1

            if ("TOMOUSDT end of trade" in dt) and (status_trade_TOMOUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_TOMOUSDT:
                    close_trade("TOMOUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_TOMOUSDT = 0
                    curr_num = curr_num - 1


            if "TOMOUSDT LONG" in dt and (status_trade_TOMOUSDT == -1 or status_trade_TOMOUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_TOMOUSDT:
                    close_trade("TOMOUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_TOMOUSDT = 0
                    curr_num = curr_num - 1

            if "TOMOUSDT SHORT" in dt and (status_trade_TOMOUSDT == -1 or status_trade_TOMOUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_TOMOUSDT:
                    close_trade("TOMOUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_TOMOUSDT = 0
                    curr_num = curr_num - 1  




            if "IOTAUSDT LONG" in dt and status_trade_IOTAUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_IOTAUSDT = bar
                open_trade("IOTAUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_IOTAUSDT = 1
                curr_num = curr_num + 1
                    
            if "IOTAUSDT SHORT" in dt and status_trade_IOTAUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_IOTAUSDT = bar
                open_trade("IOTAUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_IOTAUSDT = -1
                curr_num = curr_num + 1

            if ("IOTAUSDT end of trade" in dt) and (status_trade_IOTAUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_IOTAUSDT:
                    close_trade("IOTAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_IOTAUSDT = 0
                    curr_num = curr_num - 1

            if ("IOTAUSDT end of trade" in dt) and (status_trade_IOTAUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_IOTAUSDT:
                    close_trade("IOTAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_IOTAUSDT = 0
                    curr_num = curr_num - 1


            if "IOTAUSDT LONG" in dt and (status_trade_IOTAUSDT == -1 or status_trade_IOTAUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_IOTAUSDT:
                    close_trade("IOTAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_IOTAUSDT = 0
                    curr_num = curr_num - 1

            if "IOTAUSDT SHORT" in dt and (status_trade_IOTAUSDT == -1 or status_trade_IOTAUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_IOTAUSDT:
                    close_trade("IOTAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_IOTAUSDT = 0
                    curr_num = curr_num - 1  




            if "RVNUSDT LONG" in dt and status_trade_RVNUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_RVNUSDT = bar
                open_trade("RVNUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_RVNUSDT = 1
                curr_num = curr_num + 1
                    
            if "RVNUSDT SHORT" in dt and status_trade_RVNUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_RVNUSDT = bar
                open_trade("RVNUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_RVNUSDT = -1
                curr_num = curr_num + 1

            if ("RVNUSDT end of trade" in dt) and (status_trade_RVNUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RVNUSDT:
                    close_trade("RVNUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RVNUSDT = 0
                    curr_num = curr_num - 1

            if ("RVNUSDT end of trade" in dt) and (status_trade_RVNUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RVNUSDT:
                    close_trade("RVNUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RVNUSDT = 0
                    curr_num = curr_num - 1


            if "RVNUSDT LONG" in dt and (status_trade_RVNUSDT == -1 or status_trade_RVNUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RVNUSDT:
                    close_trade("RVNUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RVNUSDT = 0
                    curr_num = curr_num - 1

            if "RVNUSDT SHORT" in dt and (status_trade_RVNUSDT == -1 or status_trade_RVNUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RVNUSDT:
                    close_trade("RVNUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RVNUSDT = 0
                    curr_num = curr_num - 1  




            if "UNIUSDT LONG" in dt and status_trade_UNIUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_UNIUSDT = bar
                open_trade("UNIUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_UNIUSDT = 1
                curr_num = curr_num + 1
                    
            if "UNIUSDT SHORT" in dt and status_trade_UNIUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_UNIUSDT = bar
                open_trade("UNIUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_UNIUSDT = -1
                curr_num = curr_num + 1

            if ("UNIUSDT end of trade" in dt) and (status_trade_UNIUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_UNIUSDT:
                    close_trade("UNIUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_UNIUSDT = 0
                    curr_num = curr_num - 1

            if ("UNIUSDT end of trade" in dt) and (status_trade_UNIUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_UNIUSDT:
                    close_trade("UNIUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_UNIUSDT = 0
                    curr_num = curr_num - 1


            if "UNIUSDT LONG" in dt and (status_trade_UNIUSDT == -1 or status_trade_UNIUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_UNIUSDT:
                    close_trade("UNIUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_UNIUSDT = 0
                    curr_num = curr_num - 1

            if "UNIUSDT SHORT" in dt and (status_trade_UNIUSDT == -1 or status_trade_UNIUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_UNIUSDT:
                    close_trade("UNIUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_UNIUSDT = 0
                    curr_num = curr_num - 1  




            if "IOTXUSDT LONG" in dt and status_trade_IOTXUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_IOTXUSDT = bar
                open_trade("IOTXUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_IOTXUSDT = 1
                curr_num = curr_num + 1
                    
            if "IOTXUSDT SHORT" in dt and status_trade_IOTXUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_IOTXUSDT = bar
                open_trade("IOTXUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_IOTXUSDT = -1
                curr_num = curr_num + 1

            if ("IOTXUSDT end of trade" in dt) and (status_trade_IOTXUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_IOTXUSDT:
                    close_trade("IOTXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_IOTXUSDT = 0
                    curr_num = curr_num - 1

            if ("IOTXUSDT end of trade" in dt) and (status_trade_IOTXUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_IOTXUSDT:
                    close_trade("IOTXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_IOTXUSDT = 0
                    curr_num = curr_num - 1


            if "IOTXUSDT LONG" in dt and (status_trade_IOTXUSDT == -1 or status_trade_IOTXUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_IOTXUSDT:
                    close_trade("IOTXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_IOTXUSDT = 0
                    curr_num = curr_num - 1

            if "IOTXUSDT SHORT" in dt and (status_trade_IOTXUSDT == -1 or status_trade_IOTXUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_IOTXUSDT:
                    close_trade("IOTXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_IOTXUSDT = 0
                    curr_num = curr_num - 1  




            if "ONEUSDT LONG" in dt and status_trade_ONEUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ONEUSDT = bar
                open_trade("ONEUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ONEUSDT = 1
                curr_num = curr_num + 1
                    
            if "ONEUSDT SHORT" in dt and status_trade_ONEUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ONEUSDT = bar
                open_trade("ONEUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ONEUSDT = -1
                curr_num = curr_num + 1

            if ("ONEUSDT end of trade" in dt) and (status_trade_ONEUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ONEUSDT:
                    close_trade("ONEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ONEUSDT = 0
                    curr_num = curr_num - 1

            if ("ONEUSDT end of trade" in dt) and (status_trade_ONEUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ONEUSDT:
                    close_trade("ONEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ONEUSDT = 0
                    curr_num = curr_num - 1


            if "ONEUSDT LONG" in dt and (status_trade_ONEUSDT == -1 or status_trade_ONEUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ONEUSDT:
                    close_trade("ONEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ONEUSDT = 0
                    curr_num = curr_num - 1

            if "ONEUSDT SHORT" in dt and (status_trade_ONEUSDT == -1 or status_trade_ONEUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ONEUSDT:
                    close_trade("ONEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ONEUSDT = 0
                    curr_num = curr_num - 1  




            if "RUNEUSDT LONG" in dt and status_trade_RUNEUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_RUNEUSDT = bar
                open_trade("RUNEUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_RUNEUSDT = 1
                curr_num = curr_num + 1
                    
            if "RUNEUSDT SHORT" in dt and status_trade_RUNEUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_RUNEUSDT = bar
                open_trade("RUNEUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_RUNEUSDT = -1
                curr_num = curr_num + 1

            if ("RUNEUSDT end of trade" in dt) and (status_trade_RUNEUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RUNEUSDT:
                    close_trade("RUNEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RUNEUSDT = 0
                    curr_num = curr_num - 1

            if ("RUNEUSDT end of trade" in dt) and (status_trade_RUNEUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RUNEUSDT:
                    close_trade("RUNEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RUNEUSDT = 0
                    curr_num = curr_num - 1


            if "RUNEUSDT LONG" in dt and (status_trade_RUNEUSDT == -1 or status_trade_RUNEUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RUNEUSDT:
                    close_trade("RUNEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RUNEUSDT = 0
                    curr_num = curr_num - 1

            if "RUNEUSDT SHORT" in dt and (status_trade_RUNEUSDT == -1 or status_trade_RUNEUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RUNEUSDT:
                    close_trade("RUNEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RUNEUSDT = 0
                    curr_num = curr_num - 1  




            if "RLCUSDT LONG" in dt and status_trade_RLCUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_RLCUSDT = bar
                open_trade("RLCUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_RLCUSDT = 1
                curr_num = curr_num + 1
                    
            if "RLCUSDT SHORT" in dt and status_trade_RLCUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_RLCUSDT = bar
                open_trade("RLCUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_RLCUSDT = -1
                curr_num = curr_num + 1

            if ("RLCUSDT end of trade" in dt) and (status_trade_RLCUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RLCUSDT:
                    close_trade("RLCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RLCUSDT = 0
                    curr_num = curr_num - 1

            if ("RLCUSDT end of trade" in dt) and (status_trade_RLCUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RLCUSDT:
                    close_trade("RLCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RLCUSDT = 0
                    curr_num = curr_num - 1


            if "RLCUSDT LONG" in dt and (status_trade_RLCUSDT == -1 or status_trade_RLCUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RLCUSDT:
                    close_trade("RLCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RLCUSDT = 0
                    curr_num = curr_num - 1

            if "RLCUSDT SHORT" in dt and (status_trade_RLCUSDT == -1 or status_trade_RLCUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RLCUSDT:
                    close_trade("RLCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RLCUSDT = 0
                    curr_num = curr_num - 1  




            if "EOSUSDT LONG" in dt and status_trade_EOSUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_EOSUSDT = bar
                open_trade("EOSUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_EOSUSDT = 1
                curr_num = curr_num + 1
                    
            if "EOSUSDT SHORT" in dt and status_trade_EOSUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_EOSUSDT = bar
                open_trade("EOSUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_EOSUSDT = -1
                curr_num = curr_num + 1

            if ("EOSUSDT end of trade" in dt) and (status_trade_EOSUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_EOSUSDT:
                    close_trade("EOSUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_EOSUSDT = 0
                    curr_num = curr_num - 1

            if ("EOSUSDT end of trade" in dt) and (status_trade_EOSUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_EOSUSDT:
                    close_trade("EOSUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_EOSUSDT = 0
                    curr_num = curr_num - 1


            if "EOSUSDT LONG" in dt and (status_trade_EOSUSDT == -1 or status_trade_EOSUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_EOSUSDT:
                    close_trade("EOSUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_EOSUSDT = 0
                    curr_num = curr_num - 1

            if "EOSUSDT SHORT" in dt and (status_trade_EOSUSDT == -1 or status_trade_EOSUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_EOSUSDT:
                    close_trade("EOSUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_EOSUSDT = 0
                    curr_num = curr_num - 1  




            if "SUSHIUSDT LONG" in dt and status_trade_SUSHIUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_SUSHIUSDT = bar
                open_trade("SUSHIUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_SUSHIUSDT = 1
                curr_num = curr_num + 1
                    
            if "SUSHIUSDT SHORT" in dt and status_trade_SUSHIUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_SUSHIUSDT = bar
                open_trade("SUSHIUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_SUSHIUSDT = -1
                curr_num = curr_num + 1

            if ("SUSHIUSDT end of trade" in dt) and (status_trade_SUSHIUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SUSHIUSDT:
                    close_trade("SUSHIUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SUSHIUSDT = 0
                    curr_num = curr_num - 1

            if ("SUSHIUSDT end of trade" in dt) and (status_trade_SUSHIUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SUSHIUSDT:
                    close_trade("SUSHIUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SUSHIUSDT = 0
                    curr_num = curr_num - 1


            if "SUSHIUSDT LONG" in dt and (status_trade_SUSHIUSDT == -1 or status_trade_SUSHIUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SUSHIUSDT:
                    close_trade("SUSHIUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SUSHIUSDT = 0
                    curr_num = curr_num - 1

            if "SUSHIUSDT SHORT" in dt and (status_trade_SUSHIUSDT == -1 or status_trade_SUSHIUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SUSHIUSDT:
                    close_trade("SUSHIUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SUSHIUSDT = 0
                    curr_num = curr_num - 1  




            if "WAVESUSDT LONG" in dt and status_trade_WAVESUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_WAVESUSDT = bar
                open_trade("WAVESUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_WAVESUSDT = 1
                curr_num = curr_num + 1
                    
            if "WAVESUSDT SHORT" in dt and status_trade_WAVESUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_WAVESUSDT = bar
                open_trade("WAVESUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_WAVESUSDT = -1
                curr_num = curr_num + 1

            if ("WAVESUSDT end of trade" in dt) and (status_trade_WAVESUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_WAVESUSDT:
                    close_trade("WAVESUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_WAVESUSDT = 0
                    curr_num = curr_num - 1

            if ("WAVESUSDT end of trade" in dt) and (status_trade_WAVESUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_WAVESUSDT:
                    close_trade("WAVESUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_WAVESUSDT = 0
                    curr_num = curr_num - 1


            if "WAVESUSDT LONG" in dt and (status_trade_WAVESUSDT == -1 or status_trade_WAVESUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_WAVESUSDT:
                    close_trade("WAVESUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_WAVESUSDT = 0
                    curr_num = curr_num - 1

            if "WAVESUSDT SHORT" in dt and (status_trade_WAVESUSDT == -1 or status_trade_WAVESUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_WAVESUSDT:
                    close_trade("WAVESUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_WAVESUSDT = 0
                    curr_num = curr_num - 1  




            if "VETUSDT LONG" in dt and status_trade_VETUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_VETUSDT = bar
                open_trade("VETUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_VETUSDT = 1
                curr_num = curr_num + 1
                    
            if "VETUSDT SHORT" in dt and status_trade_VETUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_VETUSDT = bar
                open_trade("VETUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_VETUSDT = -1
                curr_num = curr_num + 1

            if ("VETUSDT end of trade" in dt) and (status_trade_VETUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_VETUSDT:
                    close_trade("VETUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_VETUSDT = 0
                    curr_num = curr_num - 1

            if ("VETUSDT end of trade" in dt) and (status_trade_VETUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_VETUSDT:
                    close_trade("VETUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_VETUSDT = 0
                    curr_num = curr_num - 1


            if "VETUSDT LONG" in dt and (status_trade_VETUSDT == -1 or status_trade_VETUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_VETUSDT:
                    close_trade("VETUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_VETUSDT = 0
                    curr_num = curr_num - 1

            if "VETUSDT SHORT" in dt and (status_trade_VETUSDT == -1 or status_trade_VETUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_VETUSDT:
                    close_trade("VETUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_VETUSDT = 0
                    curr_num = curr_num - 1  




            if "ZECUSDT LONG" in dt and status_trade_ZECUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ZECUSDT = bar
                open_trade("ZECUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ZECUSDT = 1
                curr_num = curr_num + 1
                    
            if "ZECUSDT SHORT" in dt and status_trade_ZECUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ZECUSDT = bar
                open_trade("ZECUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ZECUSDT = -1
                curr_num = curr_num + 1

            if ("ZECUSDT end of trade" in dt) and (status_trade_ZECUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ZECUSDT:
                    close_trade("ZECUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ZECUSDT = 0
                    curr_num = curr_num - 1

            if ("ZECUSDT end of trade" in dt) and (status_trade_ZECUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ZECUSDT:
                    close_trade("ZECUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ZECUSDT = 0
                    curr_num = curr_num - 1


            if "ZECUSDT LONG" in dt and (status_trade_ZECUSDT == -1 or status_trade_ZECUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ZECUSDT:
                    close_trade("ZECUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ZECUSDT = 0
                    curr_num = curr_num - 1

            if "ZECUSDT SHORT" in dt and (status_trade_ZECUSDT == -1 or status_trade_ZECUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ZECUSDT:
                    close_trade("ZECUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ZECUSDT = 0
                    curr_num = curr_num - 1  




            if "XMRUSDT LONG" in dt and status_trade_XMRUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_XMRUSDT = bar
                open_trade("XMRUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_XMRUSDT = 1
                curr_num = curr_num + 1
                    
            if "XMRUSDT SHORT" in dt and status_trade_XMRUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_XMRUSDT = bar
                open_trade("XMRUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_XMRUSDT = -1
                curr_num = curr_num + 1

            if ("XMRUSDT end of trade" in dt) and (status_trade_XMRUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_XMRUSDT:
                    close_trade("XMRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_XMRUSDT = 0
                    curr_num = curr_num - 1

            if ("XMRUSDT end of trade" in dt) and (status_trade_XMRUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_XMRUSDT:
                    close_trade("XMRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_XMRUSDT = 0
                    curr_num = curr_num - 1


            if "XMRUSDT LONG" in dt and (status_trade_XMRUSDT == -1 or status_trade_XMRUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_XMRUSDT:
                    close_trade("XMRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_XMRUSDT = 0
                    curr_num = curr_num - 1

            if "XMRUSDT SHORT" in dt and (status_trade_XMRUSDT == -1 or status_trade_XMRUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_XMRUSDT:
                    close_trade("XMRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_XMRUSDT = 0
                    curr_num = curr_num - 1  




            if "MASKUSDT LONG" in dt and status_trade_MASKUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_MASKUSDT = bar
                open_trade("MASKUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_MASKUSDT = 1
                curr_num = curr_num + 1
                    
            if "MASKUSDT SHORT" in dt and status_trade_MASKUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_MASKUSDT = bar
                open_trade("MASKUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_MASKUSDT = -1
                curr_num = curr_num + 1

            if ("MASKUSDT end of trade" in dt) and (status_trade_MASKUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_MASKUSDT:
                    close_trade("MASKUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_MASKUSDT = 0
                    curr_num = curr_num - 1

            if ("MASKUSDT end of trade" in dt) and (status_trade_MASKUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_MASKUSDT:
                    close_trade("MASKUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_MASKUSDT = 0
                    curr_num = curr_num - 1


            if "MASKUSDT LONG" in dt and (status_trade_MASKUSDT == -1 or status_trade_MASKUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_MASKUSDT:
                    close_trade("MASKUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_MASKUSDT = 0
                    curr_num = curr_num - 1

            if "MASKUSDT SHORT" in dt and (status_trade_MASKUSDT == -1 or status_trade_MASKUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_MASKUSDT:
                    close_trade("MASKUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_MASKUSDT = 0
                    curr_num = curr_num - 1  




            if "STORJUSDT LONG" in dt and status_trade_STORJUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_STORJUSDT = bar
                open_trade("STORJUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_STORJUSDT = 1
                curr_num = curr_num + 1
                    
            if "STORJUSDT SHORT" in dt and status_trade_STORJUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_STORJUSDT = bar
                open_trade("STORJUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_STORJUSDT = -1
                curr_num = curr_num + 1

            if ("STORJUSDT end of trade" in dt) and (status_trade_STORJUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_STORJUSDT:
                    close_trade("STORJUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_STORJUSDT = 0
                    curr_num = curr_num - 1

            if ("STORJUSDT end of trade" in dt) and (status_trade_STORJUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_STORJUSDT:
                    close_trade("STORJUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_STORJUSDT = 0
                    curr_num = curr_num - 1


            if "STORJUSDT LONG" in dt and (status_trade_STORJUSDT == -1 or status_trade_STORJUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_STORJUSDT:
                    close_trade("STORJUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_STORJUSDT = 0
                    curr_num = curr_num - 1

            if "STORJUSDT SHORT" in dt and (status_trade_STORJUSDT == -1 or status_trade_STORJUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_STORJUSDT:
                    close_trade("STORJUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_STORJUSDT = 0
                    curr_num = curr_num - 1  




            if "XEMUSDT LONG" in dt and status_trade_XEMUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_XEMUSDT = bar
                open_trade("XEMUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_XEMUSDT = 1
                curr_num = curr_num + 1
                    
            if "XEMUSDT SHORT" in dt and status_trade_XEMUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_XEMUSDT = bar
                open_trade("XEMUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_XEMUSDT = -1
                curr_num = curr_num + 1

            if ("XEMUSDT end of trade" in dt) and (status_trade_XEMUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_XEMUSDT:
                    close_trade("XEMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_XEMUSDT = 0
                    curr_num = curr_num - 1

            if ("XEMUSDT end of trade" in dt) and (status_trade_XEMUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_XEMUSDT:
                    close_trade("XEMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_XEMUSDT = 0
                    curr_num = curr_num - 1


            if "XEMUSDT LONG" in dt and (status_trade_XEMUSDT == -1 or status_trade_XEMUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_XEMUSDT:
                    close_trade("XEMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_XEMUSDT = 0
                    curr_num = curr_num - 1

            if "XEMUSDT SHORT" in dt and (status_trade_XEMUSDT == -1 or status_trade_XEMUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_XEMUSDT:
                    close_trade("XEMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_XEMUSDT = 0
                    curr_num = curr_num - 1  




            if "KLAYUSDT LONG" in dt and status_trade_KLAYUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_KLAYUSDT = bar
                open_trade("KLAYUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_KLAYUSDT = 1
                curr_num = curr_num + 1
                    
            if "KLAYUSDT SHORT" in dt and status_trade_KLAYUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_KLAYUSDT = bar
                open_trade("KLAYUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_KLAYUSDT = -1
                curr_num = curr_num + 1

            if ("KLAYUSDT end of trade" in dt) and (status_trade_KLAYUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_KLAYUSDT:
                    close_trade("KLAYUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_KLAYUSDT = 0
                    curr_num = curr_num - 1

            if ("KLAYUSDT end of trade" in dt) and (status_trade_KLAYUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_KLAYUSDT:
                    close_trade("KLAYUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_KLAYUSDT = 0
                    curr_num = curr_num - 1


            if "KLAYUSDT LONG" in dt and (status_trade_KLAYUSDT == -1 or status_trade_KLAYUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_KLAYUSDT:
                    close_trade("KLAYUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_KLAYUSDT = 0
                    curr_num = curr_num - 1

            if "KLAYUSDT SHORT" in dt and (status_trade_KLAYUSDT == -1 or status_trade_KLAYUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_KLAYUSDT:
                    close_trade("KLAYUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_KLAYUSDT = 0
                    curr_num = curr_num - 1  




            if "DOGEUSDT LONG" in dt and status_trade_DOGEUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_DOGEUSDT = bar
                open_trade("DOGEUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_DOGEUSDT = 1
                curr_num = curr_num + 1
                    
            if "DOGEUSDT SHORT" in dt and status_trade_DOGEUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_DOGEUSDT = bar
                open_trade("DOGEUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_DOGEUSDT = -1
                curr_num = curr_num + 1

            if ("DOGEUSDT end of trade" in dt) and (status_trade_DOGEUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DOGEUSDT:
                    close_trade("DOGEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DOGEUSDT = 0
                    curr_num = curr_num - 1

            if ("DOGEUSDT end of trade" in dt) and (status_trade_DOGEUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DOGEUSDT:
                    close_trade("DOGEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DOGEUSDT = 0
                    curr_num = curr_num - 1


            if "DOGEUSDT LONG" in dt and (status_trade_DOGEUSDT == -1 or status_trade_DOGEUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DOGEUSDT:
                    close_trade("DOGEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DOGEUSDT = 0
                    curr_num = curr_num - 1

            if "DOGEUSDT SHORT" in dt and (status_trade_DOGEUSDT == -1 or status_trade_DOGEUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DOGEUSDT:
                    close_trade("DOGEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DOGEUSDT = 0
                    curr_num = curr_num - 1  




            if "AUDIOUSDT LONG" in dt and status_trade_AUDIOUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_AUDIOUSDT = bar
                open_trade("AUDIOUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_AUDIOUSDT = 1
                curr_num = curr_num + 1
                    
            if "AUDIOUSDT SHORT" in dt and status_trade_AUDIOUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_AUDIOUSDT = bar
                open_trade("AUDIOUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_AUDIOUSDT = -1
                curr_num = curr_num + 1

            if ("AUDIOUSDT end of trade" in dt) and (status_trade_AUDIOUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_AUDIOUSDT:
                    close_trade("AUDIOUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_AUDIOUSDT = 0
                    curr_num = curr_num - 1

            if ("AUDIOUSDT end of trade" in dt) and (status_trade_AUDIOUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_AUDIOUSDT:
                    close_trade("AUDIOUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_AUDIOUSDT = 0
                    curr_num = curr_num - 1


            if "AUDIOUSDT LONG" in dt and (status_trade_AUDIOUSDT == -1 or status_trade_AUDIOUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_AUDIOUSDT:
                    close_trade("AUDIOUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_AUDIOUSDT = 0
                    curr_num = curr_num - 1

            if "AUDIOUSDT SHORT" in dt and (status_trade_AUDIOUSDT == -1 or status_trade_AUDIOUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_AUDIOUSDT:
                    close_trade("AUDIOUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_AUDIOUSDT = 0
                    curr_num = curr_num - 1  




            if "1INCHUSDT LONG" in dt and status_trade_1INCHUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_1INCHUSDT = bar
                open_trade("1INCHUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_1INCHUSDT = 1
                curr_num = curr_num + 1
                    
            if "1INCHUSDT SHORT" in dt and status_trade_1INCHUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_1INCHUSDT = bar
                open_trade("1INCHUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_1INCHUSDT = -1
                curr_num = curr_num + 1

            if ("1INCHUSDT end of trade" in dt) and (status_trade_1INCHUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_1INCHUSDT:
                    close_trade("1INCHUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_1INCHUSDT = 0
                    curr_num = curr_num - 1

            if ("1INCHUSDT end of trade" in dt) and (status_trade_1INCHUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_1INCHUSDT:
                    close_trade("1INCHUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_1INCHUSDT = 0
                    curr_num = curr_num - 1


            if "1INCHUSDT LONG" in dt and status_trade_1INCHUSDT == -1 and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_1INCHUSDT:
                    close_trade("1INCHUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_1INCHUSDT = 0
                    curr_num = curr_num - 1

            if "1INCHUSDT SHORT" in dt and status_trade_1INCHUSDT == 1 and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_1INCHUSDT:
                    close_trade("1INCHUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_1INCHUSDT = 0
                    curr_num = curr_num - 1  




            if "OGNUSDT LONG" in dt and status_trade_OGNUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_OGNUSDT = bar
                open_trade("OGNUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_OGNUSDT = 1
                curr_num = curr_num + 1
                    
            if "OGNUSDT SHORT" in dt and status_trade_OGNUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_OGNUSDT = bar
                open_trade("OGNUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_OGNUSDT = -1
                curr_num = curr_num + 1

            if ("OGNUSDT end of trade" in dt) and (status_trade_OGNUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_OGNUSDT:
                    close_trade("OGNUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_OGNUSDT = 0
                    curr_num = curr_num - 1

            if ("OGNUSDT end of trade" in dt) and (status_trade_OGNUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_OGNUSDT:
                    close_trade("OGNUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_OGNUSDT = 0
                    curr_num = curr_num - 1


            if "OGNUSDT LONG" in dt and (status_trade_OGNUSDT == -1 or status_trade_OGNUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_OGNUSDT:
                    close_trade("OGNUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_OGNUSDT = 0
                    curr_num = curr_num - 1

            if "OGNUSDT SHORT" in dt and (status_trade_OGNUSDT == -1 or status_trade_OGNUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_OGNUSDT:
                    close_trade("OGNUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_OGNUSDT = 0
                    curr_num = curr_num - 1  




            if "KSMUSDT LONG" in dt and status_trade_KSMUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_KSMUSDT = bar
                open_trade("KSMUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_KSMUSDT = 1
                curr_num = curr_num + 1
                    
            if "KSMUSDT SHORT" in dt and status_trade_KSMUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_KSMUSDT = bar
                open_trade("KSMUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_KSMUSDT = -1
                curr_num = curr_num + 1

            if ("KSMUSDT end of trade" in dt) and (status_trade_KSMUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_KSMUSDT:
                    close_trade("KSMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_KSMUSDT = 0
                    curr_num = curr_num - 1

            if ("KSMUSDT end of trade" in dt) and (status_trade_KSMUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_KSMUSDT:
                    close_trade("KSMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_KSMUSDT = 0
                    curr_num = curr_num - 1


            if "KSMUSDT LONG" in dt and (status_trade_KSMUSDT == -1 or status_trade_KSMUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_KSMUSDT:
                    close_trade("KSMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_KSMUSDT = 0
                    curr_num = curr_num - 1

            if "KSMUSDT SHORT" in dt and (status_trade_KSMUSDT == -1 or status_trade_KSMUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_KSMUSDT:
                    close_trade("KSMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_KSMUSDT = 0
                    curr_num = curr_num - 1  




            if "MTLUSDT LONG" in dt and status_trade_MTLUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_MTLUSDT = bar
                open_trade("MTLUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_MTLUSDT = 1
                curr_num = curr_num + 1
                    
            if "MTLUSDT SHORT" in dt and status_trade_MTLUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_MTLUSDT = bar
                open_trade("MTLUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_MTLUSDT = -1
                curr_num = curr_num + 1

            if ("MTLUSDT end of trade" in dt) and (status_trade_MTLUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_MTLUSDT:
                    close_trade("MTLUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_MTLUSDT = 0
                    curr_num = curr_num - 1

            if ("MTLUSDT end of trade" in dt) and (status_trade_MTLUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_MTLUSDT:
                    close_trade("MTLUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_MTLUSDT = 0
                    curr_num = curr_num - 1


            if "MTLUSDT LONG" in dt and (status_trade_MTLUSDT == -1 or status_trade_MTLUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_MTLUSDT:
                    close_trade("MTLUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_MTLUSDT = 0
                    curr_num = curr_num - 1

            if "MTLUSDT SHORT" in dt and (status_trade_MTLUSDT == -1 or status_trade_MTLUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_MTLUSDT:
                    close_trade("MTLUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_MTLUSDT = 0
                    curr_num = curr_num - 1  




            if "BCHUSDT LONG" in dt and status_trade_BCHUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BCHUSDT = bar
                open_trade("BCHUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BCHUSDT = 1
                curr_num = curr_num + 1
                    
            if "BCHUSDT SHORT" in dt and status_trade_BCHUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BCHUSDT = bar
                open_trade("BCHUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BCHUSDT = -1
                curr_num = curr_num + 1

            if ("BCHUSDT end of trade" in dt) and (status_trade_BCHUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BCHUSDT:
                    close_trade("BCHUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BCHUSDT = 0
                    curr_num = curr_num - 1

            if ("BCHUSDT end of trade" in dt) and (status_trade_BCHUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BCHUSDT:
                    close_trade("BCHUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BCHUSDT = 0
                    curr_num = curr_num - 1


            if "BCHUSDT LONG" in dt and (status_trade_BCHUSDT == -1 or status_trade_BCHUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BCHUSDT:
                    close_trade("BCHUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BCHUSDT = 0
                    curr_num = curr_num - 1

            if "BCHUSDT SHORT" in dt and (status_trade_BCHUSDT == -1 or status_trade_BCHUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BCHUSDT:
                    close_trade("BCHUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BCHUSDT = 0
                    curr_num = curr_num - 1  




            if "ICPUSDT LONG" in dt and status_trade_ICPUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ICPUSDT = bar
                open_trade("ICPUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ICPUSDT = 1
                curr_num = curr_num + 1
                    
            if "ICPUSDT SHORT" in dt and status_trade_ICPUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ICPUSDT = bar
                open_trade("ICPUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ICPUSDT = -1
                curr_num = curr_num + 1

            if ("ICPUSDT end of trade" in dt) and (status_trade_ICPUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ICPUSDT:
                    close_trade("ICPUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ICPUSDT = 0
                    curr_num = curr_num - 1

            if ("ICPUSDT end of trade" in dt) and (status_trade_ICPUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ICPUSDT:
                    close_trade("ICPUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ICPUSDT = 0
                    curr_num = curr_num - 1


            if "ICPUSDT LONG" in dt and (status_trade_ICPUSDT == -1 or status_trade_ICPUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ICPUSDT:
                    close_trade("ICPUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ICPUSDT = 0
                    curr_num = curr_num - 1

            if "ICPUSDT SHORT" in dt and (status_trade_ICPUSDT == -1 or status_trade_ICPUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ICPUSDT:
                    close_trade("ICPUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ICPUSDT = 0
                    curr_num = curr_num - 1  




            if "TRBUSDT LONG" in dt and status_trade_TRBUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_TRBUSDT = bar
                open_trade("TRBUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_TRBUSDT = 1
                curr_num = curr_num + 1
                    
            if "TRBUSDT SHORT" in dt and status_trade_TRBUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_TRBUSDT = bar
                open_trade("TRBUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_TRBUSDT = -1
                curr_num = curr_num + 1

            if ("TRBUSDT end of trade" in dt) and (status_trade_TRBUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_TRBUSDT:
                    close_trade("TRBUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_TRBUSDT = 0
                    curr_num = curr_num - 1

            if ("TRBUSDT end of trade" in dt) and (status_trade_TRBUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_TRBUSDT:
                    close_trade("TRBUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_TRBUSDT = 0
                    curr_num = curr_num - 1


            if "TRBUSDT LONG" in dt and (status_trade_TRBUSDT == -1 or status_trade_TRBUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_TRBUSDT:
                    close_trade("TRBUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_TRBUSDT = 0
                    curr_num = curr_num - 1

            if "TRBUSDT SHORT" in dt and (status_trade_TRBUSDT == -1 or status_trade_TRBUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_TRBUSDT:
                    close_trade("TRBUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_TRBUSDT = 0
                    curr_num = curr_num - 1  




            if "ETHUSDT LONG" in dt and status_trade_ETHUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ETHUSDT = bar
                open_trade("ETHUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ETHUSDT = 1
                curr_num = curr_num + 1
                    
            if "ETHUSDT SHORT" in dt and status_trade_ETHUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ETHUSDT = bar
                open_trade("ETHUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ETHUSDT = -1
                curr_num = curr_num + 1

            if ("ETHUSDT end of trade" in dt) and (status_trade_ETHUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ETHUSDT:
                    close_trade("ETHUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ETHUSDT = 0
                    curr_num = curr_num - 1

            if ("ETHUSDT end of trade" in dt) and (status_trade_ETHUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ETHUSDT:
                    close_trade("ETHUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ETHUSDT = 0
                    curr_num = curr_num - 1


            if "ETHUSDT LONG" in dt and (status_trade_ETHUSDT == -1 or status_trade_ETHUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ETHUSDT:
                    close_trade("ETHUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ETHUSDT = 0
                    curr_num = curr_num - 1

            if "ETHUSDT SHORT" in dt and (status_trade_ETHUSDT == -1 or status_trade_ETHUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ETHUSDT:
                    close_trade("ETHUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ETHUSDT = 0
                    curr_num = curr_num - 1  




            if "ETCUSDT LONG" in dt and status_trade_ETCUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ETCUSDT = bar
                open_trade("ETCUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ETCUSDT = 1
                curr_num = curr_num + 1
                    
            if "ETCUSDT SHORT" in dt and status_trade_ETCUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ETCUSDT = bar
                open_trade("ETCUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ETCUSDT = -1
                curr_num = curr_num + 1

            if ("ETCUSDT end of trade" in dt) and (status_trade_ETCUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ETCUSDT:
                    close_trade("ETCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ETCUSDT = 0
                    curr_num = curr_num - 1

            if ("ETCUSDT end of trade" in dt) and (status_trade_ETCUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ETCUSDT:
                    close_trade("ETCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ETCUSDT = 0
                    curr_num = curr_num - 1


            if "ETCUSDT LONG" in dt and (status_trade_ETCUSDT == -1 or status_trade_ETCUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ETCUSDT:
                    close_trade("ETCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ETCUSDT = 0
                    curr_num = curr_num - 1

            if "ETCUSDT SHORT" in dt and (status_trade_ETCUSDT == -1 or status_trade_ETCUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ETCUSDT:
                    close_trade("ETCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ETCUSDT = 0
                    curr_num = curr_num - 1  




            if "ATOMUSDT LONG" in dt and status_trade_ATOMUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ATOMUSDT = bar
                open_trade("ATOMUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ATOMUSDT = 1
                curr_num = curr_num + 1
                    
            if "ATOMUSDT SHORT" in dt and status_trade_ATOMUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ATOMUSDT = bar
                open_trade("ATOMUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ATOMUSDT = -1
                curr_num = curr_num + 1

            if ("ATOMUSDT end of trade" in dt) and (status_trade_ATOMUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ATOMUSDT:
                    close_trade("ATOMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ATOMUSDT = 0
                    curr_num = curr_num - 1

            if ("ATOMUSDT end of trade" in dt) and (status_trade_ATOMUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ATOMUSDT:
                    close_trade("ATOMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ATOMUSDT = 0
                    curr_num = curr_num - 1


            if "ATOMUSDT LONG" in dt and (status_trade_ATOMUSDT == -1 or status_trade_ATOMUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ATOMUSDT:
                    close_trade("ATOMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ATOMUSDT = 0
                    curr_num = curr_num - 1

            if "ATOMUSDT SHORT" in dt and (status_trade_ATOMUSDT == -1 or status_trade_ATOMUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ATOMUSDT:
                    close_trade("ATOMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ATOMUSDT = 0
                    curr_num = curr_num - 1  




            if "ONTUSDT LONG" in dt and status_trade_ONTUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ONTUSDT = bar
                open_trade("ONTUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ONTUSDT = 1
                curr_num = curr_num + 1
                    
            if "ONTUSDT SHORT" in dt and status_trade_ONTUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ONTUSDT = bar
                open_trade("ONTUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ONTUSDT = -1
                curr_num = curr_num + 1

            if ("ONTUSDT end of trade" in dt) and (status_trade_ONTUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ONTUSDT:
                    close_trade("ONTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ONTUSDT = 0
                    curr_num = curr_num - 1

            if ("ONTUSDT end of trade" in dt) and (status_trade_ONTUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ONTUSDT:
                    close_trade("ONTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ONTUSDT = 0
                    curr_num = curr_num - 1


            if "ONTUSDT LONG" in dt and (status_trade_ONTUSDT == -1 or status_trade_ONTUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ONTUSDT:
                    close_trade("ONTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ONTUSDT = 0
                    curr_num = curr_num - 1

            if "ONTUSDT SHORT" in dt and (status_trade_ONTUSDT == -1 or status_trade_ONTUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ONTUSDT:
                    close_trade("ONTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ONTUSDT = 0
                    curr_num = curr_num - 1  




            if "BATUSDT LONG" in dt and status_trade_BATUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BATUSDT = bar
                open_trade("BATUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BATUSDT = 1
                curr_num = curr_num + 1
                    
            if "BATUSDT SHORT" in dt and status_trade_BATUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BATUSDT = bar
                open_trade("BATUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BATUSDT = -1
                curr_num = curr_num + 1

            if ("BATUSDT end of trade" in dt) and (status_trade_BATUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BATUSDT:
                    close_trade("BATUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BATUSDT = 0
                    curr_num = curr_num - 1

            if ("BATUSDT end of trade" in dt) and (status_trade_BATUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BATUSDT:
                    close_trade("BATUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BATUSDT = 0
                    curr_num = curr_num - 1


            if "BATUSDT LONG" in dt and (status_trade_BATUSDT == -1 or status_trade_BATUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BATUSDT:
                    close_trade("BATUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BATUSDT = 0
                    curr_num = curr_num - 1

            if "BATUSDT SHORT" in dt and (status_trade_BATUSDT == -1 or status_trade_BATUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BATUSDT:
                    close_trade("BATUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BATUSDT = 0
                    curr_num = curr_num - 1  




            if "NEOUSDT LONG" in dt and status_trade_NEOUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_NEOUSDT = bar
                open_trade("NEOUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_NEOUSDT = 1
                curr_num = curr_num + 1
                    
            if "NEOUSDT SHORT" in dt and status_trade_NEOUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_NEOUSDT = bar
                open_trade("NEOUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_NEOUSDT = -1
                curr_num = curr_num + 1

            if ("NEOUSDT end of trade" in dt) and (status_trade_NEOUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_NEOUSDT:
                    close_trade("NEOUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_NEOUSDT = 0
                    curr_num = curr_num - 1

            if ("NEOUSDT end of trade" in dt) and (status_trade_NEOUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_NEOUSDT:
                    close_trade("NEOUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_NEOUSDT = 0
                    curr_num = curr_num - 1


            if "NEOUSDT LONG" in dt and (status_trade_NEOUSDT == -1 or status_trade_NEOUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_NEOUSDT:
                    close_trade("NEOUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_NEOUSDT = 0
                    curr_num = curr_num - 1

            if "NEOUSDT SHORT" in dt and (status_trade_NEOUSDT == -1 or status_trade_NEOUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_NEOUSDT:
                    close_trade("NEOUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_NEOUSDT = 0
                    curr_num = curr_num - 1  




            if "IOSTUSDT LONG" in dt and status_trade_IOSTUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_IOSTUSDT = bar
                open_trade("IOSTUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_IOSTUSDT = 1
                curr_num = curr_num + 1
                    
            if "IOSTUSDT SHORT" in dt and status_trade_IOSTUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_IOSTUSDT = bar
                open_trade("IOSTUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_IOSTUSDT = -1
                curr_num = curr_num + 1

            if ("IOSTUSDT end of trade" in dt) and (status_trade_IOSTUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_IOSTUSDT:
                    close_trade("IOSTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_IOSTUSDT = 0
                    curr_num = curr_num - 1

            if ("IOSTUSDT end of trade" in dt) and (status_trade_IOSTUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_IOSTUSDT:
                    close_trade("IOSTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_IOSTUSDT = 0
                    curr_num = curr_num - 1


            if "IOSTUSDT LONG" in dt and (status_trade_IOSTUSDT == -1 or status_trade_IOSTUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_IOSTUSDT:
                    close_trade("IOSTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_IOSTUSDT = 0
                    curr_num = curr_num - 1

            if "IOSTUSDT SHORT" in dt and (status_trade_IOSTUSDT == -1 or status_trade_IOSTUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_IOSTUSDT:
                    close_trade("IOSTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_IOSTUSDT = 0
                    curr_num = curr_num - 1  




            if "KNCUSDT LONG" in dt and status_trade_KNCUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_KNCUSDT = bar
                open_trade("KNCUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_KNCUSDT = 1
                curr_num = curr_num + 1
                    
            if "KNCUSDT SHORT" in dt and status_trade_KNCUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_KNCUSDT = bar
                open_trade("KNCUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_KNCUSDT = -1
                curr_num = curr_num + 1

            if ("KNCUSDT end of trade" in dt) and (status_trade_KNCUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_KNCUSDT:
                    close_trade("KNCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_KNCUSDT = 0
                    curr_num = curr_num - 1

            if ("KNCUSDT end of trade" in dt) and (status_trade_KNCUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_KNCUSDT:
                    close_trade("KNCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_KNCUSDT = 0
                    curr_num = curr_num - 1


            if "KNCUSDT LONG" in dt and (status_trade_KNCUSDT == -1 or status_trade_KNCUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_KNCUSDT:
                    close_trade("KNCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_KNCUSDT = 0
                    curr_num = curr_num - 1

            if "KNCUSDT SHORT" in dt and (status_trade_KNCUSDT == -1 or status_trade_KNCUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_KNCUSDT:
                    close_trade("KNCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_KNCUSDT = 0
                    curr_num = curr_num - 1  




            if "SXPUSDT LONG" in dt and status_trade_SXPUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_SXPUSDT = bar
                open_trade("SXPUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_SXPUSDT = 1
                curr_num = curr_num + 1
                    
            if "SXPUSDT SHORT" in dt and status_trade_SXPUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_SXPUSDT = bar
                open_trade("SXPUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_SXPUSDT = -1
                curr_num = curr_num + 1

            if ("SXPUSDT end of trade" in dt) and (status_trade_SXPUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SXPUSDT:
                    close_trade("SXPUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SXPUSDT = 0
                    curr_num = curr_num - 1

            if ("SXPUSDT end of trade" in dt) and (status_trade_SXPUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SXPUSDT:
                    close_trade("SXPUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SXPUSDT = 0
                    curr_num = curr_num - 1


            if "SXPUSDT LONG" in dt and (status_trade_SXPUSDT == -1 or status_trade_SXPUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SXPUSDT:
                    close_trade("SXPUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SXPUSDT = 0
                    curr_num = curr_num - 1

            if "SXPUSDT SHORT" in dt and (status_trade_SXPUSDT == -1 or status_trade_SXPUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SXPUSDT:
                    close_trade("SXPUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SXPUSDT = 0
                    curr_num = curr_num - 1  




            if "ZILUSDT LONG" in dt and status_trade_ZILUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ZILUSDT = bar
                open_trade("ZILUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ZILUSDT = 1
                curr_num = curr_num + 1
                    
            if "ZILUSDT SHORT" in dt and status_trade_ZILUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ZILUSDT = bar
                open_trade("ZILUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ZILUSDT = -1
                curr_num = curr_num + 1

            if ("ZILUSDT end of trade" in dt) and (status_trade_ZILUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ZILUSDT:
                    close_trade("ZILUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ZILUSDT = 0
                    curr_num = curr_num - 1

            if ("ZILUSDT end of trade" in dt) and (status_trade_ZILUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ZILUSDT:
                    close_trade("ZILUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ZILUSDT = 0
                    curr_num = curr_num - 1


            if "ZILUSDT LONG" in dt and (status_trade_ZILUSDT == -1 or status_trade_ZILUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ZILUSDT:
                    close_trade("ZILUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ZILUSDT = 0
                    curr_num = curr_num - 1

            if "ZILUSDT SHORT" in dt and (status_trade_ZILUSDT == -1 or status_trade_ZILUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ZILUSDT:
                    close_trade("ZILUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ZILUSDT = 0
                    curr_num = curr_num - 1  




            if "BANDUSDT LONG" in dt and status_trade_BANDUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BANDUSDT = bar
                open_trade("BANDUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BANDUSDT = 1
                curr_num = curr_num + 1
                    
            if "BANDUSDT SHORT" in dt and status_trade_BANDUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BANDUSDT = bar
                open_trade("BANDUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BANDUSDT = -1
                curr_num = curr_num + 1

            if ("BANDUSDT end of trade" in dt) and (status_trade_BANDUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BANDUSDT:
                    close_trade("BANDUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BANDUSDT = 0
                    curr_num = curr_num - 1

            if ("BANDUSDT end of trade" in dt) and (status_trade_BANDUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BANDUSDT:
                    close_trade("BANDUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BANDUSDT = 0
                    curr_num = curr_num - 1


            if "BANDUSDT LONG" in dt and (status_trade_BANDUSDT == -1 or status_trade_BANDUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BANDUSDT:
                    close_trade("BANDUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BANDUSDT = 0
                    curr_num = curr_num - 1

            if "BANDUSDT SHORT" in dt and (status_trade_BANDUSDT == -1 or status_trade_BANDUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BANDUSDT:
                    close_trade("BANDUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BANDUSDT = 0
                    curr_num = curr_num - 1  




            if "MKRUSDT LONG" in dt and status_trade_MKRUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_MKRUSDT = bar
                open_trade("MKRUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_MKRUSDT = 1
                curr_num = curr_num + 1
                    
            if "MKRUSDT SHORT" in dt and status_trade_MKRUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_MKRUSDT = bar
                open_trade("MKRUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_MKRUSDT = -1
                curr_num = curr_num + 1

            if ("MKRUSDT end of trade" in dt) and (status_trade_MKRUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_MKRUSDT:
                    close_trade("MKRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_MKRUSDT = 0
                    curr_num = curr_num - 1

            if ("MKRUSDT end of trade" in dt) and (status_trade_MKRUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_MKRUSDT:
                    close_trade("MKRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_MKRUSDT = 0
                    curr_num = curr_num - 1


            if "MKRUSDT LONG" in dt and (status_trade_MKRUSDT == -1 or status_trade_MKRUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_MKRUSDT:
                    close_trade("MKRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_MKRUSDT = 0
                    curr_num = curr_num - 1

            if "MKRUSDT SHORT" in dt and (status_trade_MKRUSDT == -1 or status_trade_MKRUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_MKRUSDT:
                    close_trade("MKRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_MKRUSDT = 0
                    curr_num = curr_num - 1  




            if "DEFIUSDT LONG" in dt and status_trade_DEFIUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_DEFIUSDT = bar
                open_trade("DEFIUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_DEFIUSDT = 1
                curr_num = curr_num + 1
                    
            if "DEFIUSDT SHORT" in dt and status_trade_DEFIUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_DEFIUSDT = bar
                open_trade("DEFIUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_DEFIUSDT = -1
                curr_num = curr_num + 1

            if ("DEFIUSDT end of trade" in dt) and (status_trade_DEFIUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DEFIUSDT:
                    close_trade("DEFIUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DEFIUSDT = 0
                    curr_num = curr_num - 1

            if ("DEFIUSDT end of trade" in dt) and (status_trade_DEFIUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DEFIUSDT:
                    close_trade("DEFIUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DEFIUSDT = 0
                    curr_num = curr_num - 1


            if "DEFIUSDT LONG" in dt and (status_trade_DEFIUSDT == -1 or status_trade_DEFIUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DEFIUSDT:
                    close_trade("DEFIUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DEFIUSDT = 0
                    curr_num = curr_num - 1

            if "DEFIUSDT SHORT" in dt and (status_trade_DEFIUSDT == -1 or status_trade_DEFIUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DEFIUSDT:
                    close_trade("DEFIUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DEFIUSDT = 0
                    curr_num = curr_num - 1  




            if "BALUSDT LONG" in dt and status_trade_BALUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BALUSDT = bar
                open_trade("BALUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BALUSDT = 1
                curr_num = curr_num + 1
                    
            if "BALUSDT SHORT" in dt and status_trade_BALUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BALUSDT = bar
                open_trade("BALUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BALUSDT = -1
                curr_num = curr_num + 1

            if ("BALUSDT end of trade" in dt) and (status_trade_BALUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BALUSDT:
                    close_trade("BALUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BALUSDT = 0
                    curr_num = curr_num - 1

            if ("BALUSDT end of trade" in dt) and (status_trade_BALUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BALUSDT:
                    close_trade("BALUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BALUSDT = 0
                    curr_num = curr_num - 1


            if "BALUSDT LONG" in dt and (status_trade_BALUSDT == -1 or status_trade_BALUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BALUSDT:
                    close_trade("BALUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BALUSDT = 0
                    curr_num = curr_num - 1

            if "BALUSDT SHORT" in dt and (status_trade_BALUSDT == -1 or status_trade_BALUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BALUSDT:
                    close_trade("BALUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BALUSDT = 0
                    curr_num = curr_num - 1  




            if "CRVUSDT LONG" in dt and status_trade_CRVUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_CRVUSDT = bar
                open_trade("CRVUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_CRVUSDT = 1
                curr_num = curr_num + 1
                    
            if "CRVUSDT SHORT" in dt and status_trade_CRVUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_CRVUSDT = bar
                open_trade("CRVUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_CRVUSDT = -1
                curr_num = curr_num + 1

            if ("CRVUSDT end of trade" in dt) and (status_trade_CRVUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CRVUSDT:
                    close_trade("CRVUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CRVUSDT = 0
                    curr_num = curr_num - 1

            if ("CRVUSDT end of trade" in dt) and (status_trade_CRVUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CRVUSDT:
                    close_trade("CRVUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CRVUSDT = 0
                    curr_num = curr_num - 1


            if "CRVUSDT LONG" in dt and (status_trade_CRVUSDT == -1 or status_trade_CRVUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CRVUSDT:
                    close_trade("CRVUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CRVUSDT = 0
                    curr_num = curr_num - 1

            if "CRVUSDT SHORT" in dt and (status_trade_CRVUSDT == -1 or status_trade_CRVUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CRVUSDT:
                    close_trade("CRVUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CRVUSDT = 0
                    curr_num = curr_num - 1  




            if "EGLDUSDT LONG" in dt and status_trade_EGLDUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_EGLDUSDT = bar
                open_trade("EGLDUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_EGLDUSDT = 1
                curr_num = curr_num + 1
                    
            if "EGLDUSDT SHORT" in dt and status_trade_EGLDUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_EGLDUSDT = bar
                open_trade("EGLDUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_EGLDUSDT = -1
                curr_num = curr_num + 1

            if ("EGLDUSDT end of trade" in dt) and (status_trade_EGLDUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_EGLDUSDT:
                    close_trade("EGLDUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_EGLDUSDT = 0
                    curr_num = curr_num - 1

            if ("EGLDUSDT end of trade" in dt) and (status_trade_EGLDUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_EGLDUSDT:
                    close_trade("EGLDUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_EGLDUSDT = 0
                    curr_num = curr_num - 1


            if "EGLDUSDT LONG" in dt and (status_trade_EGLDUSDT == -1 or status_trade_EGLDUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_EGLDUSDT:
                    close_trade("EGLDUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_EGLDUSDT = 0
                    curr_num = curr_num - 1

            if "EGLDUSDT SHORT" in dt and (status_trade_EGLDUSDT == -1 or status_trade_EGLDUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_EGLDUSDT:
                    close_trade("EGLDUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_EGLDUSDT = 0
                    curr_num = curr_num - 1  




            if "ICXUSDT LONG" in dt and status_trade_ICXUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ICXUSDT = bar
                open_trade("ICXUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ICXUSDT = 1
                curr_num = curr_num + 1
                    
            if "ICXUSDT SHORT" in dt and status_trade_ICXUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ICXUSDT = bar
                open_trade("ICXUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ICXUSDT = -1
                curr_num = curr_num + 1

            if ("ICXUSDT end of trade" in dt) and (status_trade_ICXUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ICXUSDT:
                    close_trade("ICXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ICXUSDT = 0
                    curr_num = curr_num - 1

            if ("ICXUSDT end of trade" in dt) and (status_trade_ICXUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ICXUSDT:
                    close_trade("ICXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ICXUSDT = 0
                    curr_num = curr_num - 1


            if "ICXUSDT LONG" in dt and (status_trade_ICXUSDT == -1 or status_trade_ICXUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ICXUSDT:
                    close_trade("ICXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ICXUSDT = 0
                    curr_num = curr_num - 1

            if "ICXUSDT SHORT" in dt and (status_trade_ICXUSDT == -1 or status_trade_ICXUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ICXUSDT:
                    close_trade("ICXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ICXUSDT = 0
                    curr_num = curr_num - 1  




            if "HNTUSDT LONG" in dt and status_trade_HNTUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_HNTUSDT = bar
                open_trade("HNTUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_HNTUSDT = 1
                curr_num = curr_num + 1
                    
            if "HNTUSDT SHORT" in dt and status_trade_HNTUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_HNTUSDT = bar
                open_trade("HNTUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_HNTUSDT = -1
                curr_num = curr_num + 1

            if ("HNTUSDT end of trade" in dt) and (status_trade_HNTUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_HNTUSDT:
                    close_trade("HNTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_HNTUSDT = 0
                    curr_num = curr_num - 1

            if ("HNTUSDT end of trade" in dt) and (status_trade_HNTUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_HNTUSDT:
                    close_trade("HNTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_HNTUSDT = 0
                    curr_num = curr_num - 1


            if "HNTUSDT LONG" in dt and (status_trade_HNTUSDT == -1 or status_trade_HNTUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_HNTUSDT:
                    close_trade("HNTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_HNTUSDT = 0
                    curr_num = curr_num - 1

            if "HNTUSDT SHORT" in dt and (status_trade_HNTUSDT == -1 or status_trade_HNTUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_HNTUSDT:
                    close_trade("HNTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_HNTUSDT = 0
                    curr_num = curr_num - 1  




            if "FLMUSDT LONG" in dt and status_trade_FLMUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_FLMUSDT = bar
                open_trade("FLMUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_FLMUSDT = 1
                curr_num = curr_num + 1
                    
            if "FLMUSDT SHORT" in dt and status_trade_FLMUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_FLMUSDT = bar
                open_trade("FLMUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_FLMUSDT = -1
                curr_num = curr_num + 1

            if ("FLMUSDT end of trade" in dt) and (status_trade_FLMUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_FLMUSDT:
                    close_trade("FLMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_FLMUSDT = 0
                    curr_num = curr_num - 1

            if ("FLMUSDT end of trade" in dt) and (status_trade_FLMUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_FLMUSDT:
                    close_trade("FLMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_FLMUSDT = 0
                    curr_num = curr_num - 1


            if "FLMUSDT LONG" in dt and (status_trade_FLMUSDT == -1 or status_trade_FLMUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_FLMUSDT:
                    close_trade("FLMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_FLMUSDT = 0
                    curr_num = curr_num - 1

            if "FLMUSDT SHORT" in dt and (status_trade_FLMUSDT == -1 or status_trade_FLMUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_FLMUSDT:
                    close_trade("FLMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_FLMUSDT = 0
                    curr_num = curr_num - 1  




            if "NEARUSDT LONG" in dt and status_trade_NEARUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_NEARUSDT = bar
                open_trade("NEARUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_NEARUSDT = 1
                curr_num = curr_num + 1
                    
            if "NEARUSDT SHORT" in dt and status_trade_NEARUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_NEARUSDT = bar
                open_trade("NEARUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_NEARUSDT = -1
                curr_num = curr_num + 1

            if ("NEARUSDT end of trade" in dt) and (status_trade_NEARUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_NEARUSDT:
                    close_trade("NEARUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_NEARUSDT = 0
                    curr_num = curr_num - 1

            if ("NEARUSDT end of trade" in dt) and (status_trade_NEARUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_NEARUSDT:
                    close_trade("NEARUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_NEARUSDT = 0
                    curr_num = curr_num - 1


            if "NEARUSDT LONG" in dt and (status_trade_NEARUSDT == -1 or status_trade_NEARUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_NEARUSDT:
                    close_trade("NEARUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_NEARUSDT = 0
                    curr_num = curr_num - 1

            if "NEARUSDT SHORT" in dt and (status_trade_NEARUSDT == -1 or status_trade_NEARUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_NEARUSDT:
                    close_trade("NEARUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_NEARUSDT = 0
                    curr_num = curr_num - 1  




            if "RSRUSDT LONG" in dt and status_trade_RSRUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_RSRUSDT = bar
                open_trade("RSRUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_RSRUSDT = 1
                curr_num = curr_num + 1
                    
            if "RSRUSDT SHORT" in dt and status_trade_RSRUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_RSRUSDT = bar
                open_trade("RSRUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_RSRUSDT = -1
                curr_num = curr_num + 1

            if ("RSRUSDT end of trade" in dt) and (status_trade_RSRUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RSRUSDT:
                    close_trade("RSRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RSRUSDT = 0
                    curr_num = curr_num - 1

            if ("RSRUSDT end of trade" in dt) and (status_trade_RSRUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RSRUSDT:
                    close_trade("RSRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RSRUSDT = 0
                    curr_num = curr_num - 1


            if "RSRUSDT LONG" in dt and (status_trade_RSRUSDT == -1 or status_trade_RSRUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RSRUSDT:
                    close_trade("RSRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RSRUSDT = 0
                    curr_num = curr_num - 1

            if "RSRUSDT SHORT" in dt and (status_trade_RSRUSDT == -1 or status_trade_RSRUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RSRUSDT:
                    close_trade("RSRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RSRUSDT = 0
                    curr_num = curr_num - 1  




            if "OCEANUSDT LONG" in dt and status_trade_OCEANUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_OCEANUSDT = bar
                open_trade("OCEANUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_OCEANUSDT = 1
                curr_num = curr_num + 1
                    
            if "OCEANUSDT SHORT" in dt and status_trade_OCEANUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_OCEANUSDT = bar
                open_trade("OCEANUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_OCEANUSDT = -1
                curr_num = curr_num + 1

            if ("OCEANUSDT end of trade" in dt) and (status_trade_OCEANUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_OCEANUSDT:
                    close_trade("OCEANUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_OCEANUSDT = 0
                    curr_num = curr_num - 1

            if ("OCEANUSDT end of trade" in dt) and (status_trade_OCEANUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_OCEANUSDT:
                    close_trade("OCEANUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_OCEANUSDT = 0
                    curr_num = curr_num - 1


            if "OCEANUSDT LONG" in dt and (status_trade_OCEANUSDT == -1 or status_trade_OCEANUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_OCEANUSDT:
                    close_trade("OCEANUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_OCEANUSDT = 0
                    curr_num = curr_num - 1

            if "OCEANUSDT SHORT" in dt and (status_trade_OCEANUSDT == -1 or status_trade_OCEANUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_OCEANUSDT:
                    close_trade("OCEANUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_OCEANUSDT = 0
                    curr_num = curr_num - 1  




            if "CVCUSDT LONG" in dt and status_trade_CVCUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_CVCUSDT = bar
                open_trade("CVCUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_CVCUSDT = 1
                curr_num = curr_num + 1
                    
            if "CVCUSDT SHORT" in dt and status_trade_CVCUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_CVCUSDT = bar
                open_trade("CVCUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_CVCUSDT = -1
                curr_num = curr_num + 1

            if ("CVCUSDT end of trade" in dt) and (status_trade_CVCUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CVCUSDT:
                    close_trade("CVCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CVCUSDT = 0
                    curr_num = curr_num - 1

            if ("CVCUSDT end of trade" in dt) and (status_trade_CVCUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CVCUSDT:
                    close_trade("CVCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CVCUSDT = 0
                    curr_num = curr_num - 1


            if "CVCUSDT LONG" in dt and (status_trade_CVCUSDT == -1 or status_trade_CVCUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CVCUSDT:
                    close_trade("CVCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CVCUSDT = 0
                    curr_num = curr_num - 1

            if "CVCUSDT SHORT" in dt and (status_trade_CVCUSDT == -1 or status_trade_CVCUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CVCUSDT:
                    close_trade("CVCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CVCUSDT = 0
                    curr_num = curr_num - 1  




            if "AXSUSDT LONG" in dt and status_trade_AXSUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_AXSUSDT = bar
                open_trade("AXSUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_AXSUSDT = 1
                curr_num = curr_num + 1
                    
            if "AXSUSDT SHORT" in dt and status_trade_AXSUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_AXSUSDT = bar
                open_trade("AXSUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_AXSUSDT = -1
                curr_num = curr_num + 1

            if ("AXSUSDT end of trade" in dt) and (status_trade_AXSUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_AXSUSDT:
                    close_trade("AXSUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_AXSUSDT = 0
                    curr_num = curr_num - 1

            if ("AXSUSDT end of trade" in dt) and (status_trade_AXSUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_AXSUSDT:
                    close_trade("AXSUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_AXSUSDT = 0
                    curr_num = curr_num - 1


            if "AXSUSDT LONG" in dt and (status_trade_AXSUSDT == -1 or status_trade_AXSUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_AXSUSDT:
                    close_trade("AXSUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_AXSUSDT = 0
                    curr_num = curr_num - 1

            if "AXSUSDT SHORT" in dt and (status_trade_AXSUSDT == -1 or status_trade_AXSUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_AXSUSDT:
                    close_trade("AXSUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_AXSUSDT = 0
                    curr_num = curr_num - 1  




            if "ALPHAUSDT LONG" in dt and status_trade_ALPHAUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ALPHAUSDT = bar
                open_trade("ALPHAUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ALPHAUSDT = 1
                curr_num = curr_num + 1
                    
            if "ALPHAUSDT SHORT" in dt and status_trade_ALPHAUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ALPHAUSDT = bar
                open_trade("ALPHAUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ALPHAUSDT = -1
                curr_num = curr_num + 1

            if ("ALPHAUSDT end of trade" in dt) and (status_trade_ALPHAUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ALPHAUSDT:
                    close_trade("ALPHAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ALPHAUSDT = 0
                    curr_num = curr_num - 1

            if ("ALPHAUSDT end of trade" in dt) and (status_trade_ALPHAUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ALPHAUSDT:
                    close_trade("ALPHAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ALPHAUSDT = 0
                    curr_num = curr_num - 1


            if "ALPHAUSDT LONG" in dt and (status_trade_ALPHAUSDT == -1 or status_trade_ALPHAUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ALPHAUSDT:
                    close_trade("ALPHAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ALPHAUSDT = 0
                    curr_num = curr_num - 1

            if "ALPHAUSDT SHORT" in dt and (status_trade_ALPHAUSDT == -1 or status_trade_ALPHAUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ALPHAUSDT:
                    close_trade("ALPHAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ALPHAUSDT = 0
                    curr_num = curr_num - 1  




            if "SKLUSDT LONG" in dt and status_trade_SKLUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_SKLUSDT = bar
                open_trade("SKLUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_SKLUSDT = 1
                curr_num = curr_num + 1
                    
            if "SKLUSDT SHORT" in dt and status_trade_SKLUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_SKLUSDT = bar
                open_trade("SKLUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_SKLUSDT = -1
                curr_num = curr_num + 1

            if ("SKLUSDT end of trade" in dt) and (status_trade_SKLUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SKLUSDT:
                    close_trade("SKLUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SKLUSDT = 0
                    curr_num = curr_num - 1

            if ("SKLUSDT end of trade" in dt) and (status_trade_SKLUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SKLUSDT:
                    close_trade("SKLUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SKLUSDT = 0
                    curr_num = curr_num - 1


            if "SKLUSDT LONG" in dt and (status_trade_SKLUSDT == -1 or status_trade_SKLUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SKLUSDT:
                    close_trade("SKLUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SKLUSDT = 0
                    curr_num = curr_num - 1

            if "SKLUSDT SHORT" in dt and (status_trade_SKLUSDT == -1 or status_trade_SKLUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SKLUSDT:
                    close_trade("SKLUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SKLUSDT = 0
                    curr_num = curr_num - 1  




            if "GRTUSDT LONG" in dt and status_trade_GRTUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_GRTUSDT = bar
                open_trade("GRTUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_GRTUSDT = 1
                curr_num = curr_num + 1
                    
            if "GRTUSDT SHORT" in dt and status_trade_GRTUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_GRTUSDT = bar
                open_trade("GRTUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_GRTUSDT = -1
                curr_num = curr_num + 1

            if ("GRTUSDT end of trade" in dt) and (status_trade_GRTUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_GRTUSDT:
                    close_trade("GRTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_GRTUSDT = 0
                    curr_num = curr_num - 1

            if ("GRTUSDT end of trade" in dt) and (status_trade_GRTUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_GRTUSDT:
                    close_trade("GRTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_GRTUSDT = 0
                    curr_num = curr_num - 1


            if "GRTUSDT LONG" in dt and (status_trade_GRTUSDT == -1 or status_trade_GRTUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_GRTUSDT:
                    close_trade("GRTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_GRTUSDT = 0
                    curr_num = curr_num - 1

            if "GRTUSDT SHORT" in dt and (status_trade_GRTUSDT == -1 or status_trade_GRTUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_GRTUSDT:
                    close_trade("GRTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_GRTUSDT = 0
                    curr_num = curr_num - 1  




            if "CHZUSDT LONG" in dt and status_trade_CHZUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_CHZUSDT = bar
                open_trade("CHZUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_CHZUSDT = 1
                curr_num = curr_num + 1
                    
            if "CHZUSDT SHORT" in dt and status_trade_CHZUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_CHZUSDT = bar
                open_trade("CHZUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_CHZUSDT = -1
                curr_num = curr_num + 1

            if ("CHZUSDT end of trade" in dt) and (status_trade_CHZUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CHZUSDT:
                    close_trade("CHZUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CHZUSDT = 0
                    curr_num = curr_num - 1

            if ("CHZUSDT end of trade" in dt) and (status_trade_CHZUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CHZUSDT:
                    close_trade("CHZUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CHZUSDT = 0
                    curr_num = curr_num - 1


            if "CHZUSDT LONG" in dt and (status_trade_CHZUSDT == -1 or status_trade_CHZUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CHZUSDT:
                    close_trade("CHZUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CHZUSDT = 0
                    curr_num = curr_num - 1

            if "CHZUSDT SHORT" in dt and (status_trade_CHZUSDT == -1 or status_trade_CHZUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CHZUSDT:
                    close_trade("CHZUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CHZUSDT = 0
                    curr_num = curr_num - 1  




            if "LITUSDT LONG" in dt and status_trade_LITUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_LITUSDT = bar
                open_trade("LITUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_LITUSDT = 1
                curr_num = curr_num + 1
                    
            if "LITUSDT SHORT" in dt and status_trade_LITUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_LITUSDT = bar
                open_trade("LITUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_LITUSDT = -1
                curr_num = curr_num + 1

            if ("LITUSDT end of trade" in dt) and (status_trade_LITUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LITUSDT:
                    close_trade("LITUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LITUSDT = 0
                    curr_num = curr_num - 1

            if ("LITUSDT end of trade" in dt) and (status_trade_LITUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LITUSDT:
                    close_trade("LITUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LITUSDT = 0
                    curr_num = curr_num - 1


            if "LITUSDT LONG" in dt and (status_trade_LITUSDT == -1 or status_trade_LITUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LITUSDT:
                    close_trade("LITUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LITUSDT = 0
                    curr_num = curr_num - 1

            if "LITUSDT SHORT" in dt and (status_trade_LITUSDT == -1 or status_trade_LITUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LITUSDT:
                    close_trade("LITUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LITUSDT = 0
                    curr_num = curr_num - 1  




            if "REEFUSDT LONG" in dt and status_trade_REEFUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_REEFUSDT = bar
                open_trade("REEFUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_REEFUSDT = 1
                curr_num = curr_num + 1
                    
            if "REEFUSDT SHORT" in dt and status_trade_REEFUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_REEFUSDT = bar
                open_trade("REEFUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_REEFUSDT = -1
                curr_num = curr_num + 1

            if ("REEFUSDT end of trade" in dt) and (status_trade_REEFUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_REEFUSDT:
                    close_trade("REEFUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_REEFUSDT = 0
                    curr_num = curr_num - 1

            if ("REEFUSDT end of trade" in dt) and (status_trade_REEFUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_REEFUSDT:
                    close_trade("REEFUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_REEFUSDT = 0
                    curr_num = curr_num - 1


            if "REEFUSDT LONG" in dt and (status_trade_REEFUSDT == -1 or status_trade_REEFUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_REEFUSDT:
                    close_trade("REEFUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_REEFUSDT = 0
                    curr_num = curr_num - 1

            if "REEFUSDT SHORT" in dt and (status_trade_REEFUSDT == -1 or status_trade_REEFUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_REEFUSDT:
                    close_trade("REEFUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_REEFUSDT = 0
                    curr_num = curr_num - 1  




            if "ARPAUSDT LONG" in dt and status_trade_ARPAUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ARPAUSDT = bar
                open_trade("ARPAUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ARPAUSDT = 1
                curr_num = curr_num + 1
                    
            if "ARPAUSDT SHORT" in dt and status_trade_ARPAUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ARPAUSDT = bar
                open_trade("ARPAUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ARPAUSDT = -1
                curr_num = curr_num + 1

            if ("ARPAUSDT end of trade" in dt) and (status_trade_ARPAUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ARPAUSDT:
                    close_trade("ARPAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ARPAUSDT = 0
                    curr_num = curr_num - 1

            if ("ARPAUSDT end of trade" in dt) and (status_trade_ARPAUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ARPAUSDT:
                    close_trade("ARPAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ARPAUSDT = 0
                    curr_num = curr_num - 1


            if "ARPAUSDT LONG" in dt and (status_trade_ARPAUSDT == -1 or status_trade_ARPAUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ARPAUSDT:
                    close_trade("ARPAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ARPAUSDT = 0
                    curr_num = curr_num - 1

            if "ARPAUSDT SHORT" in dt and (status_trade_ARPAUSDT == -1 or status_trade_ARPAUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ARPAUSDT:
                    close_trade("ARPAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ARPAUSDT = 0
                    curr_num = curr_num - 1  




            if "CELOUSDT LONG" in dt and status_trade_CELOUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_CELOUSDT = bar
                open_trade("CELOUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_CELOUSDT = 1
                curr_num = curr_num + 1
                    
            if "CELOUSDT SHORT" in dt and status_trade_CELOUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_CELOUSDT = bar
                open_trade("CELOUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_CELOUSDT = -1
                curr_num = curr_num + 1

            if ("CELOUSDT end of trade" in dt) and (status_trade_CELOUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CELOUSDT:
                    close_trade("CELOUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CELOUSDT = 0
                    curr_num = curr_num - 1

            if ("CELOUSDT end of trade" in dt) and (status_trade_CELOUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CELOUSDT:
                    close_trade("CELOUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CELOUSDT = 0
                    curr_num = curr_num - 1


            if "CELOUSDT LONG" in dt and (status_trade_CELOUSDT == -1 or status_trade_CELOUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CELOUSDT:
                    close_trade("CELOUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CELOUSDT = 0
                    curr_num = curr_num - 1

            if "CELOUSDT SHORT" in dt and (status_trade_CELOUSDT == -1 or status_trade_CELOUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CELOUSDT:
                    close_trade("CELOUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CELOUSDT = 0
                    curr_num = curr_num - 1  




            if "CELRUSDT LONG" in dt and status_trade_CELRUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_CELRUSDT = bar
                open_trade("CELRUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_CELRUSDT = 1
                curr_num = curr_num + 1
                    
            if "CELRUSDT SHORT" in dt and status_trade_CELRUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_CELRUSDT = bar
                open_trade("CELRUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_CELRUSDT = -1
                curr_num = curr_num + 1

            if ("CELRUSDT end of trade" in dt) and (status_trade_CELRUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CELRUSDT:
                    close_trade("CELRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CELRUSDT = 0
                    curr_num = curr_num - 1

            if ("CELRUSDT end of trade" in dt) and (status_trade_CELRUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CELRUSDT:
                    close_trade("CELRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CELRUSDT = 0
                    curr_num = curr_num - 1


            if "CELRUSDT LONG" in dt and (status_trade_CELRUSDT == -1 or status_trade_CELRUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CELRUSDT:
                    close_trade("CELRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CELRUSDT = 0
                    curr_num = curr_num - 1

            if "CELRUSDT SHORT" in dt and (status_trade_CELRUSDT == -1 or status_trade_CELRUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CELRUSDT:
                    close_trade("CELRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CELRUSDT = 0
                    curr_num = curr_num - 1  




            if "GALAUSDT LONG" in dt and status_trade_GALAUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_GALAUSDT = bar
                open_trade("GALAUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_GALAUSDT = 1
                curr_num = curr_num + 1
                    
            if "GALAUSDT SHORT" in dt and status_trade_GALAUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_GALAUSDT = bar
                open_trade("GALAUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_GALAUSDT = -1
                curr_num = curr_num + 1

            if ("GALAUSDT end of trade" in dt) and (status_trade_GALAUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_GALAUSDT:
                    close_trade("GALAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_GALAUSDT = 0
                    curr_num = curr_num - 1

            if ("GALAUSDT end of trade" in dt) and (status_trade_GALAUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_GALAUSDT:
                    close_trade("GALAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_GALAUSDT = 0
                    curr_num = curr_num - 1


            if "GALAUSDT LONG" in dt and (status_trade_GALAUSDT == -1 or status_trade_GALAUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_GALAUSDT:
                    close_trade("GALAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_GALAUSDT = 0
                    curr_num = curr_num - 1

            if "GALAUSDT SHORT" in dt and (status_trade_GALAUSDT == -1 or status_trade_GALAUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_GALAUSDT:
                    close_trade("GALAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_GALAUSDT = 0
                    curr_num = curr_num - 1  




            if "RAYUSDT LONG" in dt and status_trade_RAYUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_RAYUSDT = bar
                open_trade("RAYUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_RAYUSDT = 1
                curr_num = curr_num + 1
                    
            if "RAYUSDT SHORT" in dt and status_trade_RAYUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_RAYUSDT = bar
                open_trade("RAYUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_RAYUSDT = -1
                curr_num = curr_num + 1

            if ("RAYUSDT end of trade" in dt) and (status_trade_RAYUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RAYUSDT:
                    close_trade("RAYUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RAYUSDT = 0
                    curr_num = curr_num - 1

            if ("RAYUSDT end of trade" in dt) and (status_trade_RAYUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RAYUSDT:
                    close_trade("RAYUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RAYUSDT = 0
                    curr_num = curr_num - 1


            if "RAYUSDT LONG" in dt and (status_trade_RAYUSDT == -1 or status_trade_RAYUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RAYUSDT:
                    close_trade("RAYUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RAYUSDT = 0
                    curr_num = curr_num - 1

            if "RAYUSDT SHORT" in dt and (status_trade_RAYUSDT == -1 or status_trade_RAYUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RAYUSDT:
                    close_trade("RAYUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RAYUSDT = 0
                    curr_num = curr_num - 1  




            if "TLMUSDT LONG" in dt and status_trade_TLMUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_TLMUSDT = bar
                open_trade("TLMUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_TLMUSDT = 1
                curr_num = curr_num + 1
                    
            if "TLMUSDT SHORT" in dt and status_trade_TLMUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_TLMUSDT = bar
                open_trade("TLMUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_TLMUSDT = -1
                curr_num = curr_num + 1

            if ("TLMUSDT end of trade" in dt) and (status_trade_TLMUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_TLMUSDT:
                    close_trade("TLMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_TLMUSDT = 0
                    curr_num = curr_num - 1

            if ("TLMUSDT end of trade" in dt) and (status_trade_TLMUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_TLMUSDT:
                    close_trade("TLMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_TLMUSDT = 0
                    curr_num = curr_num - 1


            if "TLMUSDT LONG" in dt and (status_trade_TLMUSDT == -1 or status_trade_TLMUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_TLMUSDT:
                    close_trade("TLMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_TLMUSDT = 0
                    curr_num = curr_num - 1

            if "TLMUSDT SHORT" in dt and (status_trade_TLMUSDT == -1 or status_trade_TLMUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_TLMUSDT:
                    close_trade("TLMUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_TLMUSDT = 0
                    curr_num = curr_num - 1  




            if "BTCUSDT LONG" in dt and status_trade_BTCUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BTCUSDT = bar
                open_trade("BTCUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BTCUSDT = 1
                curr_num = curr_num + 1
                    
            if "BTCUSDT SHORT" in dt and status_trade_BTCUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BTCUSDT = bar
                open_trade("BTCUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BTCUSDT = -1
                curr_num = curr_num + 1

            if ("BTCUSDT end of trade" in dt) and (status_trade_BTCUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BTCUSDT:
                    close_trade("BTCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BTCUSDT = 0
                    curr_num = curr_num - 1

            if ("BTCUSDT end of trade" in dt) and (status_trade_BTCUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BTCUSDT:
                    close_trade("BTCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BTCUSDT = 0
                    curr_num = curr_num - 1


            if "BTCUSDT LONG" in dt and (status_trade_BTCUSDT == -1 or status_trade_BTCUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BTCUSDT:
                    close_trade("BTCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BTCUSDT = 0
                    curr_num = curr_num - 1

            if "BTCUSDT SHORT" in dt and (status_trade_BTCUSDT == -1 or status_trade_BTCUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BTCUSDT:
                    close_trade("BTCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BTCUSDT = 0
                    curr_num = curr_num - 1  




            if "SANDUSDT LONG" in dt and status_trade_SANDUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_SANDUSDT = bar
                open_trade("SANDUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_SANDUSDT = 1
                curr_num = curr_num + 1
                    
            if "SANDUSDT SHORT" in dt and status_trade_SANDUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_SANDUSDT = bar
                open_trade("SANDUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_SANDUSDT = -1
                curr_num = curr_num + 1

            if ("SANDUSDT end of trade" in dt) and (status_trade_SANDUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SANDUSDT:
                    close_trade("SANDUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SANDUSDT = 0
                    curr_num = curr_num - 1

            if ("SANDUSDT end of trade" in dt) and (status_trade_SANDUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SANDUSDT:
                    close_trade("SANDUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SANDUSDT = 0
                    curr_num = curr_num - 1


            if "SANDUSDT LONG" in dt and (status_trade_SANDUSDT == -1 or status_trade_SANDUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SANDUSDT:
                    close_trade("SANDUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SANDUSDT = 0
                    curr_num = curr_num - 1

            if "SANDUSDT SHORT" in dt and (status_trade_SANDUSDT == -1 or status_trade_SANDUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SANDUSDT:
                    close_trade("SANDUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SANDUSDT = 0
                    curr_num = curr_num - 1  




            if "GTCUSDT LONG" in dt and status_trade_GTCUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_GTCUSDT = bar
                open_trade("GTCUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_GTCUSDT = 1
                curr_num = curr_num + 1
                    
            if "GTCUSDT SHORT" in dt and status_trade_GTCUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_GTCUSDT = bar
                open_trade("GTCUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_GTCUSDT = -1
                curr_num = curr_num + 1

            if ("GTCUSDT end of trade" in dt) and (status_trade_GTCUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_GTCUSDT:
                    close_trade("GTCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_GTCUSDT = 0
                    curr_num = curr_num - 1

            if ("GTCUSDT end of trade" in dt) and (status_trade_GTCUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_GTCUSDT:
                    close_trade("GTCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_GTCUSDT = 0
                    curr_num = curr_num - 1


            if "GTCUSDT LONG" in dt and (status_trade_GTCUSDT == -1 or status_trade_GTCUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_GTCUSDT:
                    close_trade("GTCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_GTCUSDT = 0
                    curr_num = curr_num - 1

            if "GTCUSDT SHORT" in dt and (status_trade_GTCUSDT == -1 or status_trade_GTCUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_GTCUSDT:
                    close_trade("GTCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_GTCUSDT = 0
                    curr_num = curr_num - 1  




            if "STMXUSDT LONG" in dt and status_trade_STMXUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_STMXUSDT = bar
                open_trade("STMXUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_STMXUSDT = 1
                curr_num = curr_num + 1
                    
            if "STMXUSDT SHORT" in dt and status_trade_STMXUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_STMXUSDT = bar
                open_trade("STMXUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_STMXUSDT = -1
                curr_num = curr_num + 1

            if ("STMXUSDT end of trade" in dt) and (status_trade_STMXUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_STMXUSDT:
                    close_trade("STMXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_STMXUSDT = 0
                    curr_num = curr_num - 1

            if ("STMXUSDT end of trade" in dt) and (status_trade_STMXUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_STMXUSDT:
                    close_trade("STMXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_STMXUSDT = 0
                    curr_num = curr_num - 1


            if "STMXUSDT LONG" in dt and (status_trade_STMXUSDT == -1 or status_trade_STMXUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_STMXUSDT:
                    close_trade("STMXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_STMXUSDT = 0
                    curr_num = curr_num - 1

            if "STMXUSDT SHORT" in dt and (status_trade_STMXUSDT == -1 or status_trade_STMXUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_STMXUSDT:
                    close_trade("STMXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_STMXUSDT = 0
                    curr_num = curr_num - 1  




            if "ZENUSDT LONG" in dt and status_trade_ZENUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ZENUSDT = bar
                open_trade("ZENUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ZENUSDT = 1
                curr_num = curr_num + 1
                    
            if "ZENUSDT SHORT" in dt and status_trade_ZENUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ZENUSDT = bar
                open_trade("ZENUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ZENUSDT = -1
                curr_num = curr_num + 1

            if ("ZENUSDT end of trade" in dt) and (status_trade_ZENUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ZENUSDT:
                    close_trade("ZENUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ZENUSDT = 0
                    curr_num = curr_num - 1

            if ("ZENUSDT end of trade" in dt) and (status_trade_ZENUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ZENUSDT:
                    close_trade("ZENUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ZENUSDT = 0
                    curr_num = curr_num - 1


            if "ZENUSDT LONG" in dt and (status_trade_ZENUSDT == -1 or status_trade_ZENUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ZENUSDT:
                    close_trade("ZENUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ZENUSDT = 0
                    curr_num = curr_num - 1

            if "ZENUSDT SHORT" in dt and (status_trade_ZENUSDT == -1 or status_trade_ZENUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ZENUSDT:
                    close_trade("ZENUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ZENUSDT = 0
                    curr_num = curr_num - 1  




            if "HBARUSDT LONG" in dt and status_trade_HBARUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_HBARUSDT = bar
                open_trade("HBARUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_HBARUSDT = 1
                curr_num = curr_num + 1
                    
            if "HBARUSDT SHORT" in dt and status_trade_HBARUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_HBARUSDT = bar
                open_trade("HBARUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_HBARUSDT = -1
                curr_num = curr_num + 1

            if ("HBARUSDT end of trade" in dt) and (status_trade_HBARUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_HBARUSDT:
                    close_trade("HBARUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_HBARUSDT = 0
                    curr_num = curr_num - 1

            if ("HBARUSDT end of trade" in dt) and (status_trade_HBARUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_HBARUSDT:
                    close_trade("HBARUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_HBARUSDT = 0
                    curr_num = curr_num - 1


            if "HBARUSDT LONG" in dt and (status_trade_HBARUSDT == -1 or status_trade_HBARUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_HBARUSDT:
                    close_trade("HBARUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_HBARUSDT = 0
                    curr_num = curr_num - 1

            if "HBARUSDT SHORT" in dt and (status_trade_HBARUSDT == -1 or status_trade_HBARUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_HBARUSDT:
                    close_trade("HBARUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_HBARUSDT = 0
                    curr_num = curr_num - 1  




            if "MANAUSDT LONG" in dt and status_trade_MANAUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_MANAUSDT = bar
                open_trade("MANAUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_MANAUSDT = 1
                curr_num = curr_num + 1
                    
            if "MANAUSDT SHORT" in dt and status_trade_MANAUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_MANAUSDT = bar
                open_trade("MANAUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_MANAUSDT = -1
                curr_num = curr_num + 1

            if ("MANAUSDT end of trade" in dt) and (status_trade_MANAUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_MANAUSDT:
                    close_trade("MANAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_MANAUSDT = 0
                    curr_num = curr_num - 1

            if ("MANAUSDT end of trade" in dt) and (status_trade_MANAUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_MANAUSDT:
                    close_trade("MANAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_MANAUSDT = 0
                    curr_num = curr_num - 1


            if "MANAUSDT LONG" in dt and (status_trade_MANAUSDT == -1 or status_trade_MANAUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_MANAUSDT:
                    close_trade("MANAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_MANAUSDT = 0
                    curr_num = curr_num - 1

            if "MANAUSDT SHORT" in dt and (status_trade_MANAUSDT == -1 or status_trade_MANAUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_MANAUSDT:
                    close_trade("MANAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_MANAUSDT = 0
                    curr_num = curr_num - 1  




            if "LINAUSDT LONG" in dt and status_trade_LINAUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_LINAUSDT = bar
                open_trade("LINAUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_LINAUSDT = 1
                curr_num = curr_num + 1
                    
            if "LINAUSDT SHORT" in dt and status_trade_LINAUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_LINAUSDT = bar
                open_trade("LINAUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_LINAUSDT = -1
                curr_num = curr_num + 1

            if ("LINAUSDT end of trade" in dt) and (status_trade_LINAUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LINAUSDT:
                    close_trade("LINAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LINAUSDT = 0
                    curr_num = curr_num - 1

            if ("LINAUSDT end of trade" in dt) and (status_trade_LINAUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LINAUSDT:
                    close_trade("LINAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LINAUSDT = 0
                    curr_num = curr_num - 1


            if "LINAUSDT LONG" in dt and (status_trade_LINAUSDT == -1 or status_trade_LINAUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LINAUSDT:
                    close_trade("LINAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LINAUSDT = 0
                    curr_num = curr_num - 1

            if "LINAUSDT SHORT" in dt and (status_trade_LINAUSDT == -1 or status_trade_LINAUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LINAUSDT:
                    close_trade("LINAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LINAUSDT = 0
                    curr_num = curr_num - 1  




            if "BAKEUSDT LONG" in dt and status_trade_BAKEUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BAKEUSDT = bar
                open_trade("BAKEUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BAKEUSDT = 1
                curr_num = curr_num + 1
                    
            if "BAKEUSDT SHORT" in dt and status_trade_BAKEUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BAKEUSDT = bar
                open_trade("BAKEUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BAKEUSDT = -1
                curr_num = curr_num + 1

            if ("BAKEUSDT end of trade" in dt) and (status_trade_BAKEUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BAKEUSDT:
                    close_trade("BAKEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BAKEUSDT = 0
                    curr_num = curr_num - 1

            if ("BAKEUSDT end of trade" in dt) and (status_trade_BAKEUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BAKEUSDT:
                    close_trade("BAKEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BAKEUSDT = 0
                    curr_num = curr_num - 1


            if "BAKEUSDT LONG" in dt and (status_trade_BAKEUSDT == -1 or status_trade_BAKEUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BAKEUSDT:
                    close_trade("BAKEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BAKEUSDT = 0
                    curr_num = curr_num - 1

            if "BAKEUSDT SHORT" in dt and (status_trade_BAKEUSDT == -1 or status_trade_BAKEUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BAKEUSDT:
                    close_trade("BAKEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BAKEUSDT = 0
                    curr_num = curr_num - 1  




            if "NKNUSDT LONG" in dt and status_trade_NKNUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_NKNUSDT = bar
                open_trade("NKNUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_NKNUSDT = 1
                curr_num = curr_num + 1
                    
            if "NKNUSDT SHORT" in dt and status_trade_NKNUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_NKNUSDT = bar
                open_trade("NKNUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_NKNUSDT = -1
                curr_num = curr_num + 1

            if ("NKNUSDT end of trade" in dt) and (status_trade_NKNUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_NKNUSDT:
                    close_trade("NKNUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_NKNUSDT = 0
                    curr_num = curr_num - 1

            if ("NKNUSDT end of trade" in dt) and (status_trade_NKNUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_NKNUSDT:
                    close_trade("NKNUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_NKNUSDT = 0
                    curr_num = curr_num - 1


            if "NKNUSDT LONG" in dt and (status_trade_NKNUSDT == -1 or status_trade_NKNUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_NKNUSDT:
                    close_trade("NKNUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_NKNUSDT = 0
                    curr_num = curr_num - 1

            if "NKNUSDT SHORT" in dt and (status_trade_NKNUSDT == -1 or status_trade_NKNUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_NKNUSDT:
                    close_trade("NKNUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_NKNUSDT = 0
                    curr_num = curr_num - 1  




            if "SCUSDT LONG" in dt and status_trade_SCUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_SCUSDT = bar
                open_trade("SCUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_SCUSDT = 1
                curr_num = curr_num + 1
                    
            if "SCUSDT SHORT" in dt and status_trade_SCUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_SCUSDT = bar
                open_trade("SCUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_SCUSDT = -1
                curr_num = curr_num + 1

            if ("SCUSDT end of trade" in dt) and (status_trade_SCUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SCUSDT:
                    close_trade("SCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SCUSDT = 0
                    curr_num = curr_num - 1

            if ("SCUSDT end of trade" in dt) and (status_trade_SCUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SCUSDT:
                    close_trade("SCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SCUSDT = 0
                    curr_num = curr_num - 1


            if "SCUSDT LONG" in dt and (status_trade_SCUSDT == -1 or status_trade_SCUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SCUSDT:
                    close_trade("SCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SCUSDT = 0
                    curr_num = curr_num - 1

            if "SCUSDT SHORT" in dt and (status_trade_SCUSDT == -1 or status_trade_SCUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_SCUSDT:
                    close_trade("SCUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_SCUSDT = 0
                    curr_num = curr_num - 1  




            if "DENTUSDT LONG" in dt and status_trade_DENTUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_DENTUSDT = bar
                open_trade("DENTUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_DENTUSDT = 1
                curr_num = curr_num + 1
                    
            if "DENTUSDT SHORT" in dt and status_trade_DENTUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_DENTUSDT = bar
                open_trade("DENTUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_DENTUSDT = -1
                curr_num = curr_num + 1

            if ("DENTUSDT end of trade" in dt) and (status_trade_DENTUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DENTUSDT:
                    close_trade("DENTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DENTUSDT = 0
                    curr_num = curr_num - 1

            if ("DENTUSDT end of trade" in dt) and (status_trade_DENTUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DENTUSDT:
                    close_trade("DENTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DENTUSDT = 0
                    curr_num = curr_num - 1


            if "DENTUSDT LONG" in dt and (status_trade_DENTUSDT == -1 or status_trade_DENTUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DENTUSDT:
                    close_trade("DENTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DENTUSDT = 0
                    curr_num = curr_num - 1

            if "DENTUSDT SHORT" in dt and (status_trade_DENTUSDT == -1 or status_trade_DENTUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DENTUSDT:
                    close_trade("DENTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DENTUSDT = 0
                    curr_num = curr_num - 1  




            if "ANKRUSDT LONG" in dt and status_trade_ANKRUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ANKRUSDT = bar
                open_trade("ANKRUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ANKRUSDT = 1
                curr_num = curr_num + 1
                    
            if "ANKRUSDT SHORT" in dt and status_trade_ANKRUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ANKRUSDT = bar
                open_trade("ANKRUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ANKRUSDT = -1
                curr_num = curr_num + 1

            if ("ANKRUSDT end of trade" in dt) and (status_trade_ANKRUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ANKRUSDT:
                    close_trade("ANKRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ANKRUSDT = 0
                    curr_num = curr_num - 1

            if ("ANKRUSDT end of trade" in dt) and (status_trade_ANKRUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ANKRUSDT:
                    close_trade("ANKRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ANKRUSDT = 0
                    curr_num = curr_num - 1


            if "ANKRUSDT LONG" in dt and (status_trade_ANKRUSDT == -1 or status_trade_ANKRUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ANKRUSDT:
                    close_trade("ANKRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ANKRUSDT = 0
                    curr_num = curr_num - 1

            if "ANKRUSDT SHORT" in dt and (status_trade_ANKRUSDT == -1 or status_trade_ANKRUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ANKRUSDT:
                    close_trade("ANKRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ANKRUSDT = 0
                    curr_num = curr_num - 1  




            if "FLOWUSDT LONG" in dt and status_trade_FLOWUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_FLOWUSDT = bar
                open_trade("FLOWUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_FLOWUSDT = 1
                curr_num = curr_num + 1
                    
            if "FLOWUSDT SHORT" in dt and status_trade_FLOWUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_FLOWUSDT = bar
                open_trade("FLOWUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_FLOWUSDT = -1
                curr_num = curr_num + 1

            if ("FLOWUSDT end of trade" in dt) and (status_trade_FLOWUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_FLOWUSDT:
                    close_trade("FLOWUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_FLOWUSDT = 0
                    curr_num = curr_num - 1

            if ("FLOWUSDT end of trade" in dt) and (status_trade_FLOWUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_FLOWUSDT:
                    close_trade("FLOWUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_FLOWUSDT = 0
                    curr_num = curr_num - 1


            if "FLOWUSDT LONG" in dt and (status_trade_FLOWUSDT == -1 or status_trade_FLOWUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_FLOWUSDT:
                    close_trade("FLOWUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_FLOWUSDT = 0
                    curr_num = curr_num - 1

            if "FLOWUSDT SHORT" in dt and (status_trade_FLOWUSDT == -1 or status_trade_FLOWUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_FLOWUSDT:
                    close_trade("FLOWUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_FLOWUSDT = 0
                    curr_num = curr_num - 1  




            if "PEOPLEUSDT LONG" in dt and status_trade_PEOPLEUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_PEOPLEUSDT = bar
                open_trade("PEOPLEUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_PEOPLEUSDT = 1
                curr_num = curr_num + 1
                    
            if "PEOPLEUSDT SHORT" in dt and status_trade_PEOPLEUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_PEOPLEUSDT = bar
                open_trade("PEOPLEUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_PEOPLEUSDT = -1
                curr_num = curr_num + 1

            if ("PEOPLEUSDT end of trade" in dt) and (status_trade_PEOPLEUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_PEOPLEUSDT:
                    close_trade("PEOPLEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_PEOPLEUSDT = 0
                    curr_num = curr_num - 1

            if ("PEOPLEUSDT end of trade" in dt) and (status_trade_PEOPLEUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_PEOPLEUSDT:
                    close_trade("PEOPLEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_PEOPLEUSDT = 0
                    curr_num = curr_num - 1


            if "PEOPLEUSDT LONG" in dt and (status_trade_PEOPLEUSDT == -1 or status_trade_PEOPLEUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_PEOPLEUSDT:
                    close_trade("PEOPLEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_PEOPLEUSDT = 0
                    curr_num = curr_num - 1

            if "PEOPLEUSDT SHORT" in dt and (status_trade_PEOPLEUSDT == -1 or status_trade_PEOPLEUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_PEOPLEUSDT:
                    close_trade("PEOPLEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_PEOPLEUSDT = 0
                    curr_num = curr_num - 1  




            if "BELUSDT LONG" in dt and status_trade_BELUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BELUSDT = bar
                open_trade("BELUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BELUSDT = 1
                curr_num = curr_num + 1
                    
            if "BELUSDT SHORT" in dt and status_trade_BELUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BELUSDT = bar
                open_trade("BELUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BELUSDT = -1
                curr_num = curr_num + 1

            if ("BELUSDT end of trade" in dt) and (status_trade_BELUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BELUSDT:
                    close_trade("BELUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BELUSDT = 0
                    curr_num = curr_num - 1

            if ("BELUSDT end of trade" in dt) and (status_trade_BELUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BELUSDT:
                    close_trade("BELUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BELUSDT = 0
                    curr_num = curr_num - 1


            if "BELUSDT LONG" in dt and (status_trade_BELUSDT == -1 or status_trade_BELUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BELUSDT:
                    close_trade("BELUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BELUSDT = 0
                    curr_num = curr_num - 1

            if "BELUSDT SHORT" in dt and (status_trade_BELUSDT == -1 or status_trade_BELUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BELUSDT:
                    close_trade("BELUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BELUSDT = 0
                    curr_num = curr_num - 1  




            if "BNXUSDT LONG" in dt and status_trade_BNXUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BNXUSDT = bar
                open_trade("BNXUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BNXUSDT = 1
                curr_num = curr_num + 1
                    
            if "BNXUSDT SHORT" in dt and status_trade_BNXUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BNXUSDT = bar
                open_trade("BNXUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BNXUSDT = -1
                curr_num = curr_num + 1

            if ("BNXUSDT end of trade" in dt) and (status_trade_BNXUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BNXUSDT:
                    close_trade("BNXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BNXUSDT = 0
                    curr_num = curr_num - 1

            if ("BNXUSDT end of trade" in dt) and (status_trade_BNXUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BNXUSDT:
                    close_trade("BNXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BNXUSDT = 0
                    curr_num = curr_num - 1


            if "BNXUSDT LONG" in dt and (status_trade_BNXUSDT == -1 or status_trade_BNXUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BNXUSDT:
                    close_trade("BNXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BNXUSDT = 0
                    curr_num = curr_num - 1

            if "BNXUSDT SHORT" in dt and (status_trade_BNXUSDT == -1 or status_trade_BNXUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BNXUSDT:
                    close_trade("BNXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BNXUSDT = 0
                    curr_num = curr_num - 1  




            if "BTCSTUSDT LONG" in dt and status_trade_BTCSTUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BTCSTUSDT = bar
                open_trade("BTCSTUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BTCSTUSDT = 1
                curr_num = curr_num + 1
                    
            if "BTCSTUSDT SHORT" in dt and status_trade_BTCSTUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_BTCSTUSDT = bar
                open_trade("BTCSTUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_BTCSTUSDT = -1
                curr_num = curr_num + 1

            if ("BTCSTUSDT end of trade" in dt) and (status_trade_BTCSTUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BTCSTUSDT:
                    close_trade("BTCSTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BTCSTUSDT = 0
                    curr_num = curr_num - 1

            if ("BTCSTUSDT end of trade" in dt) and (status_trade_BTCSTUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BTCSTUSDT:
                    close_trade("BTCSTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BTCSTUSDT = 0
                    curr_num = curr_num - 1


            if "BTCSTUSDT LONG" in dt and (status_trade_BTCSTUSDT == -1 or status_trade_BTCSTUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BTCSTUSDT:
                    close_trade("BTCSTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BTCSTUSDT = 0
                    curr_num = curr_num - 1

            if "BTCSTUSDT SHORT" in dt and (status_trade_BTCSTUSDT == -1 or status_trade_BTCSTUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_BTCSTUSDT:
                    close_trade("BTCSTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_BTCSTUSDT = 0
                    curr_num = curr_num - 1  




            if "CHRUSDT LONG" in dt and status_trade_CHRUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_CHRUSDT = bar
                open_trade("CHRUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_CHRUSDT = 1
                curr_num = curr_num + 1
                    
            if "CHRUSDT SHORT" in dt and status_trade_CHRUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_CHRUSDT = bar
                open_trade("CHRUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_CHRUSDT = -1
                curr_num = curr_num + 1

            if ("CHRUSDT end of trade" in dt) and (status_trade_CHRUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CHRUSDT:
                    close_trade("CHRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CHRUSDT = 0
                    curr_num = curr_num - 1

            if ("CHRUSDT end of trade" in dt) and (status_trade_CHRUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CHRUSDT:
                    close_trade("CHRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CHRUSDT = 0
                    curr_num = curr_num - 1


            if "CHRUSDT LONG" in dt and (status_trade_CHRUSDT == -1 or status_trade_CHRUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CHRUSDT:
                    close_trade("CHRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CHRUSDT = 0
                    curr_num = curr_num - 1

            if "CHRUSDT SHORT" in dt and (status_trade_CHRUSDT == -1 or status_trade_CHRUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CHRUSDT:
                    close_trade("CHRUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CHRUSDT = 0
                    curr_num = curr_num - 1  




            if "CTKUSDT LONG" in dt and status_trade_CTKUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_CTKUSDT = bar
                open_trade("CTKUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_CTKUSDT = 1
                curr_num = curr_num + 1
                    
            if "CTKUSDT SHORT" in dt and status_trade_CTKUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_CTKUSDT = bar
                open_trade("CTKUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_CTKUSDT = -1
                curr_num = curr_num + 1

            if ("CTKUSDT end of trade" in dt) and (status_trade_CTKUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CTKUSDT:
                    close_trade("CTKUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CTKUSDT = 0
                    curr_num = curr_num - 1

            if ("CTKUSDT end of trade" in dt) and (status_trade_CTKUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CTKUSDT:
                    close_trade("CTKUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CTKUSDT = 0
                    curr_num = curr_num - 1


            if "CTKUSDT LONG" in dt and (status_trade_CTKUSDT == -1 or status_trade_CTKUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CTKUSDT:
                    close_trade("CTKUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CTKUSDT = 0
                    curr_num = curr_num - 1

            if "CTKUSDT SHORT" in dt and (status_trade_CTKUSDT == -1 or status_trade_CTKUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CTKUSDT:
                    close_trade("CTKUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CTKUSDT = 0
                    curr_num = curr_num - 1  




            if "CTSIUSDT LONG" in dt and status_trade_CTSIUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_CTSIUSDT = bar
                open_trade("CTSIUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_CTSIUSDT = 1
                curr_num = curr_num + 1
                    
            if "CTSIUSDT SHORT" in dt and status_trade_CTSIUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_CTSIUSDT = bar
                open_trade("CTSIUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_CTSIUSDT = -1
                curr_num = curr_num + 1

            if ("CTSIUSDT end of trade" in dt) and (status_trade_CTSIUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CTSIUSDT:
                    close_trade("CTSIUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CTSIUSDT = 0
                    curr_num = curr_num - 1

            if ("CTSIUSDT end of trade" in dt) and (status_trade_CTSIUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CTSIUSDT:
                    close_trade("CTSIUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CTSIUSDT = 0
                    curr_num = curr_num - 1


            if "CTSIUSDT LONG" in dt and (status_trade_CTSIUSDT == -1 or status_trade_CTSIUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CTSIUSDT:
                    close_trade("CTSIUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CTSIUSDT = 0
                    curr_num = curr_num - 1

            if "CTSIUSDT SHORT" in dt and (status_trade_CTSIUSDT == -1 or status_trade_CTSIUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_CTSIUSDT:
                    close_trade("CTSIUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_CTSIUSDT = 0
                    curr_num = curr_num - 1  




            if "DARUSDT LONG" in dt and status_trade_DARUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_DARUSDT = bar
                open_trade("DARUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_DARUSDT = 1
                curr_num = curr_num + 1
                    
            if "DARUSDT SHORT" in dt and status_trade_DARUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_DARUSDT = bar
                open_trade("DARUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_DARUSDT = -1
                curr_num = curr_num + 1

            if ("DARUSDT end of trade" in dt) and (status_trade_DARUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DARUSDT:
                    close_trade("DARUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DARUSDT = 0
                    curr_num = curr_num - 1

            if ("DARUSDT end of trade" in dt) and (status_trade_DARUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DARUSDT:
                    close_trade("DARUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DARUSDT = 0
                    curr_num = curr_num - 1


            if "DARUSDT LONG" in dt and (status_trade_DARUSDT == -1 or status_trade_DARUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DARUSDT:
                    close_trade("DARUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DARUSDT = 0
                    curr_num = curr_num - 1

            if "DARUSDT SHORT" in dt and (status_trade_DARUSDT == -1 or status_trade_DARUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DARUSDT:
                    close_trade("DARUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DARUSDT = 0
                    curr_num = curr_num - 1  




            if "DGBUSDT LONG" in dt and status_trade_DGBUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_DGBUSDT = bar
                open_trade("DGBUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_DGBUSDT = 1
                curr_num = curr_num + 1
                    
            if "DGBUSDT SHORT" in dt and status_trade_DGBUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_DGBUSDT = bar
                open_trade("DGBUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_DGBUSDT = -1
                curr_num = curr_num + 1

            if ("DGBUSDT end of trade" in dt) and (status_trade_DGBUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DGBUSDT:
                    close_trade("DGBUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DGBUSDT = 0
                    curr_num = curr_num - 1

            if ("DGBUSDT end of trade" in dt) and (status_trade_DGBUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DGBUSDT:
                    close_trade("DGBUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DGBUSDT = 0
                    curr_num = curr_num - 1


            if "DGBUSDT LONG" in dt and (status_trade_DGBUSDT == -1 or status_trade_DGBUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DGBUSDT:
                    close_trade("DGBUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DGBUSDT = 0
                    curr_num = curr_num - 1

            if "DGBUSDT SHORT" in dt and (status_trade_DGBUSDT == -1 or status_trade_DGBUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DGBUSDT:
                    close_trade("DGBUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DGBUSDT = 0
                    curr_num = curr_num - 1  




            if "DUSKUSDT LONG" in dt and status_trade_DUSKUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_DUSKUSDT = bar
                open_trade("DUSKUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_DUSKUSDT = 1
                curr_num = curr_num + 1
                    
            if "DUSKUSDT SHORT" in dt and status_trade_DUSKUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_DUSKUSDT = bar
                open_trade("DUSKUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_DUSKUSDT = -1
                curr_num = curr_num + 1

            if ("DUSKUSDT end of trade" in dt) and (status_trade_DUSKUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DUSKUSDT:
                    close_trade("DUSKUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DUSKUSDT = 0
                    curr_num = curr_num - 1

            if ("DUSKUSDT end of trade" in dt) and (status_trade_DUSKUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DUSKUSDT:
                    close_trade("DUSKUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DUSKUSDT = 0
                    curr_num = curr_num - 1


            if "DUSKUSDT LONG" in dt and (status_trade_DUSKUSDT == -1 or status_trade_DUSKUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DUSKUSDT:
                    close_trade("DUSKUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DUSKUSDT = 0
                    curr_num = curr_num - 1

            if "DUSKUSDT SHORT" in dt and (status_trade_DUSKUSDT == -1 or status_trade_DUSKUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_DUSKUSDT:
                    close_trade("DUSKUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_DUSKUSDT = 0
                    curr_num = curr_num - 1  




            if "ENJUSDT LONG" in dt and status_trade_ENJUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ENJUSDT = bar
                open_trade("ENJUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ENJUSDT = 1
                curr_num = curr_num + 1
                    
            if "ENJUSDT SHORT" in dt and status_trade_ENJUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ENJUSDT = bar
                open_trade("ENJUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ENJUSDT = -1
                curr_num = curr_num + 1

            if ("ENJUSDT end of trade" in dt) and (status_trade_ENJUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ENJUSDT:
                    close_trade("ENJUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ENJUSDT = 0
                    curr_num = curr_num - 1

            if ("ENJUSDT end of trade" in dt) and (status_trade_ENJUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ENJUSDT:
                    close_trade("ENJUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ENJUSDT = 0
                    curr_num = curr_num - 1


            if "ENJUSDT LONG" in dt and (status_trade_ENJUSDT == -1 or status_trade_ENJUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ENJUSDT:
                    close_trade("ENJUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ENJUSDT = 0
                    curr_num = curr_num - 1

            if "ENJUSDT SHORT" in dt and (status_trade_ENJUSDT == -1 or status_trade_ENJUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ENJUSDT:
                    close_trade("ENJUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ENJUSDT = 0
                    curr_num = curr_num - 1  




            if "ENSUSDT LONG" in dt and status_trade_ENSUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ENSUSDT = bar
                open_trade("ENSUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ENSUSDT = 1
                curr_num = curr_num + 1
                    
            if "ENSUSDT SHORT" in dt and status_trade_ENSUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ENSUSDT = bar
                open_trade("ENSUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ENSUSDT = -1
                curr_num = curr_num + 1

            if ("ENSUSDT end of trade" in dt) and (status_trade_ENSUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ENSUSDT:
                    close_trade("ENSUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ENSUSDT = 0
                    curr_num = curr_num - 1

            if ("ENSUSDT end of trade" in dt) and (status_trade_ENSUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ENSUSDT:
                    close_trade("ENSUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ENSUSDT = 0
                    curr_num = curr_num - 1


            if "ENSUSDT LONG" in dt and (status_trade_ENSUSDT == -1 or status_trade_ENSUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ENSUSDT:
                    close_trade("ENSUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ENSUSDT = 0
                    curr_num = curr_num - 1

            if "ENSUSDT SHORT" in dt and (status_trade_ENSUSDT == -1 or status_trade_ENSUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ENSUSDT:
                    close_trade("ENSUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ENSUSDT = 0
                    curr_num = curr_num - 1  




            if "FTTUSDT LONG" in dt and status_trade_FTTUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_FTTUSDT = bar
                open_trade("FTTUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_FTTUSDT = 1
                curr_num = curr_num + 1
                    
            if "FTTUSDT SHORT" in dt and status_trade_FTTUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_FTTUSDT = bar
                open_trade("FTTUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_FTTUSDT = -1
                curr_num = curr_num + 1

            if ("FTTUSDT end of trade" in dt) and (status_trade_FTTUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_FTTUSDT:
                    close_trade("FTTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_FTTUSDT = 0
                    curr_num = curr_num - 1

            if ("FTTUSDT end of trade" in dt) and (status_trade_FTTUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_FTTUSDT:
                    close_trade("FTTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_FTTUSDT = 0
                    curr_num = curr_num - 1


            if "FTTUSDT LONG" in dt and (status_trade_FTTUSDT == -1 or status_trade_FTTUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_FTTUSDT:
                    close_trade("FTTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_FTTUSDT = 0
                    curr_num = curr_num - 1

            if "FTTUSDT SHORT" in dt and (status_trade_FTTUSDT == -1 or status_trade_FTTUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_FTTUSDT:
                    close_trade("FTTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_FTTUSDT = 0
                    curr_num = curr_num - 1  




            if "GALAUSDT LONG" in dt and status_trade_GALAUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_GALAUSDT = bar
                open_trade("GALAUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_GALAUSDT = 1
                curr_num = curr_num + 1
                    
            if "GALAUSDT SHORT" in dt and status_trade_GALAUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_GALAUSDT = bar
                open_trade("GALAUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_GALAUSDT = -1
                curr_num = curr_num + 1

            if ("GALAUSDT end of trade" in dt) and (status_trade_GALAUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_GALAUSDT:
                    close_trade("GALAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_GALAUSDT = 0
                    curr_num = curr_num - 1

            if ("GALAUSDT end of trade" in dt) and (status_trade_GALAUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_GALAUSDT:
                    close_trade("GALAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_GALAUSDT = 0
                    curr_num = curr_num - 1


            if "GALAUSDT LONG" in dt and (status_trade_GALAUSDT == -1 or status_trade_GALAUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_GALAUSDT:
                    close_trade("GALAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_GALAUSDT = 0
                    curr_num = curr_num - 1

            if "GALAUSDT SHORT" in dt and (status_trade_GALAUSDT == -1 or status_trade_GALAUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_GALAUSDT:
                    close_trade("GALAUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_GALAUSDT = 0
                    curr_num = curr_num - 1  




            if "GMTUSDT LONG" in dt and status_trade_GMTUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_GMTUSDT = bar
                open_trade("GMTUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_GMTUSDT = 1
                curr_num = curr_num + 1
                    
            if "GMTUSDT SHORT" in dt and status_trade_GMTUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_GMTUSDT = bar
                open_trade("GMTUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_GMTUSDT = -1
                curr_num = curr_num + 1

            if ("GMTUSDT end of trade" in dt) and (status_trade_GMTUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_GMTUSDT:
                    close_trade("GMTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_GMTUSDT = 0
                    curr_num = curr_num - 1

            if ("GMTUSDT end of trade" in dt) and (status_trade_GMTUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_GMTUSDT:
                    close_trade("GMTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_GMTUSDT = 0
                    curr_num = curr_num - 1


            if "GMTUSDT LONG" in dt and (status_trade_GMTUSDT == -1 or status_trade_GMTUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_GMTUSDT:
                    close_trade("GMTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_GMTUSDT = 0
                    curr_num = curr_num - 1

            if "GMTUSDT SHORT" in dt and (status_trade_GMTUSDT == -1 or status_trade_GMTUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_GMTUSDT:
                    close_trade("GMTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_GMTUSDT = 0
                    curr_num = curr_num - 1  




            if "HOTUSDT LONG" in dt and status_trade_HOTUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_HOTUSDT = bar
                open_trade("HOTUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_HOTUSDT = 1
                curr_num = curr_num + 1
                    
            if "HOTUSDT SHORT" in dt and status_trade_HOTUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_HOTUSDT = bar
                open_trade("HOTUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_HOTUSDT = -1
                curr_num = curr_num + 1

            if ("HOTUSDT end of trade" in dt) and (status_trade_HOTUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_HOTUSDT:
                    close_trade("HOTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_HOTUSDT = 0
                    curr_num = curr_num - 1

            if ("HOTUSDT end of trade" in dt) and (status_trade_HOTUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_HOTUSDT:
                    close_trade("HOTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_HOTUSDT = 0
                    curr_num = curr_num - 1


            if "HOTUSDT LONG" in dt and (status_trade_HOTUSDT == -1 or status_trade_HOTUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_HOTUSDT:
                    close_trade("HOTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_HOTUSDT = 0
                    curr_num = curr_num - 1

            if "HOTUSDT SHORT" in dt and (status_trade_HOTUSDT == -1 or status_trade_HOTUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_HOTUSDT:
                    close_trade("HOTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_HOTUSDT = 0
                    curr_num = curr_num - 1  




            if "IMXUSDT LONG" in dt and status_trade_IMXUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_IMXUSDT = bar
                open_trade("IMXUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_IMXUSDT = 1
                curr_num = curr_num + 1
                    
            if "IMXUSDT SHORT" in dt and status_trade_IMXUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_IMXUSDT = bar
                open_trade("IMXUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_IMXUSDT = -1
                curr_num = curr_num + 1

            if ("IMXUSDT end of trade" in dt) and (status_trade_IMXUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_IMXUSDT:
                    close_trade("IMXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_IMXUSDT = 0
                    curr_num = curr_num - 1

            if ("IMXUSDT end of trade" in dt) and (status_trade_IMXUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_IMXUSDT:
                    close_trade("IMXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_IMXUSDT = 0
                    curr_num = curr_num - 1


            if "IMXUSDT LONG" in dt and (status_trade_IMXUSDT == -1 or status_trade_IMXUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_IMXUSDT:
                    close_trade("IMXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_IMXUSDT = 0
                    curr_num = curr_num - 1

            if "IMXUSDT SHORT" in dt and (status_trade_IMXUSDT == -1 or status_trade_IMXUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_IMXUSDT:
                    close_trade("IMXUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_IMXUSDT = 0
                    curr_num = curr_num - 1  




            if "JASMYUSDT LONG" in dt and status_trade_JASMYUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_JASMYUSDT = bar
                open_trade("JASMYUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_JASMYUSDT = 1
                curr_num = curr_num + 1
                    
            if "JASMYUSDT SHORT" in dt and status_trade_JASMYUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_JASMYUSDT = bar
                open_trade("JASMYUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_JASMYUSDT = -1
                curr_num = curr_num + 1

            if ("JASMYUSDT end of trade" in dt) and (status_trade_JASMYUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_JASMYUSDT:
                    close_trade("JASMYUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_JASMYUSDT = 0
                    curr_num = curr_num - 1

            if ("JASMYUSDT end of trade" in dt) and (status_trade_JASMYUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_JASMYUSDT:
                    close_trade("JASMYUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_JASMYUSDT = 0
                    curr_num = curr_num - 1


            if "JASMYUSDT LONG" in dt and (status_trade_JASMYUSDT == -1 or status_trade_JASMYUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_JASMYUSDT:
                    close_trade("JASMYUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_JASMYUSDT = 0
                    curr_num = curr_num - 1

            if "JASMYUSDT SHORT" in dt and (status_trade_JASMYUSDT == -1 or status_trade_JASMYUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_JASMYUSDT:
                    close_trade("JASMYUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_JASMYUSDT = 0
                    curr_num = curr_num - 1  




            if "LPTUSDT LONG" in dt and status_trade_LPTUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_LPTUSDT = bar
                open_trade("LPTUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_LPTUSDT = 1
                curr_num = curr_num + 1
                    
            if "LPTUSDT SHORT" in dt and status_trade_LPTUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_LPTUSDT = bar
                open_trade("LPTUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_LPTUSDT = -1
                curr_num = curr_num + 1

            if ("LPTUSDT end of trade" in dt) and (status_trade_LPTUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LPTUSDT:
                    close_trade("LPTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LPTUSDT = 0
                    curr_num = curr_num - 1

            if ("LPTUSDT end of trade" in dt) and (status_trade_LPTUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LPTUSDT:
                    close_trade("LPTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LPTUSDT = 0
                    curr_num = curr_num - 1


            if "LPTUSDT LONG" in dt and (status_trade_LPTUSDT == -1 or status_trade_LPTUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LPTUSDT:
                    close_trade("LPTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LPTUSDT = 0
                    curr_num = curr_num - 1

            if "LPTUSDT SHORT" in dt and (status_trade_LPTUSDT == -1 or status_trade_LPTUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_LPTUSDT:
                    close_trade("LPTUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_LPTUSDT = 0
                    curr_num = curr_num - 1  




            if "OMGUSDT LONG" in dt and status_trade_OMGUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_OMGUSDT = bar
                open_trade("OMGUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_OMGUSDT = 1
                curr_num = curr_num + 1
                    
            if "OMGUSDT SHORT" in dt and status_trade_OMGUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_OMGUSDT = bar
                open_trade("OMGUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_OMGUSDT = -1
                curr_num = curr_num + 1

            if ("OMGUSDT end of trade" in dt) and (status_trade_OMGUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_OMGUSDT:
                    close_trade("OMGUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_OMGUSDT = 0
                    curr_num = curr_num - 1

            if ("OMGUSDT end of trade" in dt) and (status_trade_OMGUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_OMGUSDT:
                    close_trade("OMGUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_OMGUSDT = 0
                    curr_num = curr_num - 1


            if "OMGUSDT LONG" in dt and (status_trade_OMGUSDT == -1 or status_trade_OMGUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_OMGUSDT:
                    close_trade("OMGUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_OMGUSDT = 0
                    curr_num = curr_num - 1

            if "OMGUSDT SHORT" in dt and (status_trade_OMGUSDT == -1 or status_trade_OMGUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_OMGUSDT:
                    close_trade("OMGUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_OMGUSDT = 0
                    curr_num = curr_num - 1  




            if "OPUSDT LONG" in dt and status_trade_OPUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_OPUSDT = bar
                open_trade("OPUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_OPUSDT = 1
                curr_num = curr_num + 1
                    
            if "OPUSDT SHORT" in dt and status_trade_OPUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_OPUSDT = bar
                open_trade("OPUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_OPUSDT = -1
                curr_num = curr_num + 1

            if ("OPUSDT end of trade" in dt) and (status_trade_OPUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_OPUSDT:
                    close_trade("OPUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_OPUSDT = 0
                    curr_num = curr_num - 1

            if ("OPUSDT end of trade" in dt) and (status_trade_OPUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_OPUSDT:
                    close_trade("OPUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_OPUSDT = 0
                    curr_num = curr_num - 1


            if "OPUSDT LONG" in dt and (status_trade_OPUSDT == -1 or status_trade_OPUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_OPUSDT:
                    close_trade("OPUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_OPUSDT = 0
                    curr_num = curr_num - 1

            if "OPUSDT SHORT" in dt and (status_trade_OPUSDT == -1 or status_trade_OPUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_OPUSDT:
                    close_trade("OPUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_OPUSDT = 0
                    curr_num = curr_num - 1  




            if "RENUSDT LONG" in dt and status_trade_RENUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_RENUSDT = bar
                open_trade("RENUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_RENUSDT = 1
                curr_num = curr_num + 1
                    
            if "RENUSDT SHORT" in dt and status_trade_RENUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_RENUSDT = bar
                open_trade("RENUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_RENUSDT = -1
                curr_num = curr_num + 1

            if ("RENUSDT end of trade" in dt) and (status_trade_RENUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RENUSDT:
                    close_trade("RENUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RENUSDT = 0
                    curr_num = curr_num - 1

            if ("RENUSDT end of trade" in dt) and (status_trade_RENUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RENUSDT:
                    close_trade("RENUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RENUSDT = 0
                    curr_num = curr_num - 1


            if "RENUSDT LONG" in dt and (status_trade_RENUSDT == -1 or status_trade_RENUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RENUSDT:
                    close_trade("RENUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RENUSDT = 0
                    curr_num = curr_num - 1

            if "RENUSDT SHORT" in dt and (status_trade_RENUSDT == -1 or status_trade_RENUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_RENUSDT:
                    close_trade("RENUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_RENUSDT = 0
                    curr_num = curr_num - 1  




            if "ROSEUSDT LONG" in dt and status_trade_ROSEUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ROSEUSDT = bar
                open_trade("ROSEUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ROSEUSDT = 1
                curr_num = curr_num + 1
                    
            if "ROSEUSDT SHORT" in dt and status_trade_ROSEUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_ROSEUSDT = bar
                open_trade("ROSEUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_ROSEUSDT = -1
                curr_num = curr_num + 1

            if ("ROSEUSDT end of trade" in dt) and (status_trade_ROSEUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ROSEUSDT:
                    close_trade("ROSEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ROSEUSDT = 0
                    curr_num = curr_num - 1

            if ("ROSEUSDT end of trade" in dt) and (status_trade_ROSEUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ROSEUSDT:
                    close_trade("ROSEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ROSEUSDT = 0
                    curr_num = curr_num - 1


            if "ROSEUSDT LONG" in dt and (status_trade_ROSEUSDT == -1 or status_trade_ROSEUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ROSEUSDT:
                    close_trade("ROSEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ROSEUSDT = 0
                    curr_num = curr_num - 1

            if "ROSEUSDT SHORT" in dt and (status_trade_ROSEUSDT == -1 or status_trade_ROSEUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_ROSEUSDT:
                    close_trade("ROSEUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_ROSEUSDT = 0
                    curr_num = curr_num - 1  




            if "WOOUSDT LONG" in dt and status_trade_WOOUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_WOOUSDT = bar
                open_trade("WOOUSDT",  "LONG", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_WOOUSDT = 1
                curr_num = curr_num + 1
                    
            if "WOOUSDT SHORT" in dt and status_trade_WOOUSDT == 0 and curr_num < max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                last_bar_WOOUSDT = bar
                open_trade("WOOUSDT",  "SHORT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                status_trade_WOOUSDT = -1
                curr_num = curr_num + 1

            if ("WOOUSDT end of trade" in dt) and (status_trade_WOOUSDT == 1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_WOOUSDT:
                    close_trade("WOOUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_WOOUSDT = 0
                    curr_num = curr_num - 1

            if ("WOOUSDT end of trade" in dt) and (status_trade_WOOUSDT == -1) and curr_num > 0:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_WOOUSDT:
                    close_trade("WOOUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_WOOUSDT = 0
                    curr_num = curr_num - 1


            if "WOOUSDT LONG" in dt and (status_trade_WOOUSDT == -1 or status_trade_WOOUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_WOOUSDT:
                    close_trade("WOOUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_WOOUSDT = 0
                    curr_num = curr_num - 1

            if "WOOUSDT SHORT" in dt and (status_trade_WOOUSDT == -1 or status_trade_WOOUSDT == 1) and curr_num <= max_trade:
                bar = dt.split("Bar_Index: ")
                bar = int(bar[1])
                if bar != last_bar_WOOUSDT:
                    close_trade("WOOUSDT", dt, "https://hook.eu1.make.com/um6rr94qe5arbu6oqbcun2655bpeonc2")
                    status_trade_WOOUSDT = 0
                    curr_num = curr_num - 1  














            #logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",str(self.path), str(status), post_data.decode('utf-8'))
            #self._set_response()
            #self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
