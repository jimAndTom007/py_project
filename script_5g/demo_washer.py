#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@IDE     ：PyCharm 
@Author  ：Zhang.Jing
@Mail    : jing.zhang2020@kingsignal.com
@Date    ：2021-8-18 15:24 
'''
#
# """
#   Base
#   /  \
#  /    \
# A      B
#  \    /
#   \  /
#    C
# """
#
# class Base(object):
#     def __init__(self):
#         print("enter Base")
#         print("leave Base")
#
# class A(Base):
#     def __init__(self):
#         print("enter A")
#         super(A, self).__init__()
#         print("leave A")
#
# class B(Base):
#     def __init__(self):
#         print("enter B")
#         super(B, self).__init__()
#         print("leave B")
#
# class C(A, B):
#     def __init__(self):
#         print("enter C")
#         super(C, self).__init__()
#         print("leave C")
#
# C()




# class Animal(object):
#     def run(self):   #父类提供统一的方法，可以是空方法
#         pass
#
# class Dog(Animal):
#     def run(self):   #子类重写父类同名方法
#         print('四条腿跑')
#
# class Person(Animal):
#     def run(self): #子类重写父类同名方法
#         print('两条腿跑')
#
# if __name__ == '__main__':
#     xiaohei = Dog()
#     xiaowang = Person()
#
#     xiaohei.run()
#     xiaowang.run()




class demo(object):
    def __init__(self):
        self.renum =0

    # def __setitem__(self, key, value):
    #     print('__setitem__方法被调用')
    #     self.__dict__[key] = value ** 2
    #
    # def __getitem__(self, key):
    #     print('__getitem__方法被调用')
    #     return self.__dict__[key]


if __name__ == '__main__':
    dd=demo()
    dd['mm']=10
    print(dd['renum'])
