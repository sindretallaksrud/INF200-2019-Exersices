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

        else:
            self.init_pos -= 1

        self.steps += 1

    def is_at_home(self):
        """Check whether the student is at home"""
        return self.init_pos == self.home_pos

    def get_position(self):
        """The students current position"""
        return self.init_pos

    def get_steps(self):
        """The number of steps the student has taken in total"""
        return self.steps


class Simulation:

    def __init__(self, start, home, seed):
        self.start = start
        self.home = home
        self.seed = random.seed(seed)

        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        """

    def single_walk(self):

        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        w = Walker(self.start, self.home)
        while not w.is_at_home():
            w.move()
        return w.get_steps()

    def run_simulation(self, num_walks):
        """
        Run a set of walks, returns list of number of steps taken.

        Arguments
        ---------
        num_walks : int
            The number of walks to simulate

        Returns
        -------
        list[int]
            List with the number of steps per walk
        """
        steps_list = []
        for _ in range(num_walks):
            steps_list.append(self.single_walk())
        return steps_list


if __name__ == "__main__":
    for _ in range(2):
        sim1 = Simulation(0, 10, 12345)
        sim2 = Simulation(10, 0, 12345)
        print(sim1.run_simulation(20))
        print(sim2.run_simulation(20))
    sim3 = Simulation(0, 10, 54321)
    sim4 = Simulation(10, 0, 54321)
    print(sim3.run_simulation(20))
    print(sim4.run_simulation(20))
