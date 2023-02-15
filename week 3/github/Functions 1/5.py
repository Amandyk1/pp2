def perm(string, i = 0):

    if i == len(string):   	 
        print("".join(string))

    for j in range(i, len(string)):

        str = [c for c in string]
        str[i], str[j] = str[j], str[i]
   	 
        perm(str, i + 1)

print(perm(input()))