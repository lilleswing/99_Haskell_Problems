__author__ = 'karl_leswing'
import random


def function(l, n):
    return random.sample(l, n)


if __name__ == '__main__':
    print function(list("abcdefgh"), 3)
