class Fib:

    def __init__(self, nn):
        print("__init__")
        self.__nn = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print('__iter__')
        return self

    def __next__(self):
        print('__next__')
        self.__i += 1
        if self.__i >= self.__nn:
            raise StopIteration
        if self.__i in (1, 2):
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        print('Class iter')
        return self.__iter

# object = Class(8)
#
# for i in object:
#     print(i)

def func(n):
    for i in range(n):
        yield i

# for v in func(5):
#     print(v)

def powerof2(n):
    pow = 1
    for i in range(n):
        yield pow
        pow *= 2

# i = list(powerof2(6))
# print(i)

def Fib(n):
    p = pp = 1
    for i in range(n):
        if i in [0,1]:
            yield 1
        else:
            n = p + pp
            p, pp = pp, n
            yield n

# fibs = list(Fib(3))
#
# print(fibs)

