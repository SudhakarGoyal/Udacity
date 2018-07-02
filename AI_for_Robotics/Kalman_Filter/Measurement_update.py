#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 12:25:25 2018

@author: engineer
"""

import numpy as np

def measurement_update(x, var_x, z, var_z):
    return ((var_z*x + var_x*z)/(var_x + var_z)), 1/((1/var_x + 1/var_z))

def motion_update(x,var_x,z,var_z):
    return ((x+z), var_x+var_z)


measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.
for i in range(len(measurements)):
    mu, sig = (measurement_update(mu,sig,measurements[i],measurement_sig))
    print("update " + str((mu))+ " " + str((sig)))
    mu,sig = (motion_update(mu,sig,motion[i],motion_sig))
    print("predict ",str(mu) + " " +str(sig))
    

    