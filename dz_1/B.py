a = float(input())
b = float(input())
c = float(input())

res = 'NO'

if a < (b + c):
    if b < (a + c):
        if c < (a + b):
            res = 'YES'

print(res)