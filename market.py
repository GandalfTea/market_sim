from dataclasses import dataclass
import numpy as np
import imports as imp
import sys

# TODO: Maybe separate the matching and executing into diferent threads.


class order:
    def __init__(self, acc : int, sec : str, otype : str, prc : float, qty : int):
        #assert isinstance(acc, int) and isinstance(prc, float) and isinstance(qty, int) 
        #assert isinstance(sec, str) and isinstance(otype, str) 
        self.account = acc
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
        for buy in self.orderFlow.buy:
            if(buy.price == -1):
                buy.price = self.orderFlow.sell[0].price
            for sell in self.orderFlow.sell:
                if(sell.price == -1):
                    sell.price = self.orderFlow.buy[0].price
                if(buy.price == sell.price and buy.security == sell.security): 
                    try:
                        assert buy in self.orderFlow.buy # TODO: BUG
                        assert imp.PARTICIPANTS[buy.account].liquidity >= sell.price * sell.quantity # enough money to buy
                        assert imp.PARTICIPANTS[sell.account].assets[sell.security] >= sell.quantity  # enough assets to sell
                        self._execute(buy, sell) 
                    except AssertionError:
                        continue


    def _execute(self, buy, sell):
        if(sell.quantity > buy.quantity):
            try:
                imp.PARTICIPANTS[buy.account].liquidity -= buy.price * buy.quantity
                imp.PARTICIPANTS[sell.account].assets[sell.security] -= buy.quantity
                imp.PARTICIPANTS[sell.account].liquidity += buy.price * buy.quantity
                imp.PARTICIPANTS[buy.account].assets[buy.security] += buy.quantity
            except IndexError:
                sys.exit(f"{imp.bcolors.FAIL}Error: could not execute order {order} because the account numbers are out of range.")
            sell.update(sell.quantity - buy.quantity)
            self._rmv_order(buy)
        elif(buy.quantity > sell.quantity):
            try:
                imp.PARTICIPANTS[buy.account].liquidity -= sell.price * sell.quantity
                imp.PARTICIPANTS[sell.account].assets[sell.security] -= sell.quantity
                imp.PARTICIPANTS[sell.account].liquidity += sell.price * sell.quantity
                imp.PARTICIPANTS[buy.account].assets[sell.security] += sell.quantity
            except IndexError:
                sys.exit(f"{imp.bcolors.FAIL}Error: could not execute order {order} because the account numbers are out of range.")
            buy.update(buy.quantity - sell.quantity)
            self._rmv_order(sell)
        elif(buy.quantity == sell.quantity):
            try:
                imp.PARTICIPANTS[buy.account].liquidity -= sell.price * sell.quantity
                imp.PARTICIPANTS[sell.account].assets[sell.security] -= sell.quantity
                imp.PARTICIPANTS[sell.account].liquidity += sell.price * sell.quantity
                imp.PARTICIPANTS[buy.account].assets[sell.security] += sell.quantity
            except IndexError:
                sys.exit(f"{imp.bcolors.FAIL}Error: could not execute order {order} because the account numbers are out of range.")
            self._rmv_order(buy)
            self._rmv_order(sell)
        else:
            raise Exception(f"{imp.bcolors.FAIL}Error: Could not execute orders {buy} : {sell}.")

        assert imp.PARTICIPANTS[buy.account].assets[buy.security] >= 0, f"{imp.bcolors.FAIL}Error: transaction failure in _execute(){imp.bcolors.ENDC}"
        assert imp.PARTICIPANTS[sell.account].assets[sell.security] >= 0, f"{imp.bcolors.FAIL}Error: transaction failure in _execute(){imp.bcolors.ENDC}"
        assert imp.PARTICIPANTS[buy.account].liquidity >= 0, f"{imp.bcolors.FAIL}Error: transaction failure in _execute(){imp.bcolors.ENDC}"
        assert imp.PARTICIPANTS[sell.account].liquidity >= 0, f"{imp.bcolors.FAIL}Error: transaction failure in _execute(){imp.bcolors.ENDC}"
        if imp.MARKET_TESTING: print(".", end="")




    def create_order(self, acc : int, sec : str, otype : str, prc : float, qty : int):
        if otype == "BUY":
            o = order(acc, sec, otype, prc, qty)
            self.orderFlow.buy.append(o)
            assert o in self.orderFlow.buy, f"{imp.bcolors.FAIL}Error: Failure in adding order to orderFlow.buy{imp.bcolors.ENDC}"
        elif otype == "SELL":
            o = order(acc, sec, otype, prc, qty)
            self.orderFlow.sell.append(o)
            assert o in self.orderFlow.sell, f"{imp.bcolors.FAIL}Error: Failure in adding order to orderFlow.sell{imp.bcolors.ENDC}"
        else:
            # return err
            raise Exception(f"\n{imp.bcolors.FAIL}Error : unexpected order type, market.py:56{imp.bcolors.ENDC}\n")



    def dump_orders(self):
        for i in self.orderFlow.buy:
            print(i)
        for i in self.orderFlow.sell:
            print(i)



    def _rmv_order(self, order):
        try:
            if order.otype == "SELL":
                self.orderFlow.sell.remove(order)
                assert order not in self.orderFlow.sell, f"{imp.bcolors.FAIL}Error: Failure in removing order from orderFlow.sell{imp.bcolors.ENDC}"
            elif order.otype == "BUY":
                self.orderFlow.buy.remove(order)
                assert order not in self.orderFlow.buy, f"{imp.bcolors.FAIL}Error: Failure in removing order from orderFlow.buy{imp.bcolors.ENDC}"
            else:
                raise Exception(f"\n{imp.bcolors.FAIL}Error : unexpected order type, market.py:94{imp.bcolors.ENDC}\n")
        except ValueError:
            sys.exit(f"\n{imp.bcolors.FAIL}Error: Tried to remove orderFlow order that does not exist.{imp.bcolors.ENDC} market.py:130 : {order}\n")
    

    def _sort(self):
        self.orderFlow.buy.sort(key = lambda x : x.price) # big to small
        self.orderFlow.sell.sort(key = lambda x : x.price, reverse=True) # small to big
