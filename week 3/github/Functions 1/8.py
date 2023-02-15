def sg(n):
    for x in range(0, len(n)):
        a0=n.index(0)
        b0=n.index(0, a0 + 1)
        a7=n.index(7)
        if n[a0 : b0 + 1] != a7 and a7 > b0:
            return True
        else:
            return False