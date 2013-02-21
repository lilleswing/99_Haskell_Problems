__author__ = 'karl_leswing'


def function(n):
    return not any(map(lambda x: n % x == 0, range(2, n)))


if __name__ == '__main__':
    print function(7)
