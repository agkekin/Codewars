def get_sum(a, b):
    if b < a:
        a1 = b
        b1 = a
    else:
        a1 = a
        b1 = b

    my_list = []
    result = 0

    my_list = list((range(a1, b1+1)))
    print(my_list)

    result = sum(my_list)
    print(result)

    return result


if __name__ == '__main__':
    assert get_sum(0, 1) == 1
    assert get_sum(0, -1) == -1
