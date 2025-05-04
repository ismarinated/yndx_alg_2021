a = int(input())
b = int(input())
c = int(input())

if a == 0 :
    if b == c * c:
        print('MANY SOLUTIONS')
    else:
        print('NO SOLUTION')
elif c < 0:
    print('NO SOLUTION')
else:
    if (((c * c - b) / a) * 10) % 10 == 0:
        print(int((c * c - b) / a))
    else:
        print('NO SOLUTION')