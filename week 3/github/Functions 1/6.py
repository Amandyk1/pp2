def reverse(words):
    r = words.split()
    return ' '.join(reversed(r))

words = str(input())
print(reverse(words))