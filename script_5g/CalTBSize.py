#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@IDE     ：PyCharm 
@Author  ：Zhang.Jing
@Mail    : jing.zhang2020@kingsignal.com
@Date    ：2021-5-13 15:18 
'''
import numpy as np
import os

def py_round(d_in):
    d_int = np.floor(d_in)
    diff = d_in - d_int
    if diff >= 0.5:
        d_out = d_int + 1
    else:
        d_out = d_int
    return d_out


def cal_tbsize(n_info, r):
    if n_info <= 3824:
        n = np.max([3, np.floor(np.log2(n_info)) - 6])
        n1_info = np.max([24, 2 ** n * np.floor(n_info / 2 ** n)])
        tbs = n1_info
    else:
        n = np.floor(np.log2(n_info - 24)) - 5
        n1_info = np.max([3840, 2 ** n * py_round((n_info - 24) / 2 ** n)])
        if r <= 1 / 4:
            c = np.ceil((n1_info + 24) / 3816)
            tbs = 8 * c * np.ceil((n1_info + 24) / (8 * c)) - 24
        else:
            if n1_info > 8424:
                c = np.ceil((n1_info + 24) / 8424)
                tbs = 8 * c * np.ceil((n1_info + 24) / (8 * c)) - 24
            else:
                tbs = 8 * np.ceil((n1_info + 24) / 8) - 24
    return tbs


def py_read(file):
    with open(file, 'r') as fid:
        f = fid.readlines()

    data = [int(fi) for fi in f]
    return np.asarray(data)


if __name__ == '__main__':
    # n_info_list = np.arange(3825, 1467648)
    # n1_info_list_less = [cal_tbsize(i, 0.1) for i in n_info_list]
    # folder=os.path.abspath('')
    # with open(os.path.join(folder,r'ratioLessThan1_4.dat'), 'w') as fid:
    #     np.savetxt(fid, np.unique(n1_info_list_less), delimiter='/n', fmt='%d')
    #
    # n1_info_list_more = [cal_tbsize(i, 1) for i in n_info_list]
    # with open(os.path.join(folder,r'ratioMoreThan1_4.dat'), 'w') as fid:
    #     np.savetxt(fid, np.unique(n1_info_list_more), delimiter='/n', fmt='%d')

    n_info = 3276*11*4*6*616/1024
    tbsize=cal_tbsize(n_info, 616/1024)

    print(tbsize/8)


    # spec_table=py_read(r'C:\Users\zhangjing\Desktop\Tbsize\table2.dat')
    # spec_table_diff = np.concatenate([spec_table,np.array([3824])])[1:] - spec_table
    # with open(r'C:\Users\zhangjing\Desktop\Tbsize\spec_diff.dat','w') as fid:
    #     np.savetxt(fid,spec_table_diff,delimiter='/n',fmt='%d')
