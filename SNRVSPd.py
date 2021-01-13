#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:39:50 2021

@author: mac
"""

#import libararies
import numpy as np
from scipy import special as sp
import math
import matplotlib.pyplot as plt

#--------------------------------------------------------
#initilizations

snr_dB = np.arange(-20, 0, 1) # SNR interval 
snr = pow(10,(snr_dB/10)) #Linear value of SNR 
pf = 0.2 # probability of false alarm
pd = [None] * len(snr_dB)  # probability of detection
pmd = [None] * len(snr_dB) # probability of miss detection
L = 1000 #Number of samples

#--------------------------------------------------------
#Simulation to plot SNR vs. Probability of Detection (Pd)
 
for m in range(0,len(snr_dB)):
    detect = 0
    for k in range(0,10000):#Number of Monte Carlo Simulations
        n = np.random.randn(1,L)#AWGN noise with mean 0 and variance 1
        s = math.sqrt(snr[m])*np.random.randn(1,L) #Real valued Gaussina Primary User Signal
        y = s+n
        energy = pow(abs(y),2)#Energy of received signal over L samples
        Statistic_test = np.sum(energy)*(1/L) #statistic test 
        val = 1-2*pf
        thresh = ((math.sqrt(2)*sp.erfinv(val))/ math.sqrt(L))+1
        if(Statistic_test >= thresh):
            detect += 1
    pd[m] = detect/k
    pmd[m] = 1-pd[m]
 
#--------------------------------------------------------    
# simulation plots
    
plt.plot(snr_dB,pd)
plt.title("ROC curve for SNR vs Probability of Detection for Pf=0.2")
plt.xlabel("Signal To Noise Ratio (dB)")
plt.ylabel("probability of detection");
plt.show()
