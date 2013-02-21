__author__ = 'karl_leswing'


def flatter(a, b):
    if(len(a)) == 0:
        a.append(b)
    elif a[-1] != b:
        a.append(b)
    return a


def function(l):
    return reduce(flatter, l, list())

if __name__ == '__main__':
    print function(["a","a","a","a","b","c","c","a","a","d","e","e","e","e"])
