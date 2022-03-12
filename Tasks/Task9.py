"""
5 kyu
Regex Password Validation

You need to write regex that will validate a password to make sure it meets the following criteria:

    At least six characters long
    contains a lowercase letter
    contains an uppercase letter
    contains a number

Valid passwords will only be alphanumeric characters.

Вам нужно написать регулярное выражение, которое будет проверять пароль, чтобы убедиться, что он соответствует
 следующим критериям:

     Не менее шести символов
     содержит строчную букву
     содержит заглавную букву
     содержит номер

Действительные пароли будут состоять только из буквенно-цифровых символов.

"""

import re

def pwd_control(letters: str) -> bool:
    if re.fullmatch('^((?!.*\s)(?!.*\W)(?!.*[_])(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{6,}$)', letters):
        return True
    else:
        return False


# from re import search
#
# regex = "^((?!.*\s)(?!.*\W)(?!.*[_])(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{6,}$)"
#
# def pwd_control(letters: str) -> bool:
#     if re.fullmatch(regex, letters):
#         return True
#     else:
#         return False
# import string
# def pwd_control(letters: str) -> bool:
#     digits = string.digits
#     lowers = string.ascii_lowercase
#     uppers = string.ascii_uppercase
#     whitespace = string.whitespace
#     punctuation = string.punctuation
#
#
#
#     if len(letters) < 6:
#         return False
#     if any(e in digits for e in letters) and any(e in lowers for e in letters) and any(
#             e in uppers for e in letters) and not any(e in whitespace for e in letters) and not any(e in punctuation for e in letters):
#         return True
#     else:
#         return False

if __name__ == '__main__':
    assert pwd_control('fjd3IR9') == True
    assert pwd_control('ghdfj32') == False
    assert pwd_control('DSJKHD23') == False
    assert pwd_control('dsF43') == False
    assert pwd_control('4fdg5Fj3') == True
    assert pwd_control('DHSJdhjsU') == False
    assert pwd_control('fjd3IR9.;') == False
    assert pwd_control('fjd3  IR9') == False
    assert pwd_control('djI38D55') == True
    assert pwd_control('a2.d412') == False
    assert pwd_control('JHD5FJ53') == False
    assert pwd_control('!fdjn345') == False
    assert pwd_control('jfkdfj3j') == False
    assert pwd_control('123') == False
    assert pwd_control('abc') == False
    assert pwd_control('123abcABC') == True
    assert pwd_control('ABC123abc') == True
    assert pwd_control('Password123') == True
