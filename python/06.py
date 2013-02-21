__author__ = 'karl_leswing'


def function(l):
    k = list(l)
    k.reverse()
    return k == l

if __name__ == '__main__':
    print function([1, 2, 3, 4, 3, 2, 1])
    print function("Hello, world!")
