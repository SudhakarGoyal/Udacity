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

# =============================================================================
# def sense(p_,Z,motion):
#     final_q = []
#     for i in range(np.shape(colors)[0]):
#         q = []
#         for j in range(np.shape(colors)[1]):
#             if (motion[0] == 0 and (motion[1] == 0 or motion[1] ==1 or motion[1] == -1)):
#                 if(Z == colors[i][j]):
#                     q.append(pHit*p_[i][j])
#                 else:
#                     q.append((1-pHit)*p_[i][j])
#             else:
#                 if(Z == colors[i][j]):
#                     q.append(pHit*p_[i][j])
#                 else:
#                     q.append((1-pHit)*p_[i][j])                                                       
#                 
#         final_q.append(q)       
#     
# # =============================================================================
# #     for j in range(np.shape(colors)[1]):
# #         q = []
# #         for i in range(np.shape(colors)[0]):
# #             if (motion[1] == 0 and (motion[0] == 1 or motion[0] == -1)):
# #                 if(Z == colors[i][j]):
# #                     q.append(pHit*p_[i][j])
# #                 else:
# #                     q.append((1-pHit)*p_[i][j])
# #         final_q.append(q)    
# # =============================================================================
#         
#           
#     return final_q/np.sum(final_q)
# =============================================================================

def sense(p_,Z,motion):
    final_q = []
    if (motion[0] == 0 and (motion[1] == 0 or motion[1] ==1 or motion[1] == -1)):
        for i in range(np.shape(colors)[0]):
            q = []
            for j in range(np.shape(colors)[1]):       
                if(Z == colors[i][j]):
                    q.append(pHit*p_[i][j])
                else:
                    q.append((1-pHit)*p_[i][j])
            final_q.append(q)      
    else:
        cl = np.transpose(colors)
        p_ = np.transpose(p_)
        
        for i in range(np.shape(cl)[0]):
            q = []
            for j in range(np.shape(cl)[1]):       
                if(Z == cl[i][j]):
                    q.append(pHit*p_[i][j])
                else:
                    q.append((1-pHit)*p_[i][j])                                                     
                
            final_q.append(q)    
        final_q = np.transpose(final_q)
    
# =============================================================================
#     for j in range(np.shape(colors)[1]):
#         q = []
#         for i in range(np.shape(colors)[0]):
#             if (motion[1] == 0 and (motion[0] == 1 or motion[0] == -1)):
#                 if(Z == colors[i][j]):
#                     q.append(pHit*p_[i][j])
#                 else:
#                     q.append((1-pHit)*p_[i][j])
#         final_q.append(q)    
# =============================================================================
    sum_ = 0
    for i in range(np.shape(final_q)[0]):
        for j in range(np.shape(final_q)[1]):
            sum_ += final_q[i][j]
    
    final_q/=sum_
    return final_q

# =============================================================================
# def move(p, motion):
#     q_final = []
# 
#     for i in range(np.shape(colors)[0]):
#         q_ = []
#         for j in range(np.shape(colors)[1]):
#             if (motion[0] == 0 and (motion[1] == 0 or motion[1] ==1 or motion[1] == -1)): # [0 0] dont move|| [0 1]-> right || [0 -1]->left
#                 s = (pExact*(p[i][(j - motion[1])%np.shape(colors)[0]]))
#                 s+= (1-pExact)*p[i][j]
#                 q_.append(s)                      
#         q_final.append(q_)  
#     
#     
#     for j in range(np.shape(colors)[1]):
#         q_ = []    
#         for i in range(np.shape(colors)[0]):
#             if (motion[1] == 0 and (motion[0] == 1 or motion[0] == -1)): # [1 0] down move|| [-1 0]-> up 
#                 s = (pExact*(p[(i - motion[1])%np.shape(colors)[0]][j]))
#                 s+= (1-pExact)*p[i][j]
#                 q_.append(s)                     
#  
#         q_final.append(q_) 
#     
#     return q_final    
# =============================================================================

def move(p, motion):
    q_final = []

    if (motion[0] == 0 and (motion[1] == 0 or motion[1] ==1 or motion[1] == -1)):                 # [0 0] dont move|| [0 1]-> right || [0 -1]->left
        for i in range(np.shape(colors)[0]):
            q_ = []
            for j in range(np.shape(colors)[1]):
                s = (pExact*(p[i][(j - motion[1])%np.shape(colors)[0]]))
                s+= (1-pExact)*p[i][j]
                q_.append(s)                      
            q_final.append(q_)  
        
# =============================================================================
#     if (motion[1] == 0 and (motion[0] == 1 or motion[0] == -1)): # [1 0] down move|| [-1 0]-> up   
# =============================================================================
    else:
        cl = np.transpose(colors)
        p = np.transpose(p)
        for i in range(np.shape(cl)[0]):
            q_ = []
            for j in range(np.shape(cl)[1]):
                s = (pExact*(p[i][(j - motion[0])%np.shape(cl)[1]]))
                s+= (1-pExact)*p[i][j]                
                q_.append(s)                      
            q_final.append(q_) 
        q_final = np.transpose(q_final)
             
    return q_final                  


for i in range(len(measurements)):
    p = move(p,motions[i])
# =============================================================================
#     print(np.shape(p))   
# =============================================================================
    p = sense(p,measurements[i],motions[i])   
# =============================================================================
#     print(np.shape(p))
# =============================================================================
   
print((p)) 

