# -*- coding: utf-8 -*-

__author__ = 'Sindre Tallaksrud'
__email__ = 'sindrtal@nmbu.no'

import random


class Walker:
    def __init__(self, init_pos, home_pos):
        self.init_pos = init_pos
        self.home_pos = home_pos
        self.steps = 0

    def move(self):
        """One step"""
        n = random.randint(0, 1)
        if n == 1:
            self.init_pos += 1
            self.steps += 1
        else:
            self.init_pos -= 1
            self.steps += 1

    def is_at_home(self):
        """Check whether the student is at home"""
        if not self.init_pos == self.home_pos:
            return False
        else:
            return self.home_pos

    def get_position(self):
        """The students current position"""
        return self.init_pos

    def get_steps(self):
        return self.steps
        """The number of steps the student has taken in total"""


if __name__ == "__main__":
    distance = [1, 2, 5, 10, 20, 50, 100]
    for i in distance:
        my_list = []
        for _ in range(5):
            k = Walker(0, i)
            while not k.init_pos == k.home_pos:
                k.move()
            my_list.append(k.get_steps())
        print('Distance:   {0} -> Path lengths: {1}'.format(i, my_list))
