from math import hypot

class Vector:

    def __init__(self, x=3, y=2):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

def Foo(n):
    def multiplier(x):
        return x * n
    return multiplier

a = Foo(5)
b = Foo(5)

print(a(b(2)))


