#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@IDE     ：PyCharm 
@Author  ：Zhang.Jing
@Mail    : jing.zhang2020@kingsignal.com
@Date    ：2021-9-17 13:55 
'''

import matplotlib.pyplot as plt
import scipy.io as sio
import scipy.fftpack as scf
import numpy as np


def read_mat(data_path,name):
    temp=sio.loadmat(data_path)
    return temp[name]


def generation_sequence(u,cv):
    zc_root = np.zeros([839],complex)
    for n in range(839):
        m = np.mod(n+cv,839)
        zc_root[n] = np.exp(-1j*np.pi*u*m*(m+1)/839)

    zcf = scf.fft(zc_root)/np.sqrt(839)
    return zcf

def demo_test():
    print('\033[1;31;46m字体变色，但无背景色 \033[0m')  # 有高亮 或者 print('\033[1;35m字体有色，但无背景色 \033[0m')
    print('\033[1;45m 字体不变色，有背景色 \033[0m')  # 有高亮
    print('\033[0;33;0m 字体有色，且有背景色 \033[0m')  # 有高亮
    print('\033[0;35;46m 字体有色，且有背景色 \033[0m')  # 无高亮
    seq1=generation_sequence(133,10)
    seq_local = generation_sequence(133,0)

    # h = seq1*np.conj(seq_local)
    # plt.figure()
    # plt.plot(abs(scf.ifft(h)))
    # plt.show()

if __name__ == '__main__':
    demo_test()
    resource_grid = np.zeros([100], complex)
    # resource_grid[(24576-840)//2:24576//2]=1
    # resource_grid[24576 // 2:(24576+840)//2] = 10
    resource_grid[10] = 10

    time_grid = scf.ifft(scf.fftshift(resource_grid))
    # time_grid = scf.ifft(resource_grid, axis=-1)
    time_comp=time_grid*np.exp(2j*np.pi*40*np.arange(100)/100)
    # time_downresampe = time_grid[::16]
    freq=scf.ifftshift(scf.fft(time_comp))
    # freq = scf.fft(time_downresampe, axis=-1)
    # plt.figure()
    # plt.plot(abs(freq).T)
    # plt.show()

