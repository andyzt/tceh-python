# -*- coding: utf-8 -*-

__author__ = 'sobolevn'


class MathObject(object):
    def __init__(self, value):
        self.value = value

    # Comparing:
    def __eq__(self, other):
        return self.value == other

    def __ge__(self, other):
        return self.value >= other

    def __gt__(self, other):
        return self.value > other

    # Operations:
    def __neg__(self):
        return -self.value

    def __add__(self, other):
        return self.value + other

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        return self.value * other

if __name__ == '__main__':
    m = MathObject(10)
    print(m > 10)
    print(m >= 10)
    print(m == 10)

    print(-m)
    print(m + 2 == 2 + m)

    m += 3
    print(m)

    try:
        print(2 * m)
    except TypeError as ex:
        print(ex)
