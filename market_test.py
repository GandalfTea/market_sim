import imports as imp
import sim as sim
import market as mk
import random


# To Test:
#   * Order matching
#   * Order execution
#   * Not enough funds or securities
#   * Price update


imp.MARKET_TESTING = True
class user:
    def __init__(self, acc):
        self.acc = acc
        self.liquidity = random.randint(100, 1000)
        self.assets = {
            "DICK" : random.randint(0, 100),
            "BALLS" : random.randint(0, 100),
            "GAY" : random.randint(0, 100),
            "HEY" : random.randint(0, 100),
            "GURL" : random.randint(0, 100),
            "GAMER" : random.randint(0, 100),
            "HIT" : random.randint(0, 100),
            "OR" : random.randint(0, 100),
            "MISS" : random.randint(0, 100),
        }
sec = ["DICK", "BALLS", "GAY", "HEY", "GURL", "GAMER", "HIT", "OR", "MISS"]
prc = [202, 25, 458, 54, 23, 154, 89, 874, 54]
RUN_TIMES = 10000
market = mk.market()


def test_matching():
    print("TESTING: Matching")
    for i in range(10000000):
        for i in range(RUN_TIMES):
            acc = i
            imp.PARTICIPANTS.append(user(i))
            idx =  random.randint(0,len(sec)-1)
            security = sec[idx]
            otype = "BUY" if random.random() > 0.5 else "SELL"
            price = prc[idx] + random.randrange(0, 20) 
            qty = random.randint(1, 200)
            market.create_order(acc, security, otype, price, qty)
        try:
            market._match()
        except ValueError:
            print("TEST FAILED: ValueError raised.")
            break
    print("TEST COMPLETED")

def test_execution():
    for i in range(RUN_TIMES):
        acc = i
        imp.PARTICIPANTS.append(user(i))
        idx =  random.randint(0,len(sec)-1)
        security = sec[idx]
        otype = "BUY" if random.random() > 0.5 else "SELL"
        price = prc[idx] + random.randrange(0, 20) 
        qty = random.randint(1, 200)
        market.create_order(acc, security, otype, price, qty)
    market._match()

def test_errors():
    RUN_TIMES = 4
    for i in range(RUN_TIMES):
        acc = i
        imp.PARTICIPANTS.append(user(i))
        idx =  random.randint(0,len(sec)-1)
        security = sec[idx]
        otype = "BUY" if random.random() > 0.5 else "SELL"
        price = prc[idx] + random.randrange(0, 20) 
        qty = random.randint(1, 200)
        market.create_order(acc, security, otype, price, qty)
    


tests = [test_matching, test_execution]


for i in range(2):
    func = tests[i]
    func()
    print("\n\nPress ENTER to continue")
    input("")
