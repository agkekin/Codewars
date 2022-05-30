def symmetric_point(p: list, q: list) -> list:
    p1 = []

    print ( p, q )

    delta_x = 0
    delta_y = 0

    delta_x = q[0] - p[0]
    delta_y = q[1] - p[1]

    p1_x = q[0] + delta_x
    p1_y = q[1] + delta_y

    p1.append ( p1_x )
    p1.append ( p1_y )

    print ( p1 )
    return p1


if __name__ == '__main__':
    assert symmetric_point ( [0, 0], [1, 1] ) == [2, 2]
    assert symmetric_point ( [2, 6], [-2, -6] ) == [-6, -18]
    assert symmetric_point ( [10, -10], [-10, 10] ) == [-30, 30]
    assert symmetric_point ( [1, -35], [-12, 1] ) == [-25, 37]
    assert symmetric_point ( [1000, 15], [-7, -214] ) == [-1014, -443]
    assert symmetric_point ( [0, 0], [0, 0] ) == [0, 0]
