# -*- coding: utf-8 -*-

__author__ = 'Sindre Tallaksrud'
__email__ = 'sindrtal@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.seed = seed
        self.count = 0
        self.r = [0]

    def rand(self):
        self.r[0] = self.seed
        self.r.append(0)
        a = 7**5
        m = 2**31-1
        self.r[self.count + 1] = a * self.r[self.count] % m
        self.count += 1
        return self.r[self.count]


class ListRand:
    def __init__(self, my_list):
        self.my_list = my_list
        self.n = -1

    def rand(self):
        self.n += 1
        if self.n >= len(self.my_list):
            raise RuntimeError('when n is bigger than the length of my_list')
        else:
            number = self.my_list[self.n]
            return number
