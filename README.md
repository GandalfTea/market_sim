&nbsp;
### About
Simulates a simple stock market with a variable number of securities and participants. Made to potentially test an implementation of an information or prediction market by updating a personal trust variable that acts as weight in the final outcome.

&nbsp;

### To Use
```bash
git clone https://github.com/gandalftea/market_sim.git
python run.py 
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

The program runs in cycles. Every cycle participants have a chance to trade.

Init:

* Initialize a set number of participants who have:
    * Random sum of money distributed in an exponential fashion 
    * Random risk tolerance (for now, will probably calibrate after every trade)
    * Personal bias variable to introduce irrationality
    * Buy / Sell algorithm 
* Init a number of securities :
    * Calculate unbiased probability of the stock going up every cycle (from the total influence over market, volatility and general market volatility)
    * Every participant modifies this probability by a vector of personal bias and decides wheather to buy or sell depending on risk variable and personal risk tolerance. 
* Market Maker :
    * Automatic price (if participant decides)
    * Partial execution of orders
  
&nbsp;

  
### TODO:
* Test market.py with some dummy thick tests.
* Multiprocessing (sim and market)
* Polish state dumps
