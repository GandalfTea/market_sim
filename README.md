&nbsp;

Stock market simulator made in python.

&nbsp;

### To Use
```bash
git clone https://github.com/gandalftea/market_sim.git
python market.py
```
   
   
```bash
-p [int]            Init number of participants
-s [int]            Init number of securities
-t                  Time Elapsed 
-v, -verbose        Verbose print all
-vs                 Verbose print securities details
-vp                 Verbose print participant information
-vm                 Verbose print market transaction details
--h, --help         Help
```

&nbsp;

### How it works:

The program runs in cycles. Every cycle participants have a chance to participate in trade.

Init:

* Initialize a number of participants who have:
    * Rand sum of money distributed in an exponential fashion 
    * Rand pressure tolerance (for now)
    * Security choosing algorithm 
    * Buy / Sell algorithm
* Init a number of securities :
    * Calculate unbiased probability of the stock going up every cycle
    * Every participant modifies this probability by a vector of personal bias.
* Market Maker :
    * Partial execution
    * No auto pricing (for now)
