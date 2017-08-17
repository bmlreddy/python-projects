def Foo(n):
    def m(z):
        return z * n
    return m

a = Foo(5)
b = Foo(5)

print(a(b(5)))
