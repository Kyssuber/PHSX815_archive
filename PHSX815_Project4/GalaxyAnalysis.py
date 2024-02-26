from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from Random import Random


# main function for dice roll Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print ("   -input0 [filename]  name of file for H0 data")
        print ("   -input1 [filename]  name of file for H1 data")
        print
        sys.exit(1)
    
    
    
    # default single probabilities for field
    p1_0 = 0.01266
    p2_0 = 0.06674
    p3_0 = 0.25547
    p4_0 = 0.29459
    p5_0 = 0.22325
    p6_0 = 0.09551
    p7_0 = 0.02532
    p8_0 = 0.00230
    
    # default single probabilities for cluster
    p1_1 = 0.02514
    p2_1 = 0.06425
    p3_1 = 0.15363
    p4_1 = 0.25698
    p5_1 = 0.20670
    p6_1 = 0.16760
    p7_1 = 0.08380
    p8_1 = 0.01955

    prob0_list = [p1_0,p2_0,p3_0,p4_0,p5_0,p6_0,p7_0,p8_0]
    prob1_list = [p1_1,p2_1,p3_1,p4_1,p5_1,p6_1,p7_1,p8_1]
    print('probabilities of field masses: ', prob0_list)
    print('probabilities of cluster masses: ',prob1_list)
    
    
    haveH0 = False
    haveH1 = False
    
    if '-input0' in sys.argv:
        p = sys.argv.index('-input0')
        InputFile0 = sys.argv[p+1]
        haveH0 = True
    if '-input1' in sys.argv:
        p = sys.argv.index('-input1')
        InputFile1 = sys.argv[p+1]
        haveH1 = True
                             
             

    
    #arbitary value for Nroll ... will change to correct integer below.
    Nroll = 1
    #field
    Npass678_H0 = []
    LogLikeRatio0 = []
    #cluster
    Npass678_H1 = []
    LogLikeRatio1 = []


    
#LLR_1 --> number of galaxies that occupy bin 6, 7, or 8
    
    if haveH1:
        #NOW test Npass6,Npass7,Npass8 per line...acquire LogLikeRatio1 list                   
        with open(InputFile1) as ifile:
            for line in ifile:
                lineVals = line.split()
                Nroll = len(lineVals)
                Npass678 = 0
                LLR = 0
                for v in lineVals:
                    if (str(v) == str(6))|(str(v) == str(7))|(str(v) == str(8)):
                        Npass678 += float(1)
                    LLR += math.log( prob1_list[int(v)-1]/prob0_list[int(v)-1] )
                    Npass678_H1.append(Npass678)
                    LogLikeRatio1.append(LLR)

    
    
    with open(InputFile0) as ifile:
        for line in ifile:
            lineVals = line.split()
            Nroll = len(lineVals)
            #success counters for 1,2,3,4,5,6,7,8 "rolls" of random number generator...begin at 0
            #will count how often each "roll" occurs
            Npass678 = 0
            LLR = 0
            for v in lineVals:
# += adds a number to the variable, changing the variable in the process. x=2 --> x += 5 --> x=7
# will count number of occurrences of 3 per line
                if (str(v) == str(6))|(str(v) == str(7))|(str(v) == str(8)):
                    Npass678 += float(1)                    
                
#if there is an incidence of 3, then grab the probability of a 3 roll according to H1 and divide by that of H0 (since p1, p0 are vector arrays, grab element in index 2 (which will be probability for 3)). Does likewise (pun intended) for other integer rolls.
                LLR += math.log( prob1_list[int(v)-1]/prob0_list[int(v)-1] )
                Npass678_H0.append(Npass678) 
                LogLikeRatio0.append(LLR)



                
#let alpha = 0.05 such that there is only a 5% chance of a false positive
# --> if we observe a value that only has a 5% chance of occurring assuming H0, then 
#we can reject H0 given the assigned alpha
    
    alpha = 0.05    
    
#sort LogLikeRatio0 using np.sort...then find 9500th entry, assuming Ntot is 10000. This value will, by definition, be the critical lambda value, since the values to its right (considered in total) will comprise 5%, or 0.05, of the sample.
    
    LogLikeRatio0_sorted = np.sort(LogLikeRatio0)
    
    critical_lambda = LogLikeRatio0_sorted[int(.95*len(LogLikeRatio0))]
    print('critical_lambda:', critical_lambda)
    
#find beta...sort LogLikeRatio1, find maximum index for which the LogLikeRatio1 values are below critical_lambda, extract its value, divide by total number of experiments to find fraction 
    
    LogLikeRatio1_sorted = np.sort(LogLikeRatio1)
    LLR1_below_lamb = np.where(LogLikeRatio1_sorted < critical_lambda)
    try:
        beta = np.max(LLR1_below_lamb[0])/len(LogLikeRatio1)
        print('beta:',np.max(LLR1_below_lamb[0])/len(LogLikeRatio1))
    except:
        beta = LLR1_below_lamb[0]/len(LogLikeRatio1)
        print('beta:',LLR1_below_lamb[0]/len(LogLikeRatio1))
    
#note --> find beta values for various types of Nexp and Nmeas, compare and contrast in paper
                
                

    title = str(Nroll) +  " rolls / experiment"
    
    print('maximum number of 678 passes for field galaxies: ',np.max(Npass678_H0))            
    # make Npass figure
    plt.figure()
    
    #normalization routine
    weights_field = np.ones_like(Npass678_H0) / len(Npass678_H0)
    weights_cluster = np.ones_like(Npass678_H1) / len(Npass678_H1)    

    
    plt.hist(Npass678_H0, bins=np.arange(0,Nroll+1,1), weights=weights_field, facecolor='b', alpha=0.5, label="assuming $\\mathbb{H}_0$")
    if haveH1:
        plt.hist(Npass678_H1, bins=np.arange(0,Nroll+1,1), weights=weights_cluster, facecolor='g', alpha=0.7, label="assuming $\\mathbb{H}_1$")
        plt.legend()
    plt.xlabel('$\\lambda = N_{pass}$' + ' (Incidence of 6, 7, or 8 per line)')
    plt.ylabel('Probability')
    plt.title(title)
    plt.grid(True)

    plt.show()

    
    
    
    #normalization routine
    weights_field2 = np.ones_like(LogLikeRatio0) / len(LogLikeRatio0)
    weights_cluster2 = np.ones_like(LogLikeRatio1) / len(LogLikeRatio1)
    
    # make LLR figure
    plt.figure()
    plt.hist(LogLikeRatio0, bins = 100, weights=weights_field2, facecolor='b', alpha=0.5, label="assuming $\\mathbb{H}_0$")
    if haveH1:
        plt.hist(LogLikeRatio1, bins=100,weights=weights_cluster2, facecolor='g', alpha=0.7, label="assuming $\\mathbb{H}_1$")
        
        plt.axvline(x=critical_lambda,label=r'$\lambda_c =$'+ ' ' + str("%.4f" % critical_lambda))
        plt.plot([], [], ' ', label=r'$\beta =$' + str("%.3f" % beta))
        
        plt.legend()
    plt.xlabel('$\\lambda = \\log({\\cal L}_{\\mathbb{H}_{1}}/{\\cal L}_{\\mathbb{H}_{0}})$')
    plt.ylabel('Probability')
    plt.title(title)
    plt.grid(True)

    plt.show()