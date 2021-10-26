
#from market import market
import sim
import timeit
import math
import matplotlib.pyplot as plt
import numpy as np
import imports as imp


start = timeit.default_timer()
state = sim.state()
state._probs()
stop = timeit.default_timer()
print("\n\n")
if imp.TIME_ELAPSED or imp.VERBOSE: print(f'{imp.bcolors.OKGREEN}State cycle start time: ' + f'{stop-start:.20f}{imp.bcolors.ENDC}')  


vals_tolerance = [] 
vals_liquidity = []
probs = {} 

figure, axis = plt.subplots(2, 2)


start = timeit.default_timer()
g = sim.__bias_liq(1000)
for i in range(1000):
    #print("\n")
    obj = sim.prt()
    obj.liquidity = g[i]
    obj.probs = obj.pprob()
    vals_tolerance.append(obj.tolerance)
    vals_liquidity.append(obj.liquidity)
    if(imp.VERBOSE_PARTICIPANTS): print("\nLiquidity :" + str(obj.liquidity) + " \nTolerance :  " + str(obj.tolerance) + " \nNonce : " + str(obj.nonce) + " \nProbs : " + str(obj.probs))
    if(len(obj.probs) != 0):
        for i in obj.probs:
            #print(str(obj.probs[i][1][0]) + " " + str(state.probs[i][0]))
            probs[i] = [obj.probs[i][1][0], state.probs[i][0]]
            axis[1,0].plot(probs[i], linewidth=0.3)

stop = timeit.default_timer()
if(imp.TIME_ELAPSED or imp.VERBOSE): print(f'{imp.bcolors.OKGREEN}Participant initialization time: ' + f'{stop-start:.20f}{imp.bcolors.ENDC}')  
    
vals = np.array(vals_liquidity)
vals = np.sort(vals)
t_vals = np.sort(np.array(vals_tolerance))

axis[1,0].set(ylim=(-1,1))

axis[0,0].plot(vals, linewidth=0.6)
axis[0,0].set_title("Liquidity dist")
axis[0,1].plot(t_vals ,linewidth=0.6)
axis[0,1].set_title("Tolerance dist")
plt.show()


