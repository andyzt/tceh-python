
# -*- coding: utf-8 -*-


__author__ = 'sobolevn'


# first:
my_global_var = 3

if my_global_var > 2:
    inner_if_var = 'set'

print(inner_if_var)

if my_global_var != 3:
    this_wont_happen = 'Nein!'
else:
    but_this_will = 'Yes.'

print(but_this_will)
print(this_wont_happen)


# second:
var = 1
value = var
var = 10


# third:
var = 'big string, very long. so memory usage.'
other = var
del var  # you should not really do that.


# fourth:
var = 'string'
value = var
value += ' is immutable'


# what can be stored inside a variable? everything!
string_inside = 'abc'
int_inside = 123
function_inside = len
class_inside = object
object_inside = object()
list_inside = [1, 2, 3]
none_inside = None

import math
module_inside = math
