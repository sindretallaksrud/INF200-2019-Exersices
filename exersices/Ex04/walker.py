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
        random.randint(0, 1)
        if n == 1:
            self.init_pos += 1
            self.steps += 1
        else:
            self.init_pos -= 1
            self.steps += 1



    def is_at_home(self):
        """Check whether the student is at home"""

    def get_position(self):
        """The students current position"""

    def get_steps(self):
        """The number of steps the student has taken in total"""
