# -*- coding: utf-8 -*-

import sys


# which function to use?
if sys.version_info[0] == 2:
    input_function = raw_input
else:
    input_function = input

# Infinitive loop:
while True:
    users_input = input_function('Please, input positive number: ')
    if float(users_input) > 0:
        print('Your number is: %s' % users_input)
        break
    else:
        print('%s is a wrong number.' % users_input)
        continue


# Iterating over a chars in the string:
for char in '12345679':
    print(int(char) + 100)
