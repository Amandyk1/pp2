def histogram(n):
    for i in n:
        res = ''
        a = i
        
        while(a > 0):
          res += '*'
          a = a - 1
        print(res)

histogram([1, 4, 7])