#! /usr/bin/env python

import math
import numpy as np

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
    

    def cate_H0(self,p1=1/6,p2=1/6,p3=1/6,p4=1/6,p5=1/6,p6=1/6):
        
        R = self.rand()
        
        if R < p1:
            return 1
        if (R > p1) & (R < p1+p2):
            return 2
        if (R > p1+p2) & (R < p1+p2+p3):
            return 3
        if (R > p1+p2+p3) & (R < p1+p2+p3+p4):
            return 4
        if (R > p1+p2+p3+p4) & (R < p1+p2+p3+p4+p5):
            return 5
        if (R > p1+p2+p3+p4+p5) & (R<1):
            return 6
        else:
            return 0
        
    def cate_H1(self,p1=1/9,p2=1/9,p3=4/9,p4=1/9,p5=1/9,p6=1/9):
        
        R = self.rand()
        
        if R < p1:
            return 1
        if (R > p1) & (R < p1+p2):
            return 2
        
        #gap between "ends" here is larger, so ideally 3 will be a more common output
        if (R > p1+p2) & (R < p1+p2+p3):
            return 3
        
        if (R > p1+p2+p3) & (R < p1+p2+p3+p4):
            return 4
        if (R > p1+p2+p3+p4) & (R < p1+p2+p3+p4+p5):
            return 5
        if (R > p1+p2+p3+p4+p5) & (R<1):
            return 6
        else:
            return 0
        
        
    def cate(self,prob_list):
        
        R = self.rand()
        
        if R < prob_list[0]:
            return 1
        if (R > prob_list[0]) & (R < prob_list[0]+prob_list[1]):
            return 2
        
        #gap between "ends" here is larger, so ideally 3 will be a more common output
        if (R > prob_list[0]+prob_list[1]) & (R < prob_list[0]+prob_list[1]+prob_list[2]):
            return 3
        
        if (R > prob_list[0]+prob_list[1]+prob_list[2]) & (R < prob_list[0]+prob_list[1]+prob_list[2]+prob_list[3]):
            return 4
        if (R > prob_list[0]+prob_list[1]+prob_list[2]+prob_list[3]) & (R < prob_list[0] + prob_list[1] + prob_list[2] + prob_list[3] + prob_list[4]):
            return 5
        if (R > prob_list[0] + prob_list[1] + prob_list[2] + prob_list[3] + prob_list[4]) & (R<1):
            return 6
        else:
            return 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        