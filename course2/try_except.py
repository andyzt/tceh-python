# -*- coding: utf-8 -*-

try:
    print(1/0)
except:
    print('Bad operation!')


try:
    print(1/0)
except Exception as ex:  # there's difference with `except:`
    print('Bad operation!', type(ex), ex)

try:
    print(1/0)
except ZeroDivisionError as ex:
    print('Divided by zero!', ex)


try:
    raise ValueError()
except ZeroDivisionError:
    print('Divided by zero!')
except AttributeError:
    print('Key is missing!')
except Exception as ex:
    print("I don't know what's going on!")
    print(ex)


try:
    print('try')
    dict_ = {1: '1'}
    print(dict_[2])
except KeyError as ex:
    print('except', ex)
finally:
    print('finally')


try:
    print('try')
except:
    pass
else:
    print('else')
finally:
    print('finally')


try:
    raise RuntimeError('Kill process')
finally:
    print('This will be printed')

