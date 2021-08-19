"""
Simple Pig Latin

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

Переместите первую букву каждого слова в его конец, затем добавьте «ау» в конец слова. Не трогайте знаки препинания.

"""


def pig_it(text):
    pass

if __name__ == '__main__':
    assert pig_it ( "Pig latin is cool" ) == "igPay atinlay siay oolcay"
    assert pig_it ( "This is my string" ) == "hisTay siay ymay tringsay"
    assert pig_it ( "Hello world !" ) == "elloHay orldway !"



