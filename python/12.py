import collections

__author__ = 'karl_leswing'


def expand(a):
    if isinstance(a, tuple):
        return [a[1]] * a[0]
    else:
        return [a]


def flatter(a, b):
    if isinstance(b, (list, tuple, set)):
        a.extend(flatten_list(b))
    else:
        a.append(b)
    return a


def flatten_list(l):
    return reduce(flatter, l, list())


def function(l):
    return flatten_list(map(expand, l))


if __name__ == '__main__':
    print function([(4, 'a'), 'b', (2, 'c'), (2, 'a'), 'd', (4, 'e')])
