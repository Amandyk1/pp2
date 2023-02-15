import math


class Point(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b


    def show(self):
        return self.a, self.b


    def move(self, a, b):
        self.a += a
        self.b += b


    def dist(self, pt):
        dx = pt.a - self.a
        dy = pt.b - self.b
        return math.sqrt(dx ** 2 + dy ** 2)