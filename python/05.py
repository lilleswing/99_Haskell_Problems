__author__ = 'karl_leswing'


def function(l):
    l = list(l)
    l.reverse()
    return l

if __name__ == '__main__':
    print function([1, 2, 3, 4])
    print function("Hello, world!")
