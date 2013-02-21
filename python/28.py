__author__ = 'karl_leswing'


def get_freq(x, l):
    return len(filter(lambda y: len(y) == len(x), l))


def function2(l):
    return sorted(l, key=lambda x: get_freq(x, l))


def function(l):
    return sorted(l, key=lambda x: len(x))


if __name__ == '__main__':
    print function(["abc", "de", "fgh", "de", "ijkl", "mn", "o"])
    print function2(["abc", "de", "fgh", "de", "ijkl", "mn", "o"])
