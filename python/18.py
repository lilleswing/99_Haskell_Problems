__author__ = 'karl_leswing'


def function(l, m,  n):
    return l[m - 1:n]


if __name__ == '__main__':
    print function("abcdefghik", 3, 7)
