# -*- coding: utf-8 -*-

__author__ = 'sobolevn'


class DictFunctionality(object):
    def __init__(self, values=None):
        if values is None:
            self.values = {}
        elif issubclass(values, dict):
            self.values = values
        else:
            raise ValueError()

    def __repr__(self):
        return str(self.values) if self.values else ''

    def __str__(self):
        return self.__repr__()

    # Items management:
    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    # Iteration:
    def __iter__(self):
        return iter(self.values)

    # `in` operation:
    def __contains__(self, item):
        return item in self.values


if __name__ == '__main__':
    l = DictFunctionality()
    l[0] = 'item1'
    l[1] = 'item2'
    print(l, l[0])

    for item in l:
        print(item)

    print('s' in l)
    print(l[123])
