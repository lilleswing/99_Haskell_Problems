__author__ = 'karl_leswing'


def dropper(a, b):
    if a[0] % a[1] != 0:
        a.append(b)
    a[0] += 1
    return a


def function(l, n):
    return reduce(dropper,  l, [1, n])[2:]


if __name__ == '__main__':
    print function("abcdefghik", 3)
