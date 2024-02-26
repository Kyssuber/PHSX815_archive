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
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)

    #default prob0 list (fair die)
    p0 = [1/6,1/6,1/6,1/6,1/6,1/6]
    p0 = np.asarray(p0)
    print('p0: ',p0)
    
#note: prob_1 will differ slightly for this project, since there is an additional parameter to consider.
#p1_list = [N1/Ntot,N2/Ntot,N3/Ntot,N4/Ntot,N5/Ntot,N6/Ntot]
    
    
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
        
        
#the following creates probability vector for H0 dice rolls given list input (-prob0) 
        
    if '-prob0' in sys.argv:
        p = sys.argv.index('-prob0')
        ptemp = sys.argv[p+1]
        ptemp = list(ptemp.strip('[]').split(','))
        B = []
        for item in ptemp:
            B.append(float(eval(item)))
        p0 = B
        p0 = np.asarray(p0)
        print('p0: ',p0)                  
                     
             
    if '-h' in sys.argv or '--help' in sys.argv or not haveH0:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print ("   -input0 [filename]  name of file for H0 data")
        print ("   -input1 [filename]  name of file for H1 data")
        print ("   -prob0 [list]     probability list for single die roll for H0")
        #print ("   -prob1 [list]     probability list for single die roll for H1")
        print
        sys.exit(1)
    
    #arbitary value for Nroll ... will change to correct integer below.
    Nroll = 1
    Npass3_H0 = []
    LogLikeRatio0 = []
    Npass3_H1 = []
    LogLikeRatio1 = []


    
#I will create H1 LLR first, since the routine involves the creation of p1 (which is then necessary for H0 LLR)
    
    
    if haveH1:
        #the following generates empirical probability vector for p1
        Npass1 = 0
        Npass2 = 0
        Npass3 = 0
        Npass4 = 0
        Npass5 = 0
        Npass6 = 0
        with open(InputFile1) as ifile:
            for line in ifile:
                lineVals = line.split()
                Nroll = len(lineVals)
                
                for v in lineVals:
                    if str(v) == str(1):
                        Npass1 += float(1)
                    if str(v) == str(2):
                        Npass2 += float(1)
                    if str(v) == str(3):
                        Npass3 += float(1)
                    if str(v) == str(4):
                        Npass4 += float(1)
                    if str(v) == str(5):
                        Npass5 += float(1)
                    if str(v) == str(6):
                        Npass6 += float(1)

            #the modified p1 list is now (combining both die)...
            Npass = [Npass1,Npass2,Npass3,Npass4,Npass5,Npass6]
            Npass = np.asarray(Npass)
            Ntot = np.sum(Npass)
            p1 = Npass/Ntot
            print('p1: ',p1)
        
        
        
        #NOW test Npass3 per line...acquire LogLikeRatio1 list                   
        with open(InputFile1) as ifile:
            for line in ifile:
                lineVals = line.split()
                Nroll = len(lineVals)
                Npass3 = 0
                LLR = 0
                for v in lineVals:
                    if str(v) == str(3):
                        Npass3 += float(1)
                    LLR += math.log( p1[int(v)-1]/p0[int(v)-1] )
                    Npass3_H1.append(Npass3)
                    LogLikeRatio1.append(LLR)
                                        

    
    
    
    with open(InputFile0) as ifile:
        for line in ifile:
            lineVals = line.split()
            Nroll = len(lineVals)
            #success counters for 1,2,3,4,5,6 "rolls" of random number generator...begin at 0
            #will count how often each "roll" occurs
            Npass3 = 0
            
            LLR = 0
            for v in lineVals:
# += adds a number to the variable, changing the variable in the process. x=2 --> x += 5 --> x=7
# will count number of occurrences of 3 per line
                if str(v) == str(3):
                    Npass3 += float(1)                    
                
#if there is an incidence of 3, then grab the probability of a 3 roll according to H1 and divide by that of H0 (since p1, p0 are vector arrays, grab element in index 2 (which will be probability for 3)). Does likewise (pun intended) for other integer rolls.
                LLR += math.log( p1[int(v)-1]/p0[int(v)-1] )
                Npass3_H0.append(Npass3) 
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
    beta = np.max(LLR1_below_lamb[0])/len(LogLikeRatio1)
    
    print('beta:',np.max(LLR1_below_lamb[0])/len(LogLikeRatio1))
    
    
#note --> find beta values for various types of Nexp and Nmeas, compare and contrast in paper
                
                

    title = str(Nroll) +  " rolls / experiment"
    print(np.max(Npass3_H0))            
    # make Npass figure
    plt.figure()
    

    plt.hist(Npass3_H0, bins=np.arange(0,Nroll+1,1), density=True, facecolor='b', alpha=0.5, label="assuming $\\mathbb{H}_0$")
    if haveH1:
        plt.hist(Npass3_H1, bins=np.arange(0,Nroll+1,1), density=True, facecolor='g', alpha=0.7, label="assuming $\\mathbb{H}_1$")
        plt.legend()
    plt.xlabel('$\\lambda = N_{pass}$' + ' (Incidence of 3 per line)')
    plt.ylabel('Probability')
    plt.title(title)
    plt.grid(True)

    plt.show()

    # make LLR figure
    plt.figure()
    plt.hist(LogLikeRatio0, bins = 15, density=True, facecolor='b', alpha=0.5, label="assuming $\\mathbb{H}_0$")
    if haveH1:
        plt.hist(LogLikeRatio1, bins=15,density=True, facecolor='g', alpha=0.7, label="assuming $\\mathbb{H}_1$")
        
        plt.axvline(x=critical_lambda,label=r'$\lambda_c =$'+ ' ' + str("%.4f" % critical_lambda))
        plt.text(9,0.19,r'$\beta =$' + str("%.3f" % beta))
        plt.text(2,0.2,r'$\lambda _c$',label='test')
        
        plt.legend()
    plt.xlabel('$\\lambda = \\log({\\cal L}_{\\mathbb{H}_{1}}/{\\cal L}_{\\mathbb{H}_{0}})$')
    plt.ylabel('Probability')
    plt.title(title)
    plt.grid(True)

    plt.show()