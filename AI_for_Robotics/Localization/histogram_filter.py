#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 15:15:39 2018

@author: engineer
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 12:14:29 2018

@author: engineer
"""

import numpy as np

# =============================================================================
# 
# colors = [['G', 'G', 'G'],
#           ['G', 'R', 'R'],
#           ['G', 'G', 'G']]
# 
# 
# 
# measurements = ['R', 'R']
# 
# motions = [[0,0],[0,1]]
# =============================================================================

colors = [['R','G','G','R','R'],
          ['R','R','G','R','R'],
          ['R','R','G','G','R'],
          ['R','R','R','R','R']]
measurements = ['G','G','G','G','G']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

p = np.ones([np.shape(colors)[0], np.shape(colors)[1]])/(np.shape(colors)[0]*np.shape(colors)[1])
print(p)
pHit = 0.7 #sensor_right
pExact = 0.8  #p_move

def sense(p_,Z,motion):
    q = np.zeros([len(p_), len(p_[0])])
    for i in range(len(p_)):
        for j in range(len(p_[i])):       
            if(Z == colors[i][j]):
                q[i][j] = (pHit*p_[i][j])
            else:
                q[i][j] = ((1-pHit)*p_[i][j])   
    sum_ = 0
    for i in range(np.shape(q)[0]):
        for j in range(np.shape(q)[1]):
            sum_ += q[i][j]
    
    q/=sum_
    return q


def move(p, motion):
    q_final = np.zeros([len(p), len(p[0])])

    for i in range(len(p)):
        for j in range(len(p[i])):
            q_final[i][j] = pExact*p[(i-motion[0])%len(p)][(j-motion[1])%len(p[i])]  + (1-pExact)*p[i][j]
    
    
    return q_final                  


for i in range(len(measurements)):
    p = move(p,motions[i])
    p = sense(p,measurements[i],motions[i])   
    
print((p)) 

