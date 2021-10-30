from dataclasses import dataclass
import numpy as np
import imports as imp
import sys

# TODO: Maybe separate the matching and executing into diferent threads.


class order:
    def __init__(self, acc : int, sec : str, otype : str, prc : float, qty : int):
        self.account = int(acc)
        self.security = sec 
        self.otype = otype
        self.price = prc
        self.quantity = qty
    
    def update(self, qty):
        self.quantity = qty

    def __repr__(self):
        return(self.security + " " + self.otype + " : " + str(self.price) + " - " + str(self.quantity) + ", " + str(self.account))

@dataclass
class order_flow:
    buy = []
    sell = []



@dataclass
class market:
    orderFlow = order_flow()    
    
    def run(self):
        while True:
            self._match()

    def _match(self):
        self._sort()
        for i in self.orderFlow.buy:
            if(i.price == -1):
                i.price = self.orderFlow.sell[0].price
            for j in self.orderFlow.sell:
                if(j.price == -1):
                    j.price = self.orderFlow.buy[0].price
                if(i.price == j.price): 
                    if(i.security == j.security):
                        if(imp.PARTICIPANTS[i.account].liquidity >= j.price * j.quantity): # assert enough money to buy
                            if(imp.PARTICIPANTS[j.account].assets[j.security] >= j.quantity): # assert enough assets to sell
                                self._execute(i, j) 
            #if i not in self.orderFlow.buy: print(f"{i}")
    def _execute(self, buy, sell):
        print(".", end="")
        #if imp.MARKET_TESTING: 
        #    print("Buy : ", imp.PARTICIPANTS[buy.account].assets[buy.security])
        #    print("Sell : ", imp.PARTICIPANTS[sell.account].liquidity)
        if(sell.quantity > buy.quantity):
            imp.PARTICIPANTS[buy.account].liquidity -= buy.price * buy.quantity
            imp.PARTICIPANTS[sell.account].assets[sell.security] -= buy.quantity
            imp.PARTICIPANTS[sell.account].liquidity += buy.price * buy.quantity
            imp.PARTICIPANTS[buy.account].assets[buy.security] += buy.quantity
            sell.update(sell.quantity - buy.quantity)   
            #if imp.MARKET_TESTING: 
            #    print("Executed : ", buy, " ", sell)
            #    print("Buy : ", imp.PARTICIPANTS[buy.account].assets[buy.security])
            #    print("Sell : ", imp.PARTICIPANTS[sell.account].liquidity)
            #    print()
            self._rmv_order(buy)
        elif(buy.quantity > sell.quantity):
            imp.PARTICIPANTS[buy.account].liquidity -= sell.price * sell.quantity
            imp.PARTICIPANTS[sell.account].assets[sell.security] -= sell.quantity
            imp.PARTICIPANTS[sell.account].liquidity += sell.price * sell.quantity
            imp.PARTICIPANTS[buy.account].assets[sell.security] += sell.quantity
           # if imp.MARKET_TESTING: 
           #     print("Executed : ", buy, " ", sell)
           #     print("Buy : ", imp.PARTICIPANTS[buy.account].assets[buy.security])
           #     print("Sell : ", imp.PARTICIPANTS[sell.account].liquidity)
           #     print()
            buy.update(buy.quantity - sell.quantity)
            self._rmv_order(sell)
        elif(buy.quantity == sell.quantity):
            imp.PARTICIPANTS[buy.account].liquidity -= sell.price * sell.quantity
            imp.PARTICIPANTS[sell.account].assets[sell.security] -= sell.quantity
            imp.PARTICIPANTS[sell.account].liquidity += sell.price * sell.quantity
            imp.PARTICIPANTS[buy.account].assets[sell.security] += sell.quantity
            #if imp.MARKET_TESTING: 
            #    print("Executed : ", buy, " ", sell)
            #    print("Buy : ", imp.PARTICIPANTS[buy.account].assets[buy.security])
            #    print("Sell : ", imp.PARTICIPANTS[sell.account].liquidity)
            #    print()
            self._rmv_order(buy)
            self._rmv_order(sell)
        assert imp.PARTICIPANTS[buy.account].assets[buy.security] >= 0
        assert imp.PARTICIPANTS[sell.account].assets[sell.security] >= 0
        assert imp.PARTICIPANTS[buy.account].liquidity >= 0
        assert imp.PARTICIPANTS[sell.account].liquidity >= 0

    def create_order(self, acc : int, sec : str, otype : str, prc : float, qty : int):
        if imp.MARKET_TESTING == True:
            sbefore = len(self.orderFlow.sell)
            bbefore = len(self.orderFlow.buy)
        if otype == "BUY":
            o = order(acc, sec, otype, prc, qty)
            self.orderFlow.buy.append(o)
            if imp.MARKET_TESTING : assert o in self.orderFlow.buy
            if imp.MARKET_TESTING : assert len(self.orderFlow.buy) == bbefore + 1, f"{imp.bcolors.FAIL}Error: Failure in adding order to orderFlow{imp.bcolors.ENDC}"
        elif otype == "SELL":
            self.orderFlow.sell.append(order(acc, sec, otype, prc, qty))
            if imp.MARKET_TESTING : assert len(self.orderFlow.sell) == sbefore + 1, f"{imp.bcolors.FAIL}Error: Failure in adding order to orderFlow{imp.bcolors.ENDC}"
        else:
            raise Exception(f"\n{imp.bcolors.FAIL}Error : unexpected order type, market.py:56{imp.bcolors.ENDC}\n")

    def dump_orders(self):
        for i in self.orderFlow.buy:
            print(i)
        for i in self.orderFlow.sell:
            print(i)

    def _rmv_order(self, order):
        if imp.MARKET_TESTING == True:
            sbefore = len(self.orderFlow.sell)
            bbefore = len(self.orderFlow.buy)
        try:
            if order.otype == "SELL":
                self.orderFlow.sell.remove(order)
                if imp.MARKET_TESTING : assert len(self.orderFlow.sell) == sbefore - 1, f"{imp.bcolors.FAIL}Error: Failure in removing order from orderFlow{imp.bcolors.ENDC}"
            elif order.otype == "BUY":
                self.orderFlow.buy.remove(order)
                if imp.MARKET_TESTING : assert len(self.orderFlow.buy) == bbefore - 1, f"{imp.bcolors.FAIL}Error: Failure in removing order from orderFlow{imp.bcolors.ENDC}"
            else:
                raise Exception(f"\n{imp.bcolors.FAIL}Error : unexpected order type, market.py:94{imp.bcolors.ENDC}\n")
        except ValueError:
            sys.exit(f"\n{imp.bcolors.FAIL}Error: Tried to remove orderFlow order that does not exist.{imp.bcolors.ENDC} market.py:130 : {order}\n")
    
    def _sort(self):
        self.orderFlow.buy.sort(key = lambda x : x.price) # big to small
        self.orderFlow.sell.sort(key = lambda x : x.price, reverse=True) # small to big
