from collections import Counter


def number_of_pairs(gloves):
    c = Counter(gloves)
    print(c)
    res = max(list(c.values()))
    print(res)
    return res



if __name__ == '__main__':
    # assert number_of_pairs(["red", "red"]) == 1
    # assert number_of_pairs(["red", "green", "blue"]) == 0
    assert number_of_pairs(["gray", "black", "purple", "purple", "gray", "black"]) == 3
    # assert number_of_pairs([]) == 0
    # assert number_of_pairs(["red", "green", "blue", "blue", "red", "green", "red", "red", "red"]) == 4
