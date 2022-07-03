def sort_array(source_array):
    print('source_array = ', source_array)

    a = []
    my_list = source_array
    my_list_even = my_list.copy()
    my_list_even.sort()

    print('my_list_even.sort = ', my_list_even)

    for i in range(len(my_list_even)):
        print(my_list_even[i])
        if my_list_even[i] % 2 == 0:
            my_list_even.remove(i)
    print('my_list.even = ', my_list_even)

    for i, j in enumerate(source_array):
        if j % 2 != 0:
            a.append('0')
        else:
            a.append(j)
    print('a            = ', a)

    ch = 0

    for i in range(len(a)):
        if a[i] == '0':
            a[i] = my_list_even[ch]
            ch += 1
    print(a)
    return a


if __name__ == '__main__':
    # assert sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
    # assert sort_array([5, 3, 1, 8, 0]) == [1, 3, 5, 8, 0]
    # assert sort_array([]) == []
    assert sort_array([2, 22, 37, 11, 4, 1, 5, 0]) == [2, 22, 1, 5, 4, 11, 37, 0]

