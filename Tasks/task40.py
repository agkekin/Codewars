def array_diff(a, b):
    my_list = []

    if not b:
        return a

    for x in a:
        if x not in b:
            my_list.append(x)

    # print(my_list)
    return my_list

if __name__ == '__main__':
    assert array_diff([1, 2], [1]) == [2]
    assert array_diff([1, 2, 2], [1]) == [2, 2]
    assert array_diff([1, 2, 2], [2]) == [1]
    assert array_diff([1,2,2], []) == [1,2,2]
    assert array_diff([], [1, 2]) == []
    assert array_diff([1, 2, 3], [1,2]) == [3]
