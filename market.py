import sys
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
class _sentry():   # History entry for security
    price : float = 0. 
    volume : int = 0

@dataclass
class security:
    name : str = ""
    price : float = 0.
    volume : int = 0 
    full_volume : int = 0
    history = []        # collection of past 100 cycles of volume and price

    def __repr__(self) -> str:
        return self.name + " : " + str(self.price) + " : " + str(self.volume)

    def record(self, o_price : float, o_volume : int):
        history.append(_sentry(o_price, o_volume))
        

@dataclass
class state:
    # dummy sec declaration
    s = { "ASS"  : security("ASS",  218.54,  3000000),
          "GAY"  : security("GAY",  21.34,   8500000),
          "RPG"  : security("RPG",  1.35,    800000),
          "LOL"  : security("LOL",  0.5,     120000000),
          "METH" : security("METH", 420.69,  3000000)}

    v100, p100 = {}, {}
    total_v : int = 0
    total_p : int = 0
    
    # called every cycle
    def init(self):
        self.update()
        self._probs()

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

    #dump state
    def __repr__(self):
        for sec in s:
            print(sec.name + "\n" + "Price : " + str(sec.price) + "\n" + "Current Volume : " + str(sec.volume))


    def record(self):
        for sec in s:
            sec.record(sec.price, sec.volume)
            sec.volume = 0


    # calculate unbiased stock probability 
    # RUNS ONCE PER CYCLE
    def _probs(self):

        # Calculate average price and volume over last 100 cycles per stock
        prc_avg = 0
        vol_avg = 0
        for key, sec in enumerate(self.s):
            for frame in self.s[sec].history:
                prc_avg += frame.price
                vol_avg += frame.volume
            try:
                prc_avg /= len(self.s[sec].history)
                vol_avg /= len(self.s[sec].history)
            except ZeroDivisionError:
                sys.exit("\033[91m FATAL ERROR: Division by zero in uprob(). No items found in history stack.\n")
            except:
                sys.exit("FATAL ERROR: Fatal error in uprob().")
         
        #    Stock Influence Variable
        # the influence of volume is heavily biased towards the lower priced stocks
        # we debias this by calculating the influence of mean price over mean total of all prices
        vol_inf =  1 - ((total_v - vol_avg) / total_v)
        prc_inf =  1 - ((total_p - prc_avg) / total_p)
        influence = (vol_inf + prc_inf) / 2


        #   Volidity Variable
        # Change in price : Linear regretion average for price over last 100 cycles
        # Inverse exponential danger toward higher values
        # Corelate with inverse exponential stored in cache 
        # 2 volatility variables, one 100 days, one last day
        # Calculate probabilitye from all 3 variables and store into memory for the cycle

        # Calculate R value 

        # At the end, you have 4 variables:
        #   * % change in market
        #   * Danger potential
        #   * Total Influence
        #   * Nonce

        # * calculate influence of price and volume from total of 100 cycles
        # * total volume = 1 . Persantage of each stock is redacted from this 1
        # * This biases both sides because high price will have way more influence on price average and cheap
        # stocks will have way more influence in volume average.
        #  * This can be canceled out by averaging the two probabilities at the end.
        


state = state()


# Participants
class prt:
    def __init__(self):
        self.nonce = random.randrange(1, 1000)  # measure of personal bias and irrationality
        self.tolerance = random.random()        # will be updated after every 10 cycles depending on trading results
        self.liquidity : int = 0                # init in __bias_liq() 
        self.assets = np.zeros(NUM_OF_SECURITIES) 
        #self.prob = self.pprob() 

    def __repr__(self):
        space = (20 - len(str(self.liquidity))) * " "   # nice console formatting
        return str(self.liquidity) + space + str(self.tolerance) + " "

    # personal probability. Adds bias and tolerance
    def pprob():
        die()

        
    def cycle():
        die()
        

def __bias_liq(num):
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
vals = np.sort(vals)
t_vals = np.sort(np.array(vals_tolerance))

figure, axis = plt.subplots(2, 2)
axis[0,0].plot(vals, linewidth=0.6)
axis[0,0].set_title("Liquidity dist")
axis[0,1].plot(t_vals ,linewidth=0.6)
axis[0,1].set_title("Tolerance dist")
plt.show()


