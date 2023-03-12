import os

if os.path.exists('C:\Users\Amandyk\Desktop\pp2\week 6\github\dir-and-files\\aa.txt'):
    os.remove('C:\Users\Amandyk\Desktop\pp2\week 6\github\dir-and-files\\aa.txt')
else:
    print("Given path does not exist!")