__author__ = 'karl_leswing'


def flatter(a, b):
    if isinstance(b, (list, tuple, set)):
        a.extend(function(b))
    else:
        a.append(b)
    return a


def function(l):
    return reduce(flatter, l, list())

if __name__ == '__main__':
    print function([1, 2, [3, [4, 5]], 3, 2, 1])
