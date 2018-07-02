#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:27:13 2018

@author: engineer
"""

import numpy as np

def Gaussian(value, mean, variance):     # exp(-(x-mean)**2/(2*variance))/(sqrt(2*pi*variance))
    denominator = 1/np.sqrt(2*np.pi*variance)
    numerator = (value - mean)**2/(2*variance)
    return denominator*np.exp(-numerator)


print (Gaussian(10, 10.0, 4.0))