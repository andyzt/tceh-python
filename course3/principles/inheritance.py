# -*- coding: utf-8 -*-

from __future__ import print_function

__author__ = 'sobolevn'


class Parent(object):
    def __init__(self):
        print('Parent inited')
        self.value = 'Parent'

    def do(self):
        print('Parent do(): %s' % self.value)

    @staticmethod
    def static_do():
        print('Parent static_do()')

    @classmethod
    def class_do(cls):
        print('Parent class_do(): %s' % cls)


class Child(Parent):
    def __init__(self):
        super(Child, self).__init__()

        print('Child inited')
        self.value = 'Child'

    @staticmethod
    def static_do():
        print('Child static_do()')


class Mixin(object):
    @classmethod
    def class_do(cls):
        print('Mixed: %s' % cls)


class MixedChildOne(Parent, Mixin):
    pass


class MixedChildTwo(Mixin, Parent):
    pass


class MixedChildThree(Parent, Mixin):
    @classmethod
    def class_do(cls):
        Mixin.class_do()


if __name__ == '__main__':
    Parent.static_do()
    Parent.class_do()

    parent = Parent()
    parent.do()
    Parent.do(parent)  # do not use this!

    parent.class_do()
    parent.static_do()
    parent.__class__.class_do()
    parent.__class__.static_do()

    # Child:
    Child.static_do()
    Child.class_do()

    child = Child()
    child.do()

    # Mixins:
    mixin1 = MixedChildOne()
    mixin1.class_do()
    print(mixin1.__class__.__mro__)

    mixin2 = MixedChildTwo()
    mixin2.class_do()
    print(mixin2.__class__.__mro__)

    mixin3 = MixedChildThree()
    mixin3.class_do()
    print(mixin3.__class__.__mro__)
