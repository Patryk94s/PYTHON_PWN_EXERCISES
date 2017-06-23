class A(object):
    def foo(self):
        print ('A')
 
class B(A):
    def foo(self):
        print ('B')
        super(B, self).foo()
 
class C(A):
    def foo(self):
        print ('C')
        super(C, self).foo()
 
class D(B,C):
    def foo(self):
        print ('D')
        super(D, self).foo()
        
d = D()
d.foo()


class A1:
    a=1
    b=2
    def __init__(self, a):
        self.a = a
    
    def zwroc(self):   
        return 'jestem w A1'
    def dodawanie(self):
        return self.a + self.a
class B1(A1):
    def __init__(self, a, b):
        super(B1,self)
        self.b = b
        print(self.a + self.b)
        
    def zwroc(self):
        return super(B1,self).zwroc() + 'jestem w B1'

    def dodawanie(self, x):
        super(B1,self)
        self.x = x
        return self.a + self.x
o1 = B1(1,4)
print(o1.zwroc())
print(o1.dodawanie(6))

