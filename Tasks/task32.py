def tower_builder(n_floors):
    res = []

    for i in range(1,n_floors+1):
        mm = 2 * i - 1

    for i in range(1,n_floors+1):
        stars = 2 * i - 1
        s = stars * '*'
        s1 = s.center(mm, ' ')
        res.append(s1)
    return res




if __name__ == '__main__':
    # assert tower_builder(1) == ['*', ]
    # assert tower_builder(2) == [' * ', '***']
    assert tower_builder(3) == ['  *  ', ' *** ', '*****']

