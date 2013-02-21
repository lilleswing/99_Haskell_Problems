#TODO unimplemented in all ways

__author__ = 'karl_leswing'


def combinations(a, b):
    return a + map(lambda x: x + [b], a) + [[b]]


def function(l, n):
    return filter(lambda x: len(x) == n, reduce(combinations, l, list()))


if __name__ == '__main__':
    print function(["abc", "de", "fgh", "de", "ijkl", "mn", "o"])
    print len(function(list("abcdef"), 3))
