def points(games):
    res = 0

    for i in games:
        # print(i[0], i[-1])
        if int(i[0]) > int(i[-1]):
            res += 3
        elif int(i[0]) < int(i[-1]):
            res += 0
        elif int(i[0]) == int(i[-1]):
            res += 1
    print(res)
    return res

if __name__ == '__main__':
    assert points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']) == 30