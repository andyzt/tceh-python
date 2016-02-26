# -*- coding: utf-8 -*-

from __future__ import print_function

__author__ = 'sobolevn'


class Parent(object):
    def call(self):
        print('Parent')


class Child(Parent):
    def call(self):
        print('Child')


if __name__ == '__main__':
    print(Parent().call())
    print(Child().call())
