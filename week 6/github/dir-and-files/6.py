import string, os

if not os.path.exists("letters"):
   os.makedirs("letters")
   
for l in string.ascii_uppercase:
   with open(l + ".txt", "w") as f:
       f.writelines(l)