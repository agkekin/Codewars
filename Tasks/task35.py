def find_it(seq):
    my_list = []
    my_count = 0
    result = 0
    my_set = set(seq)
    # print(my_set)

    for i in my_set:
        my_count = 0
        for j in seq:
            if j == i:
                my_count += 1
                # print('my_count =', my_count, 'j =',j)
        my_list.append(my_count)
    # print(my_list)

    my_list_set = list(my_set)
    # print(my_list_set)
    for k, val in enumerate(my_list):
        if val % 2 != 0:
            result = my_list_set[k]
            # print('k=', k, 'result =', result )
    return result


if __name__ == '__main__':
    assert find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]) == 5
    assert find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) == -1
    assert find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) == 5
    assert find_it([10]) == 10
    assert find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]) == 10
    assert find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]) == 1
