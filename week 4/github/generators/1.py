class gen():
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a * self.a <= n:
            b = self.a
            self.a += 1
            return b**2
        else:
            raise StopIteration

n = int(input())
g = gen()
i = iter(g)
for c in i:
    print(c)