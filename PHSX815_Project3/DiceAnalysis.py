from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.optimize import curve_fit

# import our Random class from Random.py file
sys.path.append(".")
from Random import Random


# main function for dice roll Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)

    #default p3 (fair die)
    p3 = 1/6
    
    if '-input' in sys.argv:
        p = sys.argv.index('-input')
        InputFile = sys.argv[p+1]
        
        
    if '-p3' in sys.argv:
        p = sys.argv.index('-p3')
        p3 = sys.argv[p+1]
        print('true probability: ',p3)                  
                     
             
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print ("   -input [filename]  name of file for data")
        print ("   -p3_true [fraction]    true probability p3 for single die roll")
        print
        sys.exit(1)

        
    p3_hat_list = []

    #Npass3 counter
    Npass3 = 0
    N_not3 = 0
    
    
    #fill p3_hat_list (empirical p3_hat for each experiment)
    with open(InputFile) as ifile:
        
        for line in ifile:
            lineVals = line.split()
            Nroll = len(lineVals)    
            Npass3_list = 0
            for v in lineVals:
                if str(v) == str(3):
                    Npass3_list += float(1)       
            p3_hat_list.append(Npass3_list/Nroll)
                
    #the following represents a discrete posterior distribution of the data; gives likelihood (since histogram is a function of p_true). 
    #will resemble Gaussian distribution
    #I define the mean of this distribution to represent the sort of p_best 
    mu, sigma = norm.fit(p3_hat_list)
    
    title = str(Nroll) +  " rolls / experiment"       
    plt.figure()
    
    n = plt.hist(p3_hat_list, bins=Nroll+20, facecolor='b')
    plt.xlabel('$\hat p$' + ' (N3/Nroll per experiment)')
    plt.ylabel('Counts')
    plt.title(title)
    plt.grid(True)

    plt.show()
    
    #defining p_approx to represent the mean of the posterior distribution
    p_approx = mu
    print('p_approx from histogram:',p_approx)
    
    
    #the next task is to generate likelihood arrays for the experimental data, given p_approx and the p_hat values for each experiment, as doing so will ultimately yield the p_approx uncertainties necessary to communicate results. Treating the dice rolls as generating a Bernoulli distribution (either face-3 or not face-3),
    
    likelihood_approx = []
    likelihood_array = []
    Ntot = 0
    Npass3_tot = 0
    p3 = []
    
    with open(InputFile) as ifile:
        for line in ifile:
            lineVals = line.split()
            Npass3 = 0
            N_not3 = 0
            for v in lineVals:
                if str(v) == str(3):
                    Npass3 += float(1)
                    Npass3_tot += float(1)
                else:
                    N_not3 += float(1)
                Ntot += 1
            L_p = ((p_approx)**Npass3) * ((1-p_approx)**N_not3)
            likelihood_approx.append(L_p)
            #gives p_hat values for each experiment, appends them to likelihood_array
            L_p_array = ((Npass3/(Nroll))**Npass3) * (((N_not3/(Nroll)))**N_not3)
            likelihood_array.append(L_p_array)
            
            p3.append(Npass3/(N_not3+Npass3))
    
    likelihood_approx = np.asarray(likelihood_approx)
    likelihood_array = np.asarray(likelihood_array)
    
    
    
    #LLR = np.log(likelihood_approx/likelihood_array)
    LLR = np.log(likelihood_approx/likelihood_array)
    
    
    #the maximum of the LLR will be p_approx
    #the uncertainty (+/- one sigma) is given by the points at which the LLR = -1/2.
    #(that is, the interval of p3 such that their LLR >= 1/2.
    #since none are precisely -1/2, I first flag LLR values < -0.50.
    one_sigma_p_flag = (LLR>-0.50)
    #I will now try to isolate the point(s) nearest to this -1/2 mark, both to the left and to the right of the maximum (p_approx)
    left_half_p3_flag = (p3 < p_approx)
    right_half_p3_flag = (p3 > p_approx)
    LLR_left_flag = one_sigma_p_flag & left_half_p3_flag
    LLR_right_flag = one_sigma_p_flag & right_half_p3_flag
    
    LLR_mark_lower = np.min(LLR[LLR_left_flag])
    LLR_mark_upper = np.min(LLR[LLR_right_flag])
    print('LLR nearest to -1/2:')
    print('LLR to left,',LLR_mark_lower)
    print('LLR to right,',LLR_mark_upper)
    
    #convert list of p_hat values, denoted p3 here, into numpy array
    p3=np.asarray(p3)
    #find min and max of p_hat (p3) array
    lower_p3 = p3[(np.where(LLR == LLR_mark_lower))[0]]
    upper_p3 = p3[(np.where(LLR == LLR_mark_upper))[0]]
    
    #And, lastly, calculate the +1 sigma and -1 sigma values.
    sigma_1_up = np.abs(upper_p3 - p_approx)
    sigma_1_low = np.abs(p_approx - lower_p3)    
    
    print('p_best:','%0.3f'%p_approx)
    print('Lower uncertainty estimate (data):','%0.4f'%(np.mean(sigma_1_low)))
    print('Upper uncertainty estimate (data):','%0.4f'%(np.mean(sigma_1_up)))
    
    #the following prints p_true for comparison, but only if user inputs initial p_true used to generate data with the first program. 
    try:
        print('p_true',p3_true)
    except:
        print('no p_true given')
    
    
    def func(p,unc):
        return -(p - p_approx)**2 /(2*unc**2)
    

    
    plt.figure()
    plt.scatter(p3,LLR,s=2)
    plt.axhline(-0.5,color='steelblue',linestyle='--',alpha=0.5,label='-1/2 line')
    #plt.axvline(p_approx,color='r',linestyle='--',alpha=0.5)
    plt.ylabel('LLR',fontsize=16)
    plt.xlabel('p3',fontsize=16)
    
    p3_sort = np.sort(p3)
    LLR_sort = np.sort(LLR)

    popt,pcov = curve_fit(func,p3,LLR)
    plt.plot(p3_sort,func(p3_sort,*popt),'r-',label='fit')
    if popt[0] > 0:
        print('Uncertainty from curve_fit:','%0.3f'%(popt[0]))
    else:
        print('Uncertainty from curve_fit:','%0.3f'%(-1*popt[0]))
    plt.legend()
    plt.show()    
    
