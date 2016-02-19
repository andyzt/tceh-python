# -*- coding: utf-8 -*-


# String types:
print("This is a string.")
print('This is also a string.')

print('We are equal' == "We are equal")

print(r'This is a raw sting.')
print(u'Я русская строка.')
print(b'I am a byte array.')

print("""
This string contains multiline
    text. And extra spaces. And a \t tab;
""")







# Escape chars:
print('I\'m a multiline string \n too. With extra \t tab.')
print("I'm a string with escaped \".")
print('I am noisy! \a')


# Casting to string:
print(str(4))
print(str(4 + 1))
print(str(4) + '1')
print(str(None), str(True), str(False), str(object))


# String operations:
print('123' + '456')
# but it is impossiable to '123' - '3'
print('4' * 4)

print('Chars'[0], '123'[1], 'abc'[-1])
print('Cut me'[0:3])
print('Cut last two chars'[0:-2])

print('be' in 'To be or not to be?')
print('123' in '123')
print('100' in '200')
print('I am not there' not in 'String')


# Raw string:
# print(r'There\'re no escaped \\ chars in \n me. ')


# String format:
print('My name is %s.' % 'Monty')
# width of 10 chars, 3 chars of precision:
print('I am %d years old and %10.3f meters tall.' % (49, 1.93))
print('It is also possiable to use {} function, with {} or more args.'.format(
    'format()', 1))


# string length:
print(len('7 chars'))
