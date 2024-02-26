from __future__ import division
from __future__ import print_function

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
from scipy.stats import beta as scipybeta
from matplotlib import pyplot as plt


# import our Random class from Random.py file
sys.path.append(".")
from Random import Random

# main function for die roll Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    #enter fraction for p3
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number] [-p3 fraction] [-Nroll number] [-Nexp number] [-output filename]" % sys.argv[0])
        print
        sys.exit(1)

    # default seed
    seed = 5555

    # default single die roll probability for faces 1-6, 
    p1 = 1/6
    p2 = 1/6
    p3 = 1/6
    p4 = 1/6
    p5 = 1/6

    # default number of die rolls (per experiment)
    Nroll = 5

    # default number of experiments
    Nexp = 3

    # output file default
    doOutputFile = False
    
    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]            
    
    if '-p3' in sys.argv:
        p = sys.argv.index('-p3')
        ptemp = float(eval(sys.argv[p+1]))
        if ptemp >= 0 and ptemp <= 1:
            p3 = ptemp
            #"residual" probability found by subtracting p3 from 1.
            x = (1 - p3)
            #remaining faces assume same probability value... (residual)/(# remaining faces)
            p1 = x/5
            p2 = x/5
            p4 = x/5
            p5 = x/5
            p6 = x/5
    
    if '-Nroll' in sys.argv:
        p = sys.argv.index('-Nroll')
        Nt = int(sys.argv[p+1])
        if Nt > 0:
            Nroll = Nt
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nexp = Ne
    
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True   
    
        
    #create p6 using the probability inputs  
    p6 = 1 - (p1+p2+p3+p4+p5)
        
    #entering probabilities into list format
    prob_list = [p1,p2,p3,p4,p5,p6]
    print('probabilities of unfair die: ', prob_list)
    
    # class instance of our Random class using seed
    random = Random(seed)

    if doOutputFile:
        outfile = open(OutputFileName, 'w')
        for e in range(0,Nexp):
            for t in range(0,Nroll):
                outfile.write(str(random.rolls(prob_list))+" ")
            outfile.write(" \n")
        outfile.close()
    else:
        print('Outcomes')
        for e in range(0,Nexp):
            for t in range(0,Nroll):
                print(random.rolls(prob_list),end= " ")
            print(" ")


