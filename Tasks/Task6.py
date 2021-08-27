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

    my_listR = []
    my_listG = []
    my_listB = []
    my_list =  []

    vowels = set('0123456789')

    my_listR.append(R)
    for x in my_listR:
        if x in vowels:
            my_listR = "0" + x


    my_listG.append(G)
    for x in my_listG:
        if x in vowels:
            my_listG = "0" + x

    my_listB.append(B)
    for x in my_listB:
        if x in vowels:
            my_listB = "0" + x

    my_strR = "".join(my_listR)
    my_strG = "".join(my_listG)
    my_strB = "".join(my_listB)

    my_str = my_strR + my_strG + my_strB

    # print("my_str = ", my_str)

    return my_str


if __name__ == '__main__':
    assert rgb(255, 255, 255) == "FFFFFF"
    assert rgb(255, 255, 300) == "FFFFFF"
    assert rgb(0, 0, 0) == "000000"
    assert rgb(148, 0, 211) == "9400D3"
    assert rgb(1, 2, 3) == "010203"
    assert rgb(254, 253, 252) == "FEFDFC"
    assert rgb(-20, 275, 125) == "00FF7D"
