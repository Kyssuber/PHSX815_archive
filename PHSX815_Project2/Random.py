from __future__ import division

#! /usr/bin/env python

import math
import numpy as np
from numpy.random import beta as npbeta
from scipy.stats import beta as scipybeta
from matplotlib import pyplot as plt

#################
# Random class
#################
# class that can generate random numbers
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
    

        
    def cate_H0(self,prob_list):
        
        R = self.rand()
        
        if R < prob_list[0]:
            return 1
        if (R > prob_list[0]) & (R < np.sum(prob_list[0:2])):
            return 2
        
        #gap between "ends" here is larger, so ideally 3 will be a more common output
        if (R > np.sum(prob_list[0:2])) & (R < np.sum(prob_list[0:3])):
            return 3
        
        if (R > np.sum(prob_list[0:3])) & (R < np.sum(prob_list[0:4])):
            return 4
        if (R > np.sum(prob_list[0:4])) & (R < np.sum(prob_list[0:5])):
            return 5
        if (R > np.sum(prob_list[0:5])) & (R<1):
            return 6
        else:
            return 1
        
        
        
    def cate_H1(self,prob_list_one,prob_list_two):
        
        
        a,b = 7,3
        
        #draw sample from beta distribution
        #this distribution between zero and one
        beta_dist_sample = npbeta(a,b)
        
        
        #R_die = self.rand()
        
        #determine whether to roll unfair_die_one or unfair_die_two
        
        
        if 0 < beta_dist_sample < 0.5:
            prob_list = prob_list_one
        else:
            prob_list = prob_list_two
        
      
        #with the die selected, proceed with the precise routine as cate()

        R = self.rand()
        if R < prob_list[0]:
            return 1
        if (R > prob_list[0]) & (R < np.sum(prob_list[0:2])):
            return 2
        
        #gap between "ends" here is larger, so ideally 3 will be a more common output
        if (R > np.sum(prob_list[0:2])) & (R < np.sum(prob_list[0:3])):
            return 3
        
        if (R > np.sum(prob_list[0:3])) & (R < np.sum(prob_list[0:4])):
            return 4
        if (R > np.sum(prob_list[0:4])) & (R < np.sum(prob_list[0:5])):
            return 5
        if (R > np.sum(prob_list[0:5])) & (R<1):
            return 6
        else:
            return 1
        
        
        
        
        