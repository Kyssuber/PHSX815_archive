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
    #use either default (for H0.txt) or p1a_3 & p1b_3 (for H1.txt)
    #p1a_3 represents probability of rolling face-3 for unfair die one
    #p1b_3 represents probability of rolling face-3 for unfair die two
    #enter fractions for both
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number] [-p1a_3 number] [-p1b_3 number] [-Nroll number] [-Nexp number] [-outputH0 filename] [-outputH1 filename]" % sys.argv[0])
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

    # output file defaults
    doOutputFileH0 = False
    doOutputFileH1 = False
    
    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]            
    
    if '-p1a_3' in sys.argv:
        p = sys.argv.index('-p1a_3')
        ptemp = float(eval(sys.argv[p+1]))
        if ptemp >= 0 and ptemp <= 1:
            p1a_3 = ptemp
            #"residual" probability found by subtracting p1a_3 from 1.
            x = (1 - p1a_3)
            #remaining faces assume same probability value... (residual)/(# remaining faces)
            p1a_1 = x/5
            p1a_2 = x/5
            p1a_4 = x/5
            p1a_5 = x/5
            p1a_6 = x/5
    if '-p1b_3' in sys.argv:
        p = sys.argv.index('-p1b_3')
        ptemp = float(eval(sys.argv[p+1]))
        if ptemp >= 0 and ptemp <= 1:
            p1b_3 = ptemp
            #"residual" pobability found by subtracting p1b_3 from 1.
            x = (1 - p1b_3)
            #remaining faces assume same probability value... (residual)/(# remaining faces)
            p1b_1 = x/5
            p1b_2 = x/5
            p1b_4 = x/5
            p1b_5 = x/5
            p1b_6 = x/5
    
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
    
    #output filename --> either H0_roll.txt or H1_roll.txt recommended
    if '-outputH0' in sys.argv:
        p = sys.argv.index('-outputH0')
        OutputFileNameH0 = sys.argv[p+1]
        doOutputFileH0 = True
        
    if '-outputH1' in sys.argv:
        p = sys.argv.index('-outputH1')
        OutputFileNameH1 = sys.argv[p+1]
        doOutputFileH1 = True
    

    
    
    

        
    #create p6 using the probability inputs, if H0    
    p6 = 1 - (p1+p2+p3+p4+p5)
        
    #entering probabilities into list format
    prob_list = [p1,p2,p3,p4,p5,p6]
    prob1a_list = [p1a_1, p1a_2, p1a_3, p1a_4, p1a_5, p1a_6]
    prob1b_list = [p1b_1, p1b_2, p1b_3, p1b_4, p1b_5, p1b_6]
    print('probabilities of unfair die one: ', prob1a_list)
    print('probabilities of unfair die two: ',prob1b_list)
    
    # class instance of our Random class using seed
    random = Random(seed)

    
    a = 7
    b = 3
    
    #plot beta distribution
    
#    x = np.arange (0.01, 1, 0.01)
#    y = scipybeta.pdf(x,a,b)
#    plt.figure()
#    plt.plot(x,y,label = r'$\alpha =$' + str(a) +', '+ r'$\beta =$' + str(b))
#    plt.axvline(0.5,color='r',linestyle='--')
#    plt.text(0.2,1.5,'P1',fontsize=20)
#    plt.text(0.7,1.5,'P2',fontsize=20)
#    plt.xlabel('x',fontsize=16)
#    plt.ylabel(r'Beta($\alpha, \beta$)',fontsize=16)
#    plt.legend(fontsize=10)
#    plt.show()
    
    
    if doOutputFileH0:
        outfile = open(OutputFileNameH0, 'w')
        for e in range(0,Nexp):
            for t in range(0,Nroll):
                outfile.write(str(random.cate_H0(prob_list))+" ")
            outfile.write(" \n")
        outfile.close()
    else:
        print('H0 outcomes')
        for e in range(0,Nexp):
            for t in range(0,Nroll):
                print(random.cate_H0(prob_list),end= " ")
            print(" ")
   

    if doOutputFileH1:
        outfile = open(OutputFileNameH1, 'w')
        for e in range(0,Nexp):
            for t in range(0,Nroll):
                outfile.write(str(random.cate_H1(prob1a_list,prob1b_list))+" ")
            outfile.write(' \n')
        outfile.close()
            
    else:
        print('H1 outcomes')
        for e in range(0,Nexp):
            for t in range(0,Nroll):
                print(random.cate_H1(prob1a_list,prob1b_list),end= " ")
            print(" ")


