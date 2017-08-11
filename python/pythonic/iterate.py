def iterate1(x, y):
    dist = {'a':2, 'b':5, 'c':10}
    for item in dist.items():
        a =1

def iterate2(x, y):
    dist = {'a': 2, 'b': 5, 'c': 10}
    for item in dist.items():
        a =1
if __name__ == '__main__':
    import timeit
    print(timeit.repeat("swap1(4, 5)", setup="from __main__ import swap1"))

    print(timeit.repeat("swap2(4, 5)", setup="from __main__ import swap2"))
