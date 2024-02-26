#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import csv
from matplotlib import pyplot as plt
import sys

if __name__ == "__main__":
    if '-h' in sys.argv or '--help' in sys.argv:
        print("Usage: %s [-seed number]" % sys.argv[0])
        print(".csv and .py must be in same directory; cd to said directory before running in terminal.")
        print
        sys.exit(1)
            
    #default seed
    seed = 5555
    
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    
    np.random.seed(seed)
    N = 10000
    arr = np.random.rand(N)

    with open('random_list.csv','w') as f:
        writer = csv.writer(f,delimiter=',')
        writer.writerow(arr)
        
        #for item in arr:
            #f.write(str(item))
        f.close()
        
#open csv file, convert each delimited string into a float, append to list

    list = []
    with open('random_list.csv','r') as f:
        reader = csv.reader(f,delimiter=',')
        for row in reader:
            for i in range(0,N):
                num = float(row[i])
                list.append(num)
            
    n,bins,patches = plt.hist(list,50,density=True,facecolor='g',alpha=0.75)
    plt.xlabel('x',fontsize=16)
    plt.ylabel('Counts',fontsize=16)
    plt.title('Uniform Random Number',fontsize=16)
    plt.grid()
    
    plt.show()

