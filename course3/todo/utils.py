# -*- coding: utf-8 -*-

__author__ = 'sobolevn'


__all__ = ('get_input_function', )


def get_input_function():
    try:
        input_function = raw_input
    except NameError:
        input_function = input

    return input_function
