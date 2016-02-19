# -*- coding: utf-8 -*-

list_ = [[]]
multiplied = list_ * 3
multiplied[0].append('foo')
print(multiplied)


def bad_function(param=[]):
    param.append(1)
    print(param)
bad_function()
bad_function()


old_list = list
list = []
list.append(1)

try:
    l1 = list()
except TypeError:
    list = old_list

