__author__ = 'karl_leswing'


def function(l, n):
    return [l[:n], l[n:]]


if __name__ == '__main__':
    print function("abcdefghik", 3)
