__author__ = 'karl_leswing'


def flatter(a, b):
    if(len(a)) == 0:
        a.append(list(b))
    elif a[-1][0] != b:
        a.append(list(b))
    else:
        a[-1].append(b)
    return a


def function(l):
    return reduce(flatter, l, list())

if __name__ == '__main__':
    print function(["a","a","a","a","b","c","c","a","a","d","e","e","e","e"])
