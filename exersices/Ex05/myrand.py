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

    def random_sequence(self, length):
        return RandIter(self, length)

    def infinite_random_sequence(self):

        """
        Generate an infinite sequence of random numbers.

        Yields
        ------
        int
            A random number.
        """
        while True:
            yield self.rand()


class RandIter:
    def __init__(self, random_number_generator, length):
        """

        Arguments
        ---------
        random_number_generator :
            A random number generator with a ``rand`` method that
            takes no arguments and returns a random number.
        length : int
            The number of random numbers to generate
        """
        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):
        if self.num_generated_numbers is not None:
            raise RuntimeError()
        self.num_generated_numbers = 0
        return self

    """
        Initialise the iterator.

        Returns
        -------
        self : RandIter

        Raises
        ------
        RuntimeError
            If iter is called twice on the same RandIter object.
    """

    def __next__(self):
        """
        Generate the next random number.

        Returns
        -------
        int
            A random number.

        Raises
        ------
        RuntimeError
            If the ``__next__`` method is called before ``__iter__``.
        StopIteration
            If ``self.length`` random numbers are generated.
            """

        if self.num_generated_numbers is None:
            raise RuntimeError()
        if self.num_generated_numbers == self.length:
            raise StopIteration

        self.num_generated_numbers += 1
        return self.generator.rand()



generator = LCGRand(1)

for rand in generator.random_sequence(10):
    print(rand)

i = 0
while i < 100:
    rand = generator.infinite_random_sequence()
    print(f'The {i}-th random number is {next(rand)}')
    i += 1
