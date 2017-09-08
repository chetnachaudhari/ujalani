def concat1():
    nums = ""
    for n in range(20):
        nums += str(n)
    print(nums)
    return True

def concat2():
    nums = []
    for n in range(20):
        nums.append(str(n))
    print("".join(nums))
    return True

def concat3():
    nums = [str(n) for n in range(20)]
    print("".join(nums))
    return True

def concat4():
    nums = map(str, range(20))
    print("".join(nums))
    return True

if __name__ == '__main__':
    import timeit
    print(timeit.repeat("concat1", setup="from __main__ import concat1"))
    print(timeit.repeat("concat2", setup="from __main__ import concat2"))
    print(timeit.repeat("concat3", setup="from __main__ import concat3"))
    print(timeit.repeat("concat4", setup="from __main__ import concat4"))
