from __future__ import division

#! /usr/bin/env python

import math
import numpy as np
from matplotlib import pyplot as plt



class Random:
    """A random number generator class"""

    # initialization method for Random class
    def __init__(self, seed = 5555):
        self.seed = seed
        self.m_v = np.uint64(4101842887655102017)
        self.m_w = np.uint64(1)
        self.m_u = np.uint64(1)
        
        self.m_u = np.uint64(self.seed) ^ self.m_v
        self.int64()
        self.m_v = self.m_u
        self.int64()
        self.m_w = self.m_v
        self.int64()

    # function returns a random 64 bit integer
    def int64(self):
        with np.errstate(over='ignore'):
            self.m_u = np.uint64(self.m_u * 2862933555777941757) + np.uint64(7046029254386353087)
        self.m_v ^= self.m_v >> np.uint64(17)
        self.m_v ^= self.m_v << np.uint64(31)
        self.m_v ^= self.m_v >> np.uint64(8)
        self.m_w = np.uint64(np.uint64(4294957665)*(self.m_w & np.uint64(0xffffffff))) + np.uint64((self.m_w >> np.uint64(32)))
        x = np.uint64(self.m_u ^ (self.m_u << np.uint64(21)))
        x ^= x >> np.uint64(35)
        x ^= x << np.uint64(4)
        with np.errstate(over='ignore'):
            return (x + self.m_v)^self.m_w

        
        
    # function returns a random floating point number between (0, 1) (uniform)
    def rand(self):
        return 5.42101086242752217E-20 * self.int64()    
    

    #field galaxy, cluster galaxy probability distributions will be inputted here 
    #there will be eight bins, as defined in the accompanying .ipynb
    
    def cate_gal(self,prob_list):

        R = self.rand()
        if R < prob_list[0]:
            return 1
        if (R > prob_list[0]) & (R < np.sum(prob_list[0:2])):
            return 2
        if (R > np.sum(prob_list[0:2])) & (R < np.sum(prob_list[0:3])):
            return 3
        if (R > np.sum(prob_list[0:3])) & (R < np.sum(prob_list[0:4])):
            return 4
        if (R > np.sum(prob_list[0:4])) & (R < np.sum(prob_list[0:5])):
            return 5
        if (R > np.sum(prob_list[0:5])) & (R < np.sum(prob_list[0:6])):
            return 6
        if (R > np.sum(prob_list[0:6])) & (R < np.sum(prob_list[0:7])):
            return 7
        if (R > np.sum(prob_list[0:7])) & (R < np.sum(prob_list[0:8])):
            return 8       
        else:
            return 1
        
        
        
        
        