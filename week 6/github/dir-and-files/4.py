def fl(fname):
    with open(fname, 'r') as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print("Number of lines in the file: ", fl('C:\Users\Amandyk\Desktop\pp2\week 6\github\dir-and-files\\aa.txt'))