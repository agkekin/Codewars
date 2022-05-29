def are_coprime(n,m):
    while n != 0 and m != 0:
        if n > m:
            n = n % m
        else:
            m = m % n

    if (n + m) == 1:
        return True
    else:
        return False
if __name__ == '__main__':
    assert are_coprime(20,27) == True
    assert are_coprime(12,39) == False
