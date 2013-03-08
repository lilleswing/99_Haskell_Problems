__author__ = 'karl_leswing'
#TODO


def is_prime(n):
    return not any(map(lambda x: n % x == 0, range(2, n)))


def function(n, m):
    return map(lambda x: x[0], filter(lambda x: x[1], zip(range(n, m + 1), map(is_prime, range(n, m + 1)))))


if __name__ == '__main__':
    print function(10, 20)
