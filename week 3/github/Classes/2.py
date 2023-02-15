class Shape():
    def __init__(self):
        pass

    def sq(self):
        return 0

class Square(Shape):
    def __init__(self,len = 0):
        Shape.__init__(self)
        self.len = len

    def sq(self):
        return self.len*self.len

Asqr = Square(5)
print(Asqr.sq())      

print(Square().sq())