"""
Реализуйте функцию unique_in_order, которая принимает в качестве аргумента последовательность и возвращает список
элементов без каких-либо элементов с одинаковым значением рядом друг с другом и с сохранением исходного порядка
элементов.
For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]

"""

def unique_in_order(iterable):
    my_list = []
    prev = 0
    for elem in iterable:
        if prev == elem:
            continue
        my_list.append(elem)
        prev = elem
    return my_list


if __name__ == '__main__':
    assert unique_in_order("AAAABBBCCDAABBB") == ['A','B','C','D','A','B']
