__author__ = 'karl_leswing'


def is_prime(n):
    return not any(map(lambda x: n % x == 0, range(2, n)))


def prime_range(n, m):
    return map(lambda x: x[0], filter(lambda x: x[1], zip(range(n, m + 1), map(is_prime, range(n, m + 1)))))


def function(n):
    return filter(lambda x: x[0] + x[1] == n, [(x, y) for x in prime_range(2, n) for y in prime_range(2, n)])

if __name__ == '__main__':
    print function(20)
