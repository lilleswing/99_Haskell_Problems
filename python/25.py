__author__ = 'karl_leswing'
import random


def function(l):
    return random.sample(l, len(l))


if __name__ == '__main__':
    print function(list("abcdef"))
