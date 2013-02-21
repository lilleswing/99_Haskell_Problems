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


def function(l):
    return reduce(encode, l, list())


if __name__ == '__main__':
    print function(["a", "a", "a", "a", "b", "c", "c", "a", "a", "d", "e", "e", "e", "e"])
