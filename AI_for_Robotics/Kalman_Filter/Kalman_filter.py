#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 15:05:08 2018

@author: engineer
"""
from math import *
import numpy as np


measurements = [1, 2, 3]

x = np.array([[0.], [0.]]) # initial state (location and velocity)
P = np.array([[1000., 0.], [0., 1000.]]) # initial uncertainty
u = np.array([[0.], [0.]]) # external motion
F = np.array([[1., 1.], [0, 1.]]) # next state function
H = np.array([[1., 0.]]) # measurement function
R = np.array([[1.]]) # measurement uncertainty
I = np.array([[1., 0.], [0., 1.]]) # identity matrix
########################################

# Implement the filter function below

def kalman_filter(x, P):
    for i in range(len(measurements)):
        
        # measurement update
        Y = measurements[i] - np.dot(H,x)
        a = np.dot(H,P) 
        S = np.dot(a,np.transpose(H)) + R
        K = np.dot(np.dot(P,np.transpose(H)),np.linalg.inv(S))
        x = x + np.dot(K,Y)
        r_temp = np.dot(K,H)
        P_temp = I - r_temp
        
        P = np.dot(P_temp,P)
        # prediction
    
        x = np.dot(F,x) + u
        P = np.dot(np.dot(F,P),np.transpose(F))
        
    return x,P
    

############################################
### use the code below to test your filter!
############################################

print(kalman_filter(x, P))
# output should be:
# x: [[3.9996664447958645], [0.9999998335552873]]
# P: [[2.3318904241194827, 0.9991676099921091], [0.9991676099921067, 0.49950058263974184]]
