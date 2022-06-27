def array_diff(a, b):
    my_list = []
    for i in a:
        print(i)
        if i != b[0]:
            my_list.append(i)
    print(my_list)
    return my_list
    #your code here

if __name__ == '__main__':
    assert array_diff([1, 2], [1]) == [2]