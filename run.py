
from market import market

import sim
import timeit
import math
import matplotlib.pyplot as plt
import numpy as np
import imports as imp


def start():
    # Init state and initial probs 
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

    # Init Participants
    start = timeit.default_timer()
    g = sim.__bias_liq(1000)
    for i in range(1000):
        #print("\n")
        obj = sim.prt(i)
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
    

    
    #     Plot
    vals = np.array(vals_liquidity)
    vals = np.sort(vals)
    t_vals = np.sort(np.array(vals_tolerance))

    axis[1,0].set(ylim=(-1,1))

    axis[0,0].plot(vals, linewidth=0.6)
    axis[0,0].set_title("Liquidity dist")
    axis[0,1].plot(t_vals ,linewidth=0.6)
    axis[0,1].set_title("Tolerance dist")
    #plt.show()

    while True:
        print("")


# Main Menu

while True:
    print("\n~sim > ", end="")
    i = input()
    if i == "start":
        start()
    elif i == ".exit" or i == "exit":
        break
    elif i == ".help":
        print("\nstart \t\t\t: Start Simulation")
        print("p [num] \t\t: Set number of participants")
        print("s [num] \t\t: Set number of securities")
        print("bset [int] [int] \t: Set brake points at iteration number")
        print("brm [int] [int] \t: Remove brake points at iteration number")
        print("set [int] \t\t: Set running time in iteration")
        print("set none \t\t: Set running time to infinite")
        print("what \t\t\t: Print all current settings")
        print(".exit \t\t\t: Exit aplication")
    elif "bset" in i:
        i = i.split(" ")
        for n in i[1:]:
            try:
                brk = int(n)
                imp.BRAKEPOINTS.append(brk)
                imp.BRAKEPOINTS.sort()
            except ValueError:
                print("Error: brakepoint index value is not int")
        print("Brakepoints : ", imp.BRAKEPOINTS)
    elif "brm" in i:
        i = i.split(" ")
        for n in i[1:]:
            try:
                brk = int(n)
                imp.BRAKEPOINTS.remove(brk)
            except ValueError:
                print("Error: value is not an int or breakepoint does not exist")
        print("Brakepoints : ", imp.BRAKEPOINTS)
    elif "set" in i:
        i = i.split(" ")
        if len(i) >= 3:
            print("Error: Too many values. Only one value accepted.")
        if i[1] == "none":
            imp.RUNNING_TIME = -1
            print("Running Cycles : infinite")
        elif len(i) == 2:
            try:
                fin = i[1]
                imp.RUNNING_TIME = fin
                print("Running Cycles : ", imp.RUNNING_TIME)
            except ValueError:
                print("Error: value is not an int.")
        else:
            print("Command not recognized. Do .help for a list of al commands")
    elif i == "what":
        print("\nParticipants : ", imp.NUM_OF_PARTICIPANTS)
        print("Securities : ", imp.NUM_OF_SECURITIES)
        if imp.VERBOSE or imp.VERBOSE_PARTICIPANTS or imp.VERBOSE_SECURITIES or imp.VERBOSE_MARKET:
            print("Printing : ", end="")
        if imp.VERBOSE:
            print(" verbose", end="")
        if imp.VERBOSE_PARTICIPANTS:
            print(" participants", end="")
        if imp.VERBOSE_SECURITIES:
            print(" securities", end="")
        if imp.VERBOSE_MARKET:
            print(" market", end="")
        if imp.TIME_ELAPSED:
            if imp.VERBOSE or imp.VERBOSE_PARTICIPANTS or imp.VERBOSE_SECURITIES or imp.VERBOSE_MARKET:
                print("\n", end="")
            print("Calculating time elapsed")
        print("Brakepoints : ", imp.BRAKEPOINTS)
        if imp.RUNNING_TIME != -1:
            print("Running Cycles : ", imp.RUNNING_TIME)
        elif imp.RUNNING_TIME == -1:
            print("Running Cycles : infinite")
    elif "p" in i:
        i = i.split(" ")
        if len(i) > 2:
            print("Error: Too many values. Only one value accepted.")
        elif len(i) == 2:
            try:
                num = int(i[1])
                imp.NUM_OF_PARTICIPANTS = num
                print("Participants : ", imp.NUM_OF_PARTICIPANTS)
            except ValueError:
                print("Error: value is not an int.")
        else:
            print("Command not recognized. Do .help for a list of al commands")
    elif "s" in i:
        i = i.split(" ")
        if len(i) > 2:
            print("Error: Too many values. Only one value accepted.")
        elif len(i) == 2:
            try:
                num = int(i[1])
                imp.NUM_OF_SECURITIES = num
                print("Securities : ", imp.NUM_OF_PARTICIPANTS)
            except ValueError:
                print("Error: value is not an int.")
        else:
            print("Command not recognized. Do .help for a list of al commands")
    else:
        print("Command not recognized. Do .help for a list of al commands")

