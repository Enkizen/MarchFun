"""Return a reverse iterator. 
seq must be an object which has a __reversed__() method 
or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments starting at 0).

https://github.com/python/cpython/blob/master/Python/bltinmodule.c
"""


def reversedString(st):
    return str[::-1]
