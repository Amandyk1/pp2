class Rectangle():
    def __init__(self,len,wid):
        self.len = len
        self.wid = wid

    def sq(self):
        return self.len*self.wid


rectangle = Rectangle(5,8)
print(rectangle.sq())