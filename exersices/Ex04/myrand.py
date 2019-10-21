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

s = LCGRand(346)
print(s.rand())


#r[n+1] = a * r[n] mod m

class ListRand:
    def __init__(self):
        pass

    def rand(self):
        pass
