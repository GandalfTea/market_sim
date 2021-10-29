# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 15:08:53 2021

@author: Louis
"""
#e**(mt+c)
#t was count 
import timeit
# import matplotlib as plt
# import sys
# # insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(1, 'market_sim/datasets')

# from gold.py import data as prices



start=timeit.default_timer()

def expoRegression(p):
    import math
    t=[]
    tcount=0
    for n in range(len(p)):
        t.append(tcount)
        tcount+=1
    pLin=[]
    for n in range(len(p)):
        pLin.append(math.log(p[n]))
    pLinMean=sum(pLin)/len(pLin)
    tMean=t[len(t)-1]/2
    gradients=[]
    for n in range(len(pLin)-1):
        gradients.append((pLin[n+1]-pLin[n]))
    m=sum(gradients)/len(gradients)
    c=pLinMean-m*tMean
    return([m,c])


#add t and change p2 afterwards
#using octavian's
def volitility(m,c,p):
    import math
    #p2=p[-t:]
    total=[]
    for n in range(len(p)):
        total.append(abs(p[n]-(math.e)**(m*n+c))/((math.e)**(m*n+c)))
    return sum(total)/len(total)


expo=expoRegression(prices)
cheese = volitility(expo[0],expo[1],prices)

stop = timeit.default_timer()
print(cheese)
totalTime= stop - start
print("Time:", f'{totalTime:.20f}')
