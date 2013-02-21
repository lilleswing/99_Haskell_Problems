__author__ = 'karl_leswing'


def flatter(a, b):
    if(len(a)) == 0:
        a.append(list(b))
    elif a[-1][0] != b:
        a.append(list(b))
    else:
        a[-1].append(b)
    return a


def function9(l):
    return reduce(flatter, l, list())


def function(l):
    return map(lambda x: (len(x), x[0]), function9(l))


if __name__ == '__main__':
    print function(["a","a","a","a","b","c","c","a","a","d","e","e","e","e"])
