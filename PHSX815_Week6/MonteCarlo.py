#!/usr/bin/env python
# coding: utf-8


#Implement a Monte Carlo integration to a function in one or more dimensions. 
#Quantify the accuracy of your MC integral as a function of the number of sample 
#points and compare with the accuracy of your deterministic methods from HW6.

#generic steps of random sampling to approximate area under curve:
#---let Ntot = # throws
#if Ntot[i] is under the curve, 
#increment "Nexcept"
#then, approximate area under curve with Nexcept/Ntot

import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import quadrature
import random
from fractions import Fraction

import sys

sys.path.append(".")



def GausQuadVal(func,a,b):
    return quadrature(func,a,b)[0]
    
    
def GausQuadErr(func,a,b):
    return quadrature(func,a,b)[1]


    
def MonteCarlo(Nsample):

    #plotting f(x)
    plt.figure(figsize=(8,6))
    
    #x values
    x = np.linspace(start=a,stop=b,num=Nsample)  
    #array of f(x) values
    fx = func(x)

    #restricting y-range, in case f(x) extends beyond b or below a
    #fx_flag = (fx<=b) & (fx>=a)
    #fx = fx[fx_flag]
    #x[y_flag] ensures x and y are identical length arrays
    #x = x[fx_flag]

    plt.plot(x,fx)
    plt.xlabel('x',fontsize=16)

    #generate two random numbers between 0 and 1 (uniformly distributed)
    R_list = []
    accept = 0
    for i in range(0,Nsample):
        R_num = random.random()
        R_list.append(R_num)
    
    for i in range(0,len(x)):
        if R_list[i] <= func(x[i]):
            plt.scatter(x[i],R_list[i],color='b',s=5)
            accept = accept + 1
        else:
            plt.scatter(x[i],R_list[i],color='r',s=5)  
    print(accept)
    print(Nsample)
    #multiply fraction by 
    print('Area Under Curve =','%.4f'%(Fraction(accept,Nsample)*((b-a) * (np.max(fx) - np.min(fx)))))
    print('MonteCarloErr =','%.4f'%np.sqrt(float(Fraction(1,Nsample))))
    plt.show()
    
    
    
#main function
if __name__ == "__main__":
    

    

    #default start bound
    a = 0
    #default stop bound
    b = 3
    #default number of subintervals for Gaussian quadrature
    N = 20
    #default number of "darts" thrown
    Nsample = 1000
    #x values    
    
    
    if '-a' in sys.argv:
        p = sys.argv.index('-a')
        a = int(sys.argv[p+1])
        
    if '-b' in sys.argv:
        p = sys.argv.index('-b')
        b = int(sys.argv[p+1])
        
    if '-N' in sys.argv:
        p = sys.argv.index('-N')
        N = int(sys.argv[p+1])
        
    if '-Nsample' in sys.argv:
        p = sys.argv.index('-Nsample')
        Nsample = int(sys.argv[p+1])
        
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s function [-a] lower_num [-b] upper_num [-N] subint_num" % sys.argv[0],"be sure function >= 0 for x in [a,b]")
        print
        sys.exit([1])
   

    #insert function here
    #format: func = lambda x: function
    
    func = lambda x: np.abs(np.sin(x)**15 + np.cos(x)**3)
    
    GausQuadVal(func,a,b)
    print('Gaus val:',GausQuadVal(func,a,b))
    GausQuadErr(func,a,b)
    print('Gaus err:',GausQuadErr(func,a,b))
    MonteCarlo(Nsample)


