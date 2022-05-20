"""
Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation.
Lowercase characters can be numbers. If the method gets a number as input, it should return a string.
Examples

"TestController"  -->  "test_controller"
"MoviesAndBooks"  -->  "movies_and_books"
"App7Test"        -->  "app7_test"
1                 -->  "1"


Завершите функцию/метод, чтобы он принимал строку "PascalCase" и возвращал строку в нотации "snake_case".
Символы нижнего регистра могут быть цифрами. Если метод получает число в качестве входных данных, он должен вернуть
строку.
"""
import string

def to_underscore(letters: str) -> bool:


    if letters == :
        return True
    else:
        return False


if __name__ == '__main__':
    assert to_underscore('TestController') == "test_controller"
    assert to_underscore('MoviesAndBooks') == "movies_and_books"
    assert to_underscore('App7Test') == "app7_test"
    assert to_underscore(1) == 1
