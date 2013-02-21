__author__ = 'karl_leswing'


def encode(a, b):
    if len(a) == 0:
        a.append(b)
    elif isinstance(a[-1], tuple):
        if b == a[-1][1]:
            a[-1] = (a[-1][0] + 1, b)
        else:
            a.append(b)
    elif a[-1] == b:
        a[-1] = (2, b)
    else:
        a.append(b)
    return a


def prime_fact(n):
    if n == 1:
        return []
    return [filter(lambda x: n % x == 0, xrange(2, n + 1))[0]] + function(
        n / list(filter(lambda x: n % x == 0, range(2, n + 1)))[0])


def function(n):
    return reduce(encode, prime_fact(n), list())


if __name__ == '__main__':
    print function(315)
