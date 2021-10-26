import sys
import random
import math
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from functools import reduce
import imports as imp

# Initialize a number of participants who have:
#   * Rand sum of money
#   * Rand pressure tolerance
#   * Security choosing algorithm
#   * Buy / Sell algorithm
# Init a number of securities 
# Market Maker
# Trust point system



# Securities
@dataclass
class _sentry():   # History entry for security
    price : float = 0. 
    volume : int = 0

class security:
    def __init__(self, name : str, price : float, volume : int):
        self.name = name
        self.price = price 
        self.volume = volume
        self.full_volume : int = 0
        self.history = []        # collection of past 100 cycles of volume and price

    def __repr__(self) -> str:
        return self.name + " : " + str(self.price) + " : " + str(self.volume)

    def record(self, o_price : float, o_volume : int):
        self.history.append(_sentry(o_price, o_volume))
        

@dataclass
class state:
    # dummy sec declaration
    s = { "ASS"  : security("ASS",  218.54,  3000000),
          "GAY"  : security("GAY",  21.34,   8500000),
          "RPG"  : security("RPG",  1.35,    800000),
          "LOL"  : security("LOL",  0.5,     120000000),
          "METH" : security("METH", 420.69,  3000000)
    }

    s["ASS"].record(218.54, 966)
    s["ASS"].record(234.72, 334)
    s["ASS"].record(256.01, 2345)
    s["GAY"].record(22.34, 8756)
    s["GAY"].record(18.25, 15245)
    s["GAY"].record(15.20, 5692)
    s["LOL"].record(0.634, 567)
    s["LOL"].record(0.462, 1240)
    s["LOL"].record(0.55, 345)
    s["RPG"].record(1.24, 5674)
    s["RPG"].record(1.11, 3689)
    s["RPG"].record(0.96, 431)
    s["METH"].record(420.56, 5682)
    s["METH"].record(420.34, 9673)
    s["METH"].record(420.46, 8165)

    history = []
    total_v : int = 0
    total_p : float = 0
    probs = {}
    
    # called every cycle
    def refresh(self):
        self.update()
        self.record()
        self._probs()

    def update(self):
        self.total_v, self.total_p = 0, 0
        for sec in self.s:
            for i in self.s[sec].history[:100]: self.total_v += i.volume
            for i in self.s[sec].history[:100]: self.total_p += i.price

    def __repr__(self):
        for sec in s:
            print(sec.name + "\n" + "Price : " + str(sec.price) + "\n" + "Current Volume : " + str(sec.volume))


    def record(self):
        history.append(_sentry(total_p, total_v))
        for sec in self.s:
            sec.record(sec.price, sec.volume)
            sec.volume = 0


    # calculate unbiased stock probability 
    # RUNS ONCE PER CYCLE
    def _probs(self):

        # At the end, you have 3 variables:
        #   * Market Volidity 
        #   * Danger potential
        #   * Total Influence over market

        self.update()

        #   Market Volidity Variable
        #market_volatility = abs((self.history[-1].price - self.history[0].price) / self.history[-1].price)
        if(imp.VERBOSE_MARKET or imp.VERBOSE): print( "\nTotal Volume : " + str(self.total_v) + "\nTotal Price : " + str(self.total_p))

        for key, sec in enumerate(self.s):

            # Calculate average price and full volume over last 100 cycles per stock
            prc = 0
            vol = 0
            history = []
            for frame in self.s[sec].history:
                prc += frame.price
                vol += frame.volume
                history.append(frame.price)
         
            #    Stock Influence Variable
            # the influence of volume is heavily biased towards the lower priced stocks
            # we de-bias this by calculating the influence of mean price over mean total of all prices
            try:
                vol_inf =  1 - ((self.total_v - vol) / self.total_v)
                prc_inf =  1 - ((self.total_p - prc) / self.total_p)
                influence = (vol_inf + prc_inf) / 2
                if(imp.VERBOSE_SECURITIES or imp.VERBOSE): print("\n" + sec + "      influence : " + str(influence)) 
            except ZeroDivisionError:
                sys.exit(f"{imp.bcolors.WARNING} FATAL ERROR: Dision by 0 in  _probs{imp.bcolors.ENDC}'")

            #   Volatility Variable
            # Used to calculate the risk variable
            prices = []
            for i in self.s[sec].history:
                prices.append(i.price)
            diff = []
            for i in range(len(prices)-1):
                v = abs((prices[i+1] - prices[i]) / prices[i+1])
                diff.append(v)
            volatility = reduce(lambda a,b: a+b, diff) / len(diff)
            if(imp.VERBOSE_SECURITIES or imp.VERBOSE): print("\t volatility  : " +  str(volatility) + " : " + str(self.s[sec].history[0].price) + " to " + str(self.s[sec].history[-1].price))

            #   Risk Variable
            # Sigmoid function to corelate volatility
            risk = (2/(1+math.e**(-volatility / 0.01555)))-1
            if(imp.VERBOSE_SECURITIES or imp.VERBOSE): print("\t risk  : " +  str(risk)) 

            win_prob = (volatility + influence) / 2
            self.probs[sec] = [win_prob, risk]
            if(imp.VERBOSE_SECURITIES or imp.VERBOSE): print("\t win?      : " + str(win_prob))




# Participants
class prt:
    def __init__(self):
        self.nonce = random.uniform(-1, 1)              # measure of personal bias and irrationality
        self.tolerance = random.random()                # TODO:  updated after every 10 cycles depending on trading results
        self.liquidity : int = 0                        # init in __bias_liq() 
        self.assets = np.zeros(imp.NUM_OF_SECURITIES) 
        self.probs = {} 

    def __repr__(self):
        space = (20 - len(str(self.liquidity))) * " "   # nice console formatting
        return str(self.liquidity) + space + str(self.tolerance) + " "

    # personal probability. Adds bias and tolerance
    def pprob(self):

        can_buy = {} 
        for i in state.probs:
            # no partial stock buys for now
            if(self.liquidity >= state.s[i].price):
                if(self.tolerance >= state.probs[i][1]):
                    can_buy[i] = [i, state.probs[i]]
        for i in can_buy:
            can_buy[i][1][0] = (can_buy[i][1][0] + random.uniform(0, self.nonce)) / 2
        return can_buy

    def buy(self, can_buy):
        # Create market ordre
        die()
        
    def cycle(self):
        # Calc probs. Decide if to buy or sell
        die()
        

def __bias_liq(num : int):
    g = np.random.gamma(.2, 2, num + 200)
    for i in range(len(g)-1):
        g[i]  = g[i] * 1000000;
        if g[i] < 10.:
            g[i] = None 
    g = g[np.logical_not(np.isnan(g))]        
    return g


class market_maker:
    def __init__(self):
        a = 1
        
