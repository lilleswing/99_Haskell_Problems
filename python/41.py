__author__ = 'karl_leswing'


def is_prime(n):
    return not any(map(lambda x: n % x == 0, range(2, n)))


def prime_range(n, m):
    return map(lambda x: x[0], filter(lambda x: x[1], zip(range(n, m + 1), map(is_prime, range(n, m + 1)))))


def goldbach(n):
    return filter(lambda x: x[0] + x[1] == n, [(x, y) for x in prime_range(2, n) for y in prime_range(2, n)])[0]


def function(n, m):
    return map(goldbach, range(n, m + 1, 2))


def function_2(n, m, k=50):
    return filter(lambda x: x[0] > k and x[1] > k, function(n, m))


if __name__ == '__main__':
    print function(10, 100)
