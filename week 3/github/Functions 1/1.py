def conv(weight):
    new = weight * 28.3495
    return new

ounces = int(input())

grams = conv(ounces)

print(f"{grams} g")