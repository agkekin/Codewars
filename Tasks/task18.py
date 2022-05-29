def count_positives_sum_negatives(arr):
    one = []
    two = []
    res = []
    summa = 0
    q = 0
    if len(arr) == 0:
        return []
    for i in arr:
        if i > 0:
            one.append(i)

        elif i < 0:
            summa += i

    q = len(one)
    res.append(q)
    res.append(summa)

    return res


if __name__ == '__main__':
    assert count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) == [10, -65]
    assert count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]) == [8, -50]
    assert count_positives_sum_negatives([1]) == [1, 0]
    assert count_positives_sum_negatives([-1]) == [0, -1]
    assert count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0]
    assert count_positives_sum_negatives([]) == []

