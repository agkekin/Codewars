def to_underscore(string):
    for i,j in enumerate(string):
        # print(i)
        if i == i.upper():
            i(j-1) ==
            print(i)
    pass

if __name__ == '__main__':
    assert to_underscore("TestController") == "test_controller"
    assert to_underscore("MoviesAndBooks") =="movies_and_books"
    assert to_underscore("App7Test") =='app7_test'
    assert to_underscore(1) =="1"