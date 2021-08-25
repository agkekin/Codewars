"""
RGB To Hex Conversion

The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
 representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range
 must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Функция rgb не завершена. Завершите его так, чтобы передача десятичных значений RGB приводила к возврату
шестнадцатеричного представления. Допустимые десятичные значения для RGB: 0 - 255. Любые значения, выходящие
за пределы этого диапазона, должны быть округлены до ближайшего допустимого значения.

Примечание. Ваш ответ всегда должен состоять из 6 символов, сокращение с 3 здесь не работает.


The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3

"""


def rgb(r, g, b):
    R = G = B = 0
    my_str = ""

    if r > 255:
        r = 255
    if r < 0:
        r = 0
    R = (hex(r).split("x")[-1].upper())
    # print(R)

    if g > 255:
        g = 255
    if g < 0:
        g = 0
    G = (hex(g).split("x")[-1].upper())
    # print(G)

    if b > 255:
        b = 255
    if b < 0:
        b = 0
    B = (hex(b).split("x")[-1].upper())
    # print(B)

    my_list = ss = []

    my_list.append(R)
    my_list.append(G)
    my_list.append(B)
    # print(my_list)

    my_str = "".join(my_list)
    # print(my_str)

    for i in my_str:
        if i == "0":
            ss = my_str.replace('0', '00')
        if i == "1":
            ss = my_str.replace('1', '01')
        if i == "2":
            ss = my_str.replace('2', '02')
        if i == "3":
            ss = my_str.replace('3', '03')
        if i == "4":
            ss = my_str.replace('4', '04')
        if i == "5":
            ss = my_str.replace('5', '05')
        if i == "6":
            ss = my_str.replace('6', '06')
        if i == "7":
            ss = my_str.replace('7', '07')
        if i == "8":
            ss = my_str.replace('8', '08')
        if i == "9":
            ss = my_str.replace('9', '09')

    ss = "".join(ss)

    return ss


if __name__ == '__main__':
    assert rgb(255, 255, 255) == "FFFFFF"
    assert rgb(255, 255, 300) == "FFFFFF"
    assert rgb(0, 0, 0) == "000000"
    # assert rgb(148, 0, 211) == "9400D3"
    assert rgb(1, 2, 3) == "010203"
    assert rgb(254, 253, 252) == "FEFDFC"
    assert rgb(-20, 275, 125) == "00FF7D"