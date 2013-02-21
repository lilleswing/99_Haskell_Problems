__author__ = 'karl_leswing'


def combinations(a, b):
    return a + map(lambda x: x + [b], a) + [[b]]


def function(l, n):
    return filter(lambda x: len(x) == n, reduce(combinations, l, list()))


if __name__ == '__main__':
    print function(list("abcdef"), 3)
    print len(function(list("abcdef"), 3))
