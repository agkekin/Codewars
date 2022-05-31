def nines(n):
    res = 0
    for i in range(n+1):
        if str(i).count('9'):
            res += 1
    print(res)
    return res



if __name__ == '__main__':
    assert nines(1) == 0
    assert nines(10) == 1
    assert nines(100) == 19
    assert nines(1000) == 271
    assert nines(3950) == 1035

