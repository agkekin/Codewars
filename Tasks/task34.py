import re


def to_underscore(string):
    ss = str(string)

    result = re.sub(r'([A-Z])', r' \1', ss).split()
    r = '_'.join(result).lower()
    return r


if __name__ == '__main__':
    assert to_underscore("TestController") == "test_controller"
    assert to_underscore("MoviesAndBooks") == "movies_and_books"
    assert to_underscore("App7Test") =='app7_test'
    assert to_underscore(1) == "1"
