
import random
import math
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import NewType

# Initialize a number of participants who have:
#   * Rand sum of money
#   * Rand pressure tolerance
#   * Security choosing algorithm
#   * Buy / Sell algorithm
# Init a number of securities 
# Market Maker
# Trust point system




NUM_OF_PARTICIPANTS = 10000
CYCLES_PER_MINUTE = 100
NUM_OF_SECURITIES = 10
LONG = 20                 # % of people who hold long
IRRATIONALITY = 0.5       # % of people behaving irrationally
OPTIONS = False




# Securities
@dataclass
class _sentry(price, volume):   # History entry for security
    price : float = price
    volume : int = volume

@dataclass
class security:
    name : str = ""
    price : float = 0
    volume : int = 0 
    history = []        # collection of past 100 cycles of volume and price

    def __repr__(self) -> str:
        return self.name + " : " + self.price + " : " + self.volume

    def record(self, o_price : float, o_volume : int):
        history.append(_sentry(o_price, o_volume))
        

@dataclass
class state:
    # dummy sec declaration
    s = { "ASS"  : security("ASS",  218.54,  3000000),
          "GAY"  : security("GAY",  21.34,   8500000),
          "RPG"  : security("RPG",  1.35,    800000),
          "LOL"  : security("LOL",  0.5,     120000000),
          "METH" : security("METH", 420.69,  3000000)]

    v100, p100 = {}
    total_v : int, total_p : int = 0

    def update(self):
        v100.clear()
        p100.clear()
        total_v, total_p = 0

        for sec in s:
            v = sum(s[sec].history[:100].volume)
            p = sum(s[sec].history[:100].volume)
            v100[sec.name] = v
            p100[sec.name] = p
            total_v += v
            total_p += p

    def record(self):
        for sec in s:
            sec.record(sec.price, sec.volume)
            sec.volume = 0

    #dump state
    def __repr__(self):
        for sec in s:
            print(sec.name + "\n" + "Price : " + sec.price + "\n" + "Current Volume : " + sec.volume)


# Participants
class prt:
    def __init__(self):
        self.nonce = random.randrange(1, 1000)  # measure of personal bias and irrationality
        self.tolerance = random.random()
        self.liquidity : int = 0 
        self.assets = np.zeros(NUM_OF_SECURITIES) 
        self.prob = uprob() 

    def __repr__(self):
        space = (20 - len(str(self.liquidity))) * " "   # nice console formatting
        return str(self.liquidity) + space + str(self.tolerance) + " "

    def uprob():
        a = 1

        for sec in s:
            price_avg = 0
            vol_avg = 0
            for frame in sec.history:
                price_avg += frame.price
                vol_avg += frame.volume
            price_avg /= sec.history.length
            vol_avg /= sec.history.length 
        
        # * calculate influence of price and volume from total of 100 cycles
        # * total volume = 1 . Persantage of each stock is redacted from this 1
        # * This biases both sides because high price will have way more influence on price average and cheap
        # stocks will have way more influence in volume average.
        #  * This can be canceled out by averaging the two probabilities at the end.



        # to take into account:
        #   * price 
        #   * volume
        #   * risk tolerance
        #   * nonce

        # calculate unbiased stock probability based on old data and then add personal bias
        
    def cycle():
        die()
        

def __bias_liq(num):
    g = np.random.gamma(.2, 2, num + 200)
    for i in range(len(g)-1):
        g[i]  = g[i] * 1000000;
        if g[i] < 10.:
            g[i] = None 
    g = g[np.logical_not(np.isnan(g))]        

    #plt.plot(g)
    #plt.show()
    #np.set_printoptions(suppress=True)
    #print(g)

    return g



class market_maker:
    def __init__(self):
        a = 1
        

# Irrelevant 

vals_tolerance = [] 
vals_liquidity = []

g = __bias_liq(1000)
for i in range(1000):
    obj = prt()
    obj.liquidity = g[i]
    vals_tolerance.append(obj.tolerance)
    vals_liquidity.append(obj.liquidity)
    print(obj)
    
vals = np.array(vals_liquidity)
plt.plot(vals)
plt.show()


