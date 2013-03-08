__author__ = 'karl_leswing'


def update_path(nodes, k):
    return map(lambda x: (x[0], k + x[1]), nodes)


def merge_it(a, b):
    return [[a[0] + b[0], update_path(a[1], "0") + update_path(b[1], "1")]]


def huffman_step(n):
    k = sorted(n, key=lambda x: x[0])
    return merge_it(k[0], k[1]) + k[2:]


def function(n):
    if len(n) == 1:
        return n
    else:
        return function(huffman_step(n))


if __name__ == '__main__':
    print function([[45, [('a', '')]],
                    [13, [('b', '')]],
                    [12, [('c', '')]],
                    [16, [('d', '')]],
                    [9, [('e', '')]],
                    [5, [('f', '')]]
                    ])

