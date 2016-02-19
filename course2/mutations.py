# -*- coding: utf-8 -*-

import copy


# Switch to http://pythontutor.com/visualize.html#mode=edit

# example 1:
var = {'list': [[1, 2], ['a', 'b']], 'tuple': ('foo', 'bar', )}
new_var = var
var.update({'str': 'string'})
var['list'].append([True, False])
var['tuple'] += ('baz', )

print(var)
print(new_var)


# example 2:
var = {'list': [[1, 2], ['a', 'b']], 'tuple': ('foo', 'bar', )}
new_var = var.copy()
var.update({'str': 'string'})
var['list'].append([True, False])
var['tuple'] += ('baz', )

print(var)
print(new_var)


# example 3 (not supported by pythontutor) - debug:
var = {'list': [[1, 2], ['a', 'b']], 'tuple': ('foo', 'bar', )}
new_var = copy.deepcopy(var)
var.update({'str': 'string'})
var['list'].append([True, False])
var['tuple'] += ('baz', )

print(var)
print(new_var)
