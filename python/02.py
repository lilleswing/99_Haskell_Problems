__author__ = 'karl_leswing'


def function(l):
    return l[-2]

if __name__ == '__main__':
    print function([1, 2, 3, 4])
    print function(['a', 'b', 'c', 'z'])
