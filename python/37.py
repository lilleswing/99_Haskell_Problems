__author__ = 'karl_leswing'
#TODO


def gcd(m, n):
    if n == 0:
        return m
    return function(n, m % n)


def function(n):
    return reduce(encode, prime_fact(n), list())


if __name__ == '__main__':
    print function(315)
