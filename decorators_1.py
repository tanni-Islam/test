'''def outer(some_func):
    def inner():
        print "hello"
        ret = some_func()+1
        return ret+1
    return inner

def foo():
    return 1
foo = outer(foo)

print foo()
'''
'''
class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Coord:" + str(self.__dict__)

def add(a,b):
    return Coordinate(a.x+b.x , a.y+b.y)

def sub(a,b):
    return Coordinate(a.x-b.x, a.y-b.y)

one = Coordinate(100,200)
two = Coordinate(300,200)

print add(one,two)
'''
'''

def repeater(old_function):
     def new_function(*args, **kwds):
          old_function(*args, **kwds)
          old_function(*args, **kwds)
     return new_function

@repeater
def Multiply(num1, num2):
    print num1*num2

Multiply(2, 3)
'''
'''
def Double_Out(old_func):
    def new_func(*args, **kwds):
        return old_func(*args, **kwds)
    return new_func

@Double_Out
def Multiply(num1, num2):
    print num1*num2

Multiply(2, 3)
'''
