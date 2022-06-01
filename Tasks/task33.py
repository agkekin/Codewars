def reverse_seq(n):
    return [x for x in reversed(range(1, n+1))]

if __name__ == '__main__':
    assert reverse_seq(5) == [5,4,3,2,1]