def generate_hashtag(s):
    #your code here
    new = s
    print(s)

    if len(new) > 139 or len(new) == 0:
        return False
    else:
        new = '#' + new
        return new


print(generate_hashtag)



if __name__ == '__main__':
        assert generate_hashtag('Basic tests') == True