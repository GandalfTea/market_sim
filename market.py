
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
#@dataclass
#class _sentry(price, volume):   # History entry for security
#    price : float = price
#    volume : int = volume

@dataclass
class security:
    name : str = ""
    price : float = 0
    volume : int = 0 
    history = []        # collection of past 100 cycles of volume and price

    def __repr__(self) -> str:
        return self.name + " : " + self.price + " : " + self.volume

# dummy sec declaration
s = [ security("ASS", 218.54,  3000000),
      security("GAY", 21.34,   8500000),
      security("RPG", 1.35,    800000),
      security("LOL", 0.5,     120000000),
      security("METH", 420.69, 3000000)]



# Participants
class prt:
    def __init__(self):
        self.nonce = random.randrange(1, 1000)  # measure of personal bias and irrationality
        self.tolerance = random.random()
        self.liquidity : int = 0 
        self.assets = np.zeros(NUM_OF_SECURITIES) 
        #self.prob = uprob() 

    def __repr__(self):
        space = (20 - len(str(self.liquidity))) * " "   # nice console formatting
        return str(self.liquidity) + space + str(self.tolerance) + " "

    def uprob():
        a = 1
        
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


