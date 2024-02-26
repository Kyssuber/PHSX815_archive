#!/usr/bin/env python
# coding: utf-8


import numpy as np
from matplotlib import pyplot as plt
from numpy.random import random
from scipy.optimize import minimize

import sys

sys.path.append(".")


# INSTRUCTIONS: 
# Write a program that can find the minimum of a function that you define. The function can be any one (even very simple) as long as it actually has a minimum. You are welcome to use any standard or external C++ or Python libraries (you don't need to implement the minimization routine, only the function to be minimized). You can also try to visualize your function and the location of the minimum (not required).




#default minimum and maximum bounds [x_min,x_max]
x_min = -10
x_max = 5


#sample random points in function from xmin to xmax. Append to list.
def get_rand_list(xmin,xmax):
    
    rand_list = []
    
    for i in range(0,int(np.abs(x_min))+int(np.abs(x_max))):
        x = random() 
        
        if random() < 0.5:
            x = x*x_min
        else:
            x = x*x_max 
        
        rand_list.append(x)
        
    return rand_list
        

   
def global_minimum(xmin,xmax,rand_list):
    
    minimum_list_x = []
    minimum_list_f = []

    #function
    f =lambda x: np.exp(-x) * np.sin(x)

    #array of x values for plotting purposes
    x = np.linspace(x_min,x_max+0.5,5000)

    #preparing the "blank canvas"
    plt.figure(figsize=(8,6))
    plt.plot(x,f(x))

    #loop through each entry in rand_list, set as initial x0, apply scipy.optimize.minimize to f given x0
    for n in rand_list:
        x0 = n
        res = minimize(f,x0)
        #appends x,f coordinates representing approximated minimum given x0 to two separate lists
        minimum_list_x.append(res.x[0])
        minimum_list_f.append(f(res.x)[0])

        plt.scatter(res.x[0],f(res.x)[0],s=30,color='black')
    
    #find and encircle the global minimum on given function range
    minimum_list_x = np.asarray(minimum_list_x)
    minimum_list_f = np.asarray(minimum_list_f)
    min_x_coord = minimum_list_x[np.where(minimum_list_f == np.min(minimum_list_f))[0]]
    print('global minimum coordinate: ', '(','%.3f'%(min_x_coord[0]),',','%.3f'%(np.min(minimum_list_f)),')')

    plt.scatter(min_x_coord[0],np.min(minimum_list_f),s=90,color='r',marker='o',label='global minimum on interval')
    plt.legend(fontsize=18)
    plt.xlabel('x',fontsize=20)
    plt.ylabel('f(x)',fontsize=20)
    plt.show()

    
#main function
if __name__ == "__main__":  
    
    
    if '-xmin' in sys.argv:
        p = sys.argv.index('-xmin')
        x_min = float(sys.argv[p+1])
        
    if '-xmax' in sys.argv:
        p = sys.argv.index('-xmax')
        x_max = float(sys.argv[p+1])
        
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-xmin] min_bound_number [-xmax] max_bound_number" % sys.argv[0])
        print
        sys.exit([1])
        
        
    rand = get_rand_list(x_min,x_max)
    
    global_minimum(x_min,x_max,rand)
    

