__author__ = 'karl_leswing'


def coprime(m, n):
    return not any(map(
        lambda x: m % x == 0 and n % x == 0,
        xrange(2, min(m, n) + 1)
    ))


def function(n):
    if n == 1:
        return 1
    return len(filter(lambda x: coprime(n, x),
                      xrange(1, n)))


if __name__ == '__main__':
    print function(10)
