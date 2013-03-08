__author__ = 'karl_leswing'


def gray(n, reversed):
    if n == 1:
        if reversed:
            return [[1], [0]]
        return [[0], [1]]
    return map(lambda x: [0] + x, gray(n - 1, not reversed)) + map(lambda x: [1] + x, gray(n - 1, reversed))


def function(n):
    return gray(n, False)


if __name__ == '__main__':
    print function(3)

