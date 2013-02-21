__author__ = 'karl_leswing'


def function(m, n):
    if n == 0:
        return m
    return function(n, m % n)


if __name__ == '__main__':
    print function(36, 63)
