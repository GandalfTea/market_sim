from dataclasses import dataclass
import numpy as np

# TODO: Maybe separate the matching and executing into diferent threads.

class order:
    def __init__(self, acc, sec, otype, prc, qty):
        self.account = acc
        self.security = sec 
        self.otype = otype
        self.price = prc
        self.quantity = qty
    
    def update(self, qty):
        self.quantity = qty


@dataclass
class order_flow:
    buy = []
    sell = []



@dataclass
class market:
    orderFlow = order_flow()    
    
    def run():
        while True:
            _match()

    def _match():
        _sort()
        for i in self.orderFlow.buy:
            if(i.price == -1):
                i.price = self.orderFlow.sell[0].price
            for j in self.orderFlow.sell:
                if(j.price == -1):
                    j.price = self.orderFlow.buy[0].price
                if(i.price == j.price): 
                    #security check the account balance
                    self._execute(i, j) 

    def _execute(buy, sell):
        if(sell.quantity > buy.quantity):
            sell.update(sell.quantity - buy.quantity)   
            return
        elif(buy.quantity > sell.quantity):
            buy.update(buy.quantity - sell.quantity)
            return

        # transfer funds and securities    
        _rmv_order(buy)
        _rmv_order(sell)

    def create_order(acc : str, sec : str, otype : str, prc : float, qty : int):
        if otype == "BUY":
            self.orderFlow.buy.append[order(acc, sec, otype, prc, qty)]
        elif otype == "SELL":
            self.orderFlow.sell.append[order(acc, sec, otype, prc, qty)]
        else:
            raise Exception("Error : unexpected order type, market.py:56")

    def _rmv_order():
        die()
    
    def _sort():
        orderFlow.buy.sort(key = lambda x : x.price) # big to small
        orderFlow.sell.sort(key = lambda x : x.price, reverse=True) # small to big


