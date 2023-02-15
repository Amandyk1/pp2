from math import pi
def vol(r):
 return (4 * pi * r ** 3) / 3.
r = float(input())
print("Volume: {vol}".format(vol=round(vol(r), 3)))