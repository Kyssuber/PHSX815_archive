#!/usr/bin/env python
# coding: utf-8


import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import quadrature
import sys

sys.path.append(".")


#output will give numerical result (Gaussian quadrature approximation to integral) and the error (difference
#between the last two estimates of the integral)

def GausQuadVal(func,a,b):
    return quadrature(func,a,b)[0]
    
    
def GausQuadErr(func,a,b):
    return quadrature(func,a,b)[1]


def TrapRule():
    #function
    y = f(x)
    plt.figure(figsize=(8,6))
    plt.plot(x,y)
    
    #trapezoids
    area_sum = 0
    for i in range(N):
        xs = [X[i],X[i],X[i+1],X[i+1]]
        ys = [0,f(X[i]),f(X[i+1]),0]
        area = (X[i+1]-X[i]) * (f(X[i]) + f(X[i+1]))*0.5
        area_sum += area
        plt.fill(xs,ys,'b',edgecolor='b',alpha=0.2)
    
    print('Trapezoid Total Area:',area_sum)
    
    b_comp = (b/2) - np.sin(8*b)/16
    a_comp = (a/2) - np.sin(8*a)/16
    accept = b_comp - a_comp
    print('Trapezoid Err:',np.abs(accept - area_sum))
    print('Analytical Solution:',accept)
    
        
    plt.title('Trapezoid Rule, N = {}'.format(N),fontsize=16)
    plt.xlabel(r'$x$',fontsize=16)
    plt.ylabel(r'$f(x)$',fontsize=16)
    plt.show()
    
    
    
    
#main function
if __name__ == "__main__":
    

    

    #default start bound
    a = 0
    #default stop bound
    b = 3
    #default number of subintervals
    N = 20
    
    
    
    if '-a' in sys.argv:
        p = sys.argv.index('-a')
        a = int(sys.argv[p+1])
        
    if '-b' in sys.argv:
        p = sys.argv.index('-b')
        b = int(sys.argv[p+1])
        
    if '-N' in sys.argv:
        p = sys.argv.index('-N')
        N = int(sys.argv[p+1])
        
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s function [-a] lower_num [-b] upper_num [-N] subint_num" % sys.argv[0],"be sure function >= 0 for x in [a,b]")
        print
        sys.exit([1])

        
        
        
    #x array for plotting the function
    x = np.linspace(a-1,b+1,200)
    #x array for trapezoid rule
    X = np.linspace(a,b,N+1)  
    #default function
    func = lambda x: np.sin(4*x)**2
    f = func    
   
    
    
    print('Gaus val:',GausQuadVal(func,a,b))
    GausQuadErr(func,a,b)
    print('Gaus err:',GausQuadErr(func,a,b))
    TrapRule()
    
   
    
