__author__ = 'karl_leswing'


def dropper(a, b):
    if a[0] != a[1]:
        a[2].append(b)
    a[0] += 1
    return a


def function(l, n):
    return reduce(dropper, l, [1, n, list()])[2]


if __name__ == '__main__':
    print function(list("abcd"), 2)
