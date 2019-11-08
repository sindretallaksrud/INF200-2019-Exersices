# -*- coding: utf-8 -*-

__author__ = 'Sindre Tallaksrud'
__email__ = 'sindrtal@nmbu.no'


from walker_sim import Walker, Simulation


class BoundedWalker(Walker):

    def __init__(self, start, home, left_limit, right_limit):

        """
        Initialise the walker
        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        super().__init__(start, home)
        self.init_pos = start
        self.home = home
        self.left_limit = left_limit
        self.right_limit = right_limit

    def one_run(self):
        while not self.is_at_home():
            self.move()
        if self.get_position() > self.right_limit:
            self.init_pos -= 1
        if self.get_position() < self.left_limit:
            self.init_pos += 1
        return self.get_steps()


h = BoundedWalker(-1, 10, -15, 8)

print(h.one_run())


class BoundedSimulation(Simulation):

    def __init__(self, start, home, seed, left_limit, right_limit):
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
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement"""
        self.init_pos = start
        self.home = home
        self.seed = seed
        self.left_limit = left_limit
        self.right_limit = right_limit
        super().__init__(start, home, seed)

    def sim_run(self):
        k = BoundedWalker(self.start, self.home, self.left_limit,
                          self.right_limit)
        while not k.is_at_home():
            k.move()
            if k.get_position() > self.right_limit:
                k.init_pos -= 1
            if k.get_position() < self.left_limit:
                k.init_pos += 1
        return k.get_steps()


j = BoundedSimulation(-1, 10, 3, -15, 12)
print(j.sim_run())
