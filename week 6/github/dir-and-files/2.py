import os

print('Exist:', os.access('C:\Users\Amandyk\Desktop\pp2\week 6\github\dir-and-files\\a.docx', os.F_OK))
print('Readable:', os.access('C:\Users\Amandyk\Desktop\pp2\week 6\github\dir-and-files\\a.docx', os.R_OK))
print('Writable:', os.access('C:\Users\Amandyk\Desktop\pp2\week 6\github\dir-and-files\\a.docx', os.W_OK))
print('Executable:', os.access('C:\Users\Amandyk\Desktop\pp2\week 6\github\dir-and-files\\a.docx', os.X_OK))
