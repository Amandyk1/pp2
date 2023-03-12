import os
print("Test a path exists or not:")
path = r'C:\Users\Amandyk\Desktop\pp2\week 6\github\dir-and-files\\a.docx'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))