from __future__ import division
from __future__ import print_function

#!/usr/bin/env python
# coding: utf-8

import sys
import numpy as np

sys.path.append(".")
from Random import Random


# main function for die roll Python code
if __name__ == "__main__":

    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number] [-Nroll number] [-Nexp number] [-outputH0 filename] [-outputH1 filename]" % sys.argv[0])
        print
        sys.exit(1)

    # default seed
    seed = 5555

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
    

        
    #entering probabilities into list format

    prob0_list = [p1_0,p2_0,p3_0,p4_0,p5_0,p6_0,p7_0,p8_0]
    prob1_list = [p1_1,p2_1,p3_1,p4_1,p5_1,p6_1,p7_1,p8_1]
    print('probabilities of field masses: ', prob0_list)
    print('probabilities of cluster masses: ',prob1_list)
    
    # class instance of our Random class using seed
    random = Random(seed)

    
    
    if doOutputFileH0:
        outfile = open(OutputFileNameH0, 'w')
        for e in range(0,Nexp):
            for t in range(0,Nroll):
                outfile.write(str(random.cate_gal(prob0_list))+" ")
            outfile.write(" \n")
        outfile.close()
    else:
        print('H0 outcomes')
        for e in range(0,Nexp):
            for t in range(0,Nroll):
                print(random.cate_gal(prob0_list),end= " ")
            print(" ")
   

    if doOutputFileH1:
        outfile = open(OutputFileNameH1, 'w')
        for e in range(0,Nexp):
            for t in range(0,Nroll):
                outfile.write(str(random.cate_gal(prob1_list))+" ")
            outfile.write(' \n')
        outfile.close()
            
    else:
        print('H1 outcomes')
        for e in range(0,Nexp):
            for t in range(0,Nroll):
                print(random.cate_gal(prob1_list),end= " ")
            print(" ")


