from binance import ThreadedWebsocketManager
import time
import pandas as pd
import warnings
import asyncio
warnings.simplefilter(action='ignore', category=FutureWarning)

import numpy as np
import nest_asyncio
nest_asyncio.apply()


class BinanceWs:

    def __init__(self):
        self.twm = ThreadedWebsocketManager()
        self.twm.start()
        self.bidask = pd.DataFrame(columns = ["Best Bid", "Best Ask", "Bid Size", "Ask Size"])
        self.aggtrades = pd.DataFrame(columns = [ "Price", "Quantity", "Side"])
        self.run_time = 180
        self.str_time = time.time()
        self.stime = pd.to_datetime(self.str_time, unit = "s")


    def startBidAskStream(self, pair):
        self.twm.start_symbol_ticker_socket(callback=self.bidask_payload, symbol=pair)
        print("{} | Starting App ". format(self.stime))

    def bidask_payload(self, msg):
        # Interpret incoming ws messages
        event_time = pd.to_datetime(msg["E"], unit = "ms")
        bid = float(msg["b"])
        ask = float(msg["a"])
        bid_size = float(msg["B"])
        ask_size = float(msg["A"])
    
        # Update dataframe
        self.bidask.loc[event_time] = [bid, ask, bid_size, ask_size]

        #print("{} | {} | {} | {} | {}".format(event_time, bid, ask, bid_size, ask_size))

        if time.time() - self.str_time > self.run_time:
            self.twm.stop()

    def startTradeStream(self, pair):
        self.twm.start_aggtrade_socket(callback=self.aggtrade_payload, symbol=pair)
        

    def aggtrade_payload(self, msg):
        # Interpret incoming ws messages
        event_time = pd.to_datetime(msg["E"], unit = "ms")
        start_time = pd.to_datetime(msg["T"], unit = "ms")
        price = float(msg["p"])
        quantity = float(msg["q"])
        side = msg["m"]

        # Update dataframe
        self.aggtrades.loc[start_time] = [ price, quantity, side]

        print("{} | {} | {} | {}".format(event_time, price, quantity, side), flush = True)

        if time.time() - self.str_time > self.run_time:
            self.twm.stop()

if __name__ == "__main__":
    binws = BinanceWs()
    binws.startBidAskStream("BTCUSDT")
    binws.startTradeStream("BTCUSDT")
    done_time = pd.to_datetime(time.time(), unit = "s")

    #save dataframe