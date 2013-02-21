__author__ = 'karl_leswing'
import random


def function(m, n):
    return random.sample(range(1, n + 1), m)


if __name__ == '__main__':
    print function(6, 49)
