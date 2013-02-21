__author__ = 'karl_leswing'


def adder(a, b):
    if a[0] == a[1]:
        a[-1].append(a[2])
    a[-1].append(b)
    a[0] += 1
    return a


def function(l, n, k):
    return reduce(adder, l, [1, n, k, list()])[-1]


if __name__ == '__main__':
    print function(list("abcd"), 2, 'X')
