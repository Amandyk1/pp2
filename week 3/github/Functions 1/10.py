def unique_list(l):
  num = []
  for a in l:
    if a not in num:
      num.append(a)
  return num
print(unique_list(input()))