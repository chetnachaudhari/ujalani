def test_array_functions():
    arr = [3, 4, 67, 23, 5, 7, 8, 9]
    print(arr)
    print("Index of 7 in array: ", arr.index(7))
    arr.pop() ## pop the last element in array
    print(arr)
    print("Sorted array: ", sorted(arr))
    arr.append(45) ## Appends element at the end of array
    print(arr)
    arr.reverse()  ## Reverse an array
    print(arr)
    arr.sort() ## Inplace sort array
    print(arr)


def main():
    test_array_functions()


if __name__ == '__main__':
    main()
