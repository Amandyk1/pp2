cars = ['Mercedes', 'BMW', 'Toyota', 'Lexus']
with open('aa.txt', 'a') as a:
    for i in cars:
        a.write("\n")
        a.write(i)
        
text = open('aa.txt')
print(text.read())