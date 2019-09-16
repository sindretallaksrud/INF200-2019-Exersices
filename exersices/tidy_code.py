from random import randint as rand

__author__ = 'Sindre Tallaksrud'
__email__ = 'sindrtal@nmbu.no'


def bigger_than_0():
    guess = 0
    while guess < 2:
        guess = int(input('Your guess: '))
    return guess


def throw_dices():
    return rand(1, 6) + rand(1, 6)


def test(your_dices, your_guess):
    return your_dices == your_guess


if __name__ == '__main__':

    untrue = False
    max = 3
    dices = throw_dices()
    while not untrue and max > 0:
        k = bigger_than_0()
        untrue = test(dices, k)
        if not untrue:
            print('Wrong, try again!')
            max -= 1

    if max > 0:
        print('You won {} points.'.format(max))
    else:
        print('You lost. Correct answer: {}.'.format(dices))
