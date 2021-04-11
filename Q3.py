import math as m
class Complex:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def display(self):
        if self.y<0:
            print(str(self.x) + str(self.y) + "i")
        else:
            print(str(self.x) + "+" + str(self.y) + "i")

    def magnitude(self):
        return (m.sqrt(self.x**2+self.y**2))

    def conjugate(self):
        return Complex(self.x,self.y*(-1))

    def add(self,com2):
        return Complex(self.x+com2.x,self.y+com2.y)

    def multiply(self,com2):
        return Complex(self.x*com2.x-self.y*com2.y,self.x*com2.y+self.y*com2.x)

    def inverse(self):
        return Complex(self.x/self.magnitude(),self.y*(-1)/self.magnitude())

a = Complex(1,2)
a .display()
b = Complex(2,-3)
c = b.add(a)
c.display()
c.conjugate().display()
b.inverse().display()
a.multiply(c).display()