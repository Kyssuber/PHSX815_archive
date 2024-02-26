#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from MySort import MySort

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)

    Sorter = MySort()

    #sort all times from shortest to longest
    #sort time averages from shortest to longest
    
    # times = Sorter.DefaultSort(times)
    # times_avg = Sorter.DefaultSort(times_avg)
    # times_avg = Sorter.BubbleSort(times_avg)
    # times_avg = Sorter.InsertionSort(times_avg)
    times = Sorter.QuickSort(times)
    times_avg = Sorter.QuickSort(times_avg)

    #Calculating the quartiles...
    
    #regardless of whether len is even or odd, halving len and dividing by 2 will give sufficient approximation
    #for Q_i index (since sample size is large)
    
    #middle quartile (q2)
    times_q2_index = int(np.median(len(times))/2)
    times_q2 = times[times_q2_index]
    times_avg_q2_index = int(np.median(len(times_avg))/2)
    times_avg_q2 = times_avg[times_avg_q2_index]
    
    #lower quartile (q1)
    times_q1_index = int(times_q2_index/2)
    times_q1 = times[times_q1_index]
    times_avg_q1_index = int(times_avg_q2_index/2)
    times_avg_q1 = times_avg[times_avg_q1_index]
    
    #upper quartile (q3)
    times_q3_index = times_q1_index + times_q2_index
    times_q3 = times[times_q3_index]
    times_avg_q3_index = times_avg_q1_index + times_avg_q2_index
    times_avg_q3 = times_avg[times_avg_q3_index]
    
    
    # ADD YOUR CODE TO PLOT times AND times_avg HERE

    plt.figure()
    plt.hist(times,Nmeas+1, density=True, facecolor='b', alpha=0.4)
    plt.xlabel('# Counts of t',fontsize=15)
    plt.ylabel('# Occurrences per Exp',fontsize=15)
    plt.axvline(times_q1,color='b',label='q1 = '+str(times_q1))
    plt.axvline(times_q2,color='r',label='q2 = '+str(times_q2))
    plt.axvline(times_q3,color='g',label='q3 = '+str(times_q3))
    plt.legend()
    plt.grid()
    
    plt.figure()
    plt.hist(times_avg,Nmeas+1,density=True,facecolor='b',alpha=0.4)
    plt.xlabel('# Counts of t_avg',fontsize=15)
    plt.ylabel('# Exp with t_avg',fontsize=15)
    plt.axvline(times_avg_q1,color='b',label='q1 = '+str(times_avg_q1))
    plt.axvline(times_avg_q2,color='r',label='q2 = '+str(times_avg_q2))
    plt.axvline(times_avg_q3,color='g',label='q3 = '+str(times_avg_q3))
    plt.legend()
    plt.grid()

    
    
    
    

    plt.show()
    
    
    
    
    
    
    
    
    