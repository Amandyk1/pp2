import time
import math

def builtin(n, ms):
    n = int(input())
    time.sleep(ms / 1000)
    print(f"Square root of {n} after {ms} is {math.sqrt(n)}")