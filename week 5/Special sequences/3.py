import re

txt = "The rain in Spain"

x = re.findall(r"ain\b", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")