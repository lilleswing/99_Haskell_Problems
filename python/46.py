__author__ = 'karl_leswing'


def function(f):
    return map(lambda x: tuple(list(x) + [f(x[0], x[1])]), [(x, y) for x in [False, True] for y in [False, True]])


if __name__ == '__main__':
    print function(lambda x, y: x and y)
    print function(lambda x, y: x or y)
    print function(lambda x, y: x != y)  # xor
    print function(lambda x, y: x == y)

