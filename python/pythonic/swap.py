def swap1(x, y):
	temp = x
  	x = y
  	y = temp

def swap2(x, y):
	x, y = y, x

if __name__ == '__main__':
    import timeit
    print(timeit.repeat("swap1(4, 5)", setup="from __main__ import swap1"))

    print(timeit.repeat("swap2(4, 5)", setup="from __main__ import swap2"))
