from random import randint as a

__author__ = 'Sindre Tallaksrud'
__email__ = 'sindrtal@nmbu.no'


def b():
    c = 0
    while c < 1:
        c = int(input('Your guess: '))
    return c

def d():
    return a(1, 6) + a(1, 6)

def e(f, g):
    return f == g

if __name__ == '__main__':

    h = False
    i = 3
    j = d()
    while not h and i > 0:
        k = b()
        h = e(j, k)
        if not h:
            print('Wrong, try again!')
            i -= 1

    if i > 0:
        print('You won {} points.'.format(i))
    else:
        print('You lost. Correct answer: {}.'.format(j))