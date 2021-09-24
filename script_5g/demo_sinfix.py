#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@IDE     ：PyCharm 
@Author  ：Zhang.Jing
@Mail    : jing.zhang2020@kingsignal.com
@Date    ：2021-2-24 18:02 
'''
import numpy as np
import matplotlib.pyplot as plt
import os
import scipy.io as sio
import re
from functools import reduce

def read_file(file_path, shape, fix_len=None):
    partten = re.compile('[0-9.-]+')
    with open(file_path, 'r') as fid:
        lines = fid.readlines()
        str_list = partten.findall(' '.join(lines))

    table_tmp = [int(ss) if '.' not in ss else float(ss) for ss in str_list]
    if fix_len is not None:
        lenght = reduce(lambda x, y: x * y, shape)
    else:
        lenght = len(table_tmp)
    table_output = np.reshape(table_tmp[:lenght], shape)
    return table_output


if __name__ == '__main__':
    dir_path = os.path.abspath('.')
    file_path = os.path.join(r'D:\workspace\multi_processing\PhySimulation\lib', 'MappingForL839Table.dat')
    mapping_table = read_file(file_path, [839- 1])
    result=np.zeros([838])
    sort_table = sorted(mapping_table)
    for idx,u in enumerate(sort_table):
        for i in range(1,1000):
            remain=i*u%839
            if remain ==1:
                break
        result[idx]=i


    # with open(r'D:\workspace\multi_processing\PhySimulation\lib\prach_restrictedSetQ.dat','w') as fid:
    #     np.savetxt(fid,result,fmt='%d',delimiter='\t',newline='\n')




