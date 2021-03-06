#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:36:42 2021

@author: mac
"""

#import libararies
import numpy as np
from scipy import special as sp
import math
import matplotlib.pyplot as plt

#--------------------------------------------------------
#initilizations

snr_dB = -10  # fSNR in dB
snr = pow(10,(snr_dB/10)) #Linear value of SNR 
pf = np.arange(0.01, 1, 0.01)# probability of false alarm 
pd = np.arange(0.01, 1, 0.01)# probability of detection
pmd = np.arange(0.01, 1, 0.01)# probability of miss detection
L = 1000 #Number of samples
thresh = [None] * len(pf) # the threshold

#--------------------------------------------------------
#Simulation to plot Probability of miss Detection (Pd) vs. Probability of False Alarm (Pf) 

for m in range(0,len(pf)):
    detect = 0
    for k in range(0,10000):#Number of Monte Carlo Simulations
        n = np.random.randn(1,L)#AWGN noise with mean 0 and variance 1
        s = math.sqrt(snr)*np.random.randn(1,L) #Real valued Gaussina Primary User Signal
        y = s+n
        energy = pow(abs(y),2)#Energy of received signal over L samples
        Statistic_test = np.sum(energy)*(1/L)
        val = 1-2*pf[m]
        thresh[m] = ((math.sqrt(2)*sp.erfinv(val))/ math.sqrt(L))+1
        if(Statistic_test >= thresh[m]):
            detect += 1
    pd[m] = detect/k
    pmd[m]= 1-pd[m]

#--------------------------------------------------------    
# simulation plots
    
plt.plot(pf,pmd)
plt.title("Pf Vs Pmd")
plt.xlabel("probability of false alarm")
plt.ylabel("probability of miss detection");
plt.show()
