__author__ = 'karl_leswing'


def extender(a, b):
    a.extend(b)
    return a


def function(l):
    return reduce(extender,  map(lambda x: (x, x), l), list())


if __name__ == '__main__':
    print function([1, 2, 3, 3, 4])
