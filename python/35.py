__author__ = 'karl_leswing'


def function(n):
    if (n == 1):
        return []
    return [filter(lambda x: n % x == 0, xrange(2, n + 1))[0]] + function(n / list(filter(lambda x: n % x == 0, range(2, n + 1)))[0])


if __name__ == '__main__':
    print function(315)
