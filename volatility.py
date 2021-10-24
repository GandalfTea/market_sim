
from functools import reduce
import timeit
from gas import data
import matplotlib.pyplot as plt
import math

start = timeit.default_timer()
def volidity(prices, t):
    prices = prices[-t:]
    diff = []
    for i in range(len(prices)-1):
        v = abs((prices[i+1] - prices[i]) / prices[i+1])
        diff.append(v)
    return reduce(lambda a,b: a+b, diff) / len(diff)
stop = timeit.default_timer()

volatility_10 = volidity(data, 10)
volatility_100 = volidity(data, 100)
volatility_1000 = volidity(data, 6000)


def risk(v):
    return (2/(1+math.e**(-v / 0.01555)))-1

plt.plot(data)
plt.show()

print("10 : ",volatility_10)
print(risk(volatility_10))
print("100 : ",volatility_100)
print(risk(volatility_100))
print("6000 : ",volatility_1000)
print(risk(volatility_1000))

print('\033[92mTime: ' + f'{stop-start:.20f}')  

