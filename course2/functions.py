# -*- coding: utf-8 -*-


print('Starting...')


# Step 0:
try:
    not_callable = 0
    not_callable()
except TypeError as ex:
    print('Failed!', ex)


# Step 1:

def my_function(input_var1, input_var2):
    print(type(input_var1), type(input_var2))
    # note the difference between print as a keyword in python2:
    # print type(input_var1), type(input_var2)
    types_match = type(input_var1) == type(input_var2)
    return types_match

print(my_function, type(my_function), callable(my_function))

try:  # We are handling exceptions
    print(my_function())
except TypeError as ex:  # We know, that my_function() won't work
    print('Failed!', ex)  # And we are ready to this


first_call = my_function('1', 1)
print(first_call)

second_call = my_function(1, 123)
print(second_call)


# Step 2:

def my_function(var1, var2, var3):
    print("No way I'm using this: {}, {}, {}".format(var1, var2, var3))

new_call = my_function(1, 2, 3)
print(new_call)

try:
    # my_function now is redefined to accept 3 arguments:
    print(my_function(1, 2))
except TypeError as ex:
    print('Failed!', ex)


# Step 3:

def do_callback(function, argument):  # you can pass functions as an arguments
    return function(argument)  # this is called "callback"

result = do_callback(len, 'string')
print(result)


# Step 4:
def factorial(n):  # This function is recursive, it calls itself.
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(4))  # 4 * 3 * 2 * 1 = 24


# Step 5:
def sum_all(*args):
    print(args, type(args))

    result = 0
    for arg in args:
        result += arg
    return result

print(sum_all(1, 2, 3, 4, 5))


# Step 6:
def print_or_return(value, mode='print'):
    if mode == 'print':
        print(value)
    elif mode == 'return':
        return value
    else:
        raise ValueError('Bad mode passed.')

print_or_return('some text')
print_or_return('some other text', mode='print')
returned = print_or_return('foo', mode='return')
print(returned)


# Step 7:
def all_together(value, *args, **kwargs):
    message = kwargs.pop('message', 'default message')
    if value > sum(args):
        print(message)
    else:
        print('value is not bigger than sum(args)')

all_together(1, 0)
all_together(1, 2, 3, 4)
all_together(5, 1, 1, 2, message='Done!')


# Step 8:
def enclosing(value):
    def _inner():
        print('value: {value}, new_value: {new_value}'.format(
            new_value=new_value, value=value,
        ))

    new_value = str(value * 10) * 2
    _inner()
    return new_value

enclosing(25)


# Step 9:
def decorator(function):
    def _inner(value):
        print(function(value))

    print('called')
    return _inner

decorated = decorator(len)
decorated([1, 2, 3])
