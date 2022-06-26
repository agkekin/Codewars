def number(bus_stops):
    result = 0
    for i in bus_stops:
        # print(i)
        result += i[0] - i[1]
    # print(result)
    return result


if __name__ == '__main__':
    assert number([[10, 0], [3, 5], [5, 8]]) == 5
    assert number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]) == 17
    assert number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]) == 21
