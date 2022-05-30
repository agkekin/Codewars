def each_cons(lst, n):
    a = []
    for i in range ( len ( lst ) - n + 1 ):
        a.append ( lst[i:i + n] )
    print ( a )
    return a


if __name__ == '__main__':
    assert each_cons ( [1, 2, 3, 4], 2 ) ==  [[1,2], [2,3], [3,4]]
