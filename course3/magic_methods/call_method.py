# -*- coding: utf-8 -*-

__author__ = 'sobolevn'


class CallableObject(object):
    def __init__(self, _callable):
        self._callable = _callable

    def __call__(self, *args):
        return self._callable(args)


if __name__ == '__main__':
    co = CallableObject(sum)
    print(co(1, 3, 19))
