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
            return True

    def get_position(self):
        """The students current position"""
        return self.init_pos

    def get_steps(self):
        """The number of steps the student has taken in total"""
        return self.steps


if __name__ == "__main__":
    distance = [1, 2, 5, 10, 20, 50, 100]
    for i in distance:
        """7 different distances"""
        my_list = []
        """Empty list refills for each time in for-loop"""
        for _ in range(5):
            k = Walker(0, i)
            while not k.is_at_home():
                """Moves if not at home"""
                k.move()
            my_list.append(k.get_steps())
        print('Distance:   {0} -> Path lengths: {1}'.format(i, my_list))
