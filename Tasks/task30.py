def count_deaf_rats(town):
    res = 0
    cnt = 0
    cnt_p = 0
    cnt_m = 0
    cnt_p1 = 0
    cnt_m1 = 0
    cnt_p2 = 0
    cnt_m2 = 0

    cnt1 = 0
    cnt2 = 0
    my_str = town.split('P')
    print(my_str)

    if my_str[0] == '':
        print('P left')
        a = my_str[1].replace(' ', '')
        print(a)
        for i in range(0, len(a), 2):
            if a[i] == '~':
                cnt_p += 1
            else:
                cnt_m += 1

        print('cnt_p', cnt_p, 'cnt_m', cnt_m)
        return cnt_p

    elif my_str[1] == '':
        print('P right')
        b = my_str[0].replace(' ', '')
        print(b)

        for i in range(0, len(b), 2):
            if b[i] == '~':
                cnt_p += 1
            else:
                cnt_m += 1

        print('cnt_p', cnt_p, 'cnt_m', cnt_m)
        return cnt_m

    else:
        print('P midle')

        print('P left')
        a = my_str[1].replace(' ', '')
        print(a)
        for i in range(0, len(a), 2):
            if a[i] == '~':
                cnt_p1 += 1
            else:
                cnt_m1 += 1

        print('cnt_p1', cnt_p1, 'cnt_m1', cnt_m1)


        print('P right')
        b = my_str[0].replace(' ', '')
        print(b)

        for i in range(0, len(b), 2):
            if b[i] == '~':
                cnt_p2 += 1
            else:
                cnt_m2 += 1

        print('cnt_p2', cnt_p2, 'cnt_m2', cnt_m2)

        print('cnt', cnt_m2 + cnt_p1)
        return cnt_m2 + cnt_p1


if __name__ == '__main__':
    # assert count_deaf_rats("~O~O~O~O P") == 0
    # assert count_deaf_rats("O~O~O~O~ P") == 4

    # assert count_deaf_rats("P O~ O~ ~O O~") == 1
    # assert count_deaf_rats("P ~O ~0 O~ ~O") == 3
    # assert count_deaf_rats("~O~O~O~OP~O~OO~") == 2
    assert count_deaf_rats('O~~OO~~OO~~OO~P~OO~~OO~~OO~~O') == 8
