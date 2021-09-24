#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@IDE     ：PyCharm 
@Author  ：Zhang.Jing
@Mail    : jing.zhang2020@kingsignal.com
@Date    ：2021-8-31 10:01 
'''

"""
特征值分解
"""

import numpy as np
import numpy.linalg as la

# matrix_size = [1,64]
# h0 = np.random.random(matrix_size)+np.random.random(matrix_size)*1j
# h1 = np.random.random(matrix_size)+np.random.random(matrix_size)*1j
# h2 = np.random.random(matrix_size)+np.random.random(matrix_size)*1j

# hh = h0+h1+h2
hh=np.array([[3,2],[2,3]])

U,s,V=la.svd(hh)

print(s)




