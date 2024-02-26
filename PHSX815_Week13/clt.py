#!/usr/bin/env python
# coding: utf-8


import sys
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import beta as scipybeta
from numpy.random import beta as npbeta


sys.path.append(".")


# main function
if __name__ == "__main__":

    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-Ntrial number] [-Nexp number]" % sys.argv[0])
        print
        sys.exit(1)

        
    # default number of trials (per experiment)
    N_samples = 50

    # default number of experiments
    M_exp = 100
           
    
    if '-Ntrial' in sys.argv:
        p = sys.argv.index('-Ntrial')
        ptemp = int(sys.argv[p+1])
        N = ptemp
        if N > 0:
            N_samples = N
        else:
            print('Enter positive Ntrial arg.')

    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        M = int(sys.argv[p+1])
        if M > 0:
            M_exp = M
        else:
            print('Enter positive Nexp arg.')
 


    #the probability distribution from which to sample --> beta function with parameters a, b
    a,b=7,3
    
    x = np.arange (0.01, 1, 0.01)
    y = scipybeta.pdf(x,a,b)
    plt.figure()
    plt.plot(x,y,label = r'$\alpha =$' + str(a) +', '+ r'$\beta =$' + str(b))
    plt.xlabel('x',fontsize=16)
    plt.ylabel(r'Beta($\alpha, \beta$)',fontsize=16)
    plt.legend(fontsize=10)
    plt.title('Non-Normalized, Continuous Prob Distribution',fontsize=15)
    plt.show()


    average_list = []
    for i in range(0,M_exp):    
        vals=[]
        for i in range(0,N_samples):
            vals.append(npbeta(a,b))
        vals = np.asarray(vals)    
        average = np.mean(vals)
        average_list.append(average)

    plt.hist(average_list,bins=50)
    plt.xlabel('x',fontsize=14)
    plt.ylabel('Counts',fontsize=14)
    #plt.legend(fontsize=15)
    plt.title(str(M_exp)+' Exp, '+str(N_samples)+' Samples per Exp.',fontsize=15)
    plt.show()



