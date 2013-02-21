__author__ = 'karl_leswing'


def function(m, n):
    return not any(map(
        lambda x: m % x == 0 and n % x == 0,
        xrange(2, min(m, n))
    ))


if __name__ == '__main__':
    print function(35, 64)
